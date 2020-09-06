from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log user in
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})
