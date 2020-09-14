# Tutorial_ObjectDetection_Keras_MaskRCNN

1. Dataset Preparation

Your dataset directory should contain the following files:

MaskRCNN/
--...
--dataset/
----Annotations/
--------1.xml
--------2.xml
--------...
----images/
------train/
----------1.jpg
----------1.xml
----------2.jpg
----------2.xml
--------...	
------val/
----------81.jpg
----------81.xml
----------82.jpg
----------82.xml
--------...
----test/
----------example.jpg
--------...

Assuming you have 100 images, separating them based on 8:2 ratio. Train images will have 80 images while validation images will have 20 images.
    


    
