#Belide Aakash (Data Science Internship Task - Unplan)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

#Install Chrome driver before running the code
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#Url on which web scraping has to be done
url = "https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa,Residential-Plot&cityName=Bangalore"
driver.get(url)
parentGUID = driver.current_window_handle

a_price = []
a_headline = []
a_address = []
a_owner = []
a_bedrooms = []
a_bathrooms = []
a_balconies = []
a_super_area = []
a_pps = []
a_status = []
a_transaction_type = []
a_floor = []
a_car_parking = []
a_furnished = []
a_lifts = []
a_descrption = []
a_price_breakup = []
a_address2 = []
a_landmarks = []
a_aoc = []
a_pc = []
a_er = []
a_emi = []

def scroll(driver, timeout, t):
    scroll_pause_time = timeout
    scroll_times = t

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    for k in range(scroll_times):
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height


try:
    scroll(driver, 5, 18)
    card = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "m-srp-card")))
    for i in range(500):
        card[i].click()
        allGUID = driver.window_handles
        for guid in allGUID:
            if(guid != parentGUID):
                driver.switch_to_window(guid)
                #Price
                try:
                    price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "p_price")))
                    a_price.append(price.text[2:])
                except:
                    a_price.append('NA')

                #Headline
                try:
                    headline = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "p_bhk")))
                    a_headline.append(headline.text)
                except:
                    a_headline.append('NA')

                #Address
                try:
                    address = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "p_address")))
                    a_address.append(address.text)
                except:
                    a_address.append('NA')

                #Owner
                try:
                    owner = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "agentName")))
                    a_owner.append(owner.text)
                except:
                    a_owner.append('NA')

                #Bedrooms
                try:
                    bed = driver.find_element_by_xpath("//*[contains(text(), 'Bedrooms')]")
                    bed_n = driver.find_element_by_xpath("//*[contains(text(), 'Bedrooms')]/following-sibling::div")
                    a_bedrooms.append(bed_n.text)
                except:
                    a_bedrooms.append("NA")
                
                #Bathrooms
                try:
                    bath = driver.find_element_by_xpath("//*[contains(text(), 'Bathrooms')]")
                    bath_n = driver.find_element_by_xpath("//*[contains(text(), 'Bathrooms')]/following-sibling::div")
                    a_bathrooms.append(bath_n.text)
                except:
                    a_bathrooms.append("NA")
                
                #Balconies
                try:
                    bal = driver.find_element_by_xpath("//*[contains(text(), 'Balconies')]")
                    bal_n = driver.find_element_by_xpath("//*[contains(text(), 'Balconies')]/following-sibling::div")
                    a_balconies.append(bal_n.text)
                except:
                    a_balconies.append("NA")
                
                #Super area
                try:
                    sa = driver.find_element_by_xpath("//*[contains(text(), 'Super area')]")
                    sa_n = driver.find_element_by_xpath("//*[contains(text(), 'Super area')]/following-sibling::div")
                    a_super_area.append(sa_n.text)
                except:
                    a_super_area.append("NA")
                
                #Price per sqft
                try:
                    pps = driver.find_element_by_xpath("//*[contains(text(), '/sqft')]")
                    a_pps.append(pps.text[2:])
                except:
                    a_pps.append("NA")
                
                #Status
                try:
                    st = driver.find_element_by_xpath("//*[contains(text(), 'Status')]")
                    st_n = driver.find_element_by_xpath("//*[contains(text(), 'Status')]/following-sibling::div")
                    a_status.append(st_n.text)
                except:
                    a_status.append("NA")
                
                #Transaction type
                try:
                    trn = driver.find_element_by_xpath("//*[contains(text(), 'Transaction type')]")
                    trn_n = driver.find_element_by_xpath("//*[contains(text(), 'Transaction type')]/following-sibling::div")
                    a_transaction_type.append(trn_n.text)
                except:
                    a_transaction_type.append("NA")
                #Floor
                try:
                    flr = driver.find_element_by_xpath("//*[contains(text(), 'Floor')]")
                    flr_n = driver.find_element_by_xpath("//*[contains(text(), 'Floor')]/following-sibling::div")
                    a_floor.append(flr_n.text)
                except:
                    a_floor.append("NA")
                
                #Car parking
                try:
                    cp = driver.find_element_by_xpath("//*[contains(text(), 'Car parking')]")
                    cp_n = driver.find_element_by_xpath("//*[contains(text(), 'Car parking')]/following-sibling::div")
                    a_car_parking.append(cp_n.text)
                except:
                    a_car_parking.append("NA")
                
                #Furnished status
                try:
                    fur = driver.find_element_by_xpath("//*[contains(text(), 'Furnished status')]")
                    fur_n = driver.find_element_by_xpath("//*[contains(text(), 'Furnished status')]/following-sibling::div")
                    a_furnished.append(fur_n.text)
                except:
                    a_furnished.append("NA")
                
                #Lifts
                try:
                    lft = driver.find_element_by_xpath("//*[contains(text(), 'Lifts')]")
                    lft_n = driver.find_element_by_xpath("//*[contains(text(), 'Lifts')]/following-sibling::div")
                    a_lifts.append(lft_n.text)
                except:
                    a_lifts.append("NA")
                
                #Description
                try:
                    desc = driver.find_element_by_id("prop-detail-desc")
                    a_descrption.append(desc.text)
                except:
                    a_descrption.append("NA")
                
                #Price Breakup
                try:
                    pb = driver.find_element_by_xpath("//*[contains(text(), 'Price Breakup')]")
                    pb_n = driver.find_element_by_xpath("//*[contains(text(), 'Price Breakup')]/following-sibling::div")
                    a_price_breakup.append(pb_n.text[2:])
                except:
                    a_price_breakup.append("NA")

                #Address
                try:
                    addr = driver.find_element_by_xpath("//*[contains(text(), 'Address')]")
                    addr_n = driver.find_element_by_xpath("//*[contains(text(), 'Address')]/following-sibling::div")
                    a_address2.append(addr_n.text)
                except:
                    a_address2.append("NA")
                
                #Landmarks
                try:
                    lndm = driver.find_element_by_xpath("//*[contains(text(), 'Landmarks')]")
                    lndm_n = driver.find_element_by_xpath("//*[contains(text(), 'Landmarks')]/following-sibling::div")
                    a_landmarks.append(lndm_n.text)
                except:
                    a_landmarks.append("NA")
                
                #Age of Construction
                try:
                    aoc = driver.find_element_by_xpath("//*[contains(text(), 'Age of Construction')]")
                    aoc_n = driver.find_element_by_xpath("//*[contains(text(), 'Age of Construction')]/following-sibling::div")
                    a_aoc.append(aoc_n.text)
                except:
                    a_aoc.append("NA")
                
                #Price comparison
                try:
                    pc = driver.find_element_by_xpath("//*[contains(text(), 'Price comparison')]")
                    pc_n = driver.find_element_by_xpath("//*[contains(text(), 'Price comparison')]/following-sibling::div")
                    a_pc.append(pc_n.text)
                except:
                    a_pc.append("NA")

                #Expected rent
                try:
                    er = driver.find_element_by_xpath("//*[contains(text(), 'Expected rent')]")
                    er_n = driver.find_element_by_xpath("//*[contains(text(), 'Expected rent')]/following-sibling::div")
                    a_er.append(er_n.text)
                except:
                    a_er.append("NA")
                
                #Monthly EMI
                try:
                    emi = driver.find_element_by_xpath("//*[contains(text(), 'Monthly EMI')]")
                    emi_n = driver.find_element_by_xpath("//*[contains(text(), 'Monthly EMI')]/following-sibling::div")
                    a_emi.append(emi_n.text)
                except:
                    a_emi.append("NA")
                
                driver.close()
                driver.switch_to_window(parentGUID)
finally:
    driver.quit()


df = pd.DataFrame(list(zip(a_price, a_headline, a_address, a_owner, a_bedrooms, a_bathrooms, a_balconies, a_super_area, a_pps, a_status, a_transaction_type, a_floor, a_car_parking, a_furnished, a_lifts, a_descrption, a_price_breakup, a_address2, a_landmarks, a_aoc, a_pc, a_er,a_emi)), columns=['Price', 'Headline', 'Address', 'Owner', 'Bedrooms', 'Bathrooms', 'Balconies', 'Super area', 'Price Per sqft', 'Status', 'Transaction type', 'Floor', 'Car parking', 'Furnished', 'Lifts', 'Descrption', 'Price breakup', 'Address2', 'Landmarks', 'Age of Construction', 'Price comparison', 'Expected rent','Monthly EMI'])

unplan_magic_bricks_bnglr = df.to_csv('unplan_internship.csv', index=False)