
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import nums_from_string
import wget
import glob
import time
import os
dir = "/Users/sydney/Desktop/yhack-mini/"
# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
# go to page
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\\Selenium\\chromedriver.exe")
driver.get("https://www.cclerk.hctx.net/applications/websearch/CourtSearch_R.aspx?ID=5rboVfNJYS8mH7Mxhu4+EVBMtA0R5zGMtVhdi9+X6GLANzZlvaRfuunC69j28BUVojC/22RiYYLEIogpg7Izgu9ywCNw0JstpbpG+l2P9OTXEPA7UOTk4Q9yDEd1aJnM#")
driver.maximize_window()

#entering date
print("Enter a date from in the format 'MM/DD/YYYY'")
user_date_from = input()

#user_date_from = '01/01/2022'
#user_date_to = "01/03/2022"

date_from = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtDateFrom")
date_from.clear()
date_from.send_keys(user_date_from)
print("Enter a date to in the format 'MM/DD/YYYY'")
user_date_to = input()
date_to = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtDateTo")
date_to.clear()
date_to.send_keys(user_date_to, Keys.RETURN)
#driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblListViewPartiesEmptyMsg") == False

print('Enter your username.')
username_input = input()
#username_input = 'ronaldh'
print('Enter your password.')
password_input = input()
#password_input = 'dwy!ypa_RFM4zvb8gcr'

def log_in(user = username_input, passw = password_input):
    username = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_Login1_UserName')
    username.clear()
    username.send_keys(user)
    password = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_Login1_Password')
    password.clear()
    password.send_keys(passw, Keys.RETURN)

#Find a will
def find_wills():
    total_string = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblCount")
    total = nums_from_string.get_nums(total_string.text)
    for j in total:
        number = j
    counter = 0
    while counter < number:
        type_desc = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ListViewCases_ctrl{}_Td8".format(counter))
        if "PROBATE OF WILL" in type_desc.text:
            case = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ListViewCases_ctrl{}_btnSelect".format(counter))
            case.click()
            doc_total_string = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblCount")
            doc_total = nums_from_string.get_nums(doc_total_string.text)
            for k in doc_total:
                doc_number = k
            doc_counter = 2
            while doc_counter < doc_number+1:
                type_doc = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_gridViewEvents_ctl{}_gridViewEventDocs_ctl02_lblDocDesc".format(f"{doc_counter:02}"))
                if "Admitted Will" in type_doc.text:
                    case = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_gridViewEvents_ctl{}_gridViewEventDocs_ctl02_HyperLinkFCEC".format(f"{doc_counter:02}"))
                    try:
                        case.click()
                    except:
                        break
                    handle_list = []
                    for handle in reversed(driver.window_handles):
                        handle_list.append(handle)
                    handle_counter = 1
                    for handle in handle_list:
                        if handle_counter == 1:
                            driver.switch_to.window(handle)
                            try:
                                log_in()
                            except NoSuchElementException:
                                pass
                            link = driver.current_url+"pdf"
                            wget.download(link,out = dir)
                            print('Download')
                            list_of_files = glob.glob(dir+'/*') 
                            latest_file = max(list_of_files, key=os.path.getmtime)
                            os.rename(os.path.join(dir, latest_file), os.path.join(dir,"Doc" + str(counter) ))
                            driver.close()
                        elif handle_counter == 2:
                            driver.switch_to.window(handle)
                            break
                        handle_counter += 1
                doc_counter += 1
            driver.back()
                

                    
                


            

                
        counter += 1
    
        
   # for e in all_type_desc:
   #     print("here it is", e.text)



find_wills()