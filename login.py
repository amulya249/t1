from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

...

def login_request(request):
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "main/login.html",
                  context={"form":form})