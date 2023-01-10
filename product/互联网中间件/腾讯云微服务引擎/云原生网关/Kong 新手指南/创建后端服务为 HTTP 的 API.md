本文将快速引导您如何在云原生 API 网关 Kong 中，发布后端服务为 HTTP 类型的 API。

## 概述
您需要依次完成以下步骤：
1. [创建 Kong 网关实例](#step1)
2. [登录 Konga 控制台](#step2)
3. [定义后端服务信息](#step3)
4. [为服务配置路由规则](#step4)
5. [调用 API](#step5)

## 操作步骤
[](id:step1)
### 步骤1：创建 Kong 网关实例
参见 [实例管理](https://cloud.tencent.com/document/product/1364/72495)，创建一个 Kong 网关。

[](id:step2)
### 步骤2：登录 Konga 控制台
单击创建好的 Kong 网关的 ID，进入基本信息页面，在页面上方选择**访问控制**页签，使用 **Konga 访问地址**模块的公网访问地址或内网访问地址和管理员账号密码，登录 Konga。
>?可配置公网访问策略，详情参见 [访问控制](https://cloud.tencent.com/document/product/1364/72496)。
>
<img src="https://qcloudimg.tencent-cloud.cn/raw/b98dd1db82f4bc4a6cfa7496f0038ebe.png" style="width:700px">  


[](id:step3)
### 步骤3：定义后端服务信息
1. 在 Konga 控制台左侧导航栏选择**Services**，单击**ADD NEW SERVICE**，添加服务。
<img src="https://qcloudimg.tencent-cloud.cn/raw/817c7d569181e416aa7828aa24318a6e.png" style="width:700px">  
2. 填写后端服务信息，单击**SUBMIT SERVICE**。
>?本步骤是指定在 Kong 收到 Client 端的请求后，转发到哪个后端服务。本例中的后端服务可以为腾讯云上或在互联网上的任何可以访问到的地址。
>
<img src="https://qcloudimg.tencent-cloud.cn/raw/5c678c8f0343f2e11d9665352ac8c7a8.png" style="width:700px">  


[](id:step4)
### 步骤4：为后端服务配置路由
1. 后端服务添加完成后，点击后端服务名称进入基本信息页面，单击**Routes** > **ADD ROUTE**，添加路由。
<img src="https://qcloudimg.tencent-cloud.cn/raw/95a0c0ee6f0d45b5afb1dda2da0731b2.png" style="width:700px">  
2. 创建匹配路由，设置好 Path 和 Method，单击**SUBMIT ROUTE**。
>!Host/Path/Method，填写后需要输入回车。
>
<img src="https://qcloudimg.tencent-cloud.cn/raw/7b2e55f74444f914eb13bf721d6c7a9b.png" style="width:700px">  


[](id:step5)
### 步骤5：调用 API
1. 进入 Kong 网关的**访问控制**页面，获取负载均衡地址。
<img src="https://qcloudimg.tencent-cloud.cn/raw/bf556922e84828150d5dc7ba7721da96.png" style="width:700px">  
2. 使用负载均衡地址和配置的路由路径访问 API，执行curl 命令测试，已通过 Kong 访问到后端服务。
<img src="https://qcloudimg.tencent-cloud.cn/raw/98fe2ab99311da9afff5cc23a1409760.png" style="width:700px">  
