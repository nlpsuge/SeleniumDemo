from selenium import webdriver
from selenium.common.exceptions import JavascriptException


class ModifyPageSourceTest:

    def __init__(self):
        self.firefox_binary = '/usr/bin/firefox'
        self.executable_path = './geckodriver'
        self.my_driver = None
        self.url = 'https://duckduckgo.com/?q=saying&iax=images&ia=images&iai=https%3A%2F%2Fwww.rd.com%2Fwp-content%2Fuploads%2Fsites%2F2%2F2016%2F04%2Fcommon-sayings-nonsense-money-happiness.jpg'
        self.ddg_heading_xpath = ".//div[@id='zci-images']/div[2]/div[@class='detail__wrap']/div[1]/div[contains(@style, 'transform: translateX(0px);')]/div/div[2]/div/h5/a"

    def _run_firefox(self):
        print('opening browser')

        # set open link in current tab
        options = webdriver.FirefoxOptions()
        options.set_preference('browser.link.open_newwindow', 1)
        options.set_preference('browser.tabs.loadDivertedInBackground', False)

        self.my_driver = webdriver.Firefox(executable_path=self.executable_path,
                                     firefox_binary=self.firefox_binary,
                                     firefox_options=options)

    def _process_page_source(self):
        self.my_driver.execute_script('window.open("%s")' % self.url)
        while 1:
            try:
                heading = self.my_driver.find_element_by_xpath(self.ddg_heading_xpath)

                if self._element_exist_by_id('imagepicker_identity_id') is False:
                    tag_check_box = "<input id=\"imagepicker_identity_id\" />"
                    tag_a = heading.find_element_by_xpath("..")
                    self.my_driver.execute_script("var ele=arguments[0]; ele.innerHTML = '%s';"
                                                  % (tag_a.get_attribute('innerHTML') + tag_check_box), tag_a)

            except JavascriptException:
                import traceback
                print(traceback.format_exc())
                break
            except:
                pass

    def _element_exist_by_id(self, id):
        try:
            self.my_driver.find_element_by_id(id)
            return True
        except:
            return False


mpst = ModifyPageSourceTest()

mpst._run_firefox()
mpst._process_page_source()

