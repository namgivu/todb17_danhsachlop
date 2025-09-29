from flask import Flask
import requests
import json
import os


app = Flask(__name__)

@app.route('/')
def index():
  # API_URL='http://localhost:88'  #TODO why network=bride dont understand localhost mapped port

  API_URL='http://apiapp_c:5000'  #NOTE must run in same network for apiapp n webapp eg docker run --network nn
  res = requests.get(f'{API_URL}/danhsachlop', timeout=2)
  res.raise_for_status()
  j = res.json()

  NAME = os.environ.get('NAME')
  if not NAME: NAME='todb'  # set here as notpassed NAME envvar will be passed w/ blank string
  print(f'{NAME=}', flush=True)

  #region cook markdownrendered_s
  markdownrendered_s = ''

  import json
  data = j
  headers = list(data[0].keys())

  # find max width for each column
  col_widths = {
    h: max(len(h), max(len(str(row[h])) for row in data))
    for h in headers
  }

  # print header row
  header_row = "| " + " | ".join(f"{h:<{col_widths[h]}}" for h in headers) + " |"
  markdownrendered_s += header_row

  # print separator row
  separator_row = "| " + " | ".join("-" * col_widths[h] for h in headers) + " |"
  markdownrendered_s += separator_row

  # print data rows
  for row in data:
    markdownrendered_s += "| " + " | ".join(f"{str(row[h]):<{col_widths[h]}}" for h in headers) + " |"


  #endregion cook markdownrendered_s

  return f'''
  <!DOCTYPE html>
  <body>
    <h1>Welcome to Flask App {NAME}!</h1>
    <pre>{json.dumps(j, indent=2)}</pre>  #TODO render list of members in list j as html table
    
    <br>
    <hr>
    <pre>{markdownrendered_s}</pre>  #TODO render list of members in list j as html table
  </body>
  </html>
  '''

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
