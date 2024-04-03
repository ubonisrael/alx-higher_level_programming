$(() => {
  $('#add_item').on('click', () => {
    $('UL.my_list').append('<li>Item</li>');
  });

  $('#remove_item').on('click', () => {
    $('UL.my_list').children().last().remove();
  });

  $('#clear_list').on('click', () => {
    $('UL.my_list').empty();
  });
});
