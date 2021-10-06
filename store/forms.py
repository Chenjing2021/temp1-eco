from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


from .models import OrderItem, Order, Customer, Comment,ReturnManagement


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['name', 'content']




class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']



class OrderItemForm(ModelForm):
	class Meta:
		model = OrderItem
		fields = '__all__'



class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = ['delivered', 'delivered_date']



class ReturnItemForm(ModelForm):
	class Meta:
		model = ReturnManagement
		fields = '__all__'