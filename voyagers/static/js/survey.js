$(function () {
    $("#wizard").steps({
        headerTag: "h4",
        bodyTag: "section",
        transitionEffect: "fade",
        enableAllSteps: true,
        transitionEffectSpeed: 500,
        onStepChanging: function (event, currentIndex, newIndex) {
            if (newIndex === 1) {
                $('.steps ul').addClass('step-2');
            } else {
                $('.steps ul').removeClass('step-2');
            }
            if (newIndex === 2) {
                $('.steps ul').addClass('step-3');
            } else {
                $('.steps ul').removeClass('step-3');
            }

            if (newIndex === 3) {
                $('.steps ul').addClass('step-4');
                $('.actions ul').addClass('step-last');
            } else {
                $('.steps ul').removeClass('step-4');
                $('.actions ul').removeClass('step-last');
            }
            return true;
        },
        labels: {
            finish: "Place Holder",
            next: "Next",
            previous: "Previous"
        }
    });
    // Custom Steps Jquery Steps
    $('.wizard > .steps li a').click(function () {
        $(this).parent().addClass('checked');
        $(this).parent().prevAll().addClass('checked');
        $(this).parent().nextAll().removeClass('checked');
    });
    // Custom Button Jquery Steps
    $('.forward').click(function () {
        $("#wizard").steps('next');
    })
    $('.backward').click(function () {
        $("#wizard").steps('previous');
    })
    // Checkbox
    $('.checkbox-circle label').click(function () {
        $('.checkbox-circle label').removeClass('active');
        $(this).addClass('active');
    })
})

var subjectObject = {
    "United States of America": {
        "New York": { "New York 3-day Adventure. Explore the City!": "2021 - 05 - 06" },
        "San Diego": { "Explore the most popular attractions in the city in San Diego!": '2021-05-10' }

    },
    "China": {
        "Beijing": { "Discover Beijing!": "2021-04-07" },
        "Shanghai": { "Exploring Shanghai": "2021-04-07" }
    },

    "France": {
        "Paris": { "Discover Beijing!": "2021-04-07" },
        "Bordeax": { "Exploring Shanghai": "2021-04-07" }
    },

}
window.onload = function () {
    var countrySel = document.getElementById("country");
    var citySel = document.getElementById("city");
    var attractionName = document.getElementById("attractionName");
    var departureSel = document.getElementById("departure");
    for (var x in subjectObject) {
        countrySel.options[countrySel.options.length] = new Option(x, x);
    }
    countrySel.onchange = function () {
        //display correct values
        for (var y in subjectObject[this.value]) {
            citySel.options[citySel.options.length] = new Option(y, y);
        }
    }
    citySel.onchange = function () {
        //display correct values
        var z = subjectObject[subjectSel.value][this.value];
        for (var i = 0; i < z.length; i++) {
            attractionName.options[attractionName.options.length] = new Option(z[i], z[i]);
        }
    }
    attractionName.onchange = function () {
        //display correct values
        var a = subjectObject[subjectSel.value][this.value];
        for (var b = 0; b < a.length; b++) {
            departureSel.options[departureSel.options.length] = new Option(a[b], a[b]);
        }
    }
}