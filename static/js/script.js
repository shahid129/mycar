// Show message for 3 seconds
$('#msg').delay(3000).fadeOut('slow');

// Add css active class to bootstrap carousel
$('.carousel-item').first().addClass('active')

// Add Toggle / sliding effect on about page
$(".show-mission").hide();
$(".mission").hover(function () {
    $(".show-mission").slideToggle(1000);
    // $(".show-privacy").slideUp(1000);
    // $(".show-contact").slideUp(1000);

});

$(".show-privacy").hide();
$(".privacy").hover(function () {
    $(".show-privacy").slideToggle(1000)
    // $(".show-mission").slideUp(1000);
    // $(".show-contact").slideUp(1000);

})

$(".show-contact").hide();
$(".contact").hover(function () {
    $(".show-contact").slideToggle(1000)
    // $(".show-privacy").slideUp(1000);
    // $(".show-mission").slideUp(1000);
})


$(".brand-name").hover(function () {
        $(".my").css("color", "black");
        $(".mycar").css("color", "#D9391E");
    },
    function () {
        $(".my").css("color", "#D9391E");
        $(".mycar").css("color", "black");
    })

// Burger menu hide and toggle

$("#navbar-toggler-icon-2").hide();
let click = 0;
$(".navbar-toggler").click(function(){
    if (click % 2 == 0){
        $("#navbar-toggler-icon-2").fadeIn(500);
        $("#navbar-toggler-icon").hide();
    } else {
        $("#navbar-toggler-icon").fadeIn(500);
        $("#navbar-toggler-icon-2").hide();
    }
    click++;
});
