# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Profile
# from .forms import ExtendUserCreationForm, ProfileForm
# from django.contrib.auth import authenticate, login

# # Create your views here.
# def register(request):
#     if request.method == 'POST':
#         form = ExtendUserCreationForm(request.POST)
#         profile_form = ProfileForm(request.POST)

#         if form.is_valid() and profile_form.is_valid():
#             user = form.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.save()

#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)

#             login(request, user)

#             return redirect('dashboard')

#     else:
#         form = ExtendUserCreationForm()
#         profile_form = ProfileForm()

#     context = {'form' : form, 'profile_form' : profile_form}
#     return render(request, 'dashboard/register.html', context)


# @login_required
# def dashboard(request):
#     #fetch data from mongo and display
#     if request.user.is_authenticated:
#         username = request.user.username
#         userid = request.user.id
#         useremail = request.user.email
#         profiles = Profile.objects.order_by('id')
#         context = {'profiles': profiles, 'username' : username, 'userid': userid, 'useremail' : useremail}

#     else:
#         profiles = Profile.objects.order_by('id')
#         context = {'profiles' : profiles}
#     # Render the HTML template index.html
#     return render(request, 'dashboard.html', context)

# def editing(request):

#     #update mongo user details with user's changes
#     if request.method == 'POST':
#         form = ProfileForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     else:
#         form = ProfileForm()
#     context = {'form': form}

#     return render(request, 'editing.html', context)
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
    # fetch data from mongo and display
    # args = {'user':request.user}
    # return render(request, 'dashboard.html', args)
    # if request.user.is_authenticated:
    #     username = request.user.username
    #     userid = request.user.id
    #     useremail = request.user.email
    #     profiles = Profile.objects.order_by('id')
    #     context = {'profiles': profiles, 'username': username,
    #                'userid': userid, 'useremail': useremail}

    # else:
    #     profiles = Profile.objects.order_by('id')
    #     context = {'profiles': profiles}
    # # Render the HTML template index.html
    return render(request,'dashboard.html')


def editing(request):
    # profile = Profile(user=request.user)

    # # update mongo user details with user's changes
    # if request.method == 'POST':
    #     # a = (User.objects.order_by('date_joined'))
    #     # a = str(a)
    #     # a = a.replace("<","").replace(">","").replace("QuerySet","").replace("User: ","").replace("[","").replace("]","")
    #     # a = a.split(",")
    #     # ru = f" {request.user}"
    #     # if ru in a:
    #     form = UserForm(request.POST, instance=request.user)
    #     profile_form = ProfileForm(
    #         request.POST, request.FILES, instance=profile)
    #     if form.is_valid() and profile_form.is_valid():
    #         user_form = form.save()
    #         custom_form = profile_form.save(False)
    #         custom_form.user = user_form
    #         custom_form.save(update_fields=['middlename',                                                                      'telephone',
    #                                         'website',
    #                                         'occupation',
    #                                         'date_of_birth',
    #                                         'bio',
    #                                         'twitter_handle',
    #                                         'fb_handle',
    #                                         'insta_handle',
    #                                         'address1',
    #                                         'address2',
    #                                         'city',
    #                                         'state',
    #                                         'zipcode'])
    #         return render(request,'dashboard.html')

    # else:
    #     form = UserForm(instance=request.user)
    #     profile_form = ProfileForm(instance=profile)
    #     args = {}
    #     # args.update(csrf(request))
    #     args['form'] = form
    #     args['profile_form'] = profile_form
    #     return render(request, 'editing.html', args)
# def edit_user(request, pk):
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
