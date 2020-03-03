CUDA (Compute Unified Device Architecture) is a computing platform published by the graphic card vendor NVIDIA. As a generic parallel computing architecture, CUDA(tm) allows GPUs to solve complex computing problems. It contains CUDA instruction set architecture (ISA) and parallel computing engine within the GPU. Now, developers can write programs for CUDA (tm) architecture using C, C++. These programs can be run with great performance on processors that support CUDA(tm).
GCC instances use NVIDIA graphic cards and you need to install CUDA development operating environment for them. As the most frequently used one, CUDA 7.5 can be installed by following the steps below.
## In Linux System
1. Log in to [Download CUDA Driver](https://developer.nvidia.com/cuda-75-downloads-archive) or copy the link https://developer.nvidia.com/cuda-75-downloads-archive.
2. Select the operating system and installation package. Suppose we use CentOS 7.2 (64 bit), we choose as follows:
![](//mc.qcloudimg.com/static/img/a69a79a2d6cbd1f442b58bfb423d8cca/image.jpg)
> **Note:**
> It is recommended to choose rpm (network) for "Installer Type".
> network: Network installation package. The package is small, and you need to download the actual installation package in the CVM via private network.
> local: Local installation package. The package is large because it contains the installation packages for all downloaded installation components.

3. Right click "Download" -> "Copy Link Address".
![](//mc.qcloudimg.com/static/img/3a2552b7e1637055bae0a1391520713b/image.png)
4. Log in to the GCC instance, and paste the link address copied in the previous step to download the installation package by executing `wget` command. Or, you can download the CUDA installation package to a local system, and upload it to the GCC instance server.
![](//mc.qcloudimg.com/static/img/e40ed1109aaed75d51b3781fe0045eb6/image.png)
5. Run the following commands in the directory where the CUDA installation package is located:
`sudo rpm -i cuda-repo-rhel7-7.5-18.x86_64.rpm`
`sudo yum clean all`
`sudo yum install cuda`
6. Go to the	` /usr/local/cuda-7.5/samples/1_Utilities/deviceQuery ` directory and execute `make` command to compile the deviceQuery program.
7. Execute deviceQuery. The CUDA installation is successful if the following device information is displayed.
![](//mc.qcloudimg.com/static/img/d545951dc869591d83bf23e27831287a/image.jpg)

## In Windows System
To install CUDA on Windows instance, use the remote desktop to log in to your Windows instance as admin.
1. Download the CUDA installation package from [CUDA Driver Official Website](https://developer.nvidia.com/cuda-75-downloads-archive).
2. Select the operating system and installation package. Suppose we use Win Server 2012 R2 (64 bit), we choose as follows:
![](//mc.qcloudimg.com/static/img/ecf81426ceb95fd4ed549cf0bc627895/image.jpg)
![](//mc.qcloudimg.com/static/img/525b743130bda690a7223cbd5533ec75/image.jpg)
3. Launch the installation program and proceed according to the instructions. Installation is successful when you see the final dialog indicating the end of the process.
![](//mc.qcloudimg.com/static/img/52aef97b2d048f884c467d8446fed003/image.jpg)




