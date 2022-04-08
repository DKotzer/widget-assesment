from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def widgets(request):
    widget_form = WidgetForm()
    return render(request,'widgets.html', {'widget_form':widget_form})


def add_widget(request, widget_id):
    form = WidgetForm(request.POST)
    
    if form.is_valid():
        new_widget = form.save()
        new_widget.save()
    return render(request,'widgets.html',widget_id = widget_id )

