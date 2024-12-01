chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "analyzeUrls" && message.urls && message.urls.length > 0) {
    let analysisResults = [];
    
    message.urls.forEach(url => {
      const result = detectPhishing(url);
      analysisResults.push({ url: url, result: result });
    });

    sendResponse({ analysis: analysisResults });
  }
  return true; 
});

function detectPhishing(url) {
  const ipPattern = /(?:\d{1,3}\.){3}\d{1,3}|0x[0-9A-Fa-f]{1,2}\.0x[0-9A-Fa-f]{1,2}\.0x[0-9A-Fa-f]{1,2}\.0x[0-9A-Fa-f]{1,2}/;

  if (ipPattern.test(url)) {
    return "Warning: Detected IP address-like pattern in URL. This could indicate a phishing attempt.";
  }

  if (url.includes("@")) {
    return "Warning: '@' symbol detected in URL. This could indicate a phishing attempt.";
  }

  const lastDoubleSlashIndex = url.lastIndexOf("//");
  if (lastDoubleSlashIndex > 7) {
    return "Warning: The last occurrence of '//' is beyond the domain part. This could indicate a phishing attempt.";
  }

  if (!url.startsWith("http://") && !url.startsWith("https://")) {
    return "Warning: The URL does not start with 'http://' or 'https://'. This could indicate a phishing attempt.";
  }

  const suspiciousDomains = ["bit.ly", "tinyurl.com", "goo.gl"];
  if (suspiciousDomains.some(domain => url.includes(domain))) {
    return "Warning: Detected link shortener. This could indicate a phishing attempt.";
  }

  const domainPattern = /\/\/([^/]+)/;
  const domainMatch = url.match(domainPattern);
  if (domainMatch && domainMatch[1]) {
    const domain = domainMatch[1];

    if (domain.includes("-")) {
      return "Warning: Hyphens detected in the domain name. This could indicate a phishing attempt.";
    }

    if (/[0-9]/.test(domain)) {
      return "Warning: Numbers detected in the domain name. This could indicate a phishing attempt.";
    }

    if (domain.split('.').length > 3) {
      return "Warning: The domain name contains more than 2 dots. This could indicate a phishing attempt.";
    }
  }

  return "No phishing indicators detected.";
}

