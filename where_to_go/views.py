from django.shortcuts import render


def show_main_page(request):
    '''Main_page view'''
    return render(request, 'main_page.html')
