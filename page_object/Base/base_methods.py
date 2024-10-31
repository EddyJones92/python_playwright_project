from playwright.sync_api import Page
from playwright.sync_api import expect
import re


class BaseMethods:

    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, path):
        expect(self.page).to_have_url(re.compile(path))
