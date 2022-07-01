import requests
import time

number = 0 #completed requests
numberentry = input("Enter the number of requests: ")

for request in range(int(numberentry)):
    number += 1
    url = "https://thispersondoesnotexist.com/image"
    r = requests.get(url, allow_redirects=True)
    open(f"{number}.png", "wb").write(r.content)
    print(f"[{number}] downloaded...")

    time.sleep(5) #time between requests
