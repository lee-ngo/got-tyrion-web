$( document ).ready(function(){
  bronn_health = 10;
  vardis_health = 10;
  // start off with the health of each fighter
  $('#bronn-health').text(bronn_health);
  $('#vardis-health').text(vardis_health);

  // jquery change is bronn wins
  var bronn_victory = function() {
    $('#bronn-wins').removeClass('hidden');
    $('#combat-page').addClass('hidden');

  // jquery change if bronn loses
  };
  var bronn_defeat = function() {
    $('#bronn-loses').removeClass('hidden');
    $('#combat-page').addClass('hidden');
  };

  // clicking slash will do the following
  $('#slash').click(function(){
    vardis_choice = Math.random();
    if (vardis_choice <= 0.33) {
      vardis_choice = "SLASH";
      bronn_health -= 3;
      vardis_health -= 2;
    } else if (vardis_choice <= 0.66) {
      vardis_choice = "THRUST";
      vardis_health -= 1;
      bronn_health -= 1;
    } else {
      vardis_choice = "BLOCK";
    };
    $('#bronn-health').text(bronn_health);
    $('#vardis-health').text(vardis_health);
    $('#battle-update').text("You chose SLASH and Vardis chose "+vardis_choice+"!");
    // conditional that outlines win/lose
    if (vardis_health <= 0 && bronn_health > 0) {
      bronn_victory();
    } else if (bronn_health <= 0 && vardis_health > 0) {
      bronn_defeat();
    } else {
    };

  });
// clicking thrust will do the following
  $('#thrust').click(function(){
    vardis_choice = Math.random();
    vardis_health -= 1;
    if (vardis_choice <= 0.33) {
      vardis_choice = "SLASH";
      bronn_health -= 3;
    } else if (vardis_choice <= 0.66) {
      vardis_choice = "THRUST";
      bronn_health -= 1;
    } else {
      vardis_choice = "BLOCK";
    };
    $('#bronn-health').text(bronn_health);
    $('#vardis-health').text(vardis_health);
    $('#battle-update').text("You chose THRUST and Vardis chose "+vardis_choice+"!");

    if (vardis_health <= 0 && bronn_health > 0) {
      bronn_victory();
    } else if (bronn_health <= 0 && vardis_health > 0) {
      bronn_defeat();
    } else {
    };

  });
// click block will do the following
 $('#block').click(function(){
    vardis_choice = Math.random();
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
    if (vardis_health <= 0 && bronn_health > 0) {
      bronn_victory();
    } else if (bronn_health <= 0 && vardis_health > 0) {
      bronn_defeat();
    } else {
    };

  });

});
