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
<<<<<<< HEAD
    app.run(debug=True)
=======
    app.run()
>>>>>>> 2d077b513ed70c4283e9295240fea592b83a36eb

