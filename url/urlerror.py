import urllib

if __name__ == '__main__':
    try:
        res = urllib.request.urlopen("http://notexist")
    except urllib.error.URLError as e:
        print(e.reason)
