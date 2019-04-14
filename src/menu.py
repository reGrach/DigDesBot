from telebot import types
import src.static as stc


def get_main_markup():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Авторизация", request_contact=True)
    markup.add("Новости", "Развозка")
    markup.add("Вакансии", "Найти DD")
    markup.add(button_phone, "FAQ")
    return markup


def get_destination():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    buttons = []
    for key, val in stc.SHUTTLE.items():
        buttons.append(types.InlineKeyboardButton(val['title'], callback_data=key))
    markup.add(buttons[0], buttons[1])
    return markup
