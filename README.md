
import re

def contains_url(message):
    # Regular expression to match URLs
    url_pattern = r"(http|https)://[^\s]+"
    return bool(re.search(url_pattern, message))

def contains_phone_number(message):
    # Regular expression to match phone numbers
    phone_number_pattern = r"\b\d{10}\b"
    return bool(re.search(phone_number_pattern, message))

def contains_financial_terms(message):
    # List of financial terms
    financial_terms = ["bank", "account", "password", "PIN", "SSN"]
    for term in financial_terms:
        if term in message.lower():
            return True
    return False

def contains_urgency_or_threats(message):
    # List of urgency and threat keywords
    urgency_keywords = ["urgent", "lockout", "security breach", "legal action"]
    for keyword in urgency_keywords:
        if keyword in message.lower():
            return True
    return False

def contains_grammatical_errors(message):
    # Check for common grammatical errors
    # For simplicity, we can assume that messages containing all uppercase characters have poor grammar
    if message.isupper():
        return True
    return False

def contains_spoofed_sender_information(sender):
    # Check if sender information appears spoofed or suspicious
    # This could involve checking against a list of known legitimate sender IDs or domains
    known_sender_domains = ["amazon.com", "bankofamerica.com", "paypal.com"]
    if sender.lower() not in known_sender_domains:
        return True
    return False

def is_unsolicited_message(sender):
    # Check if the message is from an unknown or unsolicited sender
    # This could involve comparing against a whitelist of known contacts
    known_contacts = ["+1234567890", "+1987654321"]
    if sender not in known_contacts:
        return True
    return False

def contains_phishing_like_content(message):
    # Check for phishing-like content such as requests for personal information or verification codes
    phishing_keywords = ["verify", "confirm", "click", "login"]
    for keyword in phishing_keywords:
        if keyword in message.lower():
            return True
    return False

def contains_unusual_requests(message):
    # Check for unusual requests such as downloading attachments or providing sensitive information
    unusual_keywords = ["download", "attachment", "ssn", "password"]
    for keyword in unusual_keywords:
        if keyword in message.lower():
            return True
    return False

def contains_offers_and_prizes(message):
    # Check for messages offering prizes, rewards, or lottery winnings
    offer_keywords = ["prize", "reward", "winner", "lottery"]
    for keyword in offer_keywords:
        if keyword in message.lower():
            return True
    return False

def detect_smishing(message, sender):
    # Combine all features to detect smishing
    return any([
        contains_url(message),
        contains_phone_number(message),
        contains_financial_terms(message),
        contains_urgency_or_threats(message),
        contains_grammatical_errors(message),
        contains_spoofed_sender_information(sender),
        is_unsolicited_message(sender),
        contains_phishing_like_content(message),
        contains_unusual_requests(message),
        contains_offers_and_prizes(message)
    ])

if  __name__ == "__main__":
    # Take input from the user for message and sender information
    message = input("Enter the message: ")
    sender = input("Enter the sender information: ")
    
    # Check if message is a smishing attempt
    if detect_smishing(message, sender):
        print("Potential smishing detected!")
    else:
        print("Not a smishing attempt.")
