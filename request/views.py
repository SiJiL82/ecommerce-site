from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewRequestForm
from .models import Request


def request(request):
    """ A view to return the product request page """
    my_requests = None
    if request.user.is_authenticated:
        my_requests = Request.objects.filter(
            user_id=request.user, fulfilled=False)
    context = {
        'new_request_form': NewRequestForm(),
        'my_requests': my_requests
    }

    if request.method == 'POST':
        new_request_form = NewRequestForm(data=request.POST)
        if new_request_form.is_valid():
            new_request = new_request_form.save(commit=False)
            new_request.user_id = request.user
            new_request.email_address = request.user.email
            new_request.save()
        return render(request, 'request/request.html', context)
    else:
        return render(request, 'request/request.html', context)


@login_required
def remove_request(request, requestid):
    """Remove the request """

    try:
        selected_request = get_object_or_404(Request, pk=requestid)
        selected_request.delete()
        return HttpResponse(status=200)
    except Exception:
        return HttpResponse(status=500)


@login_required
def update_request(request, requestid):
    """ Update the specified request """

    selected_request = get_object_or_404(Request, pk=requestid)

    if request.method == 'POST':
        context = {
            'new_request_form': NewRequestForm(),
            'my_requests': Request.objects.filter(user_id=request.user,
                                                  fulfilled=False)
        }
        request_form = NewRequestForm(request.POST)

        if request_form.is_valid():
            req_category = request_form.cleaned_data['category']
            req_size = request_form.cleaned_data['size']
            req_description = request_form.cleaned_data['description']
            req_user_id = request.user
            req_name = request_form.cleaned_data['name']
            req_email_address = request.user.email
            req = Request(
                id=requestid,
                category=req_category,
                size=req_size,
                description=req_description,
                user_id=req_user_id,
                name=req_name,
                email_address=req_email_address,
                date_created=selected_request.date_created
            )
            req.save()

        return render(request, 'request/request.html', context)
    else:
        request_form = NewRequestForm(initial={
            'name': selected_request.name,
            'category': selected_request.category,
            'size': selected_request.size,
            'description': selected_request.description
        })

        context = {
            'request_form': request_form
        }

        return render(request, 'request/request_update.html', context)
