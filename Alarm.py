# M A D E  B Y  S V K  - T 3 C H
# D M  M E  O N  D I S C O R D  F O R  A N Y  F E E D B A C K -> 's.v.karthikeya.dev'
import time
import os

def valid_time(t):
    if ":" not in t:
        return False
    hh, mm = t.split(":", 1)

    if not (hh.isdigit() and mm.isdigit()):
        return False

    hh = int(hh)
    mm = int(mm)

    if not (0 <= hh <= 23 and 0 <= mm <= 59):
        return False

    return True


print('What OS are you using?')
print('\n1) Linux')
print('2) Windows')
print('3) Mac')
choice = input('Enter -> 1/2/3: ').strip()

while choice not in ['1', '2', '3']:
    print('Please enter a valid option. Try again.')
    choice = input('Enter -> 1/2/3: ').strip()

if choice == '1':
    Os = 'linux'
elif choice == '2':
    Os = 'windows'
elif choice == '3':
    Os = 'mac'


while True:
    alarm_time = input('Enter alarm time [HH:MM]: ').strip()
    if valid_time(alarm_time):
        break
    else:
        print('Please enter a valid time. Try again.')

print(f'Alarm time: {alarm_time}')


while True:
    now = time.strftime('%H:%M')
    if now == alarm_time:
        break
    time.sleep(1)

if Os == 'windows':
    import winsound
    winsound.Beep(1000, 2000)

elif Os == 'linux':
    os.system('paplay /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga')

elif Os == 'mac':
    os.system('afplay /System/Library/Sounds/Glass.aiff')

print('Alarm completed.')
while True:
    retry = input('Do you want to retry? [y/n]: ').lower()
    if retry == 'n':
        print('Thank you for using the program!')
        break
    while retry not in ['y', 'n']:
        print('Please enter a valid option. Try again.')

