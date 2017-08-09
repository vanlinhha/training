#! /usr/bin/env python

import contextlib
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import ui


def read_file_conf(file_name):
    file = open(file_name, 'r')
    data = {}
    for line in file.readlines():
        temp = ''.join(line.split()).split('=')
        data.update({temp[0]: temp[1]})
    return data


def login(driver, username, password):
    driver.get(url)

    login_field = driver.find_element_by_id(u'login')
    login_field.send_keys(username)
    password_field = driver.find_element_by_id(u'password')
    password_field.send_keys(password)

    login_button = driver.find_element_by_css_selector('.btn-primary')
    # with wait_for_page_load():
    login_button.click()


if __name__ == '__main__':
    data = read_file_conf('odoo.conf')
    print 'data ', data
    driver = webdriver.Chrome()

    try:
        port = int(data['port'])
        db_name = data['db_name']
        url = 'http://localhost:%s/web?db=%s' % (port, db_name)
        login(driver, 'admin', 'admin')

    except Exception:
        os.system('pkill chromedriver')
        print 'Wrong value in odoo.conf file'
    os.system('pkill chromedriver')
