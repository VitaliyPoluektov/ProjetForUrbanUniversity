def send_email (message, recipient, sender = 'university.help@gmail.com'):
    print(recipient[len(recipient)-4:])
    if recipient.find('@') == -1 or sender.find('@') == -1 or (recipient[len(recipient)-4:] != '.com'\
            and recipient[len(recipient)-4:] != '.net' and recipient[len(recipient)-3:] != '.ru')\
            or (sender[len(sender)-4:] != '.net' and sender[len(sender)-3:] != '.ru' and sender[len(sender)-4:] != '.com'):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')



    # '.com'
    # '.ru'
    # '.net'
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')