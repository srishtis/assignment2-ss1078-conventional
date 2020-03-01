import time
import logging
from flask import Flask

app = Flask(__name__)
count=0
# counter = redis.Redis(host='redis', port=6379)


def visits_count():
    global count
    count = count + 1
    return count    


@app.route('/')
def hello():
    count = visits_count()
    return 'This site has been visited {} times.\n Refresh to see a change!'.format(count)


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
