# AutoSticker

## Introduction
* The repo is to add telegram stickers on [Pixiv](https://www.pixiv.net/) automatically.

## Prepare before use
0. Of course, download python(3.8.10 is recommanded)
1. `pip install -r requirement.txt`
2. Fill up the .env.example and rename it with `.env`
  * get your api_id and api_hash from [Telegram App Configuration](https://my.telegram.org/apps)
  * get your sticker_set name with [Official Stickers Bot](https://t.me/Stickers)
  * get user_id on [Pixiv](https://www.pixiv.net/). just browse the artist you like and copy the numbers in URL.
    * for example, I'm `12345678`
    * ![](https://i.imgur.com/SzRfbIZ.png)
  * get tag when you browse the works from the artist
    * for example, your favorite artist always tag `#cat` for his/her illustrations, and you can fill `cat` up
  * if limit is 10, it'll find first 10 illustrations.
 
## Usage
1. `python main.py` or `python main.py 5` to replace the limit number with `5`.
![](https://i.imgur.com/QmU2mSH.png)
2. Select what you want and click **send**
3. Waiting... you can watch your command window or telegram chatroom with [Stickers Bot](https://t.me/Stickers)
