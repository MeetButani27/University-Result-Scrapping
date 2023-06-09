from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import csv

s_data = dict()
Institue = 'CSPIT'
Branch = 'BTECH(CS)'
Semester = '5'
Year = 'NOVEMBER 2022'

BASE_USERNAME = '20CS'
start = 1
end = 10
D2D_BASE_USERNAME = 'D21CS'
d2d_start = 1
d2d_end = 1


driver = webdriver.Firefox()
driver.get("https://charusat.edu.in:912/UniExamResult/")


##############   CSE   ################
driver.find_element(By.XPATH,"/html/body/form/div[3]/table[2]/tbody/tr[1]/td[2]/select/option[2]").click()
driver.find_element(By.XPATH,"/html/body/form/div[3]/table[2]/tbody/tr[2]/td[2]/select/option[5]").click()
driver.find_element(By.XPATH,"/html/body/form/div[3]/table[2]/tbody/tr[3]/td[2]/select/option[6]").click()
driver.find_element(By.XPATH,"/html/body/form/div[3]/table[2]/tbody/tr[4]/td[2]/select/option[3]").click()


for i in range(start,end+1):
    try:
        s_id = BASE_USERNAME + str(i).zfill(3)
        s_data[s_id] = list()
        roll_field = driver.find_element(By.ID,"txtEnrNo")
        driver.find_element(By.ID,"txtEnrNo").clear()
        roll_field.send_keys(s_id)
        submit_btn = driver.find_element(By.XPATH, '/html/body/form/div[3]/table[2]/tbody/tr[6]/td[1]/input')
        submit_btn.click()
        
        s_data[s_id].append(driver.find_element(By.XPATH, '/html/body/form/div[3]/div/div/table[3]/tbody/tr[1]/td[6]/span').text)
        s_data[s_id].append(driver.find_element(By.XPATH, '/html/body/form/div[3]/div/div/table[3]/tbody/tr[1]/td[3]/span').text)
        s_data[s_id].append(driver.find_element(By.XPATH, '/html/body/form/div[3]/div/div/table[4]/tbody/tr[2]/td[3]/span').text)
        s_data[s_id].append(driver.find_element(By.XPATH, '/html/body/form/div[3]/div/div/table[5]/tbody/tr[2]/td[3]/span').text)
        driver.implicitly_wait(15)
        driver.back()
    except:
        continue


for i in range(d2d_start,d2d_end+1):
    try:
        s_id = D2D_BASE_USERNAME + str(i).zfill(3)
        s_data[s_id] = list()
        roll_field = driver.find_element(By.ID,"txtEnrNo")
        driver.find_element(By.ID,"txtEnrNo").clear()
        roll_field.send_keys(s_id)
        submit_btn = driver.find_element(By.XPATH, '/html/body/form/div[3]/table[2]/tbody/tr[6]/td[1]/input')
        submit_btn.click()
        
        s_data[s_id].append(driver.find_element(By.XPATH, '/html/body/form/div[3]/div/div/table[3]/tbody/tr[1]/td[6]/span').text)
        s_data[s_id].append(driver.find_element(By.XPATH, '/html/body/form/div[3]/div/div/table[3]/tbody/tr[1]/td[3]/span').text)
        s_data[s_id].append(driver.find_element(By.XPATH, '/html/body/form/div[3]/div/div/table[4]/tbody/tr[2]/td[3]/span').text)
        s_data[s_id].append(driver.find_element(By.XPATH, '/html/body/form/div[3]/div/div/table[5]/tbody/tr[2]/td[3]/span').text)
        driver.implicitly_wait(15)
        driver.back()
    except:
        continue


header = ['Roll no', 'Name', 'SGPA', 'CGPA']

with open('Scrap_CS.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for i in range(start,end+1):
        writer.writerow(s_data[BASE_USERNAME + str(i).zfill(3)])
    
    for i in range(d2d_start,d2d_end+1):
        writer.writerow(s_data[D2D_BASE_USERNAME + str(i).zfill(3)])


driver.close()
exit()