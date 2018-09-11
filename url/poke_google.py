import googlesearch

if __name__ == '__main__':
    for url in googlesearch.search("galaxy s7 edge 性能", lang="jp", stop=20):
        print(url)
