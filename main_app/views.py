from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect

# Create your views here.

def widgets(request):
    widget_form = WidgetForm()
    widget_list = Widget.objects.all()
    total = 0
    for widget in widget_list:
        total += widget.quantity
    
    
    return render(request,'widgets.html', {'total':total,'widget_form':widget_form, 'widget_list':widget_list})

def add_widget(request):
  
    new_widget = Widget.objects.create(
        description=request.POST['description'],
        quantity=request.POST['quantity'],
        
    )
    print(new_widget)
    new_widget.save() 
    
    widget_list = Widget.objects.all()
    total = 0
    for widget in widget_list:
        total += widget.quantity
    return render(request,'widgets.html', {'new_widget':new_widget, 'widget_list':widget_list, 'total':total})


# def add_widget(request):
#     form = WidgetForm(request.POST)
    
#     if form.is_valid():
#         new_widget = form.save()
#         new_widget.save()
#     return render(request,'widgets.html')

# def get_widget(request):
#     def get_widget(request):
#     # if this is a POST request we need to process the form data
#         if request.method == 'POST':
#             # create a form instance and populate it with data from the request:
#             form = WidgetForm(request.POST)
#             # check whether it's valid:
#             if form.is_valid():
#                 # process the data in form.cleaned_data as required
#                 # ...
#                 # redirect to a new URL:
#                 return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#         else:
#             form = WidgetForm()

#         return render(request, 'widget_list.html', {'form': form})



    
# class WidgetDelete(DeleteView):
#     model = Widget
#     success_url = "/widgets/"
    
def delete(request, pk):
    Widget.objects.filter(id=pk).delete()
    return redirect('widgets')
    
    