from sqlite3 import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import FeatureProduct, FoodItem
from django.contrib.auth.models import User


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            # Redirect to a success page
            
            return redirect('home')
        
    else:
        messages.error(request,'username & password may be invalid')
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Attempt to create a new user
        if User.objects.filter(username=username).exists():
            error_message = 'Username is already taken. Please choose a different username.'
            return render(request, 'signup.html', {'error_message': error_message})

        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request,"your account has been created successfully")

            # Redirect or perform additional actions for successful signup
            return redirect('login_view')
        

    # Display an error message when the username is already taken
    else:
        return render(request, 'signup.html')
    

def home(request):
    feature_items = FeatureProduct.objects.all()
    food_items = []

    for item in feature_items:
        food_items.append(item.food_items )
  
    context = {
        'food_items': food_items,
    }

    return render(request,'home.html',context)

def contact_view(request):
    return render(request,'contactus.html')

def food_item(request, feature_product_id):
    feature_product = FeatureProduct.objects.get(id=feature_product_id)
    name = feature_product.food_items.name
    description = feature_product.description
    price = feature_product.price
    image = feature_product.image
    return render(request,'menu.html')


def cart(request):
    return render(request, 'cart.html') 

