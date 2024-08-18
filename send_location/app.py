from flask import Flask
from routes import routes

app = Flask('send_location')
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)