import telepot
import logging
import module
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = "토큰입력"

def handler(msg):
    content_type, chat_Type, chat_id, msg_date, msg_id = telepot.glance(msg, long=True)

    if content_type == "text":
        str_message = msg["text"]
        if str_message = msg["text"]
        if str_message[0:1] == "/":
            args = str_message.split(" ")
            command = args[0]
            del args[0]

            if  command == "/dir" or command == "/목록":
                filepath = " ".join(args)
                if filepath.strip() == "":
                    bot.sendMessage(chat_id, "/dir [대상폴더] 로 입력해주세요.")
                else:
                    filelist = module.get_dir_list(filepath)
                    bot.sendMessage(chat_id, filelist)
            elif command == "/weather" or command == "날씨":
                w = " ".join(args)
                weather = module.get_weather(w)
                bot.sendMessage(chat_id, weather)
            elif command == "/monday":
                w = " ".join(args)
                output = module.money_traslate(w)
                bot.sendMessage(chat_id, output)
            elif command[0:4] == "/get":
                filepath = " ".join(args) # change list >> str
                if os.path.exists(filepath):
                    try:
                        if command == "/getfile":
                            bot.sendDocument(chat_id, open(filepath, "rb"))
                        elif command == "/getimage":
                            bot.sendPhoto(chat_id, open(filepath, "rb"))
                        elif command == "/getaudio":
                            bot.sendAuido(chat_id, open(filepath, "rb"))
                        elif command == "/getvideo":
                            bot.sendVideo(chat_id, open(filepath, "rb"))
                    except Exception as e:
                        bot.sendMessage(chat_id, f"{e} 파일 전송 실패")
                else:
                    bot.sendMessage(chat_id, "파일이 존재하지 않습니다.")

bot = telepot.Bot(TELEGRAM_TOKEN)
bot.message_loop(handler, run_forever=True)