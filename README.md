# Local Color Correction using Artificial Intelligence

This repo stores code to take video feed, pass it through a pretrained pytorch model, and output a color correction mask in real time.
Multiple approaches associated with multiple python scripts are provided.

The python code provided has support for x64 and ARM64 based processors

## Prerequisites

Necessary Requirements:
```
A compiled torch model
A compiled ONNX model - only necessary if running TensorRT example
Super User Permissions
A dedicated GPU (Recommended > 4GB of VRAM)
x64 or ARM64 processor
Webcam
```

Libraries and packages you'll need that you probably don't already have installed:

```
OpenCV (with support for cv2)
CUDA v10.0+
Pytorch
line_profiler
numpy
imutils
psutils
easygui
TensorRT - only necessary if running TensorRT example
Pycuda - only necessary if running TensorRT example
```


## Running and Using the code

The code can be broken down into four separate sections with all containing dependencies on the last:
1. Brand_Colors_Predictions - used to take video and color correct it in real time using pytorch
   * Predictions_Test.py
   * Predictions_Test_gui.py
   * Predictions_Test_webcam.py
   
2. Brand_Colors_Predictions_TensorRT - used to take video and color correct it in real time using TensorRT
   * Brand_Colors_Predictions_TensorRT.py

3. Brand_Colors_Predictions_webcam - used to take live webcam feed and color correct it in real time
   * Brand_Colors_Predictions_webcam.py

4. Multithreadimageload - contains the class definitions for the project
   * Multithreadimageload.py

**For more infromation on using the code:**
[Code Documentaiton](/Code/README.md)

### Brand_Colors_Predictions

  
**Outputs:** 

**Error Handling**:

**Notes**: 

### Brand_Colors_Predictions_TensorRT

  
**Outputs:** 

**Error Handling**:

**Notes**: 

### Brand_Colors_Predictions_webcam

  
**Outputs:** 

**Error Handling**:

**Notes**: 

### Multithreadimageload

  
**Outputs:** 

**Error Handling**:

**Notes**: 

## Acknowledgments

-Dr.Hudson for supervising the project

-Erica Walker for providing the source material

## Contributers
- Dr. Dane Smith
- Michelle Mayer
- John Paul Lineberger



