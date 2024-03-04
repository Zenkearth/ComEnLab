from flask import Flask,render_template

app = Flask(__name__)


import RPi.GPIO as GPIO   

led1 = 27
led2 = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)

@app .route('/<led>/<state>')
def led_control(led,state):
    if led == 'led1':
        if state == "on":
            GPIO.output(led1,True)
        if state == "off":
            GPIO.output(led1,False)
    if led == 'led2':
        if state == "on":
            GPIO.output(led2,True)
        if state == "off":
            GPIO.output(led2,False)
    return f'<h2> {led} {state} </h2>'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)