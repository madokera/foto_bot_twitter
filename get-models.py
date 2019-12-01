# model scraping for themodelbot
import requests
from bs4 import BeautifulSoup as bs
import os

# website with model images
url = 'https://www.google.com/search?biw=1745&bih=881&tbm=isch&sxsrf=ACYBGNRKKnVpYATzq_b6hSy1YdrQ1OfnZg%3A1575142319641&sa=1&ei=r8PiXfbrJtyc5OUPvbaWKA&q=imagens+aleatorias&oq=imagens+a&gs_l=img.3.0.0l10.42486.43869..44843...0.0..0.180.1169.2j8......0....1..gws-wiz-img.......35i39j0i7i30j0i67j0i131j0i10i67.Q_3jv4LWfYo/'

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# create directory for model images
if not os.path.exists('models'):
    os.makedirs('models')

# move to new directory
os.chdir('models')

# image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        url = image['src']
        response = requests.get(url)
        if response.status_code == 200:
            with open('model-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass






