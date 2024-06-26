import json
from playwright.sync_api import Page


class DealogicLoginPage:
    def __init__(self, page: Page):
        self.page = page

    async def navigate(self):
        await self.page.goto("https://cortex.dealogic.com")
        await self.page.wait_for_load_state()

    async def provide_email(self, email):
        await self.page.locator('input[name="email"]').fill(email)
        await self.page.get_by_role("button", name="Continue").click()

        button_login = self.page.locator('button[value="Log In"]')

        await button_login.wait_for(state="visible")
        await button_login.click()

        await self.page.wait_for_load_state("load")

    async def provide_password(self, password):
        input_password = self.page.locator('input[id="password"]')
        button_submit = self.page.locator('a[id="submitButton"]')

        await input_password.wait_for(state="visible")
        await input_password.fill(password)
        await button_submit.click()

        await self.page.wait_for_load_state()

    async def retrieve_access_token(self):
        # we need to wait for sessionStorage to have user data, which is an async process
        # and it eventually made available on the web client
        await self.page.wait_for_function("() => {{ return Object.keys(sessionStorage).find(row => row.startsWith('oidc.user')); }}")

        # data in sessionStorage is coded as JSON, 
        # this is unpacking user entry with access_token
        user_data = await self.page.evaluate("() => sessionStorage[Object.keys(sessionStorage).find(row => row.startsWith('oidc.user'))]")
        access_token = json.loads(user_data)['access_token']

        return access_token

