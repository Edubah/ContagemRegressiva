import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end='\t')
        time.sleep(1)
        t -= 1

    print('Tempo Terminado')

t = input('Entre com o tempo em segundos: ')
countdown(int(t))