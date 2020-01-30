import gazpacho as gzp

MEH_URL = "https://meh.com"
html = gzp.get(MEH_URL)
soup = gzp.Soup(html)
features = soup.find("section", {"class": "features"})
if __name__ == "__main__":
    print(features)
