<!--suppress HtmlDeprecatedAttribute -->
<p align="center">
    <img alt="idk" src="https://icon-icons.com/icons2/2000/PNG/72/emoji_sleep_sleeping_icon_123401.png" width=72 height=72>
  <h3 align="center">Bedtime Bot</h3>
  <p align="center">
    A telegram bot you could fall asleep to!
    <br>
    <a href="https://github.com/ScoBrun/bedtimebot/issues/new">Submit Issue</a>
  </p>
</p>

[![Build Status](https://travis-ci.com/ScoBrun/bedtimebot.svg?branch=master)](https://travis-ci.com/ScoBrun/bedtimebot) 


## Use Case and Description
This is a telegram bot that is designed for people who have difficulty determining when to sleep, for how long, as well as what to set their alarm clock for.

The bot's main purpose currently is to do the legwork of calculating the best times based on two things: taking 15 minutes to fall asleep and  90-minute cycles. Where appropriate, the bot also provides the information on a nap (25 minutes) - so you can plan a power nap through your day.

## Key Features
- `/sleepat` - Users can input a time they wish to go to bed at, returning suggested times to wake up at.
- `/sleepnow` - Users can request what time to get up at if they go to sleep right now.
- `/wakeupat` - Users can calculate what time to fall asleep based on the time that they wish to get up.

## Setup/Dev instructions
1. Configure your bot tokens via [@botfather](https://telegram.me/botfather)
2. Install the following on your python3 server via pip: `pip install -U python-telegram-bot pytest`
3. Git clone and enter directory: `https://github.com/ScoBrun/bedtimebot && cd bedtimebot`
4. Create a file called `bot_token.py` in the repo with a variable called `BOT_TOKEN_ID` inside it. Put your API token here.
4. Run the `bot.py` script.
5. Go to your bot's URL. Type in `/start` to start the telegram bot. Everything should be working immediately.

## Bugs and feature requests
Have a bug or a feature request? [Feel free to open a new issue.](https://github.com/ScoBrun/bedtimebot/issues/new)
## Technologies Used
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Telegram bot API Framework
- [Ismaestro/markdown-template](https://github.com/Ismaestro/markdown-template/blob/master/README.md) - Template base for this Readme.
- [Icon-Icons](https://icon-icons.com/icon/emoji-sleep-sleeping/123401) for repo icon. Used under CC 4.0.

Enjoy your good night's sleep!
