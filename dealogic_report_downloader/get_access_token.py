import os
import asyncio
from playwright.async_api import async_playwright, Playwright

from dealogic_report_downloader.pages.login import LoginPage

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]


async def run(playwright: Playwright):
    browser = await playwright.chromium.launch()
    page = await browser.new_page()

    login_page = LoginPage(page)

    await login_page.navigate()
    await login_page.provide_email(EMAIL)
    await login_page.provide_password(PASSWORD)

    access_token = await login_page.retrieve_access_token()

    print("access_token:\n")
    print(access_token)

    await page.close()


async def main():
    print("Retrieving access_token for provided credentials ...\n")

    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
