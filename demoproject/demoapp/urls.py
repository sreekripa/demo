
from django.urls import path
from demoapp import views
app_name='app'

urlpatterns = [
    path('',views.shop,name='shop'),
    path('shops/<int:book_id>',views.detail,name='detail'),
    path('add/',views.add_product,name='add_product'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete')
]