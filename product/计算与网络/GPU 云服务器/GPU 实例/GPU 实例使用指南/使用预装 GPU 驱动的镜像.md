## 操作场景
为方便用户使用，云市场提供了预装 GPU 驱动的镜像。在创建 GPU 实例时，可以通过镜像市场选择相关镜像完成部署。 

## 操作步骤

### 如何选择安装驱动预装镜像
1. 在购买页选择所需要的 GPU 实例，单击【下一步：选择镜像】。如下图所示：
![](https://main.qcloudimg.com/raw/e30868df402bd18751e038284f874a7d.png)
2. 选择【镜像市场】，单击【从镜像市场选择】。如下图所示：
![](	https://main.qcloudimg.com/raw/aaa7cd8bfc4ab0411199449b96b1238f.png)
3. 在弹出的 “选择镜像” 对话框的搜索框中，输入 **GPU**，单击搜索按钮。列出所有预装 GPU 驱动的镜像，如下图所示：
![](https://main.qcloudimg.com/raw/408fd024a655714dcd23cc5934c10e54.jpg)
4. 根据实际需求，选择预装 GPU 驱动的镜像，单击【免费使用】。
5. 根据界面提示，完成实例创建的配置。如下图所示：
![](https://main.qcloudimg.com/raw/00ce30ec22c0354188fd2b63fd7e5faa.png)

### NVIDIA GPU 驱动预装镜像
- [CentOS 7.2 NVIDIA GPU 基础镜像（预装驱动和 CUDA 9.2）](http://market.qcloud.com/detail.php?productId=6630&_ga=1.163902902.805765411.1545285819)
- [CentOS 7.5 NVIDIA GPU 基础镜像（预装驱动和 CUDA 9.2）](http://market.qcloud.com/detail.php?productId=6635&_ga=1.93543700.805765411.1545285819)
- [CentOS 7.6 NVIDIA GPU 基础镜像（预装驱动和 CUDA 10）](http://market.qcloud.com/detail.php?productId=6637&_ga=1.93543700.805765411.1545285819)
- [Ubuntu 18.04 NVIDIA GPU 基础镜像（预装驱动和 CUDA 10）](http://market.qcloud.com/detail.php?productId=6639&_ga=1.194663588.805765411.1545285819)

以上镜像为计算型 GPU 实例 GN2/GN6/GN6S/GN8/GN10/GN10S/GN10X 专用，预装了 NVIDIA Tesla GPU 驱动程序418.67，以及 CUDA 9.2/10.0。

>?预装镜像的驱动和 CUDA 版本是固定的，选择有限。如需自定义安装驱动和 CUDA，请参考 [安装 NVIDIA Tesla 驱动](https://cloud.tencent.com/document/product/560/8048)
