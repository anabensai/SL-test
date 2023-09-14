from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.sima-land.ru/#/")
    page.get_by_test_id("nav-item:cabinet").get_by_test_id("link").click()
    page.get_by_test_id("login-field").get_by_test_id("text-field:field").click()
    page.get_by_test_id("login-field").get_by_test_id("text-field:field").fill("qa_test@test.ru")
    page.get_by_test_id("password-field").get_by_test_id("text-field:field").click()
    page.get_by_test_id("password-field").get_by_test_id("text-field:field").fill("qa_test")
    page.get_by_test_id("button").click()
    expect(page).to_have_url("https://www.sima-land.ru/cabinet/")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)