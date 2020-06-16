$(function() {
    // For refference https://www.youtube.com/watch?v=lx0IysyYLH0
    $("#home span.glyphicon-home").parent().parent().addClass('active');
    $("#membri a:contains('Membri')").parent().addClass('active');
    $("#blog a:contains('Blog')").parent().addClass('active');
    $("#hub a:contains('Membership')").parent().parent().parent().addClass('active');
    $("#contact a:contains('Contact')").parent().addClass('active');
    $("#doilasuta a:contains('2%')").parent().addClass('active');
    $("#profile span.glyphicon-user").parent().parent().addClass('active');
       /*no need for activation!*/
    // $("#logout span.glyphicon-log-out").parent().parent().addClass('active'); 
    $("#proiecte a:contains('Proiecte')").parent().addClass('active');

    /*
    // The following is for active state for drop down menus
    if($("#photographer_pack a:contains('Photographer\'s Package')").parent().hasClass('active')){
    $(".dropdown a:contains('Our Programs')").parent().addClass('active');
    }

    if($("#joomla a:contains('Joomla Training')").parent().hasClass('active')){
    $(".dropdown a:contains('Our Programs')").parent().addClass('active');
    }

    //make menus drop automatically
    $('ul.nav li.dropdown').hover(function() {
            $('.dropdown-menu', this).fadeIn();
    }, function() {
            $('.dropdown-menu', this).fadeOut('fast');
    });//hover
    */


});



$(document).ready(function(){
$("#button").click(function () {
    $("#frame").attr("src", "https://www.wikipedia.org/");

});
});
