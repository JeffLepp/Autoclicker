import mouse as m
import keyboard as k
import time

i = 1

while True:
    if k.is_pressed('space'):
        break
    m.click('left')
    Location = m.get_position()
    print(f'iteration: {i} position: {Location}')
    i += 1
    time.sleep(1)
        
