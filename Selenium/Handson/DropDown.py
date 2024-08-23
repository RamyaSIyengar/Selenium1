import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class DropDown:
    def drop_down(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://www.salesforce.com/in/form/sem/salesforce-crm/?d=7013y000002hbRLAAY&nc=7013y000000a9thAAA&utm_source=google&utm_medium=paid_search&utm_campaign=apac_in_alllobcon&utm_content=brand-en-multi-product-search_salesforce-crm_7013y000002hbrlaay_7013y000002hbRLAAY&utm_term=Salesforce&ef_id=Cj0KCQjww5u2BhDeARIsALBuLnPfqy3BeTQjkdZa7cQxeSdCBjtA3eZUhOMcG8OnaDI2W79yuA7jL6UaAuqsEALw_wcB:G:s&s_kwcid=AL!4720!3!676565784220!e!!g!!salesforce&&ev_sid=3&ev_ln=salesforce&ev_lx=kwd-94920873&ev_crx=676565784220&ev_mt=e&ev_n=g&ev_ltx=&ev_pl=&ev_pos=&ev_dvc=c&ev_dvm=&ev_phy=9061995&ev_loc=&ev_cx=16895847353&ev_ax=137218384684&ev_efid=Cj0KCQjww5u2BhDeARIsALBuLnPfqy3BeTQjkdZa7cQxeSdCBjtA3eZUhOMcG8OnaDI2W79yuA7jL6UaAuqsEALw_wcB:G:s&url=!https://clickserve.dartsearch.net/link/click%3flid=43700074078535017&ds_s_kwgid=58700008151233901&gad_source=1&gclid=Cj0KCQjww5u2BhDeARIsALBuLnPfqy3BeTQjkdZa7cQxeSdCBjtA3eZUhOMcG8OnaDI2W79yuA7jL6UaAuqsEALw_wcB&gclsrc=aw.ds")
        driver.maximize_window()
        job_ele = driver.find_element(By.NAME, "UserTitle")
        selected_ele = Select(job_ele)
        selected_ele.select_by_value('Student / Job Seeker / Personal Interest')

        emp_ele = driver.find_element(By.NAME, "CompanyEmployees")
        selcted_emp = Select(emp_ele)
        selcted_emp.select_by_index("4")

        time.sleep(5)


drp = DropDown()
drp.drop_down()

