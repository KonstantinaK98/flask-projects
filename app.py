from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
   if request.method == 'POST':
      if request.form['submit_button'] == 'Temperature':
         return render_template('temperature.html')
      elif request.form['submit_button'] == 'Url Shortener':
         return render_template('urlshortener.html')
   else:   
      return render_template('base.html')  

@app.route('/temperature')
def temperature_converter():
   return render_template('temperature.html')

@app.route('/urlshortener', methods=['POST','GET'])
def urlshortener():
   if request.method == "POST":
      if request.form['url'] != '':
         return
      else:
         return render_template('urlshortener.html')  
   else:       
      return render_template('urlshortener.html')        

if __name__ == '__main__':
   app.run()