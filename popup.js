document.getElementById('analyzeButton').addEventListener('click', function() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      chrome.scripting.executeScript({
        target: { tabId: tabs[0].id },
        function: extractUrls
      }, (result) => {
        if (chrome.runtime.lastError) {
          console.error(chrome.runtime.lastError.message);
          document.getElementById('result').innerText = "Error: " + chrome.runtime.lastError.message;
        } else if (result && result[0] && result[0].result) {
          const urls = result[0].result;
  
          chrome.runtime.sendMessage({ action: "analyzeUrls", urls: urls }, (response) => {
            document.getElementById('result').innerHTML = ''; 
            response.analysis.forEach(item => {
              const span = document.createElement('span');
              span.textContent = `URL: ${item.url}\nResult: ${item.result}\n\n`;
  
              if (item.result.includes("phishing attempt")) {
                span.classList.add('highlight-red'); 
              } else {
                span.classList.add('highlight-green'); 
              }
              document.getElementById('result').appendChild(span);
            });
          });
        } else {
          document.getElementById('result').innerText = "No URLs found.";
        }
      });
    });
  });
  
  function extractUrls() {
    const links = document.querySelectorAll('a');
    let urls = [];
  
    links.forEach(link => {
      let url = link.href;
  
      if (!url.includes("mail.google.com") && 
          !url.includes("accounts.google.com") && 
          !url.includes("/mail/u/0/") && 
          !url.includes("/mail/u/1/") &&
          !url.includes("https://support.google.com/mail/answer/8767?src=sl&hl=en-GB?") && 
          !url.includes("https://support.google.com/mail?p=fix-gmail-loading&authuser=0") && 
          !url.includes("https://support.google.com/mail/answer/90559?hl=en-GB") && 
          !url.includes("https://www.google.co.in/intl/en-GB/about/products?tab=mh") && 
          !url.includes("https://drive.google.com/u/0/settings/storage?hl=en-") && 
          !url.includes("https://www.google.com/intl/en-GB/policies/terms/") && 
          !url.includes("https://www.google.com/gmail/about/policy/") && 
          !url.includes("https://www.google.com/intl/en-GB/policies/privacy/")) {
        urls.push(url);
      }
    });
  
    return urls;
  }
  