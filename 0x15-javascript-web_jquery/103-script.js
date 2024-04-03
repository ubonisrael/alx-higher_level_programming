$(() => {
  $('INPUT#btn_translate').on('click', fetchData);
  $('INPUT#language_code').keypress((e) => {
    if (e.which === 13) {
      fetchData();
    }
  });
});

function fetchData () {
  $.get(
    `https://hellosalut.stefanbohacek.dev/?lang=${$('INPUT#language_code').val()}`,
    (data) => {
      $('DIV#hello').text(data.hello);
    }
  );
}
