When using a GPU computing instance, if you use nvidia-smi to view the GPU status in system, the GPU usage may be displayed as 100% even there is no running application using GPU. This may be caused by the ECC Memory Scrubbing mechanism used when the instance loads NVIDIA drivers.
**Solution:**
Execute the following command in the instance system to make the GPU driver go into persistence mode.
```
nvidia-smi -pm 1
```
![](//mc.qcloudimg.com/static/img/456d59df82aa68c243b6073bfe63f490/image.png)


The GPU usage is displayed as 100% abnormally when nvidia-smi is executed:
![](//mc.qcloudimg.com/static/img/5a58bc996b38c28b94131105a3fbd000/image.png)
The GPU usage is displayed normally after the problem is fixed:
![](//mc.qcloudimg.com/static/img/460c515a0a7ac32b4c525b759e13c732/image.png)
