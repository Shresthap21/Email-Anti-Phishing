Our project involves the development of an E-mail phishing detection extension, designed to safeguard individuals from phishing scams. This extension detects potential phishing URLs in emails and web pages by analyzing patterns in the URLs. It aims to enhance online safety by identifying common phishing indicators and providing users with warnings.

How It Works:

-The extension loads when the user opens Gmail in their browser.
-A content script collects all links from the Gmail page.
-The background script analyzes the URLs using predefined phishing detection rules.
-Results are displayed in the popup with clear warnings for potential phishing links.

Installation:

-Clone this repository:
     git clone https://github.com/your-username/folder-name.git
     cd folder-name

-Open Chrome and navigate to chrome://extensions/.
-Enable Developer Mode.
-Click Load unpacked and select the project folder.
-The extension will be added to Chrome with the name Phishing Detector.

Usage:

-Open Gmail in your browser.
-Click on the Phishing Detector extension icon in the Chrome toolbar.
-Click the Analyze button to scan all links on the current page.
-View the analysis results in the popup:
     Red-highlighted warnings indicate potential phishing links.
     Green-highlighted messages indicate no phishing indicators.
     
Files and Structure:

manifest.json: Defines the extension's configuration, permissions, and scripts.
background.js: Contains the service worker logic for URL analysis.
content.js: Collects URLs from Gmail's webpage.
popup.html: Displays the UI for analyzing results.
styles.css: Styles for the popup, including highlight colors for results.
icons/: Includes icons used in the extension.

Technology Stack:

-JavaScript: Core logic for URL analysis and Chrome extension functionality.
-HTML/CSS: For creating the popup interface.
-Chrome Extension APIs: For content script communication and executing scripts.

Future Enhancements:

-Implement advanced phishing detection using machine learning.
-Add support for analyzing email headers and attachments.
-Extend compatibility to other webmail platforms like Outlook and Yahoo Mail.
-Integrate sandboxing for safer phishing detection.
