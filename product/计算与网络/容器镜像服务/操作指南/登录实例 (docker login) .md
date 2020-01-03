
## 操作场景

本文档指导您如何在命令行中使用 docker login 指令登录腾讯云容器镜像服务 (Tencent Container Registry，TCR) 中的实例。

## 前提条件

在登录实例前，您需要完成以下工作：
- 已 [创建实例](https://cloud.tencent.com/document/product/378/17985)，且实例处于 “运行中” 状态。
- 已在访问控制中放通访问客户端所在的网络环境。
- 已在访问客户端上安装 docker。

## 操作步骤

1. 登录 [腾讯云官网控制台](https://console.cloud.tencent.com)，选择【云产品】>【计算】>【[容器镜像服务](https://cloud.tencent.com/product/tcr)】，点击进入容器镜像服务控制台。
   
2. 在控制台左侧菜单栏选择 “实例列表”，进入实例列表管理页面，点击需要登录的实例，进入实例管理页面。

3. 在 “实例详情” 页中获取该实例的 “访问域名“。
![](https://main.qcloudimg.com/raw/80d62d6b76f37cd8e841b5d31b4539b7.png)

4. 在 ”访问凭证“ 页中获取登录该实例的用户名，而后点击 ”重新生成“ 临时密码，在弹窗中点击 ”复制凭证“ 获得该实例的临时登录密码。请注意，该临时密码默认有效期为 24 小时。
![](https://main.qcloudimg.com/raw/241e2a235f975a0e7677742a100e5ddd.png)

5. 在访问客户端的命令行工具中执行以下指令：
    ```
    docker login demo-tcr.tencentcloudcr.com -u [用户名] -p [临时密码]
    ```
    其中，请将 ”demo-tcr.tencentcloudcr.com“ 替换为您希望登录实例的访问域名，用户名，临时密码请填写在访问凭证中获得的有效凭证。
