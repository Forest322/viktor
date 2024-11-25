import telebot


def vkt_start(kb):
    bt = telebot.types.InlineKeyboardButton(
            'Начать викторину',
            callback_data='vk'
        )
    kb.row(bt)

def vkt_start1(kb):
    bt1 = telebot.types.InlineKeyboardButton(
        'Углерод',
        callback_data='1.1'
        )
    bt2 = telebot.types.InlineKeyboardButton(
        'Водород',
        callback_data='1.2'
        )
    bt3 = telebot.types.InlineKeyboardButton(
        'Кислород',
        callback_data='1.3'
        )
    kb.row(bt1,bt2,bt3)

def vkt_start2(kb):
    bt1 = telebot.types.InlineKeyboardButton(
        'Марс',
        callback_data='2.1'
        )
    bt2 = telebot.types.InlineKeyboardButton(
        'Венера',
        callback_data='2.2'
        )
    bt3 = telebot.types.InlineKeyboardButton(
        'Земля',
        callback_data='2.3'
        )
    kb.row(bt1,bt2,bt3)

def vkt_start3(kb):

    bt1 = telebot.types.InlineKeyboardButton(
        'Джоан Роулинг',
        callback_data='3.1'
        )
    bt2 = telebot.types.InlineKeyboardButton(
        'Стивен Кинг',
        callback_data='3.2'
        )
    bt3 = telebot.types.InlineKeyboardButton(
        'Агата Кристи',
        callback_data='3.3'
        )
    kb.row(bt1,bt2,bt3)

def vkt_start4(kb):
    bt1 = telebot.types.InlineKeyboardButton(
        'Испанский',
        callback_data='4.1'
        )
    bt2 = telebot.types.InlineKeyboardButton(
        'Английский',
        callback_data='4.2'
        )
    bt3 = telebot.types.InlineKeyboardButton(
        'Португальский',
        callback_data='4.3'
        )
    kb.row(bt1,bt2,bt3)

def vkt_start5(kb):
    bt1 = telebot.types.InlineKeyboardButton(
        'Северная Америка',
        callback_data='5.1'
        )
    bt2 = telebot.types.InlineKeyboardButton(
        'Азия',
        callback_data='5.2'
        )
    bt3 = telebot.types.InlineKeyboardButton(
        ' Европа',
        callback_data='5.3'
        )
    kb.row(bt1,bt2,bt3)

def vkt_start6(kb):
    bt1 = telebot.types.InlineKeyboardButton(
        'Кислород',
        callback_data='6.1'
        )
    bt2 = telebot.types.InlineKeyboardButton(
        'Азот',
        callback_data='6.2'
        )
    bt3 = telebot.types.InlineKeyboardButton(
        'Углекислый газ',
        callback_data='6.3'
        )
    kb.row(bt1,bt2,bt3)

def vkt_start7(kb):
    bt1 = telebot.types.InlineKeyboardButton(
        'Юрий Гагарин',
        callback_data='7.1'
        )
    bt2 = telebot.types.InlineKeyboardButton(
        'Нил Армстронг',
        callback_data='7.2'
        )
    bt3 = telebot.types.InlineKeyboardButton(
        'Майкл Коллинз',
        callback_data='7.3'
        )
    kb.row(bt1,bt2,bt3)

def vkt_start8(kb):
    bt1 = telebot.types.InlineKeyboardButton(
        'Парк Юрского периода',
        callback_data='8.1'
        )
    bt2 = telebot.types.InlineKeyboardButton(
        'Форрест Гамп',
        callback_data='8.2'
        )
    bt3 = telebot.types.InlineKeyboardButton(
        'Сияние',
        callback_data='8.3'
        )
    kb.row(bt1,bt2,bt3)

def vkt_start9(kb):
    bt1 = telebot.types.InlineKeyboardButton(
        'Железо',
        callback_data='9.1'
        )
    bt2 = telebot.types.InlineKeyboardButton(
        'Фосфор',
        callback_data='9.2'
        )
    bt3 = telebot.types.InlineKeyboardButton(
        'Фтор',
        callback_data='9.3'
        )
    kb.row(bt1,bt2,bt3)

def vkt_start10(kb):
    bt1 = telebot.types.InlineKeyboardButton(
        'Атлантический',
        callback_data='10.1'
        )
    bt2 = telebot.types.InlineKeyboardButton(
        'Индийский',
        callback_data='10.2'
        )
    bt3 = telebot.types.InlineKeyboardButton(
        'Тихий',
        callback_data='10.3'
        )
    kb.row(bt1,bt2,bt3)
    
def vkt_start11(kb):
    
    bt1 = telebot.types.InlineKeyboardButton(
        'Заново',
        callback_data='vk'
        )
    kb.row(bt1)
    