from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save(commit=False)
            if request.user.is_authenticated:
                contact_message.user = request.user
            contact_message.save()
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact/contact.html', context)

def dealer_locator(request):
    # In a real application, you would integrate with Google Maps API
    # For now, we'll use static dealer data
    dealers = [
        {
            'name': 'BMW Manhattan',
            'address': '555 West 57th Street, New York, NY 10019',
            'phone': '(212) 555-0123',
            'hours': 'Mon-Sat: 9AM-7PM, Sun: 11AM-5PM',
        },
        {
            'name': 'BMW Brooklyn',
            'address': '123 Atlantic Avenue, Brooklyn, NY 11201',
            'phone': '(718) 555-0123',
            'hours': 'Mon-Sat: 9AM-7PM, Sun: 11AM-5PM',
        },
        {
            'name': 'BMW Queens',
            'address': '45-15 Northern Blvd, Queens, NY 11101',
            'phone': '(347) 555-0123',
            'hours': 'Mon-Sat: 9AM-7PM, Sun: 11AM-5PM',
        },
    ]

    context = {'dealers': dealers}
    return render(request, 'contact/dealer_locator.html', context)