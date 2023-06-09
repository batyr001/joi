import telebot

bot = telebot.TeleBot('6229556219:AAFz9nnYHfAwf1r4UmCBJbuExEPkUWZpogg') 
# API = 'e7270624-05e0-11ee-8b7f-0242ac130002-e7270692-05e0-11ee-8b7f-0242ac130002'
API = '3d9de74844d28377e81415151cbe6a66'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет рад тебя видеть! Напиши название города')
    
    
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower
    


bot.polling(non_stop=True)
        
    
