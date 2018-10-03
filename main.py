import time
import pyaudio
import os


pomo_min = 0
pomo_sec = 0
pomo_count = 0


def pomoTimer():
    global pomo_sec
    global pomo_min

    for pomo_sec in range(59, -1, -1):
        if pomo_min >= 0:
            if pomo_sec < 10:
                os.system("clear")
                print("{}:0{}".format(pomo_min, pomo_sec))
                time.sleep(1)
            else:
                os.system("clear")
                print("{}:{}".format(pomo_min, pomo_sec))
                time.sleep(1)

            if pomo_sec == 0:
                pomo_min = pomo_min - 1
                pomoTimer()


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
    pomo_min = 24
    pomoTimer()

if choose == 2:
    pomo_min = 4
    pomoTimer()

if choose == 3:
    pomo_min = 29
    pomoTimer()

main()
