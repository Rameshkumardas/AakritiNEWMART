$(document).ready(function(){
    $('#input-field').on('keyup', function () {
        var Subject_URL = $('#input-field').val();
        Subject_URL_toLowerCase = Subject_URL.toLowerCase();
        New_URL = Subject_URL_toLowerCase.replace(/ /g,'-')
        $("#slug").val(New_URL);
    });
  });