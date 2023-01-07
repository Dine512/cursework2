from flask import Flask
from feed.feed import feed
from api.api import api

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(feed, url_prefix='/feed')
app.register_blueprint(api, url_prefix='/api')


@app.errorhandler(404)
def not_a_found(error):
    return "<h1>Страница не найдена</h1>", 404


@app.errorhandler(500)
def server_error(error):
    return "<h1>У нас тут технические шоколадки, приносим свои извинения</h1>", 500


if __name__ == "__main__":
    app.run()
