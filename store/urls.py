from django.urls import path
from django.contrib.auth.forms import UserCreationForm

from . import views

urlpatterns = [
	#Leave as empty string for base url
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
	path('', views.home, name="home"),
    path('homein/', views.homein, name="homein"),
    path('customer/', views.userPage, name="customer"),
    path('store/', views.store, name="store"),
    path('storeout/', views.storeout, name="storeout"),
	path('cart/', views.cart, name="cart"),
    path('update_item/', views.updateItem, name="update_item"),
	path('checkout/', views.checkout, name="checkout"),
    path('comments/', views.comments, name="comments"),
    path('commentsin/', views.commentsin, name="commentsin"),
    path('contact/', views.contact, name="contact"),
    path('contactin/', views.contactin, name="contactin"),
    path('process_order/', views.processOrder, name="process_order"),
    path('write_comment/', views.writeComment, name='write_comment'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('delivery/', views.delivery, name="delivery"),
    path('customer_info/', views.customerInfo, name="customer_info"),
    path('reports/', views.reports, name="reports"),
    path('website_report/<str:pk>/', views.websiteReport, name='website_report'),
    path('farm_report/<str:pk>/', views.farmReport, name='farm_report'),
    path('overall_report/<str:pk>/', views.overallReport, name='overall_report'),
    path('ReturnManagement/', views.Return, name='ReturnManagement'),
    path('enter_return_item/', views.enterItem, name='enter_return_item'),
    path('customer_setting/', views.customersetting, name='customer_setting'),
    path('order/<str:pk_test>/', views.order, name='order'),
    path('receipt/<str:pk_test>/', views.receipt, name='receipt'),
    path('updateorder/<str:pk>/', views.updateorder, name='updateorder'),
    path('deleteorder/<str:pk>/', views.deleteorder, name='deleteorder'),
    path('status/<str:pk>/', views.status, name='status'),




]
