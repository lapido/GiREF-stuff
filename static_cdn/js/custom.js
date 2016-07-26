var w = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
var x = 0;
var setter;
var obj = {
	key : 0,
	reader : function(){
		obj.key++;
		document.getElementsByTagName("b")[0].innerHTML = obj.key;
	},
	counter : function(){
		setter = setInterval(obj.reader, 1000);
	}
}


$(document).ready(function(){
	// var c = document.getElementsByClassName("block-blog-post").height;
	// alert(c);
	// $(window).scroll(function(e){
	// 	var xo = $(document).scrollTop();
	// 	$("#show").text(xo);

	// 	if (xo >= 836) {
	// 		$(".block-recent-post").css({
	// 			"position" : "fixed",
	// 			"top" : "0",
	// 			"margin-top" : "-30px",
	// 			"right" : "10px",
	// 			"overflow" : "auto"
	// 		})
	// 	}
	// 	else{
	// 		$(".block-recent-post").css({
	// 			"position" : "relative",
	// 			"margin-top" : "0px",
	// 			"right" : "0"
	// 		})
	// 	}
	// })
	
	$(".hidden-link").hover(function(){
		if (w >= 768) {
		//    $(".default-navbar").css({"background-color" : "rgba(255, 255, 255, 0.2)", "opacity" : "1", "transition" : "all .4s ease-in"});
		//    $(".default-navbar").animate({height: '100px'}, 1);
		}
	},
		function(){
		    if (w >= 768) {
			//    $(".default-navbar").css({"background" : "transparent", "opacity" : ".9", "transition" : "all 1s ease-in"});
			 //   $(".default-navbar").animate({height: '80px'});
			};
		}
	);

	$(".mobile-toggle").click(function(){
		$(".default-links").slideToggle(350);
		$(".default-links").css({
			"position" : "absolute",
			"width" : "100%",
		});
	})

// 	$(document).on("scrollstart", function(){
// 		$(".default-navbar").css({
// 			"position" : "fixed",
// 			"z-index" : "5",
// 			"width" : "100%",
// 			"background-color" : "rgba(0, 0, 0, 0.8	)",
// 			"transition" : "all 1s ease-in",
// 			"height" : "100px"
// 		})
// 		$(".default-links").slideToggle(350);
// 	})
})