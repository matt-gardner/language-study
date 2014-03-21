jQuery.fn.exists = function() {return this.length>0;}

function createDialog() {
  if (window['dialog'] == undefined) {
    console.log("Dialog not created; creating now");
    $('body').append('<div id="ls_dialog" title="Language Study">'
        + '</div>');
    window['dialog'] = $('#ls_dialog').dialog({position:
        {my: "center center", at: "center+20% center-100%"}
    });
    $('.ui-dialog').css("font-size", "small");
  }
  window['dialog'].dialog("open");
}

function getDefinition(selection, localStorage) {
  console.log("Getting definition");
  selection = $.trim(selection);
  if (selection.indexOf(' ') != -1) {
    alert('More than one word selected!');
    return;
  }
  console.log("selected: " + selection);
  var server_location = localStorage['server_location'];
  var username = localStorage['username'];
  var wordlist = localStorage['wordlist'];
  var link = 'http://' + server_location + "/extension/definition";
  link += '/' + username + '/' + wordlist;
  createDialog();
  $('#ls_dialog').append('<hr>');
  $('#ls_dialog').append('<div class="ls_def_waiting">Getting info for '
      + selection + "</div>");
  console.log("Requesting url: " + link);
  $.get(link, {word: selection}, function(data) {
    console.log("Response received");
    $('.ls_def_waiting').remove();
    var newDiv = $('<div>').append(data);
    $('#ls_dialog').append(newDiv);
    $('#ls_dialog').animate({scrollTop: $('#ls_dialog').prop('scrollHeight')},
                            500);
  });
}

function submitAsRead(selection, localStorage) {
  createDialog();
  $('#ls_dialog').append('<hr>');
  $('#ls_dialog').append('<div class="ls_submit_waiting">Submitting paragraph'
      + "</div>");
  console.log("Submitting as read");
  console.log("selected: " + selection);
  var server_location = localStorage['server_location'];
  var username = localStorage['username'];
  var wordlist = localStorage['wordlist'];
  var link = 'http://' + server_location + "/extension/read";
  link += '/' + username + '/' + wordlist;
  console.log("Requesting url: " + link);
  $.get(link, {text: selection}, function(data) {
    console.log("Response received");
    $('.ls_submit_waiting').remove();
    $('#ls_dialog').append('<div>Paragraph submitted</div>');
  });
}

if (options.request == 'definition') {
  getDefinition(options.selection, JSON.parse(options.localStorage));
} else if (options.request == 'submit') {
  submitAsRead(options.selection, JSON.parse(options.localStorage));
}

//@ sourceURL=ls_window.js
