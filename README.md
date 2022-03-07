# news-telegram-bot
install:  

- git clone https://github.com/mewmix/news-telegram-bot && cd news-telegram* 
- pip3 install -r requirements.txt 
- Edit the bot.py (soon .env) with your Telegram Chat ID & Bot Token - ((get bot token at https://t.me/botfather by making a new bot. For chat id use https://t.me/chatIDrobot )) - also set the slp variable to whatever time you want, by default it is 1 hour
- python3 bot.py (heroku deploy & more coming soon. )
