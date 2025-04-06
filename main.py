from telegram.ext import Updater
from handlers import *
import config

MODULES = [
    admin, afk, antiflood, backups, bans, blacklist, connection,
    cust_filters, disable, global_bans, keyboard, locks, log_channel,
    notes, reports, rules, warns, tagall, pin, welcomer
]

def main():
    updater = Updater(config.BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    for module in MODULES:
        module.register(dp)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
