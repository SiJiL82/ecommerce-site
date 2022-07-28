from django.shortcuts import render
from .forms import NewRequestForm

def request(request):
  """ A view to return the product request page """

  context = {
    'new_request_form': NewRequestForm()
  }

  if request.method == 'POST':
    for field in request.user._meta.fields:
      print(field.name)
    new_request_form = NewRequestForm(data=request.POST)
    if new_request_form.is_valid():
      new_request = new_request_form.save(commit=False)
      new_request.user_id = request.user
      if request.user.first_name:
        new_request.name = request.user.first_name + ' ' + request.user.last_name
      else:
        new_request.name = request.user.username
      new_request.email_address = request.user.email
      new_request.save()
    return render(request, 'request/request.html', context)
  else:
    return render(request, 'request/request.html', context)
  