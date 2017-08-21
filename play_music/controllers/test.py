# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from pyvirtualdisplay import Display
import os
from odoo import models, fields, api
class test():
    _name = "getsrc"
    def get_src(self, link):
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--mute-audio")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get(link)
        src = self.driver.find_element_by_tag_name("audio").get_attribute("src")
        self.display.stop()
        self.driver.quit()
        return src







