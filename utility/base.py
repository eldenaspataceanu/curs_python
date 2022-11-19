from abc import abstractmethod


class BaseElement:
    def __init__(self, element, driver):
        self._element = element
        self._driver = driver

    @abstractmethod
    def extract_data(self):
        pass
