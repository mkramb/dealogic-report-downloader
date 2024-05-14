from playwright.sync_api import sync_playwright


def download_report():
    with sync_playwright() as play:
        browser = play.chromium.launch()
        page = browser.new_page()

        page.goto("http://playwright.dev")

        print(page.title())
        browser.close()


if __name__ == "__main__":
    download_report()
