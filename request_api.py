import requests
from bs4 import BeautifulSoup

# r = requests.get("https://www.bbc.co.uk/iplayer/live/bbnews")
#
# print(f"The status code is {r.status_code}.")
# # should give us status code only
#
# if r.status_code in range(200, 299):
#     print(f"The server is live. Status code: {r.status_code}")
#     contents = r.content.decode("utf-8")  # get the content from the web-app endpoint
#     print(r.headers.values())
#     soup = BeautifulSoup(contents)
#     print(soup.prettify())
# else:
#     print(f"The server is not live. Status code: {r.status_code}")

# if r:  # what is it checking?
#     print("Success")
# elif r == 404:  #
#     print("Unsuccessful")
# else:
#     print(f"Oops! Status code: {r.status_code}")


class WebScraper:
    def __init__(self, url):
        """Retrieves the website"""
        self.url = url
        self.r = requests.get(self.url)
    def status_code_check(self):
        """Returns the status code with a message"""
        if self.r:
            return f"The server is live. Status code: {self.r.status_code}"
        return f"The server is unavailable. Status code: {self.r.status_code}"

    def get_content(self):
        """Processes the content and parses HTML"""
        contents = self.r.text
        soup = BeautifulSoup(contents)
        return soup.prettify()


bbc = WebScraper("https://www.bbc.co.uk/")
print(bbc.status_code_check())
print(bbc.get_content())
