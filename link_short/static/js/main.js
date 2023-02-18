if (window.innerWidth <= 900) {
   $(".log_2").hide()
}

$("#icon").on("click", function() {
    $("#hidden-menu").animate({
        "left": '0vh'
    }, 400);
});

$("#hidden-menu .close").on("click", function() {
    $("#hidden-menu").animate({
        "left": "-43vh"
    }, 300);
});


$("#main-title").hide()
$(window).on('load', function() {
    $("#main-title").show('slow')
});


$("#hr-main").hide()
$(window).on('load', function() {
    $("#hr-main").show('slow')
});


$("#icon").animate({
    "left": '-10vh'
}, 0);
$(window).on('load', function() {
    $("#icon").animate({
        "left": '1vh'
    }, 'fast');
});



$(".stickers1").on("click", function() {
    $(".log_2").toggle( 200 )
    $(".block-about").animate({
        "margin": "8vh 0"
    }, 400);
    $(".stickers2").show( 200 )
    $(".stickers1").hide( 200 )
});
$(".stickers2").on("click", function() {
    $(".log_2").toggle( 200 )
    $(".block-about").animate({
        "margin": "-8vh 0"
    }, 400);
    $(".stickers1").show( 200 )
    $(".stickers2").hide( 200 )
});


window.onresize = function () {
    width = document.documentElement.clientWidth;
    height = document.documentElement.clientHeight;
    if (width <= 900) {
        $(".log_2").hide()
    }
    else if (width > 900) {
        $(".log_2").show()
    }
}

$('.block-about-p').css('font-size', '0vw');
$('.block-about-p').css('width', '7vw');

$(window).on('load', function() {
    if (window.innerWidth > 900) {
        $(".block-about-p").animate({
            "font-size": "1.4vw",
            "width": "26vw",
        }, 700)
    }
     else if (window.innerWidth <= 900) {
        $(".block-about-p").animate({
            "font-size": "5vw",
            "width": "90vw",
        }, 700)
     }
});

window.onresize = function(event) {
    width = document.documentElement.clientWidth;
    var numbers = []
    for (var i = 890; i <= 910; i++) {
        numbers.push(i)
    }
    if (numbers.includes(width)) {
        window.location.reload();
    }
};


$(window).on('load', function() {
    $('.block-link').animate({
        "height": "60vh"
    }, 700)
});

$(window).on('load', function() {
    $(".main-register h1").animate({
            "opacity": "1",
    }, 1000)
});

$(window).on('load', function() {
    $('.block-link').animate({
        "height": "60vh"
    }, 700)
});

$(window).on('load', function() {
    $(".profile h1").animate({
            "opacity": "1",
    }, 1000)
});

$(window).on('load', function() {
    $(".main-create h1").animate({
            "opacity": "1",
    }, 1000)
});

$(window).on('load', function() {
    $("#mess").animate({
            "opacity": "0",
    }, 2500)
});

$(window).on('load', function() {
    $(".img-about").animate({
        "rotate": "360deg"
    }, 800)
});

$(window).on('load', function() {
    $(".block-link-author").animate({
        "height": "10em"
    }, 800)
    $(".update_user").animate({
        "height": "10em"
    }, 800)
    $(".update_user form").animate({
        "opacity": "1"
    }, 800)
});
