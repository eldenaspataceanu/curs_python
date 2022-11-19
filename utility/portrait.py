import requests
from uuid import uuid4
from selenium.webdriver.common.by import By


class Portrait:
    def __init__(self, element, driver):
        self.portrait_detail = None
        self._driver = driver
        self._element = element
        self._id = uuid4()
        self._name = None
        self._image_path = None
        self._details = {}

    def extract_data(self):
        link_element = self._element.find_element(By.TAG_NAME, 'a')
        name_element = self._element.find_element(By.TAG_NAME, 'h6')
        self._name = name_element.text

        self._driver.execute_script(f'window.open("{link_element.get_attribute("href")}")')
        self._driver.switch_to.window(self._driver.window_handles[-1])

        image_element = self._driver.find_element(By.XPATH, './/figure[@class="chocolat-parent"]//img')
        image_data = requests.get(url=image_element.get_attribute('src')).content
        self._image_path = f'./images/{self._id}.jpg'
        with open(self._image_path, 'wb') as image_file:
            image_file.write(image_data)

        details_body = self._driver.find_element(By.ID, 'col_details')
        title_details = details_body.find_elements(By.XPATH, './/dt[not(contains(.,"Titel"))]')
        element_details = details_body.find_elements(By.XPATH, './/dd[not(contains(.,"Dr."))]')
        for title_detail, element_detail in zip(title_details[2::], element_details[2::]):
            specs = title_detail.text
            specs_1 = element_detail.text
            self._details[specs] = specs_1
            print(self._details)

        self._driver.close()
        self._driver.switch_to.window(self._driver.window_handles[-1])

    def to_dict(self):
         return {
             'name': self._name,
             'image_path': self._image_path,
             'details': self._details
         }


