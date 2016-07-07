$( document ).ready(function(){

  $('.next-scene-click').click(function(){
     $( this ).parent().parent().next().removeClass('hidden');
     $( this ).parent().parent().hide();
   });

// jquery to go to the top of the wall
  $('#go-top-of-wall').click(function(){
    $('#top-of-wall').removeClass('hidden');
    $( this ).parent().parent().hide();
  })

// jquery to show/hide piss off wall
  $('#go-piss').click(function(){
    $('#piss-off-wall').removeClass('hidden');
    $( this ).parent().parent().hide();
  })

// jquery to show/hide piss no piss off wall
  $('#no-piss').click(function(){
    $('#no-piss-off-wall').removeClass('hidden');
    $( this ).parent().parent().hide();
  })

// jquery to show/hide the random girl in brothel
  $('#choose-random-girl').click(function(){
    $('#random-girl').removeClass('hidden');
    $( this ).parent().parent().hide();
  })
// jquery to choose tyrion as champion
  $('#go-choose-tyrion').click(function(){
    $('#choose-tyrion').removeClass('hidden');
    $( this ).parent().parent().hide();
  })
// jquery for choosing jaime
  $('#go-choose-jaime').click(function(){
    $('#choose-jaime').removeClass('hidden');
    $( this ).parent().parent().hide();
  })
// jquery for choosing bronn
  $('#go-choose-bronn').click(function(){
    $('#choose-bronn').removeClass('hidden');
    $( this ).parent().parent().hide();
  })
// jquery for accepting hand position
  $('#accept-hand').click(function(){
    $('#hand-king').removeClass('hidden');
    $( this ).parent().parent().hide();
  })

});
