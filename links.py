import webbrowser

favorite_websites = {
    'Google': 'https://www.google.com',
    'Facebook': 'https://www.facebook.com',
    'Twitter': 'https://www.twitter.com',
    'GitHub': 'https://www.github.com'
}

def Firefox(url):
    webbrowser.get("C:\Program Files\Google\Chrome\Application\chrome.exe %s").open(url)
          