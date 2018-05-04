from django.shortcuts import render

def post_list(request):
    return render(request, 'Toledo/post_list.html', {})
