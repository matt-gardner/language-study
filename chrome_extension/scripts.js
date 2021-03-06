var jqueryui = 'jquery-ui-1.10.2.custom.min.js';
var jquerycss = 'jquery-ui-1.10.2.custom.min.css';
var jquery = 'jquery-1.9.1.min.js';

function getDefinition(info, tab) {
  var code = "var options = {request: 'definition', selection: '";
  code += info.selectionText + "', localStorage: '";
  code += JSON.stringify(localStorage) + "'};";
  injectCode(code);
};

function injectCode(code) {
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
  var text = sanitizeText(info.selectionText);
  code += text + "', localStorage: '";
  code += JSON.stringify(localStorage) + "'};";
  injectCode(code);
};

function sanitizeText(_text) {
  var text = _text.replace(/"/g, '');
  text = text.replace(/'/g, '');
  text = text.replace(/;/g, '');
  text = text.replace(/\{/g, '');
  text = text.replace(/\}/g, '');
  return text;
}

chrome.contextMenus.create({"title": "Get definition",
  "contexts": ["selection"], "onclick": getDefinition});
chrome.contextMenus.create({"title": "Submit as read",
  "contexts": ["selection"], "onclick": submitAsRead});

chrome.commands.onCommand.addListener(function(command) {
  if (command === "definition") {
    var code = "var options = {request: 'definition',";
    code += " localStorage: '";
    code += JSON.stringify(localStorage) + "'};";
    code += "options['selection'] = window.getSelection().toString();";
    injectCode(code);
  } else if (command === "submit_as_read") {
    var code = "var options = {request: 'submit',";
    code += " localStorage: '";
    code += JSON.stringify(localStorage) + "'};";
    code += "options['selection'] = window.getSelection().toString();";
    injectCode(code);
  }
});
