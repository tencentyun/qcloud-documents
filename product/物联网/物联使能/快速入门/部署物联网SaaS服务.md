## 背景

为了更好地介绍腾讯云物联使能的功能，本示例构建了一个简单的 Demo，并通过两个阶段分别展示如何利用 Demo 构建物联网 SaaS。

- 阶段一：通过物联使能的 Demo 快速部署 SaaS。
- 阶段二：结合 SaaS 与规则引擎功能，实现设备状态的实时转发与展示。

## 阶段一：部署 SaaS

### 步骤一：新建 SaaS 

1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer) ，选择**公共实例**或您购买的**标准企业实例**。
2. 单击**项目 ID** 进入项目详情页面，单击**物联使能** > **SaaS 服务**进入 SaaS 列表页面。
3. 单击**新建 SaaS**，在弹出的配置框中，填写相应信息。<br>
<img src="https://main.qcloudimg.com/raw/723b6e44a63762ca4accbbc6a0a539ce.png" alt="" style=" zoom: 80%;" />

### 步骤二：创建 SaaS 托管环境

1. 完成上述步骤后，选择对应 SaaS 进入 SaaS 详情页面，单击侧边栏的**自研节点**进入自研节点页面。
<img src="https://main.qcloudimg.com/raw/83f8cb327a61fab7a6a3ad093d8f9ef7.png" alt="" style="" />
2. 单击**立即创建**，进入创建环境页面，输入任意环境名称并单击**保存**。创建环境的过程需要等待数秒。
<img src="https://main.qcloudimg.com/raw/e5f45b0ade325b2e7567490d1abaa39c.png" alt="" style="zoom: 80%;" />

### 步骤三：创建 SaaS 托管自研节点

1. 完成上述步骤后，在自研节点页面即可继续新建服务。单击**新建服务**，在弹出的配置框中，填写相应信息。

   - **服务名称**：填写 “helloiot”。
   - **备注信息**：选填。
   - **云托管网络**：选择**系统创建**。
   - **镜像仓库**：选择**使用系统默认仓库**。

   <img src="https://main.qcloudimg.com/raw/addea7e61bd1e153076086a8ae4ebd1d.png" alt="" style="zoom: 80%;" />

2. 单击**保存**，自研节点服务即可创建成功，创建成功的服务默认显示在服务列表中。

### 步骤四：部署版本

1. 完成上述步骤后，在自研节点的服务列表页面单击对应服务名称进入服务详情页面。
2. 单击**新建版本**，在弹出的版本配置页面中，需要配置如下内容：
 - **镜像来源**：选择 **Demo**。
 - **镜像名称**：选择 **iot-enable/iot_postdata**。
 - **服务端口**：填写 “80”。
 - **流量策略**：选择**部署完成后自动开启100%流量**。

<img src="https://main.qcloudimg.com/raw/49fb36c111dae7beaa32c2f852c799b7.png" alt="" style="zoom: 80%;" />

>?本 Demo 镜像为基于 php 官方镜像所构建的 php 服务镜像，其默认开放了 80 端口，并在 /var/www/html/ 目录下存放了 index.php 与 post.php 两个代码文件。其中 index.php 用于提供前端显示页面，同时读取并输出txt文件中所记录的物联网设备状态；post.php 用于获取 post 请求并将其保存在 txt 文件中。
>
3. 单击**下一步**进入托管配置页面，本示例对资源要求不高，因此可选择最小资源规格“0.25核/0.5G”。同时副本模式可选择“低成本”，当连续半小时无流量时自研节点将自动缩容实例数量至0，避免额外成本。
<img src="https://main.qcloudimg.com/raw/f14d913f9646b8acbb921b75f29ce4ae.png" alt="" style="zoom: 80%;" />
4. 单击**开始部署**，若部署成功则状态变为“正常”。
<img src="https://main.qcloudimg.com/raw/7e95460c23c1d3f4b1cdce449b49449b.png" alt="" style="" />

### 步骤五：访问服务

1. 完成上述步骤后，单击**服务配置**进入服务配置页面，单击**公网访问地址**的跳转链接，即可访问 SaaS 的前端页面。
<img src="https://main.qcloudimg.com/raw/9e3dabf221344c2c1d70f6d01f946871.jpg" alt="" style="" />
<img src="https://main.qcloudimg.com/raw/797efd6eef08e688b713ba22ece6b52d.jpg" alt="" style="" />
2. 本阶段成功部署了一个简单的前端服务，当然 Demo 的功能不局限于此，接下来还可以通过阶段二结合物联网 SaaS 与规则引擎功能，实现设备状态的实时转发与展示。

## 阶段二：实现物联网设备数据转发

本阶段的运作流程如下图所示。当设备状态更新时，将上报状态数据至物联网开发平台，再通过物联网开发平台的规则引擎功能，将数据实时转发到您的 SaaS 中；同时 SaaS 提供前端页面以查看对应数据。
<img src="https://main.qcloudimg.com/raw/d3d688cb40424f417bbcf14df45b8a9d.jpg" alt="" style="" />

### 步骤一：创建物联网开发平台产品

为实现设备状态转发，需要提前使用物联网开发平台创建产品。创建步骤请参见 [产品开发文档](https://cloud.tencent.com/document/product/1081/34738) 。

### 步骤二：设置规则引擎

1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer) ，进入项目详情页面，单击左侧菜单的**规则引擎**进入规则引擎页面。
2. 在规则引擎页面中，单击**创建规则**，填入规则名称后，单击**确定**。
<img src="https://main.qcloudimg.com/raw/c23d06c5dd85b8bfd6434c4e71272ece.jpg" style="zoom:80%;" />
3. 单击**规则名称**进入规则详情页面，单击筛选数据卡片的**编辑**按钮进入编辑规则页面。
![](https://main.qcloudimg.com/raw/1811b7f8391b268f570ae7a7a37b8234.jpg)
4. 在编辑规则页面可定义数据转发规则，需要配置如下内容：
   - **字段**：用于定义 JSON 消息中所需转发的字段。若希望转发所有字段，可填写 “\*”。本例中填写 “\*”。
   - **Topic**：用于定义需要转发的产品、设备及其转发内容。本例中选择**电气火灾监控器**、**全部设备**、**物模型属性上报**。
   - **条件**：用于定义条件规则，以过滤 Topic 中的消息。本例条件为空。

<img src="https://main.qcloudimg.com/raw/b375ff74688bd4e5088d18f2d9808326.jpg" alt="" style="zoom: 80%;" /><br>
5. 单击**确定**回到规则详情页面，单击行为操作卡片的**添加行为操作**按钮进入添加规则页面。
![](https://main.qcloudimg.com/raw/1244180e1f267f37186a3e21c1b7a33c.jpg)
6. 在添加规则页面可定义数据转发规则，需要配置如下内容：
   - 行为类型：本例选择**数据转发到第三方服务（Forward）**。
   - API 地址：可设置 SaaS 的服务地址。服务地址需要输入上一阶段得到的默认公网访问地址+“post.php”，例如 `https://***.ap-guangzhou.service.tcloudbase.com/post.php`。
<img src="https://main.qcloudimg.com/raw/17a1dcf38a22f5e972953fda71629c0c.jpg" style="zoom:80%;" />

7. 单击**保存**，返回到规则引擎列表页，开启该规则的**状态**，完成该规则的数据转发配置。
![](https://main.qcloudimg.com/raw/25f30c6bb1bfb92f06fb12bc4e57bdf0.jpg)

本示例使用的是 [规则引擎](https://cloud.tencent.com/document/product/1081/61105) 功能，若需要通过图形化界面进行数据规则定义，可通过 [数据开发](https://cloud.tencent.com/document/product/1081/61138) 配置数据流规则，并通过自定义推送模块推送至 HTTP 服务 URL。

### 步骤三：上报设备状态数据

若在物联网开发平台的产品开发的过程中已经绑定实物设备，可直接通过控制设备实现设备状态上报。

若暂无实物设备，可通过 [虚拟设备调试](https://cloud.tencent.com/document/product/1081/34741) 功能完成设备数据上报。

1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer) ，单击项目进入项目详情页面，单击**产品开发** > 选择相应产品 > **设备调试** > **虚拟设备调试**进入虚拟设备调试页面。
2. 于虚拟设备操控面板设置相应参数，单击**上报**实现设备状态数据上报。
<img src="https://main.qcloudimg.com/raw/54bdaf04974bcbe5acc9f442cf6a2d40.jpg" alt=""  />

### 步骤四：访问服务

再次访问上一阶段创建的 SaaS 服务，即可查看来自物联网开发平台所转发的设备状态数据。
<img src="https://main.qcloudimg.com/raw/8f00ff646cbd493f413abee0b0e9c8cb.jpg" alt=""  />

## 更多拓展

您可以基于本示例扩展更多物联网应用功能，如对设备的状态数据进行分析，实现状态预警功能；或将设备状态数据进行预处理，并保存至数据库中。
