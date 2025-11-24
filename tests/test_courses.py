import pytest
from playwright.sync_api import expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    toolbar_title_text = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(toolbar_title_text).to_be_visible()

    empty_view_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_view_icon).to_be_visible()

    empty_view_title_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_view_title_text).to_be_visible()

    empty_view_description_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_view_description_text).to_be_visible()
