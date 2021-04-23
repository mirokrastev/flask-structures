from app import app as flask
from app_one import app_one_bp
from app_one.views import main_index
from app_two import app_two_bp


path = flask.add_url_rule

apps = {
    'app_one': lambda **options: flask.register_blueprint(app_one_bp, **options),
    'app_two': lambda **options: flask.register_blueprint(app_two_bp, **options)
}

urlpatterns = [
    # Home
    path('/', view_func=main_index),

    # Invoke lambda func with kwargs to register the blueprint app
    apps['app_one'](url_prefix='/app_one'),
    apps['app_two'](url_prefix='/app_two'),
]
