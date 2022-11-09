#------------------- HANYA CODE REFERENSI---------------------> 


import time, datetime
import telepot
from telepot.loop import MessageLoop 
from dotenv import load_dotenv
load_dotenv() # Environment Variables
import os


now = datetime.datetime.now() #libraries

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    
    bot.sendPhoto(chat_id, (open('Ayam Sakit0.jpg', "rb")))
    bot.sendMessage(chat_id, str("Ayam Sakit"))
    
    if command == "Halo":
        print(chat_id)
        bot.sendMessage(chat_id, str("Halo, Apa Kabar Mas Brooww?"))
 
    # elif command == "Siapa Pacarku?":
    #     bot.sendMessage(chat_id, str("Maaf Jawaban Tidak tersedia"))

    # elif command == "Jam Berapa Sekarang?":
    #     bot.sendMessage(chat_id, str(now.hour)+str(":")+str(now.minute))
        
    # elif command == "Foto Ayam Sakit Terbaru":
    #     bot.sendPhoto(chat_id, (open('Ayam Sakit0.jpg', "rb")))
    
    # elif command == "Test Dong":
    #     bot.sendMessage(chat_id, str("Masuk Sayang"))

def running():
    MessageLoop(bot, handle).run_as_thread()


bot = telepot.Bot(os.getenv("TELEBOT_TOKEN")) # Token Address

if __name__ == "__main__":
    running()
    print("Aku Menunggumu....")
    while 1:
        time.sleep(10)


