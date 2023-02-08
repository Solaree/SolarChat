from flask import *
from api.token_api import *
#from chat.core import *

def flask_xd():
    app = Flask(__name__)

    def token():
        @app.route('/token')
        def token():
            return token_api()
    token()

    """
    def solarchat():
        @app.route('/solarchat')
        def chat():
            return handle()
    solarchat()
    """
    if __name__ == '__main__':
        app.run(debug=True)
flask_xd()