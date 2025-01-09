from django.urls import path
from msgapp import views
from msgapp.views import ContactForm

urlpatterns = [
    #path('urlpatter',views.fun_name)
    #path('urlpatter',ClassName.as_view())
    path('about',views.about),
    path('delete/<eid>',views.delete),
    path('classbase/<eid>',ContactForm.as_view()),
    path('hello',views.hello),
    path('main',views.main),
    path('product',views.product),
    path('cart',views.cart),
    path('message',views.message),
    path('dashboard',views.dashboard),
    path('edit/<eid>',views.edit),
    

]