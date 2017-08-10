## 步骤一：登录弹性 MapReduce 控制台
登录 [弹性 MapReduce](https://emr.qcloud.com) 管理控制台（确保已完成 [准备工作](此处加上链接)） 。
## 步骤二：创建弹性 MapReduce 集群
单击左上角【集群创建】按钮，开始创建集群。
![](//mc.qcloudimg.com/static/img/08af62a08dc8ae8c65bdbdda9ff8430a/image.png)
#### 1. 可用区与软件配置
![](//mc.qcloudimg.com/static/img/a8bd42e25bf768c711f7c2c71144b940/image.png)
* 计费模式：包括包年包月或按量计费 [详细对比](https://www.qcloud.com/document/product/213/2180)
* 地域：包括华南地区、华东地区、华北地区 [了解详情](https://www.qcloud.com/document/product/239/4106)
* 可用区：选择确定地域下的可用区
![](//mc.qcloudimg.com/static/img/e128f53117d52e07260946cf54099e74/image.png)
* 产品版本：目前仅支持 EMR-V1.0.1
* 实例规格：可选择已有的规格，也可自定义配置。
以上信息配置完成后，单击【下一步，硬件配置】按钮，进入硬件配置。
#### 2. 硬件配置
主节点（Master）配置
![](//mc.qcloudimg.com/static/img/8ac5e868e05c761cbee71bf0b7acf0c3/image.png)
核心节点（Core）配置
![](//mc.qcloudimg.com/static/img/95def6d8cf76dd23e3674501a1b77f77/image.png)
计算节点（Task）配置
![](//mc.qcloudimg.com/static/img/88820c2da4c47603aa633c6e5824cf50/image.png)
添加集群点网络
![](//mc.qcloudimg.com/static/img/60fcf4621caccb709d2a6d07822a2114/image.png)
>**注意：**
>如果无可添加网络，您需要去控制台 [新建私有网络](https://www.qcloud.com/document/product/215/8113) 或者 [新建子网](https://www.qcloud.com/document/product/215/8114)
以上信息配置完成后，单击【下一步，基础配置】按钮，进入基础配置配置。
#### 3. 基础配置
![](//mc.qcloudimg.com/static/img/c83c44f139683db1312697a79aea21a7/image.png)

以上信息配置完成后，单击【开通】，完成集群创建。



