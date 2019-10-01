import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    text = "{}<br><br>Here's my secret: {}".format(
        os.environ.get('APP_MESSAGE', 'Hello, World!'),
        os.environ.get('APP_SECRET')
        os.environ.get('SFDC_TEST_USERNAME')
        os.environ.get('SFDC_TEST_PASSWORD')
        os.environ.get('SFDC_TEST_TOKEN')
        os.environ.get('KEYID')
        os.environ.get('SKEYID')
        os.environ.get('BUCKETNAME')
        os.environ.get('RUNMODE')
        os.environ.get('INCREMENTALMODE')
    )
    return text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
