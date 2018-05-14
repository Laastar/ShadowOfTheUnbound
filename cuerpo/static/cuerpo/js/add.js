$(document).ready(function(){
    $('.sidenav').sidenav();
 	$('.slider').slider();
    $('.parallax').parallax();
    $('.carousel.carousel-slider').carousel({
    fullWidth: true
	});
	 $(document).ready(function(){
    $('.pushpin').pushpin();
  });
 });

function Ejecuta() {
 	alert("Mensaje enviado, Tus comentarios nos ayudan a seguir creciendo")
 }

 function Finalizar() {
 	alert("Tu cita se ha registrado gracias por tu preferencia")
 }

 function Registro() {
 	alert("Registro exitoso, Gracias por tu preferencia")
 	document.location.href=index.html;
 }


  $('.pushpin-demo-nav').each(function() {
    var $this = $(this);
    var $target = $('#' + $(this).attr('data-target'));
    $this.pushpin({
      top: $target.offset().top,
      bottom: $target.offset().top + $target.outerHeight() - $this.height()
    });
  });

$("#ocultar").click(function(e){        
  $("#logo").fadeOut();   
});
$("#mostrar").click(function(e){        
  $("#logo").fadeIn();    
});
        