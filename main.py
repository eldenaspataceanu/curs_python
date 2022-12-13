# import os
# import shutil
# import json
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from utility.portrait import Portrait
# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session
# from utility.base import User, Base
from gui.app import Application

if __name__ == '__main__':
#     shutil.rmtree('images/')
#     os.mkdir('images/')
#
#     chrome_executable = Service(executable_path='./chromedriver.exe')
#
#     driver = webdriver.Chrome(service=chrome_executable)
#     # driver.set_window_position(0, 0)  #setez sa mi se deschida pe ecranul principal
#     # driver.maximize_window()
#
#     driver.get('https://www.grosserrat.bs.ch/mitglieder')
#
#     persons_name = []
#     portrait_persons = driver.find_elements(By.XPATH, './/div[@id="mitglieder_portaits"]//div[@class="person"]')
#     for person_name in portrait_persons[:10]:
#         person_name = Portrait(person_name, driver=driver)
#         person_name.extract_data()
#         persons_name.append(person_name)
#
#     driver.close()
#
#     output = [
#         person_name.to_dict()
#         for person_name in persons_name
#     ]
#     #
#     engine = create_engine('mysql+mysqldb://root:Python123!@localhost:3306/proiect_final')
#     session = Session(engine)
#
#     Base.metadata.create_all(engine)
#
#     for person in output:
#         user = User(
#             name=person['name'],
#             image_path=person['image_path'],
#             address=person['details']['Adresse'],
#             postcode=person['details']['PLZ'],
#             location=person['details']['Ort'],
#             date_of_birth=person['details']['Geb. Datum'],
#             professional_activities=person['details']['Berufliche Tätigkeit'],
#             telefone=person['details']['Telefon G'] if 'Telefon G' in person['details'] else person['details'].get('Mobile'),
#             constituency=person['details']['Wahlkreis'],
#             political_party=person['details'].get('Partei'),
#             email=person['details']['E-Mail']
#         )
#
#         with Session(engine) as session:
#             session.add(user)
#             session.commit()
#
#     with open('output.json', 'w') as json_file:
#         json.dump(output, json_file, indent=2, ensure_ascii=False)

    application = Application()
    application.run()