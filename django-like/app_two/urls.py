from app_two import app_two_bp
from app_two import views

path = app_two_bp.add_url_rule

urlpatterns = [
    path('/', view_func=views.app_two_index)
]
