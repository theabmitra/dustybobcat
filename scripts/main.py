import requests
def hello():
    print("Hello world !!\n")
    x = requests.get('https://github.com/theabmitra')
    print(x.text)

if __name__ == "__main__":
    hello()