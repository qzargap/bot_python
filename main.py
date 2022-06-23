from test import *
from hisql import *
from dbusers import examination, come_users, id_user, money, us_log
from telebot import types
import telebot
import numpy
import random
bot = telebot.TeleBot('5596284668:AAFm66yYGM5uE4vlH9P-O7YPEdoa5zd_v88')

a = ''
log = ''
log_user = ''

array_dela = ["Хорошо", "Как всегда", "Ещё жив", "Какие дела? Я не при делах нынче!",
              "Ах я бедный-несчастный, так устал, мне каждый день приходится придумывать ответ на вопрос",
              "Есть два способа поставить человека в тупик: спросить у него «Как дела» и попросить рассказать что-нибудь",
              "Не знаю", "Затрудняюсь ответить", "Амбивалентно", "Лучше чем вчера, но хуже чем завтра…",
              "Также, как и пять минут назад…",
              "Я от природы бездельник", "Ногсшибательно",
              "Столько не сделано, столько не сделано! А сколько еще предстоит не сделать!",
              "Хорошо! И у тебя?", "Терпимо", "Безусловно", "Всё в шоколаде, даже клавиатура!",
              "Расту, цвету, старею…Всё как обычно",
              "Да ты меня прям до экстаза доводишь своими вопросами… Спроси ещё чем я занимаюсь и я твой на веки…",
              "Вы несравненно оригинальны в своих вопросах",
              "Да нормально, вчера нобелевскую премию получила за вклад в развитие экоструктурных подразделений в области китообразных инфузорий туфелек и тапочек и за открытие нано-технологий, которые помогут пингвинам преодолеть ледниковый период в африканских борах и гавайских пустынях в штате Масса Чуссетс округ Вашингтон.",
              "Тяжела жизнь без Ново-Пассита…", "Дела мои отлично! Жду дальнейших расспросов о своей личной жизни!",
              "Относительно. Если сравнивать с Лениным — то хорошо, если с миллионером — то не очень", "как дела?",
              "как дела", "Как дела?", "Как дела"]

isekai = 'https://myanimelist.net/anime/genre/62/Isekai'
comedi = 'https://myanimelist.net/anime/genre/4/Comedy'
drama = 'https://myanimelist.net/anime/genre/8/Drama'
adventure = 'https://myanimelist.net/anime/genre/2/Adventure'
ecchi = 'https://myanimelist.net/anime/genre/9/Ecchi'
action = 'https://myanimelist.net/anime/genre/1/Action'


@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_start(message):
    print(message)
    if message.text == "/start":
        send_mess = f"<b>Привет {message.from_user.first_name}</b>!\nНапиши привет, спроси как дела"
        bot.send_message(message.chat.id, send_mess, parse_mode='html')
    else:
        sql_hi(message)


def sql_hi(message):
    if message.text == "/sql_hi":
        bot.send_message(message.from_user.id, random_hi())
        bot.register_next_step_handler(message, sql)
    else:
        get_text_hi(message)


def sql(message):
    hi(message.text)


def get_text_hi(message):
    if message.text in records_all():
        bot.send_message(message.from_user.id, random_hi())
    elif message.text in array_dela:
        bot.send_message(message.from_user.id, numpy.random.choice(array_dela, size=3, replace=False))
    else:
        get_text_snisok(message)


def get_text_snisok(message):
    if message.text == "/anime":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('/iselai')
        btn2 = types.KeyboardButton('/comedy')
        btn3 = types.KeyboardButton('/drama')
        btn4 = types.KeyboardButton('/adventure')
        btn5 = types.KeyboardButton('/ecchi')
        btn6 = types.KeyboardButton('/action')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        send_mess = "Выберите жанр"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
        bot.send_message(message.from_user.id, '/iselai             Исекай\n' '/comedy       Комедия\n'
                                               '/drama          Драма\n' '/adventure  Приключение\n'
                                               '/ecchi             Этти\n' "/action\n")
        bot.register_next_step_handler(message, get_text_snisok_anime)
    else:
        get_text_snisok_anime(message)


def get_text_snisok_anime(message):
    random_number = random.randint(0, 99)
    if message.text == "/iselai":
        bot.send_message(message.from_user.id, anime(isekai, random_number, 1))
        bot.send_message(message.from_user.id, anime(isekai, random_number))
    elif message.text == "/comedy":
        bot.send_message(message.from_user.id, anime(action, random_number, 1))
        bot.send_message(message.from_user.id, anime(action, random_number))
    elif message.text == "/drama":
        bot.send_message(message.from_user.id, anime(drama, random_number, 1))
        bot.send_message(message.from_user.id, anime(drama, random_number))
    elif message.text == "/adventure":
        bot.send_message(message.from_user.id, anime(adventure, random_number, 1))
        bot.send_message(message.from_user.id, anime(adventure, random_number))
    elif message.text == "/ecchi":
        bot.send_message(message.from_user.id, anime(ecchi, random_number, 1))
        bot.send_message(message.from_user.id, anime(ecchi, random_number))
    elif message.text == "/action":
        bot.send_message(message.from_user.id, anime(action, random_number, 1))
        bot.send_message(message.from_user.id, anime(action, random_number))
    else:
        registration(message)


# ///////////////////////////Регистрация нового пользователя/////////////////////////////////////


def registration(message):
    if message.text == "/registration":
        bot.send_message(message.from_user.id, 'Ведите логин')
        bot.register_next_step_handler(message, password)
    else:
        come(message)


def password(message):
    global a
    a = message.text
    bot.send_message(message.from_user.id, 'Ведите пароль')
    bot.register_next_step_handler(message, about)


def about(message):
    if examination(a, message.text, message.from_user.id) is None:
        bot.send_message(message.from_user.id, 'Всё прошло отлично!')
    elif examination(a, message.text, message.from_user.id) == '/':
        bot.send_message(message.from_user.id, 'Нельзя начинать логин или пароль с "/"')
    else:
        bot.send_message(message.from_user.id, 'Такой логин уже есть')


# /////////////////////////////Пользователь хочет войти//////////////////////////////////////////


def come(message):
    if message.text == '/come':
        l: str = ''
        for i in range(len(us_log)):
            if message.from_user.id == us_log[i][4]:
                l: str = us_log[i][1]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton(l)
        markup.add(btn1)
        send_mess = "Введите свой логин"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, come_log)
    else:
        mone(message)


def come_log(message):
    global log
    log = message.text
    l: str = ''
    for i in range(len(us_log)):
        if message.from_user.id == us_log[i][4]:
            l: str = us_log[i][2]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton(l)
    markup.add(btn1)
    send_mess = "Введите пароль"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(message, come_pas)


def come_pas(message):
    bot.send_message(message.from_user.id, come_users(log, message.text))
    if come_users(log, message.text) != "Неправильный логин или пароль":
        global log_user
        log_user = '1'


# /////////////////////////////////////ФАРМ ДЕНЕГ/////////////////////////////////////////////////
@bot.message_handler(content_types=['mone'])
def mone(message):
    if message.text == '/mone':
        if log_user == '1':
            money(log)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            btn1 = types.KeyboardButton('/mone')
            btn2 = types.KeyboardButton('/balance')
            markup.add(btn1, btn2)
            send_mess = '+ 1 к балансу'
            bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
        else:
            bot.send_message(message.from_user.id, 'Вы не вошли в систему\n /come Войти')
    else:
        balance(message)


@bot.message_handler(content_types=['balance'])    # БАЛАНС ПОЛЬЗОВАТЕЛЯ
def balance(message):
    if message.text == '/balance':
        if log_user == '1':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            btn1 = types.KeyboardButton('/mone')
            btn2 = types.KeyboardButton('/balance')
            markup.add(btn1, btn2)
            send_mess = f'Вашь баланс {id_user(log)}'
            bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
        else:
            bot.send_message(message.from_user.id, 'Вы не вошли в систему\n /come Войти')
    else:
        get_text_help(message)


# ////////////////////////////////////////// HELP ////////////////////////////////////////////////////


def get_text_help(message):
    if message.text == "/help":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1, btn2 = types.KeyboardButton('/start'), types.KeyboardButton('/help')
        btn3, btn4 = types.KeyboardButton('/anime'), types.KeyboardButton('/sql_hi')
        btn5, btn6 = types.KeyboardButton('/registration'), types.KeyboardButton('/come')
        btn7, btn8 = types.KeyboardButton('/mone'), types.KeyboardButton('/balance')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        send_mess = "/start\n/help\n/anime аниме по жанрам\n/sql_hi добавляет новое приветствие в базу данных\n/registration регистрирует нового пользователя\n/come Войти\n/mone фарм денег\n/balance баланс\n"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понял. Напиши /help чтобы узнать на что я способен!")


bot.polling(none_stop=True, interval=0)
