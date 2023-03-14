from flask import Flask, render_template
import redis
import json
import os
import logging

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger()


app = Flask(__name__)

r = redis.Redis(host=os.getenv('REDIS_HOST'), port=6379, db=0)
def my_function():
    # ... some code ...
    result = {"name":'George', 'id': 12}
    # ... some more code ...
    
    # publish result to Redis channel
    r.publish('facility', json.dumps(result))
    logger.info("<<<<<<<<<<<<We have published a message>>>>>>>>>>>>>>")

    return result

@app.route('/')
def index():
    return {'msg': 'hello pub'}

@app.route('/subscribe')
def subscribe():
    pubsub = r.pubsub()
    pubsub.subscribe('my_channel')
    return render_template('subscribe.html')

@app.route('/publish')
def publish():
    result = my_function()
    return {'msg': f'Published result: {result}'}

@app.route('/stream')
def stream():
    pubsub = r.pubsub()
    pubsub.subscribe('my_channel')
    return render_template('stream.html', pubsub=pubsub)

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
