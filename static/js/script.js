
// Show message for 3 seconds
var message_element = document.getElementById('msg');
setTimeout(function () {
    message_element.style.display = 'none'
    }, 3000)

// Add css active class to bootstrap carousel
$('.carousel-item').first().addClass('active')

// Add Toggle / sliding effect on about page
$(".show-mission").hide();
$(".mission").hover(function(){
    $(".show-mission").slideToggle(1000);
    // $(".show-privacy").slideUp(1000);
    // $(".show-contact").slideUp(1000);

  });

$(".show-privacy").hide();
$(".privacy").hover(function(){
    $(".show-privacy").slideToggle(1000)
    // $(".show-mission").slideUp(1000);
    // $(".show-contact").slideUp(1000);

})

$(".show-contact").hide();
$(".contact").hover(function(){
    $(".show-contact").slideToggle(1000)
    // $(".show-privacy").slideUp(1000);
    // $(".show-mission").slideUp(1000);
})
