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
    
    
    $(window).on("load",function() {
        $(window).scroll(function() {
          var windowBottom = $(this).scrollTop() + $(this).innerHeight();
          $(".fade").each(function() {
            /* Check the location of each desired element */
            var objectBottom = $(this).offset().top + $(this).outerHeight();
            
            /* If the element is completely within bounds of the window, fade it in */
            if (objectBottom < windowBottom) { //object comes into view (scrolling down)
              if ($(this).css("opacity")==0) {$(this).fadeTo(500,1);}
            } else { //object goes out of view (scrolling up)
              if ($(this).css("opacity")==1) {$(this).fadeTo(500,0);}
            }
          });
        }).scroll(); //invoke scroll-handler on page-load
      });

});



