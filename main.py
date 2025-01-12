import telebot
import os
import random
API_TOKEN = os.getenv(<api_token>)
bot = telebot.TeleBot(API_TOKEN)
organizations=["ЮНЕСКО","ЮНИСЕФ","28-Коп","29-КОП"]
ideas=["СОЗДАЙ бота, который рассказывает пользователям сколько людей болеют из-за загрязнения окружающей среды\n",
       "СОЗДАЙ бота который готовит организации про загрязнения окружающей среды\n",
       "СОЗДАЙ бота оторый рассказывает как загразнение окружаещей среды сильно влияет на так и природу так и на антропогическую среду\n",
       "СОЗДАЙ бота, который помогает людям сортировать отходы. Подсказывает, какие предметы можно выбрасывать в обычную урну, а какие стоит отдавать на переработку."]
@bot.message_hander(commands=['make_idea_about_nature'])
def send_idea(message):
    rand_idea=random.choice(ideas)
    bot.reply_to(message,f"Бери эту идею",rand_idea)
@bot.message_hander(commands=['make_org'])
def send_org(message):
    rand_org=random.choice(organizations)
    bot.reply_to(message,f"Бери эту организацию",rand_org)
@bot.message_hander(commands=['ideas_about'])
def send_image(message):
    def get_nature_image_url():    
        url = 'https://air-quality-api.open-meteo.com/v1/air-quality?latitude=52.52&longitude=13.41&hourly=birch_pollen,grass_pollen'
        res = res.get(url)
        data = res.json()
        return data['url']
    
    
    @bot.message_handler(commands=['nature'])
    def nature(message):
        image_url = get_nature_image_url()
        bot.reply_to(message, image_url)
        bot.reply_to(message,f"Этот сайт нужно для картинок или презентаций про загрязнения окружающей среды")
