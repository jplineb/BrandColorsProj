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


**For more infromation on using the code:**
[Code Documentaiton](/Code/README.md)


## Acknowledgments

-Dr. Dane Smith for supervising the project

-Erica Walker for providing the source material

## Contributers
- Dr. Dane Smith
- Michelle Mayer
- John Paul Lineberger



