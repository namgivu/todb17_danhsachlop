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
  import json
  data = j

  # Extract headers from keys
  headers = data[0].keys()

  # Build HTML table
  html = "<table border='1' style='border-collapse:collapse;'>\n"
  html += "  <tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr>\n"

  for row in data:
    html += "  <tr>" + "".join(f"<td>{row[h]}</td>" for h in headers) + "</tr>\n"

  html += "</table>"

  markdownrendered_s = html
  #endregion cook markdownrendered_s

  return f'''
  <!DOCTYPE html>
  <body>
    <h1>Welcome to Flask App {NAME}!</h1>
    <pre>{json.dumps(j, indent=2)}</pre>  
    
    <br>
    <hr>
    <pre>{markdownrendered_s}</pre> 
  </body>
  </html>
  '''

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
