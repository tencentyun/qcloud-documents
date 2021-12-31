
## 操作场景
如果您不想通过 Git 代码仓库来构建镜像，容器服务 TKE 还提供了一种通过手动上传 Dockerfile 文件来构建镜像的方式。本文介绍如何通过 Dockerfile 文件手动构建容器镜像。

## 前提条件
- 已准备 Dockerfile 文件。
- Dockerfile 文件执行了依赖的基础镜像和依赖的其他资源，这些资源必须能够通过公网访问。


## 操作步骤

### 使用 Dockerfile 文件手动构建容器镜像
1. 登录腾讯云容器服务控制台，选择左侧导航栏中的**镜像仓库** > **[个人版](https://console.cloud.tencent.com/tke2/registry/user/self)**。
2. 单击镜像 ID 并选择**镜像构建**页签，可在页面中查看镜像的构建历史记录。如下图所示：
![](https://main.qcloudimg.com/raw/19b39784e892623146b40137349c7ceb.png)
3. 单击**立即构建**，并在弹出的“立即构建镜像”窗口中选择**使用Dockerfile进行构建**。如下图所示：
![](https://main.qcloudimg.com/raw/793871ac85e6f7298d5115cf5e64e3d4.png)
4. 输入镜像版本以及 Dockerfile 文件后，单击**构建**即可开始构建镜像。



### 查看构建日志
单击构建历史记录所在行的<img src="https://main.qcloudimg.com/raw/80161743b6960d2aab303b4427286b45.png" style="margin:-3px 0px">，可以查看通过 Dockerfile 文件构建镜像记录的日志信息。如下图所示：
![](https://main.qcloudimg.com/raw/00e2ca7f0270337a570744b994bc653c.png)
