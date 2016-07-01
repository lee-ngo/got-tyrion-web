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

  // $('#show-the-wall-p2').click(function(){
  //   $('#the-wall-p2').show();
  //   $('$the-wall-p1').hide();
  // });
  //
  // $('#show-the-wall-p3').click(function(){
  //   $('#the-wall-p2').hide();
  //   $('#the-wall-p3').show();
  // });
  //
  // $('#show-the-wall-p4').click(function(){
  //   $('#the-wall-p3').hide();
  //   $('#the-wall-p4').show();
  // });
});
