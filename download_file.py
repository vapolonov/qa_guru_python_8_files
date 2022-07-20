import os.path

import requests

with open('resources/selenium.png', 'wb') as file:
    r = requests.get('https://selenium.dev/images/selenium_logo_square_green.png')
    file.write(r.content)

print(os.path.getsize('resources/selenium.png'))
