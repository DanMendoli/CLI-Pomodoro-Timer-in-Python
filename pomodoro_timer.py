import time
import os
from playsound import playsound


pomo_min = 0
pomo_sec = 0
pomo_count = 0


def pomoTimer():
    global pomo_sec
    global pomo_min
    global pomo_count

    for pomo_min in range(24, -1, -1):
        for pomo_sec in range(59, -1, -1):
            os.system("clear")
            if pomo_sec < 10:
                print("{}:0{}".format(pomo_min, pomo_sec))
                time.sleep(1)
            else:
                print("{}:{}".format(pomo_min, pomo_sec))
                time.sleep(1)
    print("Fim do pomodoro! | Pomodoro ends!")
    playsound("analog-watch-alarm_daniel-simion.wav")
    pomo_count = pomo_count + 1

    if pomo_count == 4:
        pomo_count = 0
        os.system("clear")
        four_pomo = str(input('''Você já realizou 4 pomodoros. Recomenda-se uma pausa longa, de 15 ou 30 minutos.
Iniciar uma pausa longa?
You already realized 4 pomodoros. It's recommended a long break, of 15 or 30 minutes.
Start a long break?
[s|y] - sim|yes
[n] - não|no
 '''))
        if four_pomo in "sSyY":
            longPause()
        if four_pomo in "nN":
            main()


def shortPause():
    global pomo_sec
    global pomo_min

    for pomo_min in range(4, -1, -1):
        for pomo_sec in range(59, -1, -1):
            os.system("clear")
            if pomo_sec < 10:
                print("{}:0{}".format(pomo_min, pomo_sec))
                time.sleep(1)
            else:
                print("{}:{}".format(pomo_min, pomo_sec))
                time.sleep(1)
    print("Fim da pausa curta! | Short pause ends!")
    playsound("analog-watch-alarm_daniel-simion.wav")


def longPause():
    global pomo_sec
    global pomo_min

    long_pause_option = int(input('''
[1] 15 minutos | minutes
[2] 30 minutos | minutes
 '''))

    if long_pause_option == 1:
        for pomo_min in range(14, -1, -1):
            for pomo_sec in range(59, -1, -1):
                os.system("clear")
                if pomo_sec < 10:
                    print("{}:0{}".format(pomo_min, pomo_sec))
                    time.sleep(1)
                else:
                    print("{}:{}".format(pomo_min, pomo_sec))
                    time.sleep(1)

    if long_pause_option == 2:
        for pomo_min in range(29, -1, -1):
            for pomo_sec in range(59, -1, -1):
                os.system("clear")
                if pomo_sec < 10:
                    print("{}:0{}".format(pomo_min, pomo_sec))
                    time.sleep(1)
                else:
                    print("{}:{}".format(pomo_min, pomo_sec))
                    time.sleep(1)
    print("Fim da pausa longa! | Longe break ends!" )
    playsound("analog-watch-alarm_daniel-simion.wav")


def main():
    global pomo_sec
    global pomo_min
    global pomo_count

    os.system("clear")


    option = int(input('''
-- Escolha uma opção --
-- Pick an option --
[1] Pomodoro
[2] Pausa curta | Short break
[3] Pausa longa | Long break
[4] Sair | Exit
 '''))
    if option == 1:
        pomoTimer()
        main()

    if option == 2:
        shortPause()
        main()

    if option == 3:
        longPause()
        main()

    if option == 4:
        exit()


main()
