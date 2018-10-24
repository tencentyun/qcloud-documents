为方便用户使用，云市场提供了预装GPU驱动的镜像，在创建GPU实例时可以通过镜像市场选择相关镜像来完成部署。 

## 如何选择安装驱动预装镜像
1. 在购买页选择所需要的GPU实例后，点击一下步**选择镜像**
![](https://main.qcloudimg.com/raw/691f53446f1f8b3e21649e8e2e13626b.png)

2. 选择**镜像市场**，然后点击**从镜像市场选择**
	![](	https://main.qcloudimg.com/raw/aaa7cd8bfc4ab0411199449b96b1238f.png)

3. 出现镜像浏览页面后，在搜索框里输入**GPU**点击搜索按钮，将列出所有预装GPU驱动的镜像
![](https://main.qcloudimg.com/raw/dbd2e90bc3737f5865bfed4df9a5be39.png)

4. 确认镜像版本和预装驱动信息后，点击**免费使用**，成功选择镜像后继续后续实例创建配置流程
![](https://main.qcloudimg.com/raw/00ce30ec22c0354188fd2b63fd7e5faa.png)


## AMD GPU驱动预装镜像

1. [Windows AMD GPU镜像](http://market.qcloud.com/detail.php?productId=3204)

该镜像为渲染型GPU实例GA2专用，预装了AMD FirePro™ S7150驱动程序。

## NVIDIA GPU驱动预装镜像
1. [CentOS 7.2 NVIDIA GPU基础镜像（预装驱动和CUDA 8.0）](http://market.qcloud.com/detail.php?productId=6637)
2. [CentOS 7.2 NVIDIA GPU基础镜像（预装驱动和CUDA 9.0）](http://market.qcloud.com/detail.php?productId=6630)
3. [CentOS 7.3 NVIDIA GPU基础镜像（预装驱动和CUDA 8.0）](http://market.qcloud.com/detail.php?productId=6638)
4. [CentOS 7.3 NVIDIA GPU基础镜像（预装驱动和CUDA 9.0）](http://market.qcloud.com/detail.php?productId=6635)
5. [Ubuntu 16.04 NVIDIA GPU基础镜像（预装驱动和CUDA 9.0）](http://market.qcloud.com/detail.php?productId=6639)

以上镜像为计算型GPU实例 GN2/GN6/GN6S/GN8/GN10/GN10S专用**（GN10X暂不支持）**，预装了NVIDIA Tesla GPU驱动程序384.111，以及CUDA 8.0/9.0。

> 预装镜像的驱动和CUDA版本是固定的，选择有限，如需自定义安装驱动和CUDA，请参考[安装 NVIDIA Tesla驱动指引](https://cloud.tencent.com/document/product/560/8048)