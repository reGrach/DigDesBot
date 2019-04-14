from telebot import TeleBot, logger
import config
import logging
import src.static as stc
import src.menu as menu


_logger = logger
_logger.setLevel(logging.DEBUG)

bot = TeleBot(config.TOKEN_BOT)


@bot.message_handler(commands=['start'])
def welcome_message(msg):
    bot.send_message(
        msg.chat.id,
        stc.get_welcome_string(msg.chat.first_name),
        reply_markup=menu.get_main_markup()
    )


@bot.message_handler(func=lambda msg: msg.text == 'Развозка')
def get_shuttle_info(msg):
    answer = bot.send_message(msg.chat.id, "Выберите направление", reply_markup=menu.get_destination())
    bot.register_next_step_handler(answer, callback_shuttle)


@bot.callback_query_handler(func=lambda call: True)
# Ответ про развозку
def callback_shuttle(call):
    msg_id = call.message.chat.id
    _shuttle = stc.SHUTTLE[call.data]
    bot.send_message(msg_id, _shuttle['time'])
    bot.send_venue(msg_id,
                   _shuttle['venue']['longitude'],
                   _shuttle['venue']['latitude'],
                   _shuttle['venue']['title'],
                   _shuttle['venue']['address'])


if __name__ == "__main__":
    bot.polling(none_stop=True)
