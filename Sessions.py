from requests import Session
from lxml import html


class Sessions(Session):
    def __init__(self):
        self.response = None
        super().__init__()

    def get(self, url, **kwargs):
        self.response = super().get(url, **kwargs)
        return self.response

    def post(self, url, data=None, json=None, **kwargs):
        self.response = super().post(url, data, json, **kwargs)
        return self.response

    @property
    def parsed_response(self):
        if self.response:
            return html.fromstring(self.response.content)
        else:
            return None

    def __del__(self):
        self.response = None
        self.close()

