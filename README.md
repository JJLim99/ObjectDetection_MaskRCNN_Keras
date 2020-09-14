# Tutorial_ObjectDetection_Keras_MaskRCNN


## Dataset Preparation

Your dataset directory should contain the following files:
<br/>
MaskRCNN/<br/>
--...<br/>
--dataset/<br/>
----Annotations/<br/>
--------1.xml<br/>
--------2.xml<br/>
--------...<br/>
----images/<br/>
------train/<br/>
----------1.jpg<br/>
----------1.xml<br/>
----------2.jpg<br/>
----------2.xml<br/>
--------...	<br/>
------val/<br/>
----------81.jpg<br/>
----------81.xml<br/>
----------82.jpg<br/>
----------82.xml<br/>
--------...<br/>
----test/<br/>
----------example.jpg<br/>
--------...<br/>
<br/>
Assuming you have 100 images, separating them based on 8:2 ratio. Train images will have 80 images while validation images will have 20 images.<br/>


    


    
