from django.urls import path
from .views_unit import store
from .views import stores_route

urlpatterns = [
    path('', stores_route, name="store-entrance-list"),

    path('login/', store._login), # working

    path('check-domain-name/<domain_name>', store._check_domain),# working

    path('<store_domain>', store._get_store, name="store-instance"),# working

    path('<store_domain>/actions/start-trial', store._start_trial),#

    path('<store_domain>/actions/activate', store._activate_store),#

    path('<store_domain>/actions/deactivate', store._deactivate_store),#
]
