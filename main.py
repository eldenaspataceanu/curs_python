import os
import shutil
import json
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utility.portrait import Portrait

if __name__ == '__main__':
    shutil.rmtree('images/')
    os.mkdir('images/')

    chrome_executable = Service(executable_path='./chromedriver.exe')

    driver = webdriver.Chrome(service=chrome_executable)
    driver.set_window_position(0, 0)
    driver.maximize_window()

    driver.get('https://www.grosserrat.bs.ch/mitglieder')

    persons_name = []
    portrait_persons = driver.find_elements(By.XPATH, './/div[@id="mitglieder_portaits"]//div[@class="person"]')
    for person_name in portrait_persons[:11]:
        person_name = Portrait(person_name, driver=driver)
        person_name.extract_data()
        persons_name.append(person_name)

    driver.close()

    output = [
        person_name.to_dict()
        for person_name in persons_name

    ]
    with open('output.json', 'w') as json_file:
        json.dump(output, json_file, indent=2)

