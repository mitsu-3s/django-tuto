from django.contrib import admin
from django.urls import path

# from .views import hellofunc  # hellofuncの場所(.views)
from . import views

app_name = "polls"
urlpatterns = [
    path(
        "hello/", views.hellofunc
    ),  # /polls/hello/のリクエストを受け取ったら、hellofunc関数を実行
    path("", views.index, name="index"),  # ex: /polls/
    path(
        "<int:question_id>/", views.detail, name="detail"
    ),  # ex: /polls/5/のリクエストを受け取ったら、views.pyのdetailを実行(question_idで、pathのint:question_idを引数とする)
    path(
        "<int:question_id>/results/", views.results, name="results"
    ),  # ex: /polls/5/results/
    path(
        "<int:question_id>/vote/", views.vote, name="vote"
    ),  # ex: /polls/5/vote/
]
