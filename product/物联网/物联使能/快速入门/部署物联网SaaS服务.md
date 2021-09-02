为了更好地介绍腾讯云物联使能的功能，本示例构建了一个简单的 Demo，并通过两个阶段分别展示如何利用 Demo 构建物联网 SaaS 。

- 阶段一：通过物联使能的 Demo 快速部署 SaaS。
- 阶段二：结合 SaaS 与数据同步功能，实现设备状态的实时同步与展示。

## 阶段一：部署 SaaS

### 步骤一：新建 SaaS 

1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer) ，选择**公共实例**或您购买的**标准企业实例**。
2. 单击**项目 ID**进入项目详情页面，单击**物联使能** > **SaaS 服务**进入 SaaS 列表页面。
3. 单击**新建 SaaS**，在弹出的配置框中，填写相应信息。

<img src="https://main.qcloudimg.com/raw/723b6e44a63762ca4accbbc6a0a539ce.png" alt="" style=" zoom: 80%;" />

### 步骤二：创建 SaaS 托管环境

1. 完成上述步骤后，选择对应 SaaS 进入 SaaS 详情页面，单击侧边栏的**自研节点**进入自研节点页面。
<img src="https://main.qcloudimg.com/raw/83f8cb327a61fab7a6a3ad093d8f9ef7.png" alt="" style="zoom: 70%" />
2. 单击**立即创建**，进入创建环境页面，输入任意环境名称并单击**保存**。创建环境的过程需要等待数秒。
<img src="https://main.qcloudimg.com/raw/e5f45b0ade325b2e7567490d1abaa39c.png" alt="" style="zoom: 80%;" />

### 步骤三：创建 SaaS 托管自研节点

1. 完成上述步骤后，在自研节点页面即可继续新建服务。单击**新建服务**，在弹出的配置框中，填写相应信息。
   - **服务名称**：填写“helloiot”。
   - **备注信息**：不填。
   - **云托管网络**：选择**系统创建**。
   - **镜像仓库**：选择**使用系统默认仓库**。

<img src="https://main.qcloudimg.com/raw/addea7e61bd1e153076086a8ae4ebd1d.png" alt="" style="zoom: 80%;" />

2. 单击**保存**，服务即可创建成功，创建成功的服务默认显示在服务列表中。

### 步骤四：部署版本

1. 完成上述步骤后，在自研节点页面单击对应服务名称进入服务详情页面。
2. 单击**新建版本**，在弹出的版本配置页面中，需要配置如下内容：
   - **镜像来源**：选择**Demo**。
   - **镜像名称**：选择**iot-enable/iot_postdata**。
   - **服务端口**：填写“80”。
   - **流量策略**：选择**部署完成后自动开启100%流量**。

<img src="https://main.qcloudimg.com/raw/49fb36c111dae7beaa32c2f852c799b7.png" alt="" style="zoom: 80%;" />

>?本 Demo 镜像为基于 php 官方镜像所构建的 php 服务镜像，其默认开放了 80 端口，并在 /var/www/html/ 目录下存放了 index.php 与 post.php 两个代码文件。其中 index.php 用于提供前端显示页面，同时读取并输出 txt 文件中所记录的物联网设备状态；post.php 用于获取 post 请求并将其保存在 txt 文件中。


3. 单击**下一步**进入托管配置页面，本示例对资源要求不高，因此可选择最小资源规格“0.25核/0.5G”。同时副本模式可选择“低成本”，当连续半小时无流量时自研节点将自动缩容实例数量至0，避免额外成本。
   <img src="https://main.qcloudimg.com/raw/f14d913f9646b8acbb921b75f29ce4ae.png" alt="" style="zoom: 80%;" />
4. 单击**开始部署**，若部署成功则状态变为“正常”。
   <img src="https://main.qcloudimg.com/raw/7e95460c23c1d3f4b1cdce449b49449b.png" alt="" style="" />

### 步骤五：访问服务

1. 完成上述步骤后，单击**服务配置**进入服务配置页面，单击**公网访问地址**的跳转链接，即可访问 SaaS 的前端页面。
<img src="https://main.qcloudimg.com/raw/f7865597c0d8f5002520248b369cec52.png" alt="" style="" />
2. 本阶段成功部署了一个简单的前端服务，当然 Demo 的功能不局限于此，接下来还可以通过阶段二结合 SaaS 与数据同步功能，实现设备状态的实时同步与展示。

## 阶段二：实现物联网设备数据同步

本阶段的运作流程如下图所示。当设备状态更新时，将上报状态数据至物联网开发平台，再通过物联网开发平台的数据同步功能，将数据实时 POST 到您的 SaaS 中；同时 SaaS 提供前端页面以查看对应数据。
<img src="https://main.qcloudimg.com/raw/21939480ec2934fac372dc9603edf263.png" alt="" style="" />

### 步骤一：创建物联网开发平台产品

为实现设备状态同步，需要提前使用物联网开发平台创建产品。创建步骤请参见 [产品开发文档](https://cloud.tencent.com/document/product/1081/34738) 。

### 步骤二：设置数据同步

1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer) ，进入项目详情页面，单击左侧菜单的**数据同步**进入数据同步页面。
2. 在数据同步页面中，数据同步在未设置时，默认生效状态都为关闭，HTTP 服务地址为空。
   <img src="https://main.qcloudimg.com/raw/ccefb4e1667484c8362108c87f7c2206.png" alt="" style="" />
3. 选择需要设置数据同步的产品，单击设备列表中的**设置**，即可设置该产品需要同步的消息类型及 HTTP 服务 URL。其中URL需要输入上一步骤得到的默认公网访问地址+“post.php”，例如`https://***.ap-guangzhou.service.tcloudbase.com/post.php。`
   <img src="https://main.qcloudimg.com/raw/fd5d3496f2ecd2c2db191c5383e76baf.png" alt="" style="zoom: 80%;" />
4. 单击**保存**，跳转到列表页，可开启该产品的**生效状态**，完成该产品的数据同步配置。

本示例使用的是 [数据同步](https://cloud.tencent.com/document/product/1081/40298) 功能，若需要更精细化的数据规则定义，可通过 [数据开发](https://cloud.tencent.com/document/product/1081/40292) 配置数据流规则，并通过自定义推送模块推送至 HTTP 服务 URL。

### 步骤三：上报设备状态数据

若在物联网开发平台的产品开发的过程中已经绑定实物设备，可直接通过控制设备实现设备状态上报。

若暂无实物设备，可通过 [虚拟设备调试](https://cloud.tencent.com/document/product/1081/34741) 功能完成设备数据上报。

1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer) ，单击项目进入项目详情页面，单击**产品开发** > 选择相应产品 > **设备调试** > **虚拟设备调试**进入虚拟设备调试页面。
2. 于虚拟设备操控面板设置相应参数，单击**上报**实现设备状态数据上报。
   <img src="https://main.qcloudimg.com/raw/5dc04f19b2f5b17a23d70a0a76b68004.png" alt=""  />

### 步骤四：访问服务

再次访问上一阶段创建的 SaaS，即可查看来自物联网开发平台所同步的设备状态数据。
<img src="https://main.qcloudimg.com/raw/9e3dabf221344c2c1d70f6d01f946871.jpg" alt=""  />
<img src="https://main.qcloudimg.com/raw/ef7b56d332721f796dba3071bc3ce306.png" alt=""  />

## 更多拓展

您可以基于本示例扩展更多物联网应用功能，如对设备的状态数据进行分析，实现状态预警功能；或将设备状态数据进行预处理，并保存至数据库中。
