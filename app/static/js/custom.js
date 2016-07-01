$( document ).ready(function(){

  window.alert("Your jQuery is working!");

  $('.next-scene-click').click(function(){
    $( this ).parent().next().removeClass('hidden');
    $( this ).parent().hide();
  });

// jquery to go to the top of the wall
  $('#go-top-of-wall').click(function(){
    $('#top-of-wall').removeClass('hidden');
    $( this ).parent().hide();
  })

// jquery to show/hide piss off wall
  $('#go-piss').click(function(){
    $('#piss-off-wall').removeClass('hidden');
    $( this ).parent().hide();
  })

// jquery to show/hide piss no piss off wall
  $('#no-piss').click(function(){
    $('#no-piss-off-wall').removeClass('hidden');
    $( this ).parent().hide();
  })

// jquery to show/hide the random girl in brothel
  $('#choose-random-girl').click(function(){
    $('#random-girl').removeClass('hidden');
    $( this ).parent().hide();
  })

});
