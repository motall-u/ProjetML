from django.shortcuts import render
from .models import ImageUpload
from.forms import ImageForm



# Create your views here.
def getPredictions(image_url):
    #Load image 
    import pickle
    import os
    import numpy as np
    from PIL import Image

    #Open image    
    data_folder: str =  "C:/Users/HP/Desktop/TP_NF_ALL/Projet_NF/web_interface/tets_img_upload/img_upload/myApp"
    img_path = data_folder+""+image_url
    img = Image.open(img_path)
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

    #Processing numpy flatten
    img = np.array(img)
    img = img.flatten()
    img = np.array(img)
    img = img.reshape(1,-1)
   
    #Load model
    my_file = os.path.join(THIS_FOLDER, 'skin_cancer_rf_model.sav')
    model = pickle.load(open(my_file,"rb"))
    #Prediction
    prediction = model.predict(img)
    predict_proba = model.predict_proba(img)
    print(predict_proba[0])
    #Return Value
    if(prediction == 0):
        return "benign",predict_proba[0][0], predict_proba[0][1]
    elif(prediction == 1):
        return "malign",predict_proba[0][0], predict_proba[0][1]
    else:
        return "error"

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            #print(img_obj.image.url)
            predictions, predict_proba_0, predict_proba_1 = getPredictions(img_obj.image.url)
            return render(request, 
                            'index.html',
                             {
                                'form': form,
                                'img_obj': img_obj,
                                'predictions':predictions,
                                'predict_proba_0': predict_proba_0*100,
                                'predict_proba_1': predict_proba_1*100,
                                'predict_proba_0_css': predict_proba_0*200,
                                'predict_proba_1_css': predict_proba_1*200
                            })
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})


def test_home(request):
    return render(request,'test.html',{})