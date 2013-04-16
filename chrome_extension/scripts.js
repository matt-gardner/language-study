function getDefinition(info, tab) {
  console.log("Getting definition");
  var word = info.selectionText;
  if (word.indexOf(' ') != -1) {
    alert('More than one word selected!');
    return;
  }
  console.log("selected: " + info.selectionText);
  var server_location = localStorage['server_location'];
  var username = localStorage['username'];
  var wordlist = localStorage['wordlist'];
  var link = 'http://' + server_location + "/extension/definition";
  link += '/' + username + '/' + wordlist;
  console.log("Requesting url: " + link);
  $.get(link, {word: word}, function(data) {
    console.log("Response received");
    var definition = data;
    w = chrome.windows.create({
        url: chrome.extension.getURL("definition.html"),
        type: "popup",
        focused: true,
        width: 400,
        height: 400,
    });
    chrome.extension.sendMessage({type: 'definition', definition: data});
  });
}

function submitAsRead(info, tab) {
  alert("Submitting");
  console.log("Submitting as read");
  console.log("selected: " + info.selectionText);
  var text = info.selectionText;
  var server_location = localStorage['server_location'];
  var username = localStorage['username'];
  var wordlist = localStorage['wordlist'];
  var link = 'http://' + server_location + "/extension/read";
  link += '/' + username + '/' + wordlist;
  console.log("Requesting url: " + link);
  $.get(link, {text: text}, function(data) {
    console.log("Response received");
    alert("Submit successful");
  });
}

chrome.contextMenus.create({"title": "Get definition",
  "contexts": ["selection"], "onclick": getDefinition});
chrome.contextMenus.create({"title": "Submit as read",
  "contexts": ["selection"], "onclick": submitAsRead});
