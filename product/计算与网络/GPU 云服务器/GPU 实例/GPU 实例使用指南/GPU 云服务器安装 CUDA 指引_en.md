
> CUDA(r) (Compute Unified Device Architecture) is a computing platform published by the graphic card vendor NVIDIA. CUDA(tm) is a general parallel computing architecture developed by NVIDIA which allows GPUs to solve complex computing problems. It contains CUDA instruction set architecture (ISA) and parallel computing engine within the GPU. Now, developers can use C, C++, FORTRAN to compose programs for CUDA(tm) architecture. These programs can be run with great performance on processors that support CUDA(tm).

GCC instances use NVIDIA graphic cards and you need to install CUDA development operating environment for them. Here we take the most commonly used CUDA 7.5 as an example. You can install it by following these steps:

## Installing CUDA on Linux GCC Instance
1. To install CUDA on Linux instance, first download the CUDA installation package from *https://developer.nvidia.com/cuda-75-downloads-archive*.
2. Choose Installation Package and Operating System
Suppose we use CentOS 7.2 (64 bit), we choose as follows
![](//mc.qcloudimg.com/static/img/366bbd6ca9af49f77dda91036cf533bc/image.jpg)
>  Note: it is recommended to choose rpm (network) for "Installer Type".
> network: network installation package. The package is small, and you need to download the actual installation package in the CVM via Internet.
> local: local installation package. The package is large because it contains the installation packages for all downloaded installation components.

3. Install
![](//mc.qcloudimg.com/static/img/0dd00b1bbdc9d025109e38825be8ed71/image.jpg)
Install by following the guide above.

4. Verify Installation

- Go to the	` /usr/local/cuda-7.5/samples/1_Utilities/deviceQuery ` directory and execute `make` command to compile the deviceQuery program.
- Execute deviceQuery. The CUDA installation is successful if the following device information is displayed.

![](//mc.qcloudimg.com/static/img/d545951dc869591d83bf23e27831287a/image.jpg)


## Installing CUDA on Windows GCC Instance
1. To install CUDA on Windows instance, use the remote desktop to log in to your Windows instance as an administrator. Download the CUDA installation package from *https://developer.nvidia.com/cuda-75-downloads-archive*.
2. Choose Installation Package and Operating System
Suppose we use Win Server 2012 R2 (64 bit), we choose as follows
![](//mc.qcloudimg.com/static/img/e8e76622c35b0013cf7be9eb4bfed1d8/image.jpg)
![](//mc.qcloudimg.com/static/img/4c4e34608a54cd98b8fc7535548aeea7/image.jpg)
3. Launch the installation program and proceed according to the instructions. Installation is successful when you see the final dialog indicating the end of the process.
![](//mc.qcloudimg.com/static/img/52aef97b2d048f884c467d8446fed003/image.jpg)




