from flask import Flask, render_template

from webapp.model import db, News
from webapp.weather import weather_by_city


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        title = 'Новости python'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', page_title=title, weather=weather, news_list=news_list)
    return app


#if __name__ == '__main__':
#    app.run(debug=True) # благодаря дебагу не нужно перезагружать сервер каждый раз при внесении изменений

# запускать чепез: set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run