from django.contrib import admin
from .models import Question, Choice  # データベースモデルの場所(.models)→管理者に伝えるため

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
