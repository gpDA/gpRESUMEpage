$(document).ready(function(){
    //scroll event NAV

    var lastScrollTop = 0;
    $(window).scroll(function(event){
    var scroll = $(this).scrollTop();
    if (scroll > lastScrollTop){
        $("nav").removeClass("increase").addClass("decrease");
            $('.nav-items img').animate({height:"65px",width:"80px"}, 30);
            $('.nav-items').animate({lineHeight:"40px"}, 30);
    } else {        
        $("nav").removeClass("decrease").addClass("increase");
            $('.nav-items img').animate({height:"120px",width:"120px"}, 30);
            $('.nav-items').animate({lineHeight:"80px"}, 30);
    }
    lastScrollTop = scroll;
    });  
});



