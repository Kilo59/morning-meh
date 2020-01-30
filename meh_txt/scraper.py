import contextlib

import bs4
import requests as r


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers["Content-Type"].lower()
    return (
        resp.status_code == 200
        and content_type is not None
        and content_type.find("html") > -1
    )


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with contextlib.closing(r.get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            return None
    except r.exceptions.RequestException as e:
        print(f"Error during requests to {url} : {e}")
        return None


MEH_URL = "https://meh.com"

raw_html = simple_get(MEH_URL)
html = bs4.BeautifulSoup(raw_html, "html.parser")
article = html.select("article")
h2 = html.select("h2")
features = html.find("section", class_="features")


if __name__ == "__main__":
    print(features)
