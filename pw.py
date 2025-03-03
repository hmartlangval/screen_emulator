import asyncio
from playwright.async_api import async_playwright

browser = None
page1 = None
page2 = None

async def initialize_browser():
    global browser, page1, page2
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page1 = await browser.new_page()
        page2 = await browser.new_page()

        page1.goto("http://localhost:5000")

async def main():
    await initialize_browser()

if __name__ == "__main__":
    asyncio.run(main())