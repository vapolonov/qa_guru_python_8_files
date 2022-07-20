import os.path
import time

from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# current_dir = os.path.abspath(os.path.abspath(__file__))  # возвращает абсолютный путь к исполняемому файлу
# F:\QA-Engineer\Python_projects\qa_guru\qa_guru_python_8_files\download_from_browser.py

current_dir = os.path.dirname(os.path.abspath(__file__)) # возврщает абсолютный путь до директории,
# где находится исполняемый файл F:\QA-Engineer\Python_projects\qa_guru\qa_guru_python_8_files
# print(current_dir)

options = webdriver.ChromeOptions()
prefs = {
    'download.default_directory': os.path.join(current_dir, 'tmp'),  # объединяет несколько путей и нормализует
                                                                     # (для работы в разных версиях ОС
    'download.prompt_for_download': False
}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

browser.config.driver = driver
browser.config.hold_browser_open = True
browser.open('https://demoqa.com/upload-download')
browser.element('#downloadButton').click()
time.sleep(1)
assert os.path.getsize('tmp/sampleFile.jpeg') == 4096
os.remove('tmp/sampleFile.jpeg')
browser.close()
