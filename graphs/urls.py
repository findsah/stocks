from django.urls import path
from graphs.views import (
    customer_get_stocks,
)

app_name = 'graphs'
urlpatterns = [

    # url for user registration
    # url for user login
    path('stocks/', customer_get_stocks),
]
