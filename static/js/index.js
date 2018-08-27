$(document).ready(function(){
    $(".col-img-right-1").hover(function(){
        $(".overlay-right-1").toggle('slide', {direction: 'right'},500);
    });
    $(".col-img-right-2").hover(function(){
        $(".overlay-right-2").toggle('slide', {direction: 'right'},500);
    });    
    //scroll event NAV
    var lastScrollTop = 0;
    $(window).scroll(function(){
    //nav
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
//fadein as scroll down
$(document).on("scroll", function () {
    var pageTop = $(document).scrollTop()
    var pageBottom = pageTop + $(window).height()
    var tags = $("section")
  
    for (var i = 0; i < tags.length; i++) {
      var tag = tags[i]
  
      if ($(tag).position().top < pageBottom) {
        $(tag).addClass("fadein")
      } else {
        $(tag).removeClass("fadein")
      }
    }
  });
    






