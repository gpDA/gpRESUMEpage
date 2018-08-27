$(document).ready(function(){
    $(".col-img-right-1").hover(function(event){
        $(".overlay-right-1").toggle('slide', {direction: 'right'},500);
        event.stopPropagation();
    });
    $(".col-img-right-2").hover(function(event){
        $(".overlay-right-2").toggle('slide', {direction: 'right'},500);
        event.stopPropagation();
    });    
    
});

$(document).on("scroll", function (event) {
    //fadein as scroll down

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
    };
    //underline nav-link as scroll down
    var scrollPos = $(document).scrollTop();
    $('.navbar a').each(function () {
        var currLink = $(this);
        var refElement = $(currLink.attr("href"));
        if (refElement.position().top <= scrollPos && refElement.position().top + refElement.height() > scrollPos) {
            $(".navbar a").removeClass("active");
            currLink.addClass("active");
        }
        else{
            currLink.removeClass("active");
        }
    });

  
  });
    






