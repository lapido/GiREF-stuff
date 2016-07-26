(function($){
  $(function(){

    
    $('.parallax').parallax();
    $('.scrollspy').scrollSpy();
    $('select').material_select();
	 $('.slider').slider({
	 	full_width: true,
	 	interval:5000,
	 	transition:800,
	 	indicators:false,
	 	height:500});   

  }); // end of document ready
})(jQuery); // end of jQuery name space