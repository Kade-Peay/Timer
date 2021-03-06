import time, sys, winsound

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r', flush=True)
        time.sleep(1)
        t -= 1
    winsound.Beep(2000, 1000)
    print('Goodbye!\n')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Not enough arguments')
    else:
        try:
            countdown(int(sys.argv[1]))
        except:
            raise TypeError