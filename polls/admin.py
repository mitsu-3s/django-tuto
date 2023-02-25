from django.contrib import admin
from .models import Question, Choice  # データベースモデルの場所(.models)→管理者に伝えるため

# 管理者画面に情報を追加(認識しやすくする)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # Questionのトップ画面のデザイン
    list_display = ("question_text", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

    # それぞれのオブジェクト設定画面のデザイン
    fieldsets = [
        # Questionの追加画面にタイトルを追加
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
