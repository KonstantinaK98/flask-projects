from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('base.html')  

@app.route('/temperature')
def temperature_converter():
   return render_template('temperature.html')     

if __name__ == '__main__':
   app.run()