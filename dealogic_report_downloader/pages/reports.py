from playwright.sync_api import Page


REPORTS_URL = 'https://cortex.dealogic.com/?page={"type":"mr","params":[]}'


class ReportsPage:
    def __init__(self, page: Page):
        self.page = page

    async def navigate(self):
        await self.page.goto(REPORTS_URL)
        await self.page.wait_for_load_state()

    async def select_reports(self, path):
        view_reports = self.page.get_by_text("View All Reports")
        my_reports = self.page.get_by_text("My Reports")

        await view_reports.wait_for(state="visible")
        await view_reports.click()

        await my_reports.wait_for(state="visible")
        await my_reports.click()
