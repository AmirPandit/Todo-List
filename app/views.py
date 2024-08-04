from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from . import forms
from . import models

#for creating form in html and save the data getting from user
def create(request):
    if request.method == 'POST': # if user submit the form
        form = forms.FormList(request.POST) # assign the data from FormList to form variable 
        if form.is_valid(): #if the data are valid
            form.save() #save the form
            form = forms.FormList() #create blank form in html
    else:
        form = forms.FormList() #call the blank form 

    return render(request, 'create.html', {'form': form}) #render the request from user, template and the data
    
def view(request):
    forms = models.formdataset.objects.all().values() #gets all the values saved in model
    templates = loader.get_template('view.html') #loades the view template
    context = {
        'form' : forms #assign all values
    }

    return HttpResponse(templates.render(context, request)) #render request, data, templates

def viewdetail(request, id):
    details = models.formdataset.objects.get(id=id) #gets the data according to id
    templates = loader.get_template('viewdetail.html') #loads the template
    context = {
        'details' : details
    }

    return HttpResponse(templates.render(context, request))

def edit(request, id):
    edit_Form = get_object_or_404(models.formdataset, id=id) # gets the data according to id, if not the 404 error
    if request.method == 'POST':
        form = forms.FormList(request.POST, instance=edit_Form) #gets the updated data
        if form.is_valid(): #if correct 
            form.save() #save
            return redirect('viewdetail', id=id)
    else:
        form=forms.FormList(instance = edit_Form) #shows the form

    return render(request, 'edit.html', {'form': form})

def delet(request, id):
    dele = get_object_or_404(models.formdataset, id=id)
    dele.delete() #delete the data according to id
    return redirect('view') #redirect to view page

