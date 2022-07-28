from tkinter import Widget
from django import forms
from .models import Book, Category


class CategoryForm(forms.ModelForm):    
    class Meta:
        model = Category
        fields = ['name']                  #ADMIN ONLY!!!
        widgets = {
            'name': forms.TextInput(attrs= {'class':'form-control'})
        }








class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'photo_book',
            'photo_author',
            'pages',
            'price',
            'retal_price_day',
            'retal_period',
            'status',
            'category',   
            


          ###### ONLY ADMINNNNNNN!!!!!!!!!!!!!!!

          # you can add w/e u want here to show up in the edit mode in the main page "index" + add from models.py

         ]
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control'}),
            'photo_book' : forms.FileInput(attrs={'class':'form-control'}),# FileInput to force it to upload only files!
            'photo_author' : forms.FileInput(attrs={'class':'form-control'}),# FileInput to force it to upload only files!
            'pages' : forms.NumberInput(attrs={'class':'form-control'}),# NumperInput force it to only write numbers!
            'price' : forms.NumberInput(attrs={'class':'form-control'}),# NumperInput force it to only write numbers!
            'retal_price_day' : forms.NumberInput(attrs={'class':'form-control'}),# NumperInput force it to only write numbers!
            'retal_period' : forms.NumberInput(attrs={'class':'form-control'}), # NumperInput force it to only write numbers!
            'status' : forms.Select(attrs={'class':'form-control'}),
            'category' : forms.Select(attrs={'class':'form-control'}), # forms.select! on category to choose between  فن-تاريخ etc

            #make the forms look better with look and size and the cool big blue bar u can add more!
        }

