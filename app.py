from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    from os import environ
    from gunicorn.app.base import BaseApplication

    class Application(BaseApplication):
        def init(self, parser, opts, args):
            return {
                'bind': f"{environ.get('HOST', '127.0.0.1')}:{environ.get('PORT', 8000)}",
                'workers': 1,
            }

        def load(self):
            return app

    Application().run()

