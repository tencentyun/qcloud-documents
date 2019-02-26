## 操作场景

为方便用户使用，云市场提供了预装 GPU 驱动的镜像。在创建 GPU 实例时，可以通过镜像市场选择相关镜像完成部署。 

## 操作步骤

### 如何选择安装驱动预装镜像

1. 在购买页选择所需要的 GPU 实例，单击【下一步：选择镜像】。如下图所示：
![](https://main.qcloudimg.com/raw/691f53446f1f8b3e21649e8e2e13626b.png)

2. 选择【镜像市场】，单击【从镜像市场选择】。如下图所示：
	![](	https://main.qcloudimg.com/raw/aaa7cd8bfc4ab0411199449b96b1238f.png)

3. 在弹出的 “选择镜像” 对话框的搜索框中，输入 **GPU** ，单击搜索按钮。列出所有预装 GPU 驱动的镜像，如下图所示：
![](https://main.qcloudimg.com/raw/dbd2e90bc3737f5865bfed4df9a5be39.png)
4. 根据实际需求，选择预装 GPU 驱动的镜像，单击【免费使用】。
5. 根据界面提示，完成实例创建的配置。如下图所示：
![](https://main.qcloudimg.com/raw/00ce30ec22c0354188fd2b63fd7e5faa.png)

### AMD GPU 驱动预装镜像

[Windows AMD GPU镜像](http://market.qcloud.com/detail.php?productId=3204)
该镜像为渲染型 GPU 实例 GA2 专用，预装了 AMD FirePro™ S7150 驱动程序。

### NVIDIA GPU 驱动预装镜像
- [CentOS 7.2 NVIDIA GPU基础镜像（预装驱动和CUDA 8.0）](http://market.qcloud.com/detail.php?productId=6637)
- [CentOS 7.2 NVIDIA GPU基础镜像（预装驱动和CUDA 9.0）](http://market.qcloud.com/detail.php?productId=6630)
- [CentOS 7.3 NVIDIA GPU基础镜像（预装驱动和CUDA 8.0）](http://market.qcloud.com/detail.php?productId=6638)
- [CentOS 7.3 NVIDIA GPU基础镜像（预装驱动和CUDA 9.0）](http://market.qcloud.com/detail.php?productId=6635)
- [Ubuntu 16.04 NVIDIA GPU基础镜像（预装驱动和CUDA 9.0）](http://market.qcloud.com/detail.php?productId=6639)

以上镜像为计算型 GPU 实例 GN2/GN6/GN6S/GN8/GN10/GN10S专用**（GN10X暂不支持）**，预装了 NVIDIA Tesla GPU 驱动程序 384.111，以及 CUDA 8.0/9.0。

> 预装镜像的驱动和 CUDA 版本是固定的，选择有限，如需自定义安装驱动和CUDA，请参考 [安装 NVIDIA Tesla驱动](https://cloud.tencent.com/document/product/560/8048)
