def email_slicer(email):
    try:
        username, domain = email.split('@')
        return username, domain
    except ValueError:
        return None, None
if __name__ == "__main__":
    email = input("Enter your email address: ")
    username, domain = email_slicer(email)    
    if username and domain:
        print(f"Username: {username}")
        print(f"Domain: {domain}")
    else:
        print("Invalid email address format.")