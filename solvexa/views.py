from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ContactForm
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

# Create your views here.
def home(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        work_email = request.POST.get('email')
        company_name = request.POST.get('company')
        country_name = request.POST.get('country')
        message = request.POST.get('message')
        
        ContactForm.objects.create(
            first_name=first_name,
            last_name=last_name,
            work_email=work_email,
            company_name=company_name,
            country_name=country_name,
            message=message
        )
        # Here you would typically save the data to the database
        # For now, just print it to the console
        print(f"First Name: {first_name}, Last Name: {last_name}, Email: {work_email}, Company: {company_name}, Country: {country_name}, Message: {message}")

        messages.success(request, 'Your message has been sent successfully!')
        return redirect(request.path_info)

    return render(request, 'index.html')





def auth(request):
    if request.method == 'POST':
        # Handle login logic here
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            # User is authenticated, log them in
            login(request, user)
            return redirect('message')
        # If authentication fails, you can handle it here
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('/auth/')
        print(f"Username: {username}, Password: {password}")
        
        # For now, just render the login page again
        return render(request, 'auth/login.html', {'username': username})
    return render(request, 'auth/login.html')


@login_required(login_url="/auth/")
def message(request):
    form=ContactForm.objects.all()
    
    return render(request, 'messages.html',context={'form':form})

def logout_user(request):
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('/auth/')
   
@require_POST
@login_required(login_url="/auth/")
def mark_as_read(request, pk):
    message = get_object_or_404(ContactForm, pk=pk)
    message.is_read = True
    message.save()
    messages.success(request, 'Message marked as read.')
    return redirect('message')
   
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)  
# def contact_form(request):
    
#     # return render(request, 'contact_form.html')  # Render a contact form template