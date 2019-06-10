from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'wordcount/home.html')

def about(request):
    return render(request,'wordcount/about.html')

def singabout(request):
    return render(request, 'wordcount/singabout.html')

def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request,'wordcount/count.html',{ 'fulltext' : full_text,'total': len(word_list), 'dictionary': word_dictionary.items()})


def singing(request):

    sing_text = request.GET['singtext']
    sing_list = sing_text.split()
    sing = "으아아아으어어으이~"
    sing_ing = []



    for song in sing_list:
        singsing = song + sing
        sing_ing.append(singsing)
        

    return render(request,'wordcount/singing.html',{'singing':sing_ing})
