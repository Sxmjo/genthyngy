import requests
import webbrowser

MENU = {
    "1": ("not done yet", "https://www.youareanidiot.cc"),
    "2": ("not done yet", "https://www.youareanidiot.cc"),
    "3": ("not done yet", "https://www.youareanidiot.cc")
}

def show_menu():
    print("\nSelect an option:\n")
    for key, (name, _) in MENU.items():
        print(f"{key}. {name}")

    choice = input("\nEnter number: ").strip()

    if choice in MENU:
        name, url = MENU[choice]
        print(f"Opening {name}...")
        webbrowser.open(url)
    else:
        print("Invalid choice")


def main():
    code = input("Enter access code: ").strip()

    try:
        r = requests.post("http://127.0.0.1:5000/validate", json={"code": code})
        data = r.json()

        print(data.get("message", ""))

        if data.get("valid"):
            show_menu()
        else:
            print("Access denied")

    except Exception as err:
        print("Could not reach server:", err)


if __name__ == "__main__":
    main()