
# Using the color corrector code

## Sections

 1. Jetson Nano Startup
 2. Navigating to the project directory
 3. Running different demos
	 * Basic Predictions Demo (Best FPS)
	 * GUI Demo with sliders
	 * Webcam Demo


## Jetson Nano Startup
The Jetson Nano has a few external peripherals that you must check before turning it on: 
+ The prototype's external 500GB Samsung SSD that *has* to be plugged into a USB port. This external drive is for the Nano's swap file.
+ The Logitech wireless dongle for the wireless keyboard
+ An external display. There are two ports for this, you can either use an HDMI cable or Display Port
+ A Webcam if necessary
+  The 20A power supply so that the Nano can receive power

To power on the Nano just plug in the powersupply to an wall outlet and it will start up. The start up processes should take from 15-20 seconds and an Nvidia logo will appear as a splashscreen during such.

Once the Nano is running, a desktop will be shown like below:

![Jetson Nano Desktop](https://github.com/jplineb/ColorbrandsProj/blob/master/Documentation/photos/Screenshot%20from%202019-08-12%2015-11-25.png?raw=true)

From this, we can accesses the basic computer necessities. 

In the case of where the desktop icons are too small, select the **gear icon** in the top right of the screen and select **system settings**. The window shown below should appear:

![settings](https://github.com/jplineb/ColorbrandsProj/blob/master/Documentation/photos/Screenshot%20from%202019-08-12%2015-21-11.png?raw=true)

From here select **Displays** under the Hardware section and change the **Scale for menu and title bars** slider until satisfied and click **apply**

![enter image description here](https://github.com/jplineb/ColorbrandsProj/blob/master/Documentation/photos/Screenshot%20from%202019-08-12%2015-25-57.png?raw=true)

If for some reason you need to connect to Wifi while using the Nano, click the **Wifi signal symbol** in the top right and change the appropriate settings.

Another *Mandatory* step we must take is to put the Nano in its maximum usage mode. Normally when you start up the Nano, it is in an eco-power state that varies the the clock speed of the processor depending on the load of the system. The current version of JETPack tends to be hyperactive in changing the clock speed. For this project we want to make sure that the Nano is at maximum usability at all times.

To put the processor at its maximum clock speed, either search for the terminal window shortcut by pressing the **Windows Key** on the Logitech keyboard or select the **Terminal Shortcut** on the **Task Bar** like shown below:

![enter image description here](https://github.com/jplineb/ColorbrandsProj/blob/master/Documentation/photos/Screenshot%20from%202019-08-12%2015-38-08.png?raw=true)

With the Terminal open type the following and press **Enter**:

    Sudo jetson_clocks

To verify that the previous command worked, we can use a program called jtop. To access jtop, type the following in the Terminal:

    Sudo jtop
If done correctly the terminal should now look like the image below and if done correctly the frequency readings for each core should be *1.4GHz*

![enter image description here](https://lh3.googleusercontent.com/RK13oWmw0EqDwwnYWCFRoEjx43Pf7JlYvYR3M-e7hjo1b6AL9KiZ7A5uE7IqhCHH-UPJQtwtRBCjhvp_MlTXNSWr3gM-AVAevYfW2UWFfjW72JmBvQ0ioveWJ94MYNAODgVYOZ7hXQZ9ZBfC7lO9JQ-ycERwZd63R2nFiF274gT-izpLy78G3ETzrfKHic6qzhh2pwlFecWI7BSvBHUlWx03onfRXiWGgmycwt2ob3fph3A8RUsRshYfmGG3lZpfRgSYpCk5Z6ojvrj9m7s-fBCl0psBTMV9Unhxj_L1Hj7fl926d4aXf5nIf-wcgMPf3vnWTdxOD6gSP7QBGGdJGBrGdS_h9HjgHq5BrOUgi69RlbdI2EwmoDodpCEsRDYG4SzquhlbNSCZO76RQdWVii2bboODpy2lAcURtSDjRbfQziR53KWjfIJY9Bw02SgTOA7BM0tIh1PkrX6XTm9WWIydE3H9xzu1pZlAPwZH_f75xa_Sn0Xs2fZWUFlVGIwq_LjWlStyI2YLLwNGoY0-U_d11emso9zBR4rF4tEt2yH8ou28akkdr1cBGxOHQCiYRqI6Pj2AX8z5FYNBlzt0uoiLgSEYbWjESLuhJ-F4GkqIdxNjM2UWqRZAz_Xmp8uL7ZZpdsgQk-NO7xx-S3BVlicuZw7MVU4=w1456-h918-no)

jtop shows us useful information for looking at the performance of the Nano such as memory usage, power consumption, cpu and gpu load. You can choose to leave this open during the demo or close it by pressing **Q** on the keyboard.

The Nano is now ready for whatever you throw at it!

## Navigating to the project directory

The resources for this project are located in a folder named **BrandColorsProj** To view this directory with a file explorer, click the **Files** Shortcut located on the taskbar and select the **BrandColorsProj** folder. This folder contains 3 sub folders named:
* Code
* Data
* Models

What we want to use is the **/BrandColorsProj/Code/** directory. If you have any demo videos you want to run place them in this folder.

Open a Terminal window by either **right clicking** on the **Terminal shortcut** on the taskbar and selecting **New Terminal** or continue with the window you were just using during the jtop setup.

To navigate to the **/BrandColorsProj/Code/** directory, type the following into the Terminal: 

    cd BrandColorsProj/Code/

To see if you are in the correct directory enter the following into the Terminal:

    ls
The following should appear:

![enter image description here](https://lh3.googleusercontent.com/eD2sYX5qMRzeLHN1iXKqYeEm3pgBWYn46SPJjqQ0wO5LlMHtolykrBGkaQD7QHhV1Fv_kqOnEfoPx_1Lb-s1XYTC_1VsczRbPCuzdUsYe3e1ue4I_QvSmxuVK5Ip1qQY7dFXVtEuh42If6QQl09cZgMZZc4llTvYwZ8eWMCrqybvxXBFTE8ZsHfpNPQUvkvz37Lpr-R7kXYhnc-NDYQxamF83Ez-BM1M4lejSyP2ntFIZc07FUM1jiU9dPxSLbsT-wYAyun4L3nKwV2UL00-ThPMIKDAnXxj9t-H2QbDZhJYHL7W_DmVmegGkbvOM6kjFw3acKWFbPgJfkNVpPPro5GrZRYwzvrqHzJo68VYsCz_k40d-xZYXbUcliDX6slHw4FYxmHJuW4k_EjwVyA3SBzRuHbXF7gKE7rZ12USh0ZJ4tAyJvJkzfIBjxcqTnHDSnVxSM5agYhCxbvvGBQUzfJkl0BTX-MSNrKc9ThCmgYgSaFn-siIn4taDTWM7KH3xXRQ2X_hrYGygTa5G1pE6w_gwJNjSM47xy0bR7rZtojRv6SvJ9tnvL5Tq5NIWSATz60M5earbzgkRdNSBUq2tk_7L5Hs1nn4ZL3SZdCGoIo70OC1wH3tyXXceIYsNenpwzFMK3XFm49lZDJrIp4zKS7OHZasPfQ=w1462-h916-no)
*If this did not work type **exit** into the Terminal and press **Enter**. Then, open a new Terminal Window and try again.*

## Running Different Demos
Now that you have navigated to the correct directory in the Terminal, running the Python scripts is easy. The code folder contains three Python scripts to be used for different demos:
* Basic Predictions Demo (Best FPS)
* GUI Demo with sliders (Smoothest Output)
* Webcam Demo

Each of these demos has arguments you can pass with them to modify the demo:
 
``--demo or -d : used to run the demo with the broadcasted vs corrected``
``--profile or -p : Runs line profiler``
``--intensity or -i  : Scale factor for the correction mask``
``--cpu or -c : Runs the demo in cpu mode``
``--help or -h : provides the information above``

***Note***: You will most likely use --demo when showing the demo off as it provides the side by side comparison in the output window

If you haven't done so already, put demo footage in the **BrandColorsProj/Code/** directory. If you don't have footage on hand use Demo_Clip_720p_30.mp4

### Basic Predictions Demo
The Normal Predictions Demo is the fastest of demos when it comes to frame rate as it is only rendering the video and the demo overlay. However, it is not as smooth as the gui demo due to data being exchange between the onboard RAM and the swap file on the USB SSD.  You will notices a slight hang when this occurs. This is solely a limitation of the hardware.

To run the demo follow the steps below:

In the Terminal, with the Code directory selected, use the following code to run the Normal Predictions Demo:

    sudo python3 Predictions_Test.py -d
***Note*** : the -d argument will show the broadcasted image on the left side and the corrected image on the right

When the code starts you will get a file selection box like shown below. Here you can select the footage that you want the demo to run on:

![enter image description here](https://lh3.googleusercontent.com/vA-dzJuEdoOaWv4N2Iuqm1yEjBXtXTd_KizNPFsmy-AGpjaLhLIMaWroi2LcwK-RkObMKcLNBGpLFtg1cKFsh51eszQbGtJr1B3Ndj0vo956EwNaNf1OF-2OEmldXTt2t_SZvuTfsHkcdtYIBj3fAvshKVfQxUAVgZ_j2aiSEIt_YmxioXxVxu-VnY7lQ8_oiZuDeJ29cohrXRqUzRaY4N552PGTpXuweXuS8NyBoWhTa0t6gtbGxF0ZLCkm76FQMZ8ItgB1JCaV8IxbQlbIO2rMUjA03avXHBwC87niQVugzoyaaMM_UFgUyiD20Gj8X56WW88zhWY52b-r1_6pfYbDZnsf6t61cuZhTLK96gQM-z-fQTLo_FqFMImzTExJhx1nRUB53pz_k9ztlQN2rSZyorr5MHYv9mMa9v3WOJevmBLqVahZEdFUnzZYTrbPnaRQge5b29l6Ryp_1X1GbZJuCURcHjF4YYG1VJjE8ewdsKjt1_HB674JJTylx8i4NoajyoLTQc0tVT7HGYsheaFMZOihUw9k-dYGOH4UQ_HzJIqB7JGSJ4ouLsAhIBDgyQfWUJCR8f1jFpdpxqkT0y1bLqWsuftKZ1oKJtHdOSESk2GUlmwxdbcX429Hw4Z6_54Y-Uq7OCsLMnGdJTXMP0hBwfYp-Bs=w478-h220-no)


Once you have selected the footage, OpenCV will run a test capture to and output the resolution into the Terminal like shown below:

![enter image description here](https://lh3.googleusercontent.com/J8qlK0OIOSLb6PMq2_l80ULd-0H6TGBbdUzqNOwsmn02XplqOLNnzNAL8k75yZo9iRjJqMT8-eBLRP1jmg9iB9s78QGZYzDCqScYsDl3A8wvHWbx0aP6XxQONc1gwM7s1pPWpMtjHUBc3RBr3E-skndaSrmqfkMzfBV3jtCVqUjurwLnUUCEZbEbZ7wIc8hvHSsRmXZyAb03ePTWFe6SWgZDKVNJTOXzKQEf8MIgix1v2Hb3qgrK1iq7xfip1ljht_3ZLarLsi7BngQkDFcNu0m53X1AwrXrtOwx5eg5_aVbsKlXmrpPXP6CweQFwn-NoNgE0_QTuXo6j8lZaxoCUk0MHyDzdyvxXwmImd7aFWEmEOcml8cDXh-XHY_MDBmfuoEcHM0jCFftd7U68HC7TaabcqjulDJKriyK9djG1rAprSocuAZ27KJwviPT0dQGY3kMgLTYDnqYBoMqc7gSY3zaw5qgpkjgdbZGRupn9JKAQWG1OFDoRmQsPQ7W3kXX3qMhzQGhRZXI5O4uHD2TRU8emQADmGEjArr3pCE4hAaoujUo0_DnmTe7eP5WAD7HJ5Es3Aj70Jr5BNdlMVhB34KiRnQv_A3VYntiogb3funA76ZjlyzKjNt18G4Qu5-O9M-Y_inm9R87caG3TTYINfrmtNGLohU=w1826-h142-no)


***Note***: If the resolution outputed by the Terminal is not correct, press **Ctrl + C** until the demo has stopped and try again

The model will then be loaded on to the GPU and inference will begin. This may take 15-30 seconds to start. If you see an error such as:

    Failed to load module "canberra-gtk-module"
Do not panic, this is a bug with one of the python libraries we are using. This does not effect the demo.

When the demo starts you will now see the footage you selected earlier with its original and corrected frames side by side with the FPS located in the top right corner.

### GUI Demo with Sliders

The GUI demo was built for the purpose of showing real time adjustment to the footage. One of the parameters that effect the addition of the layer mask to the original image is the ***Intensity Adjustment Knob*** which will multiply the addition of the image output has shown. While we normally have it as a command line argument and it being a *set it once and forget about it* parameter, with the live GUI this adjustment can be changed with a slider. An added benefit is also being able to move around the Broadcasted vs. Corrected line while inference is running which adds another wow effect.

This demo will perform slightly worse than the Normal Predictions demo. This is because the GUI elements are being rendered on screen. Again, easy problem to solve with more computational horsepower. Even though the performance is worse, the overall playback of the video is smoother. This is because the time wasted to rendering the GUI elements gives time for memory to be shuffled between the onboard RAM and the swapfile on the Nano. 

To run the GUI demo follow the steps below:

In the Terminal, with the Code directory selected, use the following code to run the Normal Predictions Demo:

    sudo python3 Predictions_Test_gui.py -d
***Note*** : the -d argument will show the broadcasted image on the left side and the corrected image on the right.

When the code starts you will get a file selection box like shown below. Here you can select the footage that you want the demo to run on:

![enter image description here](https://lh3.googleusercontent.com/vA-dzJuEdoOaWv4N2Iuqm1yEjBXtXTd_KizNPFsmy-AGpjaLhLIMaWroi2LcwK-RkObMKcLNBGpLFtg1cKFsh51eszQbGtJr1B3Ndj0vo956EwNaNf1OF-2OEmldXTt2t_SZvuTfsHkcdtYIBj3fAvshKVfQxUAVgZ_j2aiSEIt_YmxioXxVxu-VnY7lQ8_oiZuDeJ29cohrXRqUzRaY4N552PGTpXuweXuS8NyBoWhTa0t6gtbGxF0ZLCkm76FQMZ8ItgB1JCaV8IxbQlbIO2rMUjA03avXHBwC87niQVugzoyaaMM_UFgUyiD20Gj8X56WW88zhWY52b-r1_6pfYbDZnsf6t61cuZhTLK96gQM-z-fQTLo_FqFMImzTExJhx1nRUB53pz_k9ztlQN2rSZyorr5MHYv9mMa9v3WOJevmBLqVahZEdFUnzZYTrbPnaRQge5b29l6Ryp_1X1GbZJuCURcHjF4YYG1VJjE8ewdsKjt1_HB674JJTylx8i4NoajyoLTQc0tVT7HGYsheaFMZOihUw9k-dYGOH4UQ_HzJIqB7JGSJ4ouLsAhIBDgyQfWUJCR8f1jFpdpxqkT0y1bLqWsuftKZ1oKJtHdOSESk2GUlmwxdbcX429Hw4Z6_54Y-Uq7OCsLMnGdJTXMP0hBwfYp-Bs=w478-h220-no)

Once you have selected the footage, OpenCV will run a test capture to and output the resolution into the Terminal like shown below:

![enter image description here](https://lh3.googleusercontent.com/J8qlK0OIOSLb6PMq2_l80ULd-0H6TGBbdUzqNOwsmn02XplqOLNnzNAL8k75yZo9iRjJqMT8-eBLRP1jmg9iB9s78QGZYzDCqScYsDl3A8wvHWbx0aP6XxQONc1gwM7s1pPWpMtjHUBc3RBr3E-skndaSrmqfkMzfBV3jtCVqUjurwLnUUCEZbEbZ7wIc8hvHSsRmXZyAb03ePTWFe6SWgZDKVNJTOXzKQEf8MIgix1v2Hb3qgrK1iq7xfip1ljht_3ZLarLsi7BngQkDFcNu0m53X1AwrXrtOwx5eg5_aVbsKlXmrpPXP6CweQFwn-NoNgE0_QTuXo6j8lZaxoCUk0MHyDzdyvxXwmImd7aFWEmEOcml8cDXh-XHY_MDBmfuoEcHM0jCFftd7U68HC7TaabcqjulDJKriyK9djG1rAprSocuAZ27KJwviPT0dQGY3kMgLTYDnqYBoMqc7gSY3zaw5qgpkjgdbZGRupn9JKAQWG1OFDoRmQsPQ7W3kXX3qMhzQGhRZXI5O4uHD2TRU8emQADmGEjArr3pCE4hAaoujUo0_DnmTe7eP5WAD7HJ5Es3Aj70Jr5BNdlMVhB34KiRnQv_A3VYntiogb3funA76ZjlyzKjNt18G4Qu5-O9M-Y_inm9R87caG3TTYINfrmtNGLohU=w1826-h142-no)


***Note***: If the resolution outputed by the Terminal is not correct, press **Ctrl + C** until the demo has stopped and try again

The model will then be loaded on to the GPU and inference will begin. This may take 15-30 seconds to start. If you see an error such as:

    Failed to load module "canberra-gtk-module"
Do not panic, this is a bug with one of the python libraries we are using. This does not effect the demo.

An OpenCV window should appear and look like the following:

![enter image description here](https://lh3.googleusercontent.com/EqtT3fZFt6SzLy-KXcukozXzAqxlXxGG2QXAGT6aRhMtwHK8RL_2CUeG6IiRJpIVfyCS3dCnTvKYqOvA0B45w-4OU99BaecUMRHuqkxdpAP6mNtKb01mqgsbrHVhIvV4FS8naGxxaDCMjksiaX7npfTY57ttwWxkLn08_VlvSQKRK129rN2HYCRGi8b9NPXYlIMqaCQtRaeCFM9MdHFMHDF50ERw3ZBBeAfh15PaJkMRDcxJ1KtdxJT4NVkX7MT18J_1TiCKPFZtcIfj8CnHvGpZXE9WegTzRJfjpL6yiipJgZgR35uxed6vPjAITfyqUW8AVChzrKfd8vbRLXNA164zmoKEKsj8akjC8vsLqDHFb3Da88SnIVLdhuE6-9BzPQLwgQwONAKtYc2uoCxKnXs-mIgbUHPQMD_da3uB6LX4dNqZWUUeyGOLgFWj-fgpPwYMx0yqqG5jZWzSj0ZecO9Q7D8lMlr-YPuLndTDh50q3bS1f0sAcb0EM-Qt2ikHTCn55EOntxWVEVBPsj_s5JQhDsdhP7NtP9sQFt1p2K-IIm_bBFUZbZgDG2mcWsw027xKUyL3kFSMKwWrnifMMVv0-1ccrkQ7ctrS_z-DmXcupY4RlH4MPsbaLaVX1wVT3wz6t47HY9vX9ccQd6Ey4GwXvDzbqzY=w1272-h772-no)

As shown above the GUI interface contains two sliders: **Intensity** and **Demoslider**. The default value for the **Intensity** slider if 43 (which represents an intensity multiplication of .43). This value, however, we have subjectively chosen and may need changing from scene to scene. The **Demoslider** will change the position of the line that separates the Broadcasted from the Corrected outputs.

This demo has a ***scalable window*** which allows you to resize the demo window to desired size. This will take a hit on performance by 1-4fps.

### Webcam Demo

The Webcam Demo is a great way to concretely show that the color correction is in fact happening in real time. However it has a few downsides as of August 13, 2019. The first is that the white balance for the webcam can not be locked, the webcam will change it depending on the scene. This is a limitation of the camera and OpenCV. The second is variability. Currently, the device might change usb ids on the Nano which means you must go in and change parameters in the code for OpenCV to recognize the camera. I plan to fix this is future releases if we get a more usable webcam.

To run the Webcam Demo, follow these steps:

In the Terminal, with the Code directory selected, use the following code to run the Normal Predictions Demo:

    sudo python3 Predictions_Test_webcam.py -d
***Note*** : the -d argument will show the broadcasted image on the left side and the corrected image on the right. Here you can also input the --intensity argument if need be.

An OpenCV window should appear in 15-30 seconds with the Broadcasted vs Corrected Shown. 

***Note***: There will be a noticeable latency in the footage. This is because we are building a inference data stream by threading the input of the frames. This will also cause the frame rate on screen to exceed 30 fps sometimes. 

To exit the demo, press **Ctrl + C** at any time. 

Last updated: August 15, 2019

Author: John Paul Lineberger (jplineb@clemson.edu)
