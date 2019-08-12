
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

If for some reason you need to connect to Wifi while using the Nano, click the **Wifi signal symbol** in the top right to adjust to your needs.
