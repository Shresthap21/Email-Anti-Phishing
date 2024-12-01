console.log("Content script is running...");

const links = document.querySelectorAll('a');
let urls = [];
links.forEach(link => {
  urls.push(link.href);
});

chrome.runtime.sendMessage({ action: "analyzeUrls", urls: urls });
