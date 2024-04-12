import re


def detect_phishing(url):
    # Check for IP address-like pattern
    ip_pattern = r'(?:\d{1,3}\.){3}\d{1,3}|0x[0-9A-Fa-f]{1,2}\.0x[0-9A-Fa-f]{1,2}\.0x[0-9A-Fa-f]{1,2}\.0x[0-9A-Fa-f]{1,2}'
    if re.search(ip_pattern, url):
        print("Warning: Detected IP address-like pattern in URL. This could indicate a phishing attempt.")
        return True

    # Check for "@" symbol in the URL
    if "@" in url:
        print("Warning: '@' symbol detected in URL. This could indicate a phishing attempt.")
        return True

    # Find the last occurrence of "//" in the URL
    last_double_slash_index = url.rfind("//")

    # Check if the position of the last "//" is greater than 7
    if last_double_slash_index > 7:
        print(
            "Warning: The position of the last occurrence of '//' in the URL is greater than 7. This could indicate a phishing attempt.")
        return True

    # Check if the URL does not start with 'http://' or 'https://'
    if not url.startswith('http://') and not url.startswith('https://'):
        print("Warning: The URL does not start with 'http://' or 'https://'. This could indicate a phishing attempt.")
        return True

    # Check for link shorteners
    if "bit.ly" in url or "tinyurl.com" in url or "goo.gl" in url:
        print("Warning: Detected the presence of a link shortener in the URL. This could indicate a phishing attempt.")
        return True

    # Check for hyphens ("-") in the domain name
    domain = re.findall(r'//([^/]+)', url)
    if domain:
        if "-" in domain[0]:
            print("Warning: Detected hyphens in the domain name. This could indicate a phishing attempt.")
            return True

        # Check for numbers in the domain name
        if any(char.isdigit() for char in domain[0]):
            print("Warning: Detected numbers in the domain name. This could indicate a phishing attempt.")
            return True

        # Check for the maximum number of dots in the domain name
        if domain[0].count(".") > 2:
            print("Warning: The domain name contains more than 2 dots. This could indicate a phishing attempt.")
            return True

    return False


def check_email(email_content):
    print("Checking email...\n")
    urls = re.findall(r'https?://\S+', email_content)
    for url in urls:
        print(url)
        result = detect_phishing(url)
        if result:
            print("Phishing detected!")
        else:
            print("No phishing indicators detected in the URL.")


def check_url(url):
    if url.startswith('http://') or url.startswith('https://'):
        print("Checking URL...\n")
        result = detect_phishing(url)
        if result:
            print("Phishing detected!")
        else:
            print("No phishing indicators detected in the URL.")
    else:
        print("Invalid URL format. Please enter a valid URL.")


# Main menu loop
while True:
    print("\nMenu:")
    print("1. Check Email")
    print("2. Check URL")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        email_content = input("Enter Email content: ")
        check_email(email_content)
    elif choice == '2':
        url = input("Enter the URL: ")
        check_url(url)
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3).")