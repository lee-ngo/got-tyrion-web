$( document ).ready(function(){

  bronn_health = 10;
  vardis_health = 10;

  $('#bronn-health').text(bronn_health);
  $('#vardis-health').text(vardis_health);
  // clicking slash will do the following
  $('#slash').click(function(){
    vardis_choice = Math.random();
    if (vardis_choice <= 0.33) {
      vardis_choice = "SLASH";
      bronn_health -= 2;
      vardis_health -= 2;
      $('#bronn-health').text(bronn_health);
      $('#vardis-health').text(vardis_health);
    } else if (vardis_choice <= 0.66) {
      vardis_choice = "THRUST";
      bronn_health -= 1;
      vardis_health -= 2;
      $('#bronn-health').text(bronn_health);
      $('#vardis-health').text(vardis_health);
    } else {
      vardis_choice = "BLOCK"
    };
    $('#battle-update').text("You chose SLASH and Vardis chose "+vardis_choice+"!");
  });
// clicking thrust will do the following
  $('#thrust').click(function(){
    vardis_choice = Math.random()
      if (vardis_choice <= 0.33) {
        vardis_choice = "SLASH";
        bronn_health -= 1;
        vardis_health -= 2;
        $('#bronn-health').text(bronn_health);
        $('#vardis-health').text(vardis_health);
      } else if (vardis_choice <= 0.66) {
        vardis_choice = "THRUST";
        bronn_health -= 1;
        vardis_health -= 1;
        $('#bronn-health').text(bronn_health);
        $('#vardis-health').text(vardis_health);
      } else {
        vardis_choice = "BLOCK";
        vardis_health -= 1;
        $('#bronn-health').text(bronn_health);
        $('#vardis-health').text(vardis_health);
      };
      $('#battle-update').text("You chose THRUST and Vardis chose "+vardis_choice+"!");
    });
// click block will do the following
 $('#block').click(function(){
    vardis_choice = Math.random()
    if (vardis_choice <= 0.33) {
       vardis_choice = "SLASH";
    } else if (vardis_choice <= 0.66) {
       vardis_choice = "THRUST";
       bronn_health -= 1;
       $('#bronn-health').text(bronn_health);
    } else {
       vardis_choice = "BLOCK";
    };
     $('#battle-update').text("You chose BLOCK and Vardis chose "+vardis_choice+"!");
  });
// launch a conditional situation
  if (vardis_health <= 0 && bronn_health > 0) {
    $('#bronn-wins').removeClass('hidden');
    $('#combat-page').hide();
  } else if (bronn_health <= 0 && vardis_health > 0) {
    $('#bronn-loses').removeClass('hidden');
    $('#combat-page').hide();
  } else {
  };

});
