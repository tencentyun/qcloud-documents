云托管服务可以通过其所在的 VPC（私有网络）访问您在腾讯云上的 MySQL 数据库。

## 背景知识
关于使用 VPC 连接 MySQL，请参见 [连接 MySQL 实例](https://cloud.tencent.com/document/product/236/3130)。单击服务所在私有网络的名称，可以跳转到私有网络控制台查看该私有网络内您有哪些 MySQL 数据库资源，可以与此服务配合使用。

## 前置条件
您的云托管服务和 MySQL 数据库处于同一 VPC 内。

## 操作步骤

### 步骤1：查询 MySQL 实例所在 VPC[](id:step1)

1. 登录 [云数据库 MySQL 控制台](https://console.cloud.tencent.com/cdb)，找到您的 MySQL 实例。
2. 在左侧菜单中，单击**实例列表**，进入实例列表。单击实例名进入详情页，进入**实例详情**选项卡，在基本信息版块中，查找到**所属网络**信息：
   ![](https://main.qcloudimg.com/raw/587ff2bf466ce705cd1b559d36d48cf8.jpg)

### 步骤2：新建云托管服务

创建时，在“云托管网络”中选择**已有私有网络**，下拉选择 [步骤1](#step1) 中查询到 MySQL 实例所在的 VPC 和子网。具体流程请参见 [新建服务](https://cloud.tencent.com/document/product/1243/46126)。

### 步骤3：部署服务

服务部署完成后，该服务将可以访问您选定的 MySQL 实例，以及同 VPC 下其他 MySQL 实例。具体流程请参见 [部署服务](https://cloud.tencent.com/document/product/1243/46127)。

## 说明

- 已有云托管服务不支持修改所在 VPC。若您已部署好了服务，误选了和 MySQL 实例不相同的 VPC，可选择：
   - 重新在正确 VPC 部署服务，删除部署错误的服务。
   - [打通多个 VPC](https://cloud.tencent.com/document/product/215/36698)。
- 云托管暂时仅支持上海、广州、北京地域。若您的 MySQL 实例不在上述地域则无法复用。更多地域将陆续开放，敬请期待。
