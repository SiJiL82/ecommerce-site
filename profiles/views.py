from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from django.contrib.auth.models import User


def profile(request):
    """ Display the user's profile """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            user = User.objects.get(pk=request.user.id)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            form.save()
            # TODO: Add success message
            #  messages.success(request, 'Details updated successfully')
        # else:
            # TODO: Add failure message
            # messages.error(request, 'Update failed. Please ensure
            # the form is valid)
    else:
        form = UserProfileForm(instance=profile)

    form = UserProfileForm(instance=profile, initial={
        'first_name': profile.user.first_name,
        'last_name': profile.user.last_name,
    })
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Display order details for a past order """
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'order_history': True
    }

    return render(request, template, context)
