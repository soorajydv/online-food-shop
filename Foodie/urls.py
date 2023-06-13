from django import views
from django.contrib import admin
from django.urls import path
from myapp.views import contact_view, home, login_view, logout_view,FoodItem,signup,cart
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('contact/',contact_view,name='contact'),
    path('menu/',FoodItem,name='FoodItem'),
    path('login/',login_view,name='login_view'),
    path('logout/',logout_view,name='logout_view'),
    path('signup/',signup,name='signup'),
    path('cart/',cart,name='cart'),
    

    # path('product/',product),
    # path('order/<int:food_item_id>/',order_now, name='order_now')
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
