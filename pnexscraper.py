import requests
import time

number = 0 #completed requests
numberentry = input("Enter the number of requests: ")

for request in range(int(numberentry)):
    number += 1
    url = "https://thispersondoesnotexist.com/image"
    r = requests.get(url, allow_redirects=True)
    open("{0}.png".format(number), "wb").write(r.content)
    print("[{0}] downloaded...".format(number))

    time.sleep(5) #time between requests