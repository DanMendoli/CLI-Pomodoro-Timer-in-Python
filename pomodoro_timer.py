import time
import os
from playsound import playsound


pomo_min = 0
pomo_sec = 0
pomo_count = 0


def pomoTimer():
    global pomo_sec
    global pomo_min

    for pomo_min in range(24, -1, -1):
        for pomo_sec in range(59, -1, -1):
            os.system("clear")
            if pomo_sec < 10:
                print("{}:0{}".format(pomo_min, pomo_sec))
                time.sleep(1)
            else:
                print("{}:{}".format(pomo_min, pomo_sec))
                time.sleep(1)
    playsound("analog-watch-alarm_daniel-simion.wav")


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
    playsound("analog-watch-alarm_daniel-simion.wav")


def main():
    global pomo_sec
    global pomo_min
    global pomo_count

    os.system("clear")


choose = int(input('''
-- Escolha uma opção --
[1] Pomodoro
[2] Pausa curta
[3] Pausa longa
 '''))
if choose == 1:
    if pomo_count == 4:
        pomo_count = 0
        '''Você já realizou quatro pomodoros. Recomenda-se uma pausa longa, de 15 ou 30 minutos.
        Deseja fazer uma pausa longa?
        [s] - sim
        [n] - não'''
    else:
        pomoTimer()
        pomo_count = pomo_count + 1


if choose == 2:
    shortPause()


main()