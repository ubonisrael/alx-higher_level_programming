$(() => {
  $('DIV#add_item').on('click', () => {
    $('UL.my_list').append('<li>Item</li>');
  });

  $('DIV#remove_item').on('click', () => {
    $('UL.my_list').children().last().remove();
  });

  $('DIV#clear_list').on('click', () => {
    $('UL.my_list').empty();
  });
});
