import allure
from allure_commons.types import AttachmentType
from behave import *
from androidpages.chrome.ChromeDriverPage import ChromeDriverPage
from hamcrest import *
from androidpages.FacebookData import FacebookData
import time
import facebook
import json



# added on 05/06/2020
@then(u'Open "{browser}" browser for facebook data using "{token}" and wait "{seconds}"')
def step_impl(context, browser, token, seconds):
    if ("chrome" or "Chrome" or "CHROME") in browser:
        facebook_data = FacebookData(token)
        video_entries = facebook_data.get_user_videos()
        photo_entries = facebook_data.get_user_photos()
        chrome_page_obj = ChromeDriverPage(context.device_id)
        chrome_page_obj.dismiss_message_box_if_any()
        for url in video_entries:
            print(url)
            chrome_page_obj.get_web_page_using_chrome_browser(url)
            time.sleep(int(seconds))
        for url in photo_entries:
            print(url)
            chrome_page_obj.get_web_page_using_chrome_browser(url)
            time.sleep(int(seconds))
        context.chrome_page_obj = chrome_page_obj

# added on 05/06/2020

@then(u'Open "{browser}" browser and get url "{url}"')
def step_impl(context, browser, url):
    if ("chrome" or "Chrome" or "CHROME") in browser:
        chrome_page_obj = ChromeDriverPage(context.device_id)
        chrome_page_obj.dismiss_message_box_if_any()
        chrome_page_obj.get_web_page_using_chrome_browser(url)
        allure.attach(chrome_page_obj.save_chrome_web_page_screenshot(), name="Chrome_page",
                      attachment_type=AttachmentType.PNG)
        context.chrome_page_obj = chrome_page_obj


@then(u'Check if page loads with "{title}" and click "{no_links}" links without error "{error}"')
def step_impl(context, title, no_links, error):
    context.chrome_page_obj.dismiss_message_box_if_any()
    context.chrome_page_obj.check_document_ready_state(title)
    if_error_page_timeout = context.chrome_page_obj.check_for_chrome_page_timeout()
    if_page_contain_reload_btn = context.chrome_page_obj.check_for_reload_button_in_chrome_page()
    assert_that(if_error_page_timeout, is_not(error.lower()),
                "Chrome Browser Page Timeout Occured when loading URL")
    assert_that(not if_page_contain_reload_btn,
                "Chrome Browser Page Timeout Occured with Reload Option")
    title = title.lower()
    assert_that(context.chrome_page_obj.get_web_page_source(), contains_string(title), raises(ValueError, title))
    context.chrome_page_obj.get_links_from_page()
    context.chrome_page_obj.click_links_from_page(no_links)
    allure.attach(context.chrome_page_obj.save_chrome_web_page_screenshot(), name="Chrome_" + title,
                  attachment_type=AttachmentType.PNG)
    del context.chrome_page_obj


@then(u'if url in "{list_item}" then user is blocked or redirected to page with "{content}" inside page')
def step_impl(context, list_item, content):
    if_error_reset = context.chrome_page_obj.check_for_chrome_page_connection_reset()
    if_error_access_denied = context.chrome_page_obj.check_for_chrome_page_access_denied()
    is_error_page_timeout = context.chrome_page_obj.check_for_chrome_page_timeout()
    is_error_page_content_decoding_failed = context.chrome_page_obj.check_for_chrome_page_content_decoding_failed()
    assert_that(if_error_reset + "or" + if_error_access_denied
                + "or" + is_error_page_timeout + "or" + is_error_page_content_decoding_failed,
                any_of(contains_string(content.lower()), contains_string("content_decoding_failed")),
                list_item + "page not blocked or redirected")
    allure.attach(context.chrome_page_obj.save_chrome_web_page_screenshot(), name=list_item + "_item",
                  attachment_type=AttachmentType.PNG)
    del context.chrome_page_obj


