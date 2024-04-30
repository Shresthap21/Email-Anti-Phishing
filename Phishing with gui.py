import tkinter as tk
import re
import csv

def detect_phishing(url):
    ip_pattern = r'(?:\d{1,3}\.){3}\d{1,3}|0x[0-9A-Fa-f]{1,2}\.0x[0-9A-Fa-f]{1,2}\.0x[0-9A-Fa-f]{1,2}\.0x[0-9A-Fa-f]{1,2}'
    if re.search(ip_pattern, url):
        return "Warning: Detected IP address-like pattern in URL. This could indicate a phishing attempt."

        if "@" in url:
            return "Warning: '@' symbol detected in URL. This could indicate a phishing attempt."

    last_double_slash_index = url.rfind("//")
    if last_double_slash_index > 7:
        return "Warning: The position of the last occurrence of '//' in the URL is greater than 7. " \
               "This could indicate a phishing attempt."

    if not url.startswith('http://') and not url.startswith('https://'):
        return "Warning: The URL does not start with 'http://' or 'https://'. This could indicate a phishing attempt."

    if "bit.ly" in url or "tinyurl.com" in url or "goo.gl" in url:
        return "Warning: Detected the presence of a link shortener in the URL. " \
               "This could indicate a phishing attempt."

    domain = re.findall(r'//([^/]+)', url)
    if domain:
        if "-" in domain[0]:
            return "Warning: Detected hyphens in the domain name. This could indicate a phishing attempt."

        if any(char.isdigit() for char in domain[0]):
            return "Warning: Detected numbers in the domain name. This could indicate a phishing attempt."

        if domain[0].count(".") > 2:
            return "Warning: The domain name contains more than 2 dots. This could indicate a phishing attempt."

    if "favicon.ico" in url:
        return "Warning: Detected 'favicon.ico' in the URL. Phishing websites often use fake favicons."

    if len(url) >= 54:
        return "Warning: The URL length is greater than or equal to 54 characters. Phishers may use long URLs to hide suspicious parts."

    return "No phishing indicators detected in the URL."

def check_phishing_with_csv(url, csv_file_path):
    try:
        with open(csv_file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row and row[0] == url:
                    return True
    except FileNotFoundError:
        print("Error: CSV file not found.")
    except csv.Error as e:
        print(f"CSV Error: {e}")

    return False

def check_email():
    email_content = email_entry.get("1.0", tk.END)
    result_display.delete("1.0", tk.END)
    result_display.insert(tk.END, "Checking email...\n")

    if "https://" in email_content or "http://" in email_content:
        urls = re.findall(r'https?://\S+', email_content)
        for url in urls:
            result_display.insert(tk.END, url + "\n")
            result_display.insert(tk.END, detect_phishing(url) + "\n")
            if detect_phishing(url) == "No phishing indicators detected in the URL.":
                is_phishing = check_phishing_with_csv(url, csv_file_path)
                if is_phishing:
                    result_display.insert(tk.END, "Phishing found using BLacklist\n")
                else:
                    result_display.insert(tk.END, "Non-Phishing\n")
    else:
        result_display.insert(tk.END, "No link included in the email.\n")

def check_url():
    url = url_entry.get()
    result_display.delete("1.0", tk.END)
    result_display.insert(tk.END, "Checking URL...\n")
    if url.startswith('http://') or url.startswith('https://'):
        result_display.insert(tk.END, detect_phishing(url) + "\n")
        if detect_phishing(url) == "No phishing indicators detected in the URL.":
            is_phishing = check_phishing_with_csv(url, csv_file_path)
            if is_phishing:
                result_display.insert(tk.END, "Phishing found using BLacklist\n")
            else:
                result_display.insert(tk.END, "Non-Phishing\n")
    else:
        result_display.insert(tk.END, "Invalid URL format. Please enter a valid URL.\n")

def open_email_window():
    email_window = tk.Toplevel(root)
    email_window.title("Check Email")
    email_window.geometry("800x600")

    email_label = tk.Label(email_window, text="Enter Email content:")
    email_label.pack()
    global email_entry
    email_entry = tk.Text(email_window, height=10, width=70)
    email_entry.pack()

    # Define the CSV file path
    global csv_file_path
    csv_file_path = r'C:\Users\raviy\Downloads\abd\verified_online.csv'

    email_button = tk.Button(email_window, text="Check Email", command=check_email)
    email_button.pack()

    global result_display
    result_display = tk.Text(email_window, height=10, width=70)
    result_display.pack()

def open_url_window():
    url_window = tk.Toplevel(root)
    url_window.title("Check URL")
    url_window.geometry("800x600")

    url_label = tk.Label(url_window, text="Enter the URL:")
    url_label.pack()
    global url_entry
    url_entry = tk.Entry(url_window, width=50)
    url_entry.pack()

    # Define the CSV file path
    global csv_file_path
    csv_file_path = r'C:\Users\raviy\Downloads\abd\verified_online.csv'

    url_button = tk.Button(url_window, text="Check URL", command=check_url)
    url_button.pack()

    global result_display
    result_display = tk.Text(url_window, height=10, width=70)
    result_display.pack()

def welcome_screen():
    welcome_frame = tk.Frame(root)
    welcome_frame.pack()

    welcome_label = tk.Label(welcome_frame, text="Welcome to Phishing Detector!", font=("Arial", 20))
    welcome_label.pack(pady=20)

    email_button = tk.Button(welcome_frame, text="Check Email", command=open_email_window, width=20)
    email_button.pack()

    url_button = tk.Button(welcome_frame, text="Check URL", command=open_url_window, width=20)
    url_button.pack()

    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = int((screen_width - root.winfo_width()) / 2)
    y_coordinate = int((screen_height - root.winfo_height()) / 2)
    root.geometry(f"{root.winfo_width()}x{root.winfo_height()}+{x_coordinate}+{y_coordinate}")

root = tk.Tk()
root.title("Phishing Detector")
root.geometry("400x300")

welcome_screen()

root.mainloop()
