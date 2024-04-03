$(() => {
  $('#btn_translate').on('click', fetchData);
  $('#language_code').keypress((e) => {
    if (e.which === 13) {
      fetchData();
    }
  });
});

function fetchData () {
  $.get(
    `https://hellosalut.stefanbohacek.dev/?lang=${$('#language_code').val()}`,
    (data) => {
      $('#hello').text(data.hello);
    }
  );
}
