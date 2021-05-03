# Fortnite-Object-Detection
Fornite Object Detection using Darknet's YOLOv3 implemented via PyTorch.<br>

Click to view YouTube demo<br>
[![IMAGE ALT TEXT](https://img.youtube.com/vi/Y0Y_G9msqrc/0.jpg)](https://www.youtube.com/watch?v=Y0Y_G9msqrc)


<b>Current functionality:</b><br>
-Read Monitor as PIL.Image then convert to Numpy array<br>
-Run Numpy arrayof monitor through neural network to detect objects<br> 
-Output tensor has all objects detected on monitor 
-Refine tensor: Remove all 'non person' objects 
-To aviod detecting yourself the object at the bottom of the screen is removed
-Draw red rectangle around identifications <br>
-Overlay image on running Fortnite with the ability to click through the image as to not effect gameplay<br>
-Mouse fires when target is in the cross hairs
<br>
<b>Future Updates:</b><br>
-Distinguish between persons identified. i.e. teammates vs. enemies<br>
-Train NN based on Fortnite footage

<br><br>
<b>Contact:</b> MichaelRomeroJr1@gmail.com
