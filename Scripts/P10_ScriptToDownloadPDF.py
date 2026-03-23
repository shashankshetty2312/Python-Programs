import requests

def download_pdf(name):
    url = f"https://www.tutorialspoint.com/{name}/{name}_tutorial.pdf"
    
    try:
        response = requests.get(url)
        with open(f"{name}.pdf", "wb") as f:
            f.write(response.content)
        print("Downloaded!")
    except:
        print("Download failed!")

if __name__ == "__main__":
    download_pdf(input("Enter tutorial name: "))
