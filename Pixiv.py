#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PIL import Image
from bs4 import BeautifulSoup
import requests
import json
import os.path

def UpdateImageFolder(user, tag, offset = 0, limit = 16, lang='zh_tw'):
    if not os.path.exists('image'):
        # Create a new directory because it does not exist
        os.makedirs('image')

    # get newest picture data
    img_list_url =  f'https://www.pixiv.net/ajax/user/{user}/illustmanga/tag?' + \
                    f'tag={tag}&offset={offset}&limit={limit}&lang={lang}'

    img_list_result = requests.get(img_list_url).json()['body']['works']

    # get each image
    artwork_url = 'https://www.pixiv.net/artworks/'

    new_images = []
    for img in img_list_result:
        # check is new picture
        filename = f"image/{img['title']}-512x512.png"
        new_images.append(filename)

        if os.path.exists(filename):
            continue
            
        # get real url from pixiv
        artwork_result = requests.get(artwork_url + img['id']).text
        artwork_soup = BeautifulSoup(artwork_result, features="html.parser")
        img_url = json.loads(artwork_soup.select_one('#meta-preload-data')['content'])['illust'][img['id']]['urls']['original']
        print('new picture:', img['title'], img_url)

        # download image and resize
        img_raw = requests.get(img_url, headers={
            'referer': 'https://www.pixiv.net/'
        }, stream=True).raw
        image = Image.open(img_raw)
        image = image.resize((512, 512))
        image.save(filename)
    
    return new_images