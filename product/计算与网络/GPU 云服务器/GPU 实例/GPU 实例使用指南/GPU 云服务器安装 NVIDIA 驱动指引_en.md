
GCC instances must have corresponding NVIDIA drivers installed. You must compile the installed NVIDIA driver for your CVM.

## Installing NVIDIA Driver on Linux GCC Instance
1. To install NVIDIA driver on Linux instance, first download the NVIDIA driver from 8http://www.nvidia.com/Download/Find.aspx8. Suppose we use M40, we choose the following driver.
![](//mc.qcloudimg.com/static/img/772ea4a736d7a9b00c77f15f08beb2eb/image.jpg)

2. For the downloaded driver file (for example `NVIDIA-Linux-x86_64-352.99.run`), add execution permission
 ` chmod +x NVIDIA-Linux-x86_64-352.99.run`

3. Install the corresponding gcc and kernel-devel packages for the current system.
  `sudo yum install -y gcc kernel-devel-xxx`
  `xxx ` is the kernel version number, which can be viewed by using `uname -r`.

4. Execute the driver installation program using `sudo /bin/bash ./NVIDIA-Linux-x86_64-352.99.ru`, and proceed according to instructions.

5. Once the installation is finished, run `nvidia-smi`. The driver installation is successful if you see GPU information displayed (similar to what is shown below).
![](//mc.qcloudimg.com/static/img/1c82b06999b15cc414a383d61961e528/image.jpg)


## Installing NVIDIA Driver on Windows GCC Instance
1. To install NVIDIA driver on Windows instance, use the remote desktop to log in to your Windows instance as administrator. Download NVIDIA driver from *http://www.nvidia.com/Download/Find.aspx*. Suppose we use M40, we choose the following driver.
![](//mc.qcloudimg.com/static/img/c3925ced580cc85a74b7e636b726fa17/image.jpg)
2. Open the folder where the downloaded driver is located and double click the installation file to launch the installation program. Install the driver according to instructions and restart your instance when required. Check the Device Manager to verify whether the GPU is functioning normally.







