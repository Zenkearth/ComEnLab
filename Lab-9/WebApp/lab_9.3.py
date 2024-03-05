import RPi.GPIO as GPIO

from flask import Flask, render_template
 
LED1 = 27

LED2 = 17

led1state = False
led2state = False
 
GPIO.setmode(GPIO.BCM)

GPIO.setup(LED1, GPIO.OUT)

GPIO.setup(LED2, GPIO.OUT)
 
app = Flask(__name__)
 
@app.route("/")

def hello():
    return render_template('9.3_index.html')
 
@app.route("/led1", methods=['POST'])
def led1on():
    global led1state
    led1state = not led1state
    GPIO.output(LED1, led1state)
    return render_template('9.3_index.html')
    
 
@app.route("/led2", methods=['POST'])
def led1off():
    global led2state
    led2state = not led2state
    GPIO.output(LED2, led2state)
    return render_template('9.3_index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=2500)