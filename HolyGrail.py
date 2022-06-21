# -*- coding: utf-8 -*-
from robot.api.deco import keyword

from Zoomba.GUILibrary import GUILibrary
from JUNOone.JUNOone import JUNOone
from time import sleep

from datetime import datetime
name = str(datetime.now())


class HolyGrail(GUILibrary, JUNOone):
    """ HolyGrail of all. 
    """

    def __init__(self):
        super(HolyGrail, self).__init__()

        self.juno_sign_in_page_name = u'xpath=//input[@name="email"]'
        self.juno_sign_in_page_password = u'xpath=//input[@name="password"]'
        self.juno_sign_in_button = u'xpath=//button[@class="el-button el-button--primary el-button--medium"]'
        self.juno_dashboard_button_plus = u'xpath=//button[@id="add-items-btn"]'
        self.juno_dashboard_plus_menu = u'xpath=//div[@class="v-menu__content theme--light menuable__content__active navbarRightMenuItemMenu"]'
        self.juno_plus_menu_project = u'xpath=//div[@id="list-item-184"]'
        self.juno_project_name = u'xpath=//label[text()="+ Add project name"]'
        self.juno_project_name_text = u'xpath=//input[@required="required" and @type="text"]'
        self.juno_project_add_labels = u'xpath=//span[contains(text(),"Add labels")]'
        self.juno_project_add_labels_open = u'xpath=//*[@id="app"]/div[4]'
        self.juno_project_add_labels_create = u'xpath=//span[contains(text(),"Create project label")]'
        self.juno_project_aad_labels_create_name = u'xpath=//input[@placeholder="Name new label"]'
        self.juno_project_add_labels_create_button = u'xpath=//div[@class="v-list pt-0 v-sheet theme--light"]//span[contains(text(),"Create")]'
        self.juno_project_labels_x = u'xpath=//i[@class="v-icon notranslate fas fa-times theme--light"]'
        self.juno_project_add_description = u'xpath=//textarea'
        self.juno_project_create = u'xpath=//button[@class="mr-4 text-white v-btn v-btn--is-elevated v-btn--has-bg theme--light v-size--default"]//span[contains(text(),"Create")]'
        self.juno_main_menu_projects = u'xpath=//span[text()="Projects"]'
        self.juno_project_list_locator = u'xpath=//span[text()="Project"]'
        self.juno_project_list_name_project = u'xpath=(//span[@class="el-tooltip item"])[1]'
        self.juno_plus_menu_task_locator = u'xpath=//div[@id="list-item-180"]'
        self.juno_task_header_locator = u'xpath=//div[@class="row form-header"]'
        self.juno_task_select_project = u'xpath=//input[@readonly="readonly" and @autocomplete= "off"]'
        self.juno_task_select_name_project = u'xpath=(//div[@class="v-list-item__title"])[1]'
        self.juno_task_name = u'xpath=//textarea[@id="input-855"]'
        self.juno_main_menu_dashboard = u'xpath=//span[text()="Dashboard"]'
        self.juno_task_add_description = u'xpath=(//span[@data-test-id="placeholder"])[1]'
        self.juno_add_attachment_locator = u'xpath=//input[@type="file"]'
        self.juno_project_add_description_text = u'xpath=//textarea[@data-test-id="wysiwyg-text-area"]'
        self.juno_task_attachment_button = u'xpath=//button[@class="text-white v-btn v-btn--has-bg theme--light v-size--x-small"]'
        self.juno_task_bold_button = u'xpath=//button[@data-test-id="bold"]'
        self.juno_task_create_button = u'xpath=//div[@class="col col-12"]//button[@class="mr-4 text-white v-btn v-btn--is-elevated v-btn--has-bg theme--light v-size--default"]'
        self.juno_task_list = u'xpath=//tr[@style="cursor: pointer;"]'
        self.juno_task_list_detail = u'xpath=//div[@class="headline mb-1 wrap-long"]'
        self.juno_project_detail_design = u'xpath=//a[contains(text(),"Design")]'
        self.juno_add_design = u'xpath=//input[@placeholder="+ Add Design"]'
        self.juno_design_type = u'xpath=//span[@class="el-tooltip mr-2 text-uppercase item cursor-pointer story-badge"]'
        self.juno_design_name = 'document.querySelector(\'[class="font-weight-bold hide-long block"]\').click()'
        self.juno_project_add_description_edit = u'xpath=//span[text()="+ Add description"]'
        self.juno_project_add_description_edit_text = u'xpath=//textarea[@id="epic-description-wysiwyg-edit{0}"]'
        self.juno_project_add_description_edit_save = u'xpath=(//div[@class="v-navigation-drawer__content"]//span[contains(text(), "Save")])[2]'
        self.juno_project_check_strong_text = u'xpath=//strong[text()="poppis projektu, ktorý som práve vytvorila"]'
        self.juno_project_edit_x = u'xpath=(//i[@class="v-icon notranslate close-icon fas fa-times theme--light"])[3]'
        self.juno_task_detail = u'xpath=//tr[@style="cursor: pointer;"]'
        self.juno_task_detail_name_locator = u'xpath=(//span[text()="Task name:"])[3]'
        self.juno_task_detail_description = u'xpath=(//p[text()="pospis tasku, ktorý vytvaram a pridám tam obrázok"])[2]'
        self.juno_task_detail_jpg = u'xpath='

#   ######## Opening and closing the browser ##########
    @keyword('Lets Open ${url} Page')
    def start_chrome(self, url):
        """ Starts Chrome. 
        """
        self.open_browser(browser="chrome",
                          executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe",
                          remote_url=False,
                          url=url)
        self.maximize_browser_window()

    @keyword('User Logs Into Page')
    def sign_in(self):
        """User Andrea logs into the page. 
        """
        self.wait_until_element_is_visible(self.juno_sign_in_page_name)
        self.input_text(self.juno_sign_in_page_name, "hulinova.l@gmail.com")
        self.wait_until_element_is_visible(self.juno_sign_in_page_password)
        self.input_text(self.juno_sign_in_page_password, "Heslo-123")
        self.click_element(self.juno_sign_in_button)

    @keyword('User Clicks Plus')
    def click_plus(self):
        """User Andrea clicks on the plus button. 
        """
        self.wait_until_element_is_visible(self.juno_dashboard_button_plus)
        self.click_element(self.juno_dashboard_button_plus)
        self.wait_until_element_is_visible(self.juno_dashboard_plus_menu)

    @keyword('User Creates Project')
    def create_project(self):
        """User Andrea creates a new project. 
        """
        self.click_element(self.juno_plus_menu_project)
        self.wait_until_element_is_visible(self.juno_project_name)
        self.double_click_element(self.juno_project_name)
        self.input_text(self.juno_project_name_text, name)
        self.wait_until_element_is_visible(self.juno_project_add_labels)
        self.wait_for_and_mouse_over_and_click(self.juno_project_add_labels)
        self.wait_until_element_is_visible(self.juno_project_add_labels_open)
        self.click_element(self.juno_project_add_labels_create)
        self.input_text(self.juno_project_aad_labels_create_name, name)
        self.click_element(self.juno_project_add_labels_create_button)
        self.click_element(self.juno_project_labels_x)
        self.double_click_element(self.juno_project_add_description)
        self.input_text(self.juno_project_add_description, "poppis projektu, ktorý som práve vytvorila")
        self.click_element(self.juno_project_create)

    @keyword('User Clicks Main Menu And Selects Project')
    def main_menu_project(self):
        """User Andrea clicks in main menu and selects Project. 
 
        """
        self.wait_for_and_mouse_over_and_click(self.juno_main_menu_projects)

    @keyword('User Verifies The Creation Of The Project')
    def verifies_project(self):
        """User Andrea verifies if the project was created. 
 
        """
        self.wait_until_element_is_visible(self.juno_project_list_locator)
        self.wait_until_element_contains(self.juno_project_list_name_project, name)

    @keyword('User Clicks Dashboard')
    def open_dashboard(self):
        """User Andrea clicks and open dashboard. 
        """
        self.click_element(self.juno_main_menu_dashboard)

    @keyword('User Clicks Create Task And Adds Name And Description')
    def create_task(self):
        """User Andrea creates task add a name and a description. 
        """
        self.click_element(self.juno_plus_menu_task_locator)
        self.wait_until_element_is_visible(self.juno_task_header_locator)
        self.double_click_element(self.juno_task_select_project)
        self.wait_for_and_mouse_over_and_click(self.juno_task_select_name_project)
        self.wait_until_element_is_visible(self.juno_task_name)
        self.double_click_element(self.juno_task_name)
        self.input_text(self.juno_task_name, name)
        self.wait_for_and_mouse_over_and_click(self.juno_task_add_description)
        self.input_text(self.juno_project_add_description_text, "pospis tasku, ktorý vytvaram a pridám tam obrázok")
        #self.click_element(self.juno_task_bold_button)
        #self.input_text(self.juno_project_add_description_text, "hrubo vyznačený text")

    @keyword('User Attaches File ${file}')
    def add_attachment(self, attachment_path):
        """ Adds attachment. 
 
         *Arguments:* 
        - attachment_path - string 
 
        """
        try:
            self.choose_file(self.juno_add_attachment_locator, attachment_path)
        except Exception:
            sleep(2)
            self.choose_file(self.juno_add_attachment_locator, attachment_path)
            sleep(5)

    @keyword('User Clicks Create Task')
    def click_create_task(self):
        """User Andrea clicks create the task. 
        """
        self.wait_for_and_mouse_over_and_click(self.juno_task_create_button)

    @keyword('User Checks Project Detail')
    def check_project(self):
        """User Andrea checks the project detail. 
        """
        self.wait_until_element_contains(self.juno_project_list_name_project, name)
        self.click_element(self.juno_project_list_name_project)
        self.wait_until_element_is_visible(self.juno_task_list_detail)

    @keyword('User Checks Detail Task')
    def check_tasak(self):
        """User Andrea checks the task detail. 
        """
        self.click_element(self.juno_task_detail)
        self.wait_until_element_is_visible(self.juno_task_detail_name_locator)
        self.wait_until_element_is_visible(self.juno_task_detail_jpg)
        self.wait_until_element_is_visible(self.juno_task_detail_description)


    @keyword('User Clicks Design')
    def click_design(self):
        """User Andrea clicks on design. 
        """
        self.double_click_element(self.juno_project_detail_design)
        self.wait_until_element_is_visible(self.juno_add_design)

    @keyword('User Creates Design')
    def create_design(self):
        """User Andrea create a design. 
        """
        self.click_element(self.juno_add_design)
        self.input_text(self.juno_add_design, name)
        self.press_keys(self.juno_add_design, "ENTER")
        self.wait_until_element_is_visible(self.juno_design_type)
        self.execute_javascript(self.juno_design_name)

    @keyword('User Edits Project')
    def edit_project(self):
        """User Andre edits the project, adds a description. 
        """
        self.wait_until_element_is_visible(self.juno_project_add_description_edit)
        self.double_click_element(self.juno_project_add_description_edit)
        self.input_text(self.juno_project_add_description_edit_text, "**poppis projektu, ktorý som práve vytvorila**")

    @keyword('User Clicks Save Edited Project')
    def project_save(self):
        """User Andrea save edit project. 
        """
        self.find_element(self.juno_project_add_description_edit_save)
        self.wait_for_and_mouse_over_and_click(self.juno_project_add_description_edit_save)
       #self.click_element(self.juno_project_add_description_edit_save)
        self.click_element(self.juno_project_edit_x)

    @keyword('Lets End The Show')
    def end_chrome(self):
        """ Ends chrome. 
        """
        self.close_all_browsers()
