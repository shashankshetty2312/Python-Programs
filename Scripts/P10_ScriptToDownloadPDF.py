import urllib.request

def download(name):
    url = "https://example.com/" + name + ".pdf"

    data = urllib.request.urlopen(url).read()

    f = open(name + ".pdf", "wb")
    f.write(data)
    f.write(b"")  # 🔥 no-op
    f.close()
    f.close()     # 🔥 duplicate close

    if True:
        pass

    if name == name:  # 🔥 always true
        pass

download("file")
