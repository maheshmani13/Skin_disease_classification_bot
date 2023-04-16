from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow

import joblib
import pickle
import bz2
import random
import os


list1 = []
list2 =[]

for i in range(1,501):
    img = Image.open('archive/train/Eczema Photos/eczema'+str(i)+'.jpg')
    img = img.resize((200,200))
    imageToMatrice = np.asarray(img)
    image = imageToMatrice.reshape(120000)
    list1.append((image/255.0).reshape(200,200,3))
    list2.append(1)


for i in range(1,501):
    img = Image.open('archive/train/Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions/actinic_keratosis_basal_cell_carcinoma'+str(i)+'.jpg')
    img = img.resize((200,200))
    imageToMatrice = np.asarray(img)
    

    image = imageToMatrice.reshape(120000)
    list1.append((image/255.0).reshape(200,200,3))
    list2.append(2)
    
for i in range(1,490):
    img = Image.open('archive/train/Atopic Dermatitis Photos/atopic_dermatitis'+str(i)+'.jpg')
    img = img.resize((200,200))
    imageToMatrice = np.asarray(img)
    image = imageToMatrice.reshape(120000)
    list1.append((image/255.0).reshape(200,200,3))
    list2.append(3)

for i in range(1,460):
    img = Image.open('archive/train/Melanoma Skin Cancer Nevi and Moles/melanoma_skin_cancer_moles'+str(i)+'.jpg')
    img = img.resize((200,200))
    imageToMatrice = np.asarray(img)
    image = imageToMatrice.reshape(120000)
    list1.append((image/255.0).reshape(200,200,3))
    list2.append(4)

for i in range(1,501):
    img = Image.open('archive/train/Tinea Ringworm Candidiasis and other Fungal Infections/ringworm_candidiasis_fungal'+str(i)+'.jpg')
    img = img.resize((200,200))
    imageToMatrice = np.asarray(img)
    image = imageToMatrice.reshape(120000)
    list1.append((image/255.0).reshape(200,200,3))
    list2.append(5)
    
for i in range(1,211):
    img = Image.open('archive/train/Urticaria Hives/urticaria_hives'+str(i)+'.jpg')
    img = img.resize((200,200))
    imageToMatrice = np.asarray(img)
    image = imageToMatrice.reshape(120000)
    list1.append((image/255.0).reshape(200,200,3))
    list2.append(6)
    

for i in range(1,501):
    img = Image.open('archive/train/Seborrheic Keratoses and other Benign Tumors/seborrheic_keratoses_and_benign_tumors'+str(i)+'.jpg')
    img = img.resize((200,200))
    imageToMatrice = np.asarray(img)
    image = imageToMatrice.reshape(120000)
    list1.append((image/255.0).reshape(200,200,3))
    list2.append(7)
    
for i in range(1,501):
    img = Image.open('archive/train/Psoriasis pictures Lichen Planus and related diseases/'+str(i)+'.jpg')
    img = img.resize((200,200))
    imageToMatrice = np.asarray(img)
    image = imageToMatrice.reshape(120000)
    list1.append((image/255.0).reshape(200,200,3))
    list2.append(8)
    
    

array1 = np.array(list1)
array2 = np.array(list2)


array2 = array2.reshape((3658,1))


X = array1
Y = array2

from tensorflow.keras.models import Sequential
from keras.layers import Convolution2D , MaxPooling2D , Dense ,Flatten


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.10, random_state=1231)


model = Sequential([
    Convolution2D(32,(3,3),activation='relu',input_shape=(200,200,3)),
    MaxPooling2D((2,2)),
    Convolution2D(32,(3,3),activation='relu'),
    MaxPooling2D((2,2)),
    Flatten(),
    Dense(128,activation='relu'),
    Dense(9,activation='softmax')
   
])


model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])




model.fit(X_train , y_train , epochs = 5 , batch_size=64)




model.fit(X_train , y_train , epochs = 50, batch_size=64)


model.evaluate(X_test , y_test)


# img = Image.open('archive/test/Atopic Dermatitis Photos/atopic_dermatitis10.jpg')

# img = img.resize((200,200))
# imageToMatrice = np.asarray(img)
# image = imageToMatrice.reshape(120000)
# image = image/255.0
# print(image)

# y_pred = model.predict(image.reshape(1,200,200,3))
# print(y_pred)

 
joblib.dump(model , 'model_joblib.pkl' )




