
// Show message for 3 seconds
var message_element = document.getElementById('msg');
setTimeout(function () {
    message_element.style.display = 'none'
    }, 3000)

// Add css active class to bootstrap carousel
$('.carousel-item').first().addClass('active')
