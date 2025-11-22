# M A D E  B Y  SVK-T3CH
#DM me on discord for any queries/feedback -> s.v.karthikeya.dev
import time
from _ast import While
while True:

 q = input('Do you wanna use-\n1)Stop watch\n2)Countdown timer\nYour choice [1/2]: ')
 if q == '2':
    print('Noted!')
    median_time = int(input('What is your medium of countdown? \n1)Seconds\n2)Minutes\n3)Hours\n-Your Choice [1/2/3]: '))
    if median_time == 1:
     Seconds = int(input(f'Enter the number of seconds you wanna use for countdown: '))
     for i in range(Seconds, 0, -1):
        print(f'Time left - {i} sec')
        time.sleep(1)
     print("Time's up! ")
    elif median_time == 2:
     Minutes = int(input(f'Enter the number of minutes you wanna use for countdown: '))
     for i in range(Minutes-1, -1, -1):
         for s in range(59, -1, -1):
             print(f'Time left - {i} min:{s} sec')
             time.sleep(1)
     print("Time's up! ")
    elif median_time == 3:
     Hours = int(input(f'Enter the number of hours you wanna use for countdown: '))
     for i in range(Hours-1, -1, -1):
         for m in range(59, -1, -1):
             for s in range(59, -1, -1):
               print(f"Time left - {i} hr:{m} min:{s} sec")
               time.sleep(1)
     print("Time's up! ")
 elif q == '1':
    import time

    print("=== Stopwatch ===")
    input("Press Enter to start...")

    start_time = time.time()

    try:
        while True:
            elapsed = int(time.time() - start_time)
            hours = elapsed // 3600
            minutes = (elapsed % 3600) // 60
            seconds = elapsed % 60
            print(f"\rTime elapsed: {hours:02d}:{minutes:02d}:{seconds:02d}", end='')
            time.sleep(1)  # wait 1 second before updating
    except KeyboardInterrupt:  # stops when user presses Ctrl+C
        elapsed = int(time.time() - start_time)
        hours = elapsed // 3600
        minutes = (elapsed % 3600) // 60
        seconds = elapsed % 60
        print(f"\nStopwatch stopped at {hours:02d}:{minutes:02d}:{seconds:02d}")
 else:
    print('Please enter a valid input')

 while True:
  again = input('Do you wanna use the program again? [y/n]: ')
  if again == 'y':
    break
  elif again == 'n':
    print('Thank you for using the program')
    exit()
  else:
    print('Please enter y or n')
