import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    text = "{}<br><br>Here's my secret: {}".format(
        os.environ.get('APP_MESSAGE', 'Hello, World!'),
        os.environ.get('SFDC_TEST_USERNAME')
    )
    return text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
