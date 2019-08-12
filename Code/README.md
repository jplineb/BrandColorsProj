
# Using the color corrector code

## Sections

 1. Jetson Nano Startup
 2. Navigating to the file location
 3. Running different demos
	 * Normal Predictions Demo (Best FPS)
	 * GUI Demo with sliders
	 * Webcam Demo


## Jetson Nano Startup
The Jetson Nano has a few external peripherials that you must check before turning it on: 
+ The prototype's external 500GB Samsung SSD that *has* to be plugged into a USB port. This external drive is for the Nano's swap file.
+ The logitech wireless dongle for the wireless keyboard
+ An external display. There are two ports for this, you can either use an HDMI cable or Display Port
+ A Webcam if necessary
+  The 20A power supply so that the Nano can receive power

To power on the Nano just plug in the powersupply to an wall outlet and it will start up. The start up processes should take from 15-20 seconds and an Nvidia logo will appear as a splashscreen during such.

Once the Nano is running, a desktop will be shown like below:

![Jetson Nano Desktop](https://lh3.googleusercontent.com/yEbF0mZLuDTrbvdGYgd3xmF2AjGdp4KTSEwSWvXN_I19uiHIr3Q34v7Xn5RsWh1yiYefUU_IbCLf-AWxfN1TZT8ioR_wkcuLooZAlJ2b7iP_RKFpbcKlJ8wYOn9k34UacSZXbs_BFL6RjQSeO1UBZxtxQfg9milGf4iR0jK-Kou_0DLR7ltmsf_u4hUdk4lZSzDUUJKD3tvWR4FOHz0ghyBGJWC68xihuDafy2JtuelqUT2CdqK7bzfFZKWrX5DyRqa8T9BZ95zA1aiSe2qqHQvAsiTeX7z6hLd3wPWdOW-PBJ9KkY6uuZ6-d1BfdM2GU8MS1c9_jwSUfY-F0PII3M0q5c_5jDZliMn4sgnkbAdE_HMMGVC4ZPbiXAtFGKWoNZF5UjZ7bthSSO_k3zYT6mcIlMIkafDbEsMAntHBRx4kdXbfSWwwdKSk2ZO4IRWXQthyxf6bKP2Jfp-p4G99OR8Sib31_n1W3XCkFC9aN_ci7re0vfPE3qoszJQ6581x7UsZa7nyi689e1XIvyWemQRA7yAEdcYaWiDx9Ssv9rLYErR_y5r07afCwkqnJwVrcZ7p-lW3HnnNNhS-9xVGp2HrwSXNLwEbldUVdMUtXfroWgx9pr0cFxrb2Aui1sa5y6_CFKHIlnJPmHMLabnhg-PzhKsByYU=w2838-h1598-no)

From this, we can accesses the basic computer necessities. 

In the case of where the desktop icons are too small, select the **gear icon** in the top right of the screen and select **system settings**. The window shown below should appear:

![enter image description here](https://lh3.googleusercontent.com/TPAOPD9-yZ-60MEYPLvQnW5_HBA7SQT8bsiGnpnWGS1whFA1PlzWE8fSHl3e8v_KuKQf9mVoefElnO5k-d1XrCZf5GmcRwREUEXKYW4mdTbtpXSAdPFqM5ys4aYFCcQt3XD92AB4KIvu24lYoi4XBgRr-gwrYt15fYqjqUiGJQ1OMOusUrzOqpIaHEAnM5jT4AaK2XPTHQ6buQVc_JebKAf06P2OI0oBuErzP_Pa49nxoLy-eP1dnG4gbYTa6cGEQ2HuiANunHIXD_UDD62K501I83kItP_lUaE_IgwnoCKj-14yJw8-jV9U6HSYAbY7Xj2KrLDG_UTgcg69NZDutF1knKPNLOHZ-1yKsjcnub-GTMomVW89ox2gSjO_BGp1J91RCDTB8ml_lOW2VtBPKQwX9KOBM5D02zSoj8tAJHt20VuyV3H1MII1zvYp0PBwUICQ-kfWA158FFYDvcDsl_i15_XRPCTPvewyz64LpDEfX_Jw6PEmEWri_GS94fIne02vRDD_JQi2CwcvW6KoPRosGqpnURo1OmjEAoOtsfwqI3quUBkYJIE83qgkxhX-bdOhWudIZns9LkJj6Px-bfL0tenUPhi0HWxEdNx0juLpQcDkJiLHkObqX1RxAx_jdvJcb6rzJBgh-s3jXrWF-5JeWvONpNs=w1688-h1168-no)

From here select **Displays** under the Hardware section and change the **Scale for menu and title bars** slider until satisfied and click **apply**

![enter image description here](https://lh3.googleusercontent.com/H2MvPaSh0-P55H9TeRjQOrc1L52jUIG778sobLRKcyPqgaAhwTTlBeDds9p0Cx4qGFVa_n4NqqnPlEwHQ_Ir5FFcBORak9qV5u8dilaXwojwD5H5GSVLEACcyPDZwaojC2x5M4ck0lV9e1kDmDq_ewUEnjpsmNznQz4FsoAVEdTGtwAI5KDplulzK8T69KDgaW9HuAzj4FyJUHQNaG3R90TOakDRrABgtcOstr67ab4T9aUSY6VGwdKxJf-4ReDHNJB1EmMNNfhZXzvqlDxIKmoZ-uI08yRrsaPBTdRe9ym0dfcsWYFJHNpc0vpub1lBDtSUrjkcThdBSGAltmX-IG_z06olJneW4vsGWJoYbPs5-RQnrMvWPmJ3xlXoYzMxjlDJa1ySJC1Tyj1tYaz60fKDxE_YTEbS74seQDVIeVlJA5Pa3WQ56Ut7n6Yx-0fAkMfpSrV9s3B7SgFAo-7kBIOVdJ18rYDSRWc4WdUQF_n7u_JJ9CtjR5drusjTdDVBL6lkLq-t2CbNj6D7FE-zLCKDIpN9b0V_X6Sdyl7YfmSgcZgH1wwpI-1IRXbqMnPTaLr3eMFtZfIS3s-PNIFm8pNjIDS2ZgxLPmkDH_bmmzzUDm4lRG5BOmX_ibh2szC58Sbx9ESyUnvLPeRx_f3qQgZGKV0Luj4=w1696-h1146-no)

If for some reason you need to connect to Wifi while using the Nano, click the **Wifi signal symbol** in the top right and change the appropriate settings.

Another *Mandatory* step we must take is to put the Nano in its maximum usage mode. Normally when you start up the Nano, it is in an eco-power state that change the the clock frequency of the processor depending on the load of the system. The current version of JETPack tends to be hyperactive in changing the clock speed. For this project we want to make sure that the Nano is at maximum usability at all times.

To put the processor at its maximum clock speed, either search for the terminal window shortcut by pressing the **Windows Key** on the logitech keyboard or select the **Terminal Shortcut** on the **Task Bar** like shown below:

![enter image description here](https://lh3.googleusercontent.com/hyTA2sUXcLDzfFHZ1gtzREG1LBHi4cpP3gl0CTSwPk6dF0muY5hs4nSw1KaMYL2yWM83DPTLkqwxJpsTDM84SSOSjRSmZWP49dah8IFbgF4dTqckuo-kN4-LRHYNAGzhqB5gebQ7AXKeQqqEOY4iv-rdmCuJPmOP4bVLof7M_KqKwkQnUbaSn4MOhK7pO-sHAZDAgyQwdRj2mNpuZbolxCnlZ5iYmJ89G2i7net2xhdOFDOoiOxkzaCfWRfG5f-cXri-Vpzt2eI380gkJaRR-tCyB8shFIj7PKcKhsXJLLjEo1UtjgV9zQonnVgLEbkAsWQXlXnI7r2E9jV1TyBN-Bvu4JPFTbE8rVBVrwwKUxryOdnlL9mP38YZCeCzn5WQogEbmywoWXaYG8Lk-DaSDOCQbv0yegmVo5A2Gk-vnKWNiE3YHiD-Ygmx2IMD86xeGFsXc6Gd9pjbAMFOTv0oBwQQcXvobCN9_hI2omuzvwPj80M5-ZMr9Y5ua9c23Mq1NlJ5gRPMdzcI1kHcpRaUcL3GlkoYhWiZTDJFeKJTykBie-ZXWzLBNzx1OTQSf1Hpo5JeyyFnhqiEwXNyU6WZM0R-UgKVfx3PeEKWumBKcRWPGbuLqQ-w5iWFyC0Vg321HQdwxp6fjFNfhezoVdKY3OV3-8Ae2zQ=w132-h124-no)

With the Terminal open type the following and press **Enter**:

    Sudo jetson_clocks

To verify that the previous command worked, we can use a program called jtop. To access jtop, type the following in the Terminal:

    Sudo jtop
If done correctly the terminal should now look like the image below and if done correctly the frequency readings for each core should be *1.4GHz*

![enter image description here](https://lh3.googleusercontent.com/RK13oWmw0EqDwwnYWCFRoEjx43Pf7JlYvYR3M-e7hjo1b6AL9KiZ7A5uE7IqhCHH-UPJQtwtRBCjhvp_MlTXNSWr3gM-AVAevYfW2UWFfjW72JmBvQ0ioveWJ94MYNAODgVYOZ7hXQZ9ZBfC7lO9JQ-ycERwZd63R2nFiF274gT-izpLy78G3ETzrfKHic6qzhh2pwlFecWI7BSvBHUlWx03onfRXiWGgmycwt2ob3fph3A8RUsRshYfmGG3lZpfRgSYpCk5Z6ojvrj9m7s-fBCl0psBTMV9Unhxj_L1Hj7fl926d4aXf5nIf-wcgMPf3vnWTdxOD6gSP7QBGGdJGBrGdS_h9HjgHq5BrOUgi69RlbdI2EwmoDodpCEsRDYG4SzquhlbNSCZO76RQdWVii2bboODpy2lAcURtSDjRbfQziR53KWjfIJY9Bw02SgTOA7BM0tIh1PkrX6XTm9WWIydE3H9xzu1pZlAPwZH_f75xa_Sn0Xs2fZWUFlVGIwq_LjWlStyI2YLLwNGoY0-U_d11emso9zBR4rF4tEt2yH8ou28akkdr1cBGxOHQCiYRqI6Pj2AX8z5FYNBlzt0uoiLgSEYbWjESLuhJ-F4GkqIdxNjM2UWqRZAz_Xmp8uL7ZZpdsgQk-NO7xx-S3BVlicuZw7MVU4=w1456-h918-no)

jtop shows us useful information for looking at the performance of the Nano such as memory usage, power consumption, cpu and gpu load. You can choose to leave this open during the demo or close it by pressing **Q** on the keyboard.

The Nano is now ready for whatever you throw at it!

## Navigating to the file location

The resources for this project is located in a folder named **BrandColorsProj** To view this directory with a file explorer, click the **Files** Shortcut located on the taskbar and select the **BrandColorsProj** folder. This folder contains 3 sub folders named:
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
