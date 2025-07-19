from playwright.sync_api import sync_playwright

def scrape_url(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, timeout=30000)
            html_content = page.content()
            browser.close()
            return html_content
    except Exception as e:
        print(f"Error fetching URL {url}: {e}")
        return None