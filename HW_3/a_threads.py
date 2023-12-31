"""
Модуль в котором содержаться потоки Qt
"""

import psutil
import time
import requests

from PySide6 import QtCore


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__delay = None
        self.__status = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1

        while True:
            cpu_value = psutil.cpu_percent()
            ram_value = psutil.virtual_memory().percent
            self.systemInfoReceived.emit([cpu_value, ram_value])
            time.sleep(self.delay)



class WeatherHandler(QtCore.QThread):
    weatherDataReceived = QtCore.Signal(dict) # TODO Пропишите сигналы, которые считаете нужными

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 10
        self.__status = None

    @property
    def status(self) -> bool:
        return self.__status

    @status.setter
    def status(self, value) -> None:
        self.__status = value

    @property
    def delay(self) -> int:
        return self.__delay

    @delay.setter
    def setDelay(self, value) -> None:
        self.__delay = value

        """
        Метод для установки времени задержки обновления сайта

        :param delay: время задержки обновления информации о доступности сайта
        :return: None
        """



    def run(self) -> None:
        # TODO настройте метод для корректной работы

        while self.__status:
            try:
                response = requests.get(self.__api_url)
            except requests.exceptions.ConnectionError:
                self.weatherResponsed.emit('Error: No internet connection!')
                time.sleep(1)
            else:
                data = response.json()
                self.weatherResponsed.emit(data)
                time.sleep(self.__delay)

    @delay.setter
    def delay(self, value):
        self._delay = value
