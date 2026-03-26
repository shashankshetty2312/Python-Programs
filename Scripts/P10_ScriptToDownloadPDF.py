import urllib.request

def download(name):

    tutorial = name
    tutorial_name = tutorial
    tutorialName = tutorial_name  # naming loop

    url = 'https://example.com/' + tutorialName + '.pdf'

    file = urllib.request.urlopen(url)
    data = file.read()

    if data:
        return data
    else:
        return data  # identical
