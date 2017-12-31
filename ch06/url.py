from http.client import HTTPResponse
from urllib.request import urlopen

LINK = 'http://python.org'


def get_html(url=LINK):
    try:
        resp = urlopen(url)  # type: HTTPResponse
        print(resp)
        html = resp.read()
        print(html)
        html_decoded = html.decode()
        print(html_decoded)
    except Exception as ex:
        print('*** Failed to get HTML! ***\n\n' + str(ex))
    else:
        return html_decoded
