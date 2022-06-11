from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime
from mix import *
import random
user_id = [867705312, 2063531206, 746144832, 5157599418, 419834517, 180316194, 750423179, 243892031, 532113134,
           375690499, 778600419, 410604681, 1738943375, 1082579902, 391366043, 367819844]

replace_first_name = ['Айрат', 'Серега', 'Руслан Батя', 'Ильгиз', 'Алешенька', 'Руслан Белый', 'Азат', 'Леха Месси',
                      'Я Рустем и я тоже хочу играть', 'Даниил', 'Тимур', 'Владик', 'Андрэ', 'Володя', 'Альмир', 'Дима']


you_not_list = ['Чувак, тебя нет в списке!', 'Ошибка, тебя нет в списке', "Опс, сначала добавься, а потом уже удаляйся",
                'Тебя нет', 'Тебя нет, но ты можешь добавиться' ]
you_in_list = ["Ты уже в списке под именем: ", 'Эээ, меня не проведешь, я тебя знаю, ты -  ']

my_list = []
dt = datetime.now().hour
limit_hour = 12


def log_name(update: Update, context: ContextTypes):
    file = open('log.csv', 'a')
    file.write(f'{update.message.from_user.id}, '
               f'{update.message.from_user.first_name}, '
               f'{update.message.text}\n')
    file.close()


async def log(update: Update, context: ContextTypes):
    log_name(update, context)


def create_message(data, limit_player, number):
    message = ''
    rezerv = ''
    message_random_data_01 = ''
    message_random_data_02 = ''
    if len(data) == 0:
        return 'Пока что список пуст'
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
        else:
            new_message = f'Твой игрок в резерве!\n' \
                          f'\n' \
                          f'Резерв!\n' \
                          f'{rezerv}' \
                          f'\n' \
                          f'Основной список:\n' \
                          f'{message}'

        return new_message


async def run(update: Update.message, context: ContextTypes):
    log_name(update, context)
    mess = ''

    if update.message.text == '+':
        user_name = update.message.from_user.id

        for i in range(len(user_id)):
            if user_name == user_id[i]:
                user_name = replace_first_name[i]
        if type(user_name) == int:
            user_name = update.message.from_user.first_name
        if user_name not in my_list:
            my_list.append(user_name)
            mess = create_message(my_list, 16, 0)
        else:
            mess = f'{you_in_list[random.randint(0,len(you_in_list) - 1)]}{user_name}'
    elif update.message.text == '-':
        user_name = update.message.from_user.id
        for i in range(len(user_id)):
            if user_name == user_id[i]:
                user_name = replace_first_name[i]
        if type(user_name) == int:
            user_name = update.message.from_user.first_name
        if user_name in my_list:
            my_list.remove(user_name)
            mess = create_message(my_list, 16, 0)
        else:
            mess = f'{you_not_list[random.randint(0, len(you_not_list) - 1)]}'
    elif update.message.text == '+1':
        if dt >= limit_hour:
            user_name = update.message.from_user.id
            for i in range(len(user_id)):
                if user_name == user_id[i]:
                    user_name = replace_first_name[i]
            if type(user_name) == int:
                user_name = update.message.from_user.first_name
            user_plus_1 = f'+1 от {user_name}'
            my_list.append(user_plus_1)
            mess = create_message(my_list, 16, 1)

        else:
            mess = f'Добавить игрока можно после {limit_hour} часов'
    elif update.message.text == '-1':
        user_name = update.message.from_user.id

        for i in range(len(user_id)):
            if user_name == user_id[i]:
                user_name = replace_first_name[i]
        if type(user_name) == int:
            user_name = update.message.from_user.first_name
        user_plus_1 = f'+1 от {user_name}'
        if user_plus_1 in my_list:
            my_list.remove(user_plus_1)
            mess = create_message(my_list, 16, 1)
        else:
            mess = 'Твоего игрока нет в списке'

    await update.message.reply_text(f'{mess}', quote=True)


async def help_command(update: Update.message, context: ContextTypes):
    await update.message.reply_text(f"Добавиться в список: отправь ' + ' \n"
                                    f"Удалиться из списка: отправь ' - ' \n"
                                    f"Добавить одного игрока в список: отправь ' +1 ' \n"
                                    f"Удалить одного игрока из списка: отправь ' -1 '\n"
                                    f"/del - обнулить список", quote=True)


async def del_command(update: Update.message, context: ContextTypes):
    global my_list
    my_list = []
    await update.message.reply_text(f"Список обнулен", quote=True)
