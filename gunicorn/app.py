from flask import Flask
from redis import Redis
from flask import send_file

app = Flask(__name__)
# redis = Redis(host='redis', port=6379)

static_dir = '/home/www/arqui/static/files'

@app.route('/')
def hello():
    # count = redis.incr('hits')
    return 'Hello World from Docker!!!!!'

@app.route("/static/<string:filename>")
def serve_static(filename):
    return send_file('{}/{}'.format(static_dir, filename))

@app.route("/process/<int:n>")
def big_for(n):
    for _ in range(n):
        for _ in range(n):
            a = 2
    return 'OK'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
