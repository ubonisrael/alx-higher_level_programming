$(() => {
  $('INPUT#btn_translate').on('click', () => {
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${$('INPUT#language_code').val()}`, (data) => {
    //   console.log(data);
      $('DIV#hello').text(data.hello);
    });
  });
});
