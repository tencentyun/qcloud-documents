## 操作场景
腾讯云容器镜像服务（Tencent Container Registry，TCR）个人版提供基础的云上镜像托管、分发服务，限额使用，仅面向个人使用或企业客户临时测试使用。个人版服务为云上共享服务，即所有个人版用户将共享服务后端及数据存储，且镜像托管及上传下载具有配额限制。容器镜像服务个人版不收取费用，您可前往 [容器服务 - 镜像仓库](https://console.cloud.tencent.com/tke2/registry) 开始使用。

本文介绍如何在物联网边缘计算平台中，使用容器镜像服务 TCR 内托管的私有镜像进行应用部署。
更多关于腾讯云容器镜像服务的介绍请参见 [容器镜像服务](https://cloud.tencent.com/document/product/1141)。

## 前提条件
[初始化 TCR 个人版服务](https://cloud.tencent.com/document/product/1141/63910)。

## 操作步骤

### 步骤1：准备容器镜像

#### 在 TCR 中创建命名空间
1.	已登录 [容器镜像服务](https://console.cloud.tencent.com/tcr)。
2.	选择左侧导航栏中的命名空间，进入“命名空间”列表页面，选择个人版实例，单击新建。
>? 命名空间用于管理实例内的镜像仓库，不直接存储容器镜像，可映射为企业内团队、项目或是其他自定义层级。
>
3.	在弹出的“新建命名空间”窗口中，参考以下提示配置命名空间信息并单击确定。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c479c58ccdd94821a8b164cbc119623c.png)
 -	名称：建议使用企业内团队或项目进行命名，个人版实例为共享实例，命名空间名称全局不可重复，即无法新建其他用户已经占用的命名空间名称。

#### 创建镜像仓库（可选）
>? 您可在完成命名空间创建后，直接通过Docker客户端向该命名空间内推送镜像，对应的镜像仓库将被自动创建。
>
1.	单击左侧导航栏中的镜像仓库，进入“镜像仓库”列表页面，在顶部选择个人版实例。
2.	单击新建并在弹出的“新建镜像仓库”窗口中，配置镜像仓库信息并单击确定。如下图所示：
其中，命名空间可选择已创建的命名空间，名称不支持多级路径，详细描述支持 Markdown 语法。
![](https://qcloudimg.tencent-cloud.cn/raw/21ce279eefcc02b06286e1e59a17607c.png)

#### 推送拉取镜像
通过以上步骤，您已经创建了命名空间及镜像仓库，接下来可通过以下步骤实现向镜像仓库内推送及拉取镜像。
>? 此步骤需要您使用一台安装有Docker的云服务器或物理机。

#### 推送容器镜像
您可在本地构建新的容器镜像或从 DockerHub 上获取一个公开镜像用于测试。
本文以 DockerHub 官方的 Nginx 最新镜像为例，在命令行工具中依次执行以下指令，即可推送该镜像。请将 project-a 及 nginx 依次替换为您实际创建的实例名称、命名空间名称及镜像仓库名。
```
sudo docker tag nginx:latest ccr.ccs.tencentyun.com/project-a/nginx:latest
```
```
sudo docker push ccr.ccs.tencentyun.com/project-a/nginx:latest
```

#### 拉取容器镜像
本文以已成功推送的 Nginx 镜像为例，在命令行中执行以下命令，即可拉取该镜像。
```
sudo docker pull ccr.ccs.tencentyun. com/project-a/nginx:latest
```


### 步骤2：使用 TCR个人版 实例内容器镜像创建工作负载
1. 登录 [边缘计算平台](https://console.cloud.tencent.com/iecp)。单击左侧导航栏中**边缘单元**，进入“边缘单元”页面。
2. 单击需要安装节点的单元**管理**，进入该单元详情页。
3. 选择页面左侧**应用管理** > **工作负载**/**Grid 应用**，进入工作负载/Grid应用列表页面，单击**新建应用**
![](https://qcloudimg.tencent-cloud.cn/raw/709f589e5b53699fcd1ee4bf121431fe.png)

	i.	镜像版本：选择好镜像后，单击选择镜像版本，在弹出的“选择镜像版本”窗口中，根据需要选择该镜像仓库的某个版本。若不选择则默认为 latest。
4. 完成其他参数设置后，单击确认完成工作负载的创建。
