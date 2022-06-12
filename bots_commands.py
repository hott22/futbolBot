from telegram import Update
from telegram.ext import ContextTypes, CallbackContext
from datetime import datetime
from mix import *
import random

user_id = [867705312, 2063531206, 746144832, 5157599418, 419834517, 180316194, 750423179, 243892031, 532113134,
           375690499, 778600419, 410604681, 1738943375, 1082579902, 391366043, 367819844, 441989210]

replace_first_name = ['Айрат', 'Серега', 'Руслан Батя', 'Ильгиз', 'Алешенька', 'Руслан Белый', 'Азат', 'Леха Месси',
                      'Я Рустем и я тоже хочу играть', 'Даниил', 'Тимур', 'Владик', 'Андрэ', 'Володя', 'Альмир', 'Дима',
                      'Макс']

you_not_list = ['Чувак, тебя нет в списке!', 'Ошибка, тебя нет в списке', "Опс, сначала добавься, а потом уже удаляйся",
                'Тебя нет', 'Тебя нет, но ты можешь добавиться', 'Кинули дважды , совести нет совсем…']
you_in_list = ["Ты уже в списке под именем: ", 'Эээ, меня не проведешь, я тебя знаю, ты -  ']

you_add_in_list = ['Могучее ТЕЛО добавлено!', 'Красава!', 'Так деражать!', 'Без тебя бы было не интересно!:-)',
                   'Я знал, что ты придешь!', 'Ура, товарищи!!!', 'Счастливый, футбол поиграешь сегодня!',
                   'Я тебя обожаю!',
                   'Счастливчик )...жаль я не умею играть (((', 'Учти, с тебя минимум дубль сегодня!',
                   'Что ж, ты в игре!',
                   'Давай только без твоих выкрутасов в стиле Месси! окей?',
                   'Почитай сначала правила игры, а потом приходи!',
                   'На тебя поступила жалоба, что ты довольно часто забиваешь в свои ворота!', 'Ты сегодня в защите!',
                   'Ты добавлен, но будь добр, приходи трезвым!', 'Пузико решил растрясти?)',
                   ' Так, смотри кто к нам пришел!',
                   'Сразу предупреждаю, у нас пеший футбол, тоесть пузико не исчезнет']

you_del_in_list = ['Бля, я так и знал что ты это сделаешь!!!', 'Пацаны, нас кинули!', 'Бейте его!!!', 'Ты куда? ёмаё!',
                   'Даю тебе последний шанс вернуться!', 'Ну и съёбывай от сюда!', 'И как тебя назвать после этого?',
                   '...No comments...', 'Ты совершил ошибку!!', "Перепутал '+' c '-' ?", 'Пиздец конечно...']

you_add_friend_in_list = ['Могучее ТЕЛО добавлено!', 'Он точно придёт?', 'Если он не приедет, платишь за него тоже!',
                          'Если он НЕ придет - отрабатываешь за двоих, учти!!!', 'Это кто? Надеюсь Рональдиньо?',
                          'Неужели это Дзюба?', 'Он умеет играть?', 'Проинструктируй его, что у нас тут пеший футбол!',
                          'Пусть приходит!', 'Недеюсь он не хоккеист?', 'О, круто, оценим чувака!',
                          'Недеюсь это защитник? Нападающих тут и так дохуя!',
                          'Если это нападающий, то ему тут делать нехуй, конкуренция страшная!']

you_del_friend_in_list = ['Бля, я так и знал что ты это сделаешь!!!', 'Пацаны, нас кинули!', 'Бейте его!!!',
                          'Куда он?','Чё происходит не пойму?','Предсказуемо конечно!',
                          'Он что вспомнил, что никогда не играл в футбол?',
                          'Скажи ему, что тут ребята огорчились!','То добавляешь, то удаляешь, давай посерьезнее?']

my_list = []
dt = datetime.now().hour
limit_hour = 12


def log_name(update: Update, context: ContextTypes):
    file = open('log.csv', 'a')
    file.write(f'{update.message.from_user.id}, '
               f'{update.message.from_user.first_name}, '
               f'{update.message.text}, '
               f'{update.message.date}, '
               f'{update.message.chat.id}\n')
    file.close()


async def log(update: Update, context: ContextTypes):
    log_name(update, context)


def create_message(data, limit_player, number):
    message = ''
    rezerv = ''
    message_random_data_01 = ''
    message_random_data_02 = ''
    if len(data) == 0:
        return 'Ау, люди вы где?'
    elif len(data) <= limit_player:
        if len(data) < limit_player:
            for i in range(len(data)):
                message += f'{i + 1}.  {data[i]}\n'
            return message
        elif len(data) == limit_player:
            for i in range(len(data)):
                message += f'{i + 1}.  {data[i]}\n'
            random_data = mix_list(data)

            len_random_data = len(random_data) // 2
            for i in range(len_random_data):
                message_random_data_01 += f'{i + 1}.  {random_data[i * 2]}\n'
            for i in range(len_random_data):
                message_random_data_02 += f'{i + 1}.  {random_data[i * 2 + 1]}\n'

            message_random_data = f'Набор:\n' \
                                  f'{message}' \
                                  f'\n' \
                                  f'Рекомендую поделиться так:\n' \
                                  f'\n' \
                                  f'Синие:\n' \
                                  f'{message_random_data_01}' \
                                  f'\n' \
                                  f'Рыжие:\n' \
                                  f'{message_random_data_02}'
            return message_random_data
    else:
        for i in range(limit_player):
            message += f'{i + 1}.  {data[i]}\n'
        data_rezerv = data[limit_player:]
        for i in range(len(data_rezerv)):
            rezerv += f'{i + 1}.  {data_rezerv[i]}\n'

        if number == 0:
            new_message = f'Ты в резерве!\n' \
                          f'\n' \
                          f'Резерв!\n' \
                          f'{rezerv}' \
                          f'\n' \
                          f'Основной список:\n' \
                          f'{message}'
            return new_message
        elif number == 1:
            new_message = f'Твой игрок в резерве!\n' \
                          f'\n' \
                          f'Резерв!\n' \
                          f'{rezerv}' \
                          f'\n' \
                          f'Основной список:\n' \
                          f'{message}'
            return new_message
        elif number == 2:
            new_message =   f'Резерв!\n' \
                            f'{rezerv}' \
                            f'\n' \
                            f'Основной список:\n' \
                            f'{message}'


            return new_message


async def run(update: Update.message, context: ContextTypes):
    log_name(update, context)
    mess = ''
    user_name = update.message.from_user.id
    if update.message.text == '+':
        for i in range(len(user_id)):
            if user_name == user_id[i]:
                user_name = replace_first_name[i]
        if type(user_name) == int:
            user_name = update.message.from_user.first_name
        if user_name not in my_list:
            my_list.append(user_name)

            mess = f'*{you_add_in_list[random.randint(0, len(you_add_in_list) - 1)]}*\n' \
                   f'\n' \
                   f'{create_message(my_list, 16, 0)}'
        else:
            mess = f'*{you_in_list[random.randint(0, len(you_in_list) - 1)]}{user_name}*'
    elif update.message.text == '-':
        for i in range(len(user_id)):
            if user_name == user_id[i]:
                user_name = replace_first_name[i]
        if type(user_name) == int:
            user_name = update.message.from_user.first_name
        if user_name in my_list:
            my_list.remove(user_name)
            mess = f'*{you_del_in_list[random.randint(0, len(you_del_in_list) - 1)]}*\n' \
                   f'\n' \
                   f'{create_message(my_list, 16, 2)}'
        else:
            mess = f'*{you_not_list[random.randint(0, len(you_not_list) - 1)]}*'
    elif update.message.text == '+1':
        if dt >= limit_hour:
            for i in range(len(user_id)):
                if user_name == user_id[i]:
                    user_name = replace_first_name[i]
            if type(user_name) == int:
                user_name = update.message.from_user.first_name
            user_plus_1 = f'+1 от {user_name}'
            my_list.append(user_plus_1)
            mess = f'*{you_add_friend_in_list[random.randint(0, len(you_add_friend_in_list) - 1)]}*\n' \
                   f'\n' \
                   f'{create_message(my_list, 16, 1)}'

        else:
            mess = f'*Добавить игрока можно после {limit_hour} часов*'
    elif update.message.text == '-1':
        for i in range(len(user_id)):
            if user_name == user_id[i]:
                user_name = replace_first_name[i]
        if type(user_name) == int:
            user_name = update.message.from_user.first_name
        user_plus_1 = f'+1 от {user_name}'
        if user_plus_1 in my_list:
            my_list.remove(user_plus_1)
            mess = f'*{you_del_friend_in_list[random.randint(0, len(you_del_friend_in_list) - 1)]}*\n' \
                   f'\n' \
                   f'{create_message(my_list, 16, 2)}'
        else:
            mess = '*Твоего игрока нет в списке*'

    await update.message.reply_text(f'{mess}', quote=True, parse_mode='Markdown')


async def help_command(update: Update.message, context: ContextTypes):
    await update.message.reply_text(f"Добавиться в список: отправь ' + ' \n"
                                    f"Удалиться из списка: отправь ' - ' \n"
                                    f"Добавить одного игрока в список: отправь ' +1 ' \n"
                                    f"Удалить одного игрока из списка: отправь ' -1 '\n"
                                    f"/del - обнулить список", quote=True)


async def del_command(update: Update.message, context: ContextTypes):
    global my_list
    my_list = []
    await update.message.reply_text(f"Эээ, список кто-то ёбнул", quote=True)

async def tela_tela(context: CallbackContext):
    global my_list
    if dt >= 16 and len(my_list) < 15:
        await context.bot.send_message(chat_id=-1001781416351, text='Тела, тела, тела, тела, тела, тела....')