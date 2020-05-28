from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    text = request.POST.get('text', 'default')
    # checkbox value check
    char_counter = request.POST.get('char_counter', 'off')
    remove_punc = request.POST.get('remove_punc', 'off')
    full_caps = request.POST.get('full_caps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    # check which check box is on
    if char_counter == "on":
        analyzed = 0
        for char in text:
            analyzed += 1
        params = {'purpose': 'Character counted', 'analyzed_text': analyzed}
        text = analyzed
    if remove_punc == "on":
        punctuations = '''!()-{}[];:"',<>.\/?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose': 'Punctuations removed', 'analyzed_text': analyzed}
        text = analyzed
    if full_caps == "on":
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        text = analyzed
    if newlineremover == "on":
        analyzed = ""
        for char in text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}

        if char_counter != "on" and remove_punc != "on" and full_caps != "on" and newlineremover != "on":
            return HttpResponse("Error")

    return render(request, 'analyze.html', params)