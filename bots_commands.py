from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime

user_id = [867705312, 2063531206, 746144832, 5157599418, 419834517, 180316194, 750423179, 243892031, 532113134]
print(f'Длина списка ID {len(user_id)}')
replace_first_name = ['Айрат', 'Серега', 'Руслан Батя', 'Ильгиз', 'Алешенька', 'Руслан Белый', 'Азат', 'Леха Месси',
                      'Старпер']
print(f'Длинга списка имен: {len(replace_first_name)}')

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
    if len(data) == 0:
        return 'Пока что список пуст'
    elif len(data) <= limit_player:
        for i in range(len(data)):
            message += f'{i + 1}.  {data[i]}\n'
        return message
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
        if user_name not in my_list:
            my_list.append(user_name)
            mess = create_message(my_list, 16, 0)
        else:
            mess = 'Ты уже в списке'
    elif update.message.text == '-':
        user_name = update.message.from_user.id
        for i in range(len(user_id)):
            if user_name == user_id[i]:
                user_name = replace_first_name[i]
        if user_name in my_list:
            my_list.remove(user_name)
            mess = create_message(my_list, 16, 0)
        else:
            mess = 'Тебя итак нет в списке'
    elif update.message.text == '+1':
        if dt >= limit_hour:
            user_name = update.message.from_user.id
            for i in range(len(user_id)):
                if user_name == user_id[i]:
                    user_name = replace_first_name[i]
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
                                    f"Удалить одного игрока из списка: отправь ' -1 '", quote=True)
