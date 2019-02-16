import config
import telebot
import requests

bot = telebot.TeleBot(config.token)

#Nothing
@bot.message_handler(content_types=["text"])
def translate(message):
    last_text=(message.text)
    token='your yandex.api'
    url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    trans_option = {'key':token, 'lang':'en-ru', 'text': last_text}
    webRequest = requests.get(url_trans, params = trans_option)
    rus_text = webRequest.text
    rus_text = rus_text[36:(len(rus_text)-3)]
    bot.send_message(message.chat.id, rus_text)
    

if __name__ == '__main__':
     bot.polling(none_stop=True)


