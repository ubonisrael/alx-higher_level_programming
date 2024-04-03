$(() => {
  $('#btn_translate').on('click', () => {
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${$('#language_code').val()}`, (data) => {
    //   console.log(data);
      $('#hello').text(data.hello);
    });
  });
});
