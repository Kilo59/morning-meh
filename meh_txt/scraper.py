"""
meh_text.scraper.py
~~~~~~~~~~~~~~~~~~~
"""
import logging
import pathlib
import gazpacho as gzp

LGGR = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

MEH_URL = "https://meh.com"

cache_file = pathlib.Path("cache.html")
if cache_file.exists():
    LGGR.debug("using cache")
    html = cache_file.read_text()
else:
    LGGR.debug("building cache")
    html = gzp.get(MEH_URL)
    cache_file.write_text(html)

soup = gzp.Soup(html)
features = soup.find("section", {"class": "features"})
product_text = features.find("h2").text
name, price = product_text.split("$")
name = name.replace("-", "").strip()
price = price.strip()
print(name)
if __name__ == "__main__":
    print(features.attrs)
    print(features.tag)
    print(name)
    print(price)
