from django.shortcuts import render
from .forms import NewsletterSignupForm
from django.contrib import messages


def signup(request):
    form = NewsletterSignupForm()

    context = {
        'newsletter_signup_form': form,
    }

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
        }
        form = NewsletterSignupForm(form_data)
        if form.is_valid():
            form.save()

            messages.success(request, 'Newsletter signup successful!')

    return render(request, 'newsletter/newsletter_signup.html', context)
