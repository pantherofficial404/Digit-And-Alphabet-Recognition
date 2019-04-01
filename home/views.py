from django.shortcuts import render,redirect
from .utility import imageProcess
from manage import loadModel
model = loadModel()
model._make_predict_function()
def home(request):
    if(request.method=="POST"):
        image_data = request.POST.get('imageData')
        image = imageProcess(image_data)
        return render(request,'home.html',{"prediction":model.predict_classes(image)[0]})
    return render(request,'home.html',{"prediction":0})