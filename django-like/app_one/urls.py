from app_one import app_one_bp
from app_one import views

path = app_one_bp.add_url_rule

urlpatterns = [
    path('/', view_func=views.app_one_index),
    path('/test', view_func=lambda: 'Lambda func works!')
]
