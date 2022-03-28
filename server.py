from flask import Flask
from flask import request
from flask import render_template
from flask import *

app = Flask(__name__)

#Pirmā lapa, kas tiks ielādēta
@app.route('/',methods = ['POST', 'GET'])
def root():
    return render_template("index.html")
    
#Pārbaudes lapa, lai saprastu, ka kods vispār strādā
@app.route('/health')
def health():
  return "OK"

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/test')
def test():
  parametri = ["Augums", "Svars", "Vecums"]
  images = ["https://cdn.wallpapersafari.com/85/47/LIbvrV.jpg", "https://p4.wallpaperbetter.com/wallpaper/801/136/845/cat-4k-widescreen-hd-wallpaper-preview.jpg", "https://c4.wallpaperflare.com/wallpaper/182/1020/990/photography-manipulation-cat-heterochromia-wallpaper-preview.jpg"]
  return render_template("test.html", param = parametri)

if __name__ == '__main__':
  app.run(debug="true")
