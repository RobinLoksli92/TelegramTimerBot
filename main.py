import ptbot
import os
from pytimeparse import parse
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = '619160718'  


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

   
def reply(time):  
    secs_left = parse(time)
    message_bar = render_progressbar(parse(time), secs_left)
    render_bar1 = bot.send_message(CHAT_ID, message_bar)
    message_id = ("{} {} {} {}".format("Прошло", secs_left, "секунды из", parse(time)))
    new_mes1 = bot.send_message(CHAT_ID, message_id)
    bot.create_countdown(parse(time)-1, notify_progress, secs_from_start = parse(time),render_bar = render_bar1, new_mes = new_mes1)
    bot.create_timer(parse(time), notify)


def notify_progress(secs_left, new_mes, secs_from_start, render_bar):
    bot.update_message(CHAT_ID, new_mes, "{} {} {} {}".format("Прошло", secs_left, "секунды из", secs_from_start))  
    bot.update_message(CHAT_ID,render_bar, render_progressbar(secs_from_start, secs_left))


def notify():
    bot_answer = "{}".format('Время вышло') 
    bot.send_message(CHAT_ID, bot_answer)


def main(reply):
    bot.send_message(CHAT_ID, "На сколько запустить таймер?")
    bot.reply_on_message(reply)
    bot.run_bot()   


if __name__ == '__main__':
    load_dotenv()
    bot = ptbot.Bot(TOKEN)
    main(reply)
