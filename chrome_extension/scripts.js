function getDefinition(info, tab) {
  console.log("Getting definition");
  var word = info.selectionText;
  if (word.indexOf(' ') != -1) {
    alert('More than one word selected!');
  }
  console.log("selected: " + info.selectionText);
  args = [word];
  var server_location = localStorage['server_location'];
  var link = 'http://' + server_location + "/extension/definition";
  $.get(link, {word: word}, function(data) {
    window.showModalDialog("definition.html", [data]);
  });
}

function submitAsRead(info, tab) {
  console.log("Submitting as read");
  console.log("selected: " + info.selectionText);
}

chrome.contextMenus.create({"title": "Get definition",
  "contexts": ["selection"], "onclick": getDefinition});
chrome.contextMenus.create({"title": "Submit as read",
  "contexts": ["selection"], "onclick": submitAsRead});
