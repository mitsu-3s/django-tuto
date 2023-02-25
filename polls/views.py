from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice  # polls/urls.pyからモデル情報インポート
from django.urls import reverse
from django.views import generic


# 汎用ビューを使う場合

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"


# 汎用ビューを使わない場合


# # Create your views here.
# def hellofunc(request):
#     return HttpResponse("Hello")


# # ショートカット前、render()を使わない
# # def index(request):
# #     # Questionモデルから、pub_dateで降順で並び替えた後に、最初の5つの要素だけを取得する
# #     latest_question_list = Question.objects.order_by("-pub_date")[:5]

# #     # templates/polls/index.htmlを読み込む
# #     template = loader.get_template("polls/index.html")

# #     context = {
# #         "latest_question_list": latest_question_list,
# #     }
# #     return HttpResponse(template.render(context, request))


# # ショートカット後
# def index(request):
#     # Questionモデルから、pub_dateで降順で並び替えた後に、最初の5つの要素だけを取得する
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     # 第1引数としてrequestオブジェクト、第2引数としてテンプレート名（場所）、第3引数（任意）で辞書
#     return render(request, "polls/index.html", context)


# # ショートカット前
# # def detail(request, question_id):  # urls.pyの<int:question_id>を引数としている
# #     try:
# #         # pkはprimary keyで、Questionモデルからquestion_idに合致するものを取得
# #         question = Question.objects.get(pk=question_id)
# #     except Question.DoesNotExist:
# #         raise Http404("Question does not exist")
# #     return render(request, "polls/detail.html", {"question": question})


# # ショートカット後
# def detail(request, question_id):
#     # オブジェクトがなかったら、Http404を送出
#     question = get_object_or_404(Question, pk=question_id)
#     # 第1引数としてrequestオブジェクト、第2引数としてテンプレート名（場所）、第3引数（任意）で辞書
#     return render(request, "polls/detail.html", {"question": question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):  # エラー処理
#         return render(
#             request,
#             "polls/detail.html",
#             {
#                 "question": question,
#                 "error_message": "You didn't select a choice.",
#             },
#         )
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # def resultsにリダイレクト
#         return HttpResponseRedirect(
#             reverse("polls:results", args=(question.id,))
#         )
