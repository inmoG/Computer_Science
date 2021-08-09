from flask import Blueprint, render_template
from flask.helpers import url_for
from werkzeug.utils import redirect
from pybo.models import Question

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/hello")
def hello_pybo():
    return "Hello, Pybo!"


@bp.route("/")
def index():
    return redirect(url_for("question._list"))
