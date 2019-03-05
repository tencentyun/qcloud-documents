&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tencent Cloud FCC instance is under internal trial. If you haven't got the purchase permission, click [here](https://cloud.tencent.com/act/apply/fpga) to apply.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If you have got the internal trial qualification of FPGA, you can get started with the FCC instance under the guidance of this chapter.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As the mobile internet industry grows, users are creating a huge collection of pictures based on user social platforms, and the number of pictures is growing rapidly. To enhance the processing capacity of image classification detection and reduce the image detection cost, we use FCC instance to accelerate the computing of Alexnet model of CNN algorithm in deep learning model.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This chapter introduces how to get started with Tencent Cloud FCC instance. It shows the image classification application based on the FCC instance and Alexnet model, a well-known image classification model of the CNN algorithm in deep learning model. This chapter describes the FPGA-based API of the model and details on how to use the API. Users can call the API to implement applications after learning about it.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Alexnet model is a well-known Convolutional Neural Network model. It won the champion of 2012 ImageNet image classification competition. For more information, please see [here](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;During implementation phase, the 5 convolution layers of Alexnet model are accelerated on the FPGA, and the calculation of the 3 fully connected layers remains on the CPU to accommodate different classification models. Therefore, the implementation has a fair degree of flexibility.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;You can also load your Alexnet model to classify images. For more information on restrictions, please see [API Description](https://cloud.tencent.com/document/product/565/8221).
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For more information on how to use the Demo of how to get started with FCC instance, please see [Usage of Demo](https://cloud.tencent.com/document/product/565/8222).
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The Demo of how to get started with FCC instance uses the AlexNet network structure and model parameter files in the 2012 ImageNet competition. For more information on performance test, please see [Performance Test Comparison](https://cloud.tencent.com/document/product/565/8223).







