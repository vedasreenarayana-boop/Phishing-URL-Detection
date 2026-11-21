url = input("Enter a URL: ")

is_suspicious = False

print("\nEntered URL:", url)

if len(url) >100:
    is_suspicious = True
    print("Warning: URL is unusually long!")
else:
    print("url length looks normal")

if "192.168." in url or "10." in url:
    is_suspicious = True
    print("Warning: URL may contain an IP address!")
else:
    print("no ip pattern is detected")

suspicious_keywords = ["login", "verify", "password", "banking", "account"]

for word in suspicious_keywords:
    if word in url.lower():
        is_suspicious = True
        print("Warning: Suspicious keyword detected:", word)

suspicious_characters = ["@", "!"]

for char in suspicious_characters:
    if char in url:
        is_suspicious = True
        print("Warning: Suspicious special character detected:", char)
   
if is_suspicious:
    print("Result: Suspicious URL")
    print("Warning: Avoid opening this URL without verification.")
else:
    print("Result: Potentially Safe URL")
