from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  return app

@app.route('/')
def Energy():
  return 'Here comes the enegry main side!'

if __name__ == '__main__':
  app.run(host='0.0.0.0')
