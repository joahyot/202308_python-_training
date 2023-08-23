# ChatGPT이메일주소체크.py
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.search(pattern, email):
        return True
    else:
        return False

# Sample email addresses
sample_emails = [
    "user@example.com",
    "john.doe@gmail.com",
    "contact@website.org",
    "invalid_email",
    "name.lastname@example.co.uk",
    "12345@yahoo.com",
    "user123@domain",
    "noatsign.com",
    "email@.com",
    "test.email123@subdomain.domain"
]

# Test the sample email addresses
for email in sample_emails:
    print(f"{email} is valid: {is_valid_email(email)}")
