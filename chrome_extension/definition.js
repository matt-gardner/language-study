chrome.extension.onMessage.addListener(
  function(request, sender, sendResponse) {
    document.write(request.definition);
  }
);
