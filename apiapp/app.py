from flask import Flask
from flask_cors import CORS
import json
import pathlib

# Load data from apiapp/data/danhsachlop.json
danhsachlop = json.loads(
  (pathlib.Path(__file__).parent/'data/danhsachlop.json').read_text()
)

app = Flask(__name__)
CORS(app)  # enable cors for all routes

@app.route('/danhsachlop')
def get_users():
  return danhsachlop

@app.route('/')
def health_check():
  return {'abb':122}


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
