from flask import Flask
import webbrowser
import threading
from src.routes.app_routes import blueprint as routes

app = Flask(__name__)

app.register_blueprint(routes)

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    threading.Timer(1.25, open_browser).start()
    app.run(debug=True)

