# Tutorial_ObjectDetection_Keras_MaskRCNN

## Supporting_Scripts
rename.py<br/>
--rename the file <br/>
--usage: python rename.py <br/>
<br/>
resize.py<br/>
--resize the image files based on your requirement within the same directory<br/>
--usage: python resize.py <br/><br/>

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
Assuming you have 100 images, separating them based on 8:2 ratio. Train images will have 80 images while validation images will have 20 images.<br/><br/>


## RealTime_Webcam
Copy all python files in RealTime_Webcam and paste it into the MaskRCNN directory (Main repository)<br/>
<br/>
video_demo.py <br/>
--usage (realtime webcam): python video_demo.py 0<br/>
--usage (realtime recorded video): python video_demo.py path_to_recorded_video.mp4<br/><br/>

visualize_cv2.py.py<br/>
--TO DO:<br/>
  1. Update the COCO_MODEL_PATH according to your dir<br/>
  2. Update the name of config class (optional)<br/>
  3. Update the NUM_CLASSES<br/>
  4. Update the class_names<br/>


    
