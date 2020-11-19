from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from .models import Profile
from .forms import UserForm, ProfileForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.contrib.auth import update_session_auth_hash


@login_required()  # only logged in users should access this
def dashboard(request):
    return render(request,'dashboard.html')


def editing(request):
    pk = request.user.pk
    # querying the User object with pk from url
    user = User.objects.get(pk=pk)
    # prepopulate UserProfileForm with retrieved user values from above.
    form = UserForm(instance=user)

    # The sorcery begins from here, see explanation below
    ProfileInlineFormset = inlineformset_factory(User, Profile, fields=('middlename',
                                                                        'telephone',
                                                                        'website',
                                                                        'occupation',
                                                                        'date_of_birth',
                                                                        'bio',
                                                                        'twitter_handle',
                                                                        'fb_handle',
                                                                        'insta_handle',
                                                                        'address1',
                                                                        'address2',
                                                                        'city',
                                                                        'state',
                                                                        'zipcode',
                                                                        ))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated and request.user.id == user.id:
        if request.method == "POST":
            form = UserForm(request.POST, instance=request.user)
            formset = ProfileInlineFormset(
                request.POST, request.FILES, instance=user)
      

            if form.is_valid():
                custom_form = form.save(commit=False)
                formset = ProfileInlineFormset(
                    request.POST, request.FILES, instance=custom_form)

                if formset.is_valid():
                    custom_form.save()
                    formset.save()
                    return redirect('dashboard')

        return render(request, "editing.html", {
            "noodle": pk,
            "noodle_form": form,
            "formset": formset,
        })
    else:
        raise PermissionDenied
