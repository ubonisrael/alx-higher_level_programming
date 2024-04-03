$('#toggle_header').on('click', () => {
  if ($('header').hasClass('red')) {
    $('header').addClass('green');
    $('header').removeClass('red');
  } else {
    $('header').addClass('red');
    $('header').removeClass('green');
  }
});
