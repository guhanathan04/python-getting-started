from django.shortcuts import render
from django.http import HttpResponse
import emoji
import itertools
import re
from gingerit.gingerit import GingerIt
from .models import Greeting
from django.http import JsonResponse



# Create your views here.
def index(request):
    unwanted_chars = [';', ':', "*",'/','$','#','=','+','%','^','_','~',"`",'<',">"]
    replace_chars=['@','&']
    
    if request.method == 'POST':
        # initializing test string
        test_string = request.POST.get('text')
        #test_string = "Gu;ha*n: @ s=r$ira*m pl+ey:s; cr*ic%ke=^t_~💕👭  andu B$o🙈th o%f t*ha_m a~r`e g+o=u#d f<r/ie*_d~😂s."
        given = test_string
        # printing original string
        #print ("Original String : " + test_string)

        # using replace() to
        # remove unwanted_chars
        for i in unwanted_chars :
            given = given.replace(i, '')
            for j in replace_chars:
                given = given.replace(j, 'and')
        #After Punctuation and replace
        #print("\nAfter Removing Special Charcaters : ",test_string)

        #For emoji removal
        p=emoji.get_emoji_regexp().sub(r'', given)
        #print("\nAfter Emoji Removal : ",p)


        s = re.sub('([.,!?()])', r' \1 ', p)
        q= re.sub('\s{2,}', ' ', s)
        a= ' '.join(k for k, _ in itertools.groupby(q.split()))
        k=re.sub(r'\s([?,.!"](?:\s|$))', r'\1', a)
        #print("\nNormal Sentence :",k)


        parser=GingerIt()
        c=parser.parse(k)
        resultt=c['result']
       

        d1=list(set(k.split(' ')) ^ set(resultt.split(' ')))

        results= " ".join(("--"+t+"**") if t in d1 else t for t in k.split())
        
        print("\nMistake Highlighted sentence:",results)
        print("\nThe correct sentence:",resultt)
        if c['text'] == c['result']:
            flag="False"
        else:
            flag = "True"
        
        context={"status":"Success","flag":flag,"original_text":test_string,"Wrong_Text":results,"corrected_text":resultt}
    
        return JsonResponse(context)
        #return render(request, "new.html",context)
    return render(request,"form.html")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
