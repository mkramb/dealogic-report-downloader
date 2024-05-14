import os
import asyncio
from playwright.async_api import async_playwright, Playwright

from dealogic_report_downloader.pages.login import LoginPage
from dealogic_report_downloader.pages.reports import ReportsPage


EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
REPORTS = os.environ["REPORTS"]


async def run(playwright: Playwright):
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()

    login_page = LoginPage(page)

    await login_page.navigate()
    await login_page.provide_email(EMAIL)
    await login_page.provide_password(PASSWORD)

    reports_page = ReportsPage(page)

    await reports_page.navigate()
    await reports_page.select_reports(REPORTS)

    await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
