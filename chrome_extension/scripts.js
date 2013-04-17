var jqueryui = 'jquery-ui-1.10.2.custom.min.js';
var jquerycss = 'jquery-ui-1.10.2.custom.min.css';
var jquery = 'jquery-1.9.1.min.js';

function getDefinition(info, tab) {
  console.log("Injecting 'getDefinition' script");
  var code = "var options = {request: 'definition', selection: '";
  code += info.selectionText + "', localStorage: '";
  code += JSON.stringify(localStorage) + "'};";
  chrome.tabs.executeScript(null, {file: jquery}, function() {
    chrome.tabs.executeScript(null, {file: jqueryui}, function() {
      chrome.tabs.insertCSS(null, {file: jquerycss}, function() {
        chrome.tabs.executeScript(null, {code: code}, function() {
          chrome.tabs.executeScript(null, {file: "window.js"});
        });
      });
    });
  });
};

function submitAsRead(info, tab) {
  console.log("Injecting 'submitAsRead' script");
  var code = "var options = {request: 'submit', selection: '";
  var text = info.selectionText.replace('"', '');
  text = text.replace("'", '');
  text = text.replace(";", '');
  text = text.replace("}", '');
  text = text.replace("{", '');
  code += text + "', localStorage: '";
  code += JSON.stringify(localStorage) + "'};";
  console.log(code);
  chrome.tabs.executeScript(null, {file: jquery}, function() {
    chrome.tabs.executeScript(null, {file: jqueryui}, function() {
      chrome.tabs.insertCSS(null, {file: jquerycss}, function() {
        chrome.tabs.executeScript(null, {code: code}, function() {
          chrome.tabs.executeScript(null, {file: "window.js"});
        });
      });
    });
  });
};

chrome.contextMenus.create({"title": "Get definition",
  "contexts": ["selection"], "onclick": getDefinition});
chrome.contextMenus.create({"title": "Submit as read",
  "contexts": ["selection"], "onclick": submitAsRead});
