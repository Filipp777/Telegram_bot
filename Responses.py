from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "sup"):
        return "Hey! How's it going"

    if user_message in ("who are you","who are you?",):
        return "I am a DumbShitBot!"

    if user_message in ("Status", "status",):
        return "Для обработки файла .frx загрузите его"

    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H/%M/%S")


        return str(date_time)

    return "I don't undertand you"