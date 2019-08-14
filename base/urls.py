from  .views import BasePageView
from django.urls import path


urlpatterns = [
    path("", BasePageView.as_view()),

]
