import RPi.GPIO as GPIO
import time

sw = 22
RED = 21
GREEN = 20
BLUE = 18

LED_color = [RED, GREEN, BLUE]
state_color = [0b000, 0b001, 0b010, 0b011, 0b100, 0b101, 0b110, 0b111]
current_state = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for pin in LED_color:   
    GPIO.setup(pin, GPIO.OUT)

def colorChange(State):
    for i in range(2, -1, -1):
        if State & 0x01:
            GPIO.output(LED_color[i], 1)
        else:
            GPIO.output(LED_color[i], 0)
        State >>= 1

try:
    for pin in LED_color:
        GPIO.output(pin, 0)
    while True:
        if GPIO.wait_for_edge(sw, GPIO.FALLING):
            current_state = (current_state + 1) % len(state_color)
            colorChange(state_color[current_state])
            time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()

print("\nBye...")