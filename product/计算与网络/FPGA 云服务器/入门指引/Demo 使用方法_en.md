## Overview
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This chapter describes the components and usage of Demo for image classification based on FPGA Alexnet model. You can experience it following the descriptions below.

## Demo Directory Organization
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The Demo of How to Get Started with FCC Instance is under the `/data/fpga_classify_demo` directory

- bin
- build
- src
- include
- lib
	- caffe
	- fpga_classify
- test
 - script

> Note: FPGA API for Alexnet image classification is under the `lib/fpga_classify` Demo directory
	
	
## Image Directory
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How to Get Started with FCC Instance saves 10,764 test images under the `/data/images` directory.

## Model Directory
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How to Get Started with FCC Instance saves the Alexnet network structure, model parameter files, image mean files and label files used in the ImageNet LSVRC-2012 under the `/data/models` directory.


## Instructions
1.	Go to the `build` directory and run `./build`;
2.	Go to the `test/script` directory and run `./test_demo.sh`;
3. Results are saved in the file `fpga_res.txt` under the current directory. The file saves classification results of all images under the `/data/images` directory. Alexnet model results can be classified into thousands of categories. This chapter displays only the first 3 categories with the highest probability.

	The following 2 rows are selected from the classification results:
	
```
n03978966_12321 : ["n03595614 jersey, T-shirt, tee shirt", 0.9920]	["n04370456 sweatshirt", 0.0047]	["n04532106 vestment", 0.0026]
n04127633_18545 : ["n04252225 snowplow, snowplough", 0.1553]	["n03384352 forklift", 0.1499]	["n03649909 lawn mower, mower", 0.0640]
```

**The results indicate that:**
The FCC instance is classified by Alexnet model,
For image **n03978966_12321**, the probability of belonging to the category label **jersey, T-shirt, tee shirt**, **sweatshirt** and **vestment** is 99.20%, 0.47% and 0.26% respectively.
For image **n04127633_18545**, the probability of belonging to the category label **snowplow, snowplough**, **forklift** and **lawn mower, mower** is 15.53%, 14.99% and 0.64% respectively.


> **Result description:**
 1. The first column shows the image name;
 2. Each of other columns is separated by brackets to indicate the label and the score of the label got by image classification. The score indicates the probability that the image belongs to this label in the range of [0.0,1.0]. 0.0 means completely impossible, and 1.0 means 100%;
 3. The total score of all labels is 1.0;
 4. Category labels are sorted in descending order by scores.



