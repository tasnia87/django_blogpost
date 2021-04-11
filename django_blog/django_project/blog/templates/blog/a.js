


$('.dropdown-content').hide()
  $('#drop').mouseenter(function(){
    $('.dropdown-content').animate({height:'toggle'})

})
$('#drop').mouseleave(function(){
  $('.dropdown-content').hide()

})

$('.r1').hide()
$('.r2').hide()
$('.fadee').mouseenter(function(){
  $('.r1').show(1000)
  $('.r2').show(2000)

$('.sort').slideUp()
})






window.onscroll = function() {myFunction()};

// Get the navbar
var navbar = document.getElementById("navbar");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position


$('.nav-link').mouseenter(function(){
  $('.nav-link').css('font-weight','bold')
})

$('.nav-link').mouseleave(function(){
  $('.nav-link').css('font-weight','normal')
})

window.onscroll = function() {
  myFunction(

)};


$('.imgname1').hide()
$('.pic1').hover(function(){
  $('.imgname1').animate({height:'toggle',time:'6000'})
})

$('.imgname2').hide()
$('.pic2').hover(function(){
  $('.imgname2').animate({height:'toggle',time:'6000'})
})

$('.imgname3').hide()
$('.pic3').hover(function(){
  $('.imgname3').animate({height:'toggle',time:'6000'})
})

$('.fadee').mouseleave(function(){
  $('.navbar-custom').animate({height:'60px',time:'1000'})
  $('.navbar-custom').css({"background-color":"pink"})
})
$('.fadee').mouseenter(function(){
  $('.navbar-custom').animate({height:'130px',time:''})
  $('.navbar-custom').css({"background-color":"#F59A87"})
})
