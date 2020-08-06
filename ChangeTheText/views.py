# User Created File.

from django.http import HttpResponse
from django.shortcuts import render

def index(request):    
    return render(request, 'index.html')

def analyze(request):
    ## Gets the text value
    djtext = request.POST.get('text', 'default')
    
    ## Checkbox values
    removepunc = request.POST.get('removepunc', 'off')  ## if removepunc is checked then it will perform the removepunc otherwise it will be off(default value)
    fullcaps = request.POST.get('fullcaps', 'off')
    smallcaps = request.POST.get('smallcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspacesremover = request.POST.get('extraspacesremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    ## check which check box is ON or OFF
    if removepunc == "on":       
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = "" 
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed

    if smallcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'Changed to Lower Case', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Lines Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspacesremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Spaces Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == 'on':
        analyzed = djtext
        params = {'purpose': 'Character Count', 'analyzed_text': len(analyzed)}
        # djtext = analyzed     ## Commented for future reference in case I need it.

    if (removepunc != "on" and fullcaps != "on" and smallcaps != "on" and newlineremover != "on" and extraspacesremover != "on" and charcount != "on"):
        return HttpResponse("Error: Please select at least one option.")

    else:
        return render(request, 'analyze.html', params)
