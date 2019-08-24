from telegram.ext import Updater, CommandHandler
import logging

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
def greet_user(bot, update):
    text = '/start'
    logging.info(text)
    update.message.reply_text(text)

def main():
    mybot = Updater('909143075:AAEzsBACVvyDyRz0n0z5PriDS959nEv5vFA', request_kwargs=PROXY)

    logging.info('bot is online')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))

    mybot.start_polling()
    mybot.idle()

main()