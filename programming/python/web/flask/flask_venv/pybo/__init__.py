from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():  # 플라스크 내부에서 정의된 함수
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    # blueprint
    from .views import main_views, question_views, answer_views

    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    # 필터
    from .filter import format_datetime

    app.jinja_env.filters["datetime"] = format_datetime

    return app


"""
pybo에서 파일 이름을 변경했지만 플라스크 기본 앱을 FLASK_APP=pybo로 설정했다. 따라서 프로젝트 루트에 있는 파이보 파일이 아닌 파이보 모듈 즉
pybo/__init__.py를 가리킨다.
"""
