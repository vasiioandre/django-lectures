from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
# def simple_view(request):
#     return HttpResponse("My function based view")

# def sports_page(request):
#     return HttpResponse("Sports Page")

# def finance_page(request):
#     return HttpResponse("Finance Page")

# articles = {
#     'sports': 'Sports Page',
#     'finance': 'Finance Page',
#     'politics': 'Politics Page'
# }

# def news_view(request, topic):
#     return HttpResponse(articles[topic])

# def news_view(request, topic):
#     try:
#         result = articles[topic]
#         return HttpResponse(articles[topic])
#     except:
#         # result = 'No page for that topic'
#         # return HttpResponseNotFound(result)
#         raise Http404("404 GENERIC ERROR")   

# def add_view(request, num1, num2):
#     #domanin.com/my_app/num1/num2
#     add_result = num1 + num2
#     result = f"{num1}+{num2} = {add_result}"
#     return HttpResponse(str(result))

# def num_page_view(request, num_page):
#     topics_list = list(articles.keys()) 
#     topic = topics_list[num_page]

#     return HttpResponseRedirect(reverse('topic-page', args=[topic]))

def simple_view(request):
    return render(request, 'my_app/example.html')
