from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def result(request):
    text=request.GET['fulltext']
    a=text.split()
    word_dictionary={}
    for word in a:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1
    
    return render(request,'result.html',{'full':text,'words':len(a),'item' : word_dictionary.items()})
# Create your views here.
