function save_options() {
  var server_location = document.getElementById("server-location").value;
  localStorage['server_location'] = server_location;

  var username = document.getElementById("username").value;
  localStorage['username'] = username;

  var wordlist = document.getElementById("wordlist").value;
  localStorage['wordlist'] = wordlist;

  var status = document.getElementById("status");
  status.innerHTML = "Options Saved.";
  setTimeout(function() { status.innerHTML = ""; }, 750);
}

function restore_options() {
  var server_location = localStorage['server_location'];
  if (server_location) {
    var server_location_box = document.getElementById("server-location");
    server_location_box.value = server_location;
  }

  var username = localStorage['username'];
  if (username) {
    var username_box = document.getElementById("username");
    username_box.value = username;
  }

  var wordlist = localStorage['wordlist'];
  if (wordlist) {
    var wordlist_box = document.getElementById("wordlist");
    wordlist_box.value = wordlist;
  }
}

document.addEventListener('DOMContentLoaded', restore_options);
document.querySelector("#save_button").addEventListener('click', save_options);
