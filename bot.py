import telebot
import config
import os
import urllib.request as urllib2

from telebot import types

bot = telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands=['start','help'])
def sendWelcome(message):
	
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item2 = types.KeyboardButton('🛑 /stop')
    item3 = types.KeyboardButton('📷 photo')
    item4 = types.KeyboardButton('🎧 audio')
    item5 = types.KeyboardButton('📄document')
    item6 = types.KeyboardButton('😀sticker')
    item7 = types.KeyboardButton('🗺️location')

    markup.add(item2, item3, item4, item5, item6, item7)

   
    bot.send_message(message.chat.id, 'Привіт, я Rocketbot. \nТут ти можеш спробувати деякі команди.\n', parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
        if message.text == '📷 photo':
            url = 'https://images.wallpaperscraft.ru/image/kamni_izgiby_polosy_202982_1280x720.jpg'
            urllib2.urlretrieve(url, 'url_image.jpg')
            img = open('url_image.jpg', 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, img)
            img.close()
       
        elif message.text == '🎧 audio':
             audio = open('E:\TelegramBot\Rocketbot/audio\Betkhoven-k-jelize.mp3', 'rb')
             bot.send_chat_action(message.from_user.id, 'upload_audio')
             bot.send_audio(message.from_user.id, audio)
             audio.close()
        
        elif message.text == '📄document':
            directory = 'E:\TelegramBot\Rocketbot\doc'
            all_files_in_directory = os.listdir(directory)
            for files in all_files_in_directory:
                document = open(directory + '/' + files, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_document')
                bot.send_document(message.from_user.id, document)
                document.close()
        
        elif message.text == '😀sticker':
                bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAPNYF3oAAEkTDgI2T03AovBKdMpp6dxAAKZDAACc9vxSvg2bNcO2zSTHgQ')

        elif message.text == '🗺️location':
        	bot.send_chat_action(message.from_user.id, 'find_location')
        	bot.send_location(message.from_user.id, 50.766978,25.363532)

        elif message.text == '🛑 /stop':
        	hide = telebot.types.ReplyKeyboardRemove()
	        bot.send_message(message.from_user.id, '...', reply_markup=hide)

        else:
            bot.send_message(message.chat.id, 'Я не знаю, що відповісти 😢')
 

bot.polling(none_stop=True)	