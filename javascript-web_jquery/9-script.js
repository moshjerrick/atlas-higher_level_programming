$(document).ready(function() {
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr').done(function (data) {
  $('DIV#hello').text(data.hello);
});
}
);