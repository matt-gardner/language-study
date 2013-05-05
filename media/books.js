$(document).ready(function() {

$('.edit-chapter').editable('edit-chapter', {
  event : "dblclick",
  submitdata : function(value, settings) {
    return {
        csrfmiddlewaretoken : $.fn.csrf.csrf_token
      }
  }
});

$('button.edit-text').live('click', function() {
  if ($(this).html() == "Edit") {
    $(this).html('Submit');
    $('<textarea rows="35" cols="50"></textarea>').appendTo('.text');
    var text = $('.text-body').text().trim();
    $('.text-body').remove();
    $('textarea').append(text);
    $(this).remove().appendTo('.text');
  } else {
    var text = $('textarea').val();
    $.get("edit-text", {text: text}, function(data) {
      location.reload(true);
    });
  }
});

});

