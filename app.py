from flask import Flask, request
import settings

settings.load_machines()

app = Flask(__name__)


@app.route('/startup')
def startup():
    print(request)
    return ''


@app.route('/shutdown')
def shutdown():
    return ''


@app.route('/status')
def status():
    return ''


if __name__ == '__main__':
    app.run(host=settings.HOST, port=settings.PORT, debug=True)
