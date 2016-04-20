from bottle import route, run, static_file

@route('/')
def index():
  return static_file('index.html', root='./')

@route('/data')
def data():
  return static_file('data.json', root='./')

run(host='localhost', port=8000, debug=True)
