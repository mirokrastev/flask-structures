from flask import Flask

app = Flask(__name__)

import settings


# Run server
if __name__ == '__main__':
    app.run()
