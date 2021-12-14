您可以通过编写云函数 SCF 来实现 Web 后端服务，然后使用负载均衡 CLB 绑定云函数 SCF 并对外提供服务。

## 背景信息
[云函数（Serverless Cloud Function，SCF）](https://cloud.tencent.com/document/product/583)是腾讯云为企业和开发者们提供的无服务器执行环境，帮助您在无需购买和管理服务器的情况下运行代码。在您创建完云函数后，可以通过创建 CLB 触发器将云函数与事件进行关联。CLB 触发器会将请求内容以参数形式传递给云函数，并将云函数返回作为响应返回给请求方。

## 使用场景
<dx-accordion>
::: 通用的\sHTTP/HTTPS\s接入
适用于电商、社交、工具等 App 应用程序，以及个人博客、活动页面等 Web 应用程序等场景。方案流程如下所示：
1. App、浏览器、H5、小程序等发起 HTTP/HTTPS 请求，通过 CLB 访问 SCF。
2. 由 CLB 做证书卸载，SCF 仅需提供 HTTP 服务。
3. 请求转给 SCF 后，继续后续处理，例如写入云数据库或调用其他 API。
![](https://main.qcloudimg.com/raw/69d3cc63adfddcb3e50d8f4c0fd1fc4a.svg)
:::
::: CVM/SCF\s平滑切换
适用于 HTTP/HTTPS 服务从 CVM 迁移至 SCF 的场景，以及当 CVM（SCF）服务有问题时，快速迁移至 SCF（CVM）的故障切换场景。方案流程如下所示：
1. App、浏览器、H5、小程序等发起 HTTP/HTTPS 请求。
2. 通过 DNS 解析将请求解析到 CLB 的 VIP 上。
3. 一个 CLB 转发请求给 CVM，另一个 CLB 转发请求给 SCF。
4. 客户端无感知，即可完成后端服务在 CVM 和 SCF 之间的平滑切换。
![](https://main.qcloudimg.com/raw/24e16ebdfe48a948ebd931ab82b02410.svg)
:::
::: CVM/SCF\s业务分流
适用于秒杀、抢购等场景，使用 SCF 处理高弹性服务、使用 CVM 处理日常业务。
1. 通过 DNS 解析将域名 A 解析到其中一个 CLB 的 VIP 上，将域名 B 解析到另外一个 CLB 的VIP 上。
2. 其中一个 CLB 转发请求给 CVM，另外一个 CLB 转发请求给 SCF。
![](https://main.qcloudimg.com/raw/79bf0625f63b5f0b285b6907f22f8c43.svg)
:::

</dx-accordion>



## 限制说明
- 仅广州、深圳金融、上海、上海金融、北京、成都、中国香港、新加坡、孟买、东京、硅谷地域支持绑定 SCF。
- 仅标准账户类型支持绑定 SCF，传统账户类型不支持。建议升级为标准账户类型，详情可参见 [账户类型升级说明](https://cloud.tencent.com/document/product/1199/49090)。 
- 传统型负载均衡不支持绑定 SCF。
- 基础网络类型不支持绑定 SCF。
- CLB 默认支持绑定同地域下的所有 SCF，可支持跨 VPC 绑定 SCF，不支持跨地域绑定。
- 目前仅 IPv4、IPv6 NAT64 版本的负载均衡支持绑定 SCF，IPv6 版本的暂不支持。
- 仅七层（HTTP、HTTPS）监听器支持绑定 SCF，四层（TCP、UDP、TCP SSL）监听器和七层 QUIC 监听器不支持。
- CLB 绑定 SCF 仅支持绑定“Event 函数”类型的云函数。


## 前提条件
1. [创建负载均衡实例](https://cloud.tencent.com/document/product/214/6149)
2. [配置 HTTP 监听器](https://cloud.tencent.com/document/product/214/36384) 或 [配置 HTTPS 监听器](https://cloud.tencent.com/document/product/214/36385)

## 操作步骤
![](https://main.qcloudimg.com/raw/297ceb4d966949ce750add4b174a402e.svg)

### 步骤一：创建云函数
1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf)，在左侧导航栏单击【函数服务】。
2. 在“函数服务”页面，单击【新建】。
3. 在“新建”函数服务页面，创建方式选择“自定义创建”，输入函数名称，地域选择与 CLB 实例相同的地域，运行环境选择“Python3.6”，在函数代码输入框中输入如下代码（本文以 Hello CLB 为例），单击【完成】。
>!CLB 绑定 SCF 时，需按照特定响应集成格式返回，详情请参见 [集成响应](https://cloud.tencent.com/document/product/583/52635#.E9.9B.86.E6.88.90.E5.93.8D.E5.BA.94)。
```plaintext
# -*- coding: utf8 -*-
import json
def main_handler(event, context):

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type":"text/html"},
        "body": "<html><body><h1>Hello CLB</h1></body></html>"
   }
```

### 步骤二：部署云函数
1. 在“函数服务”页面的列表中，单击刚才创建的函数名。
2. 在“函数管理”页面，单击【函数代码】页签，在页签底部单击【部署】。
![](https://main.qcloudimg.com/raw/aafe1535c4b30327601fdaa405c13da3.png)

### 步骤三：绑定云函数
1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb)，在左侧导航栏单击【实例管理】。
2. 在“实例管理”页面的“负载均衡”页签中，单击目标实例右侧“操作”列的【配置监听器】。
3. 在 HTTP/HTTPS 监听器列表中，选择需要绑定云函数 SCF 的监听器，分别单击目标监听器左侧的【+】和展开的域名左侧的【+】，然后选中展开的 URL 路径，单击【绑定】。
![](https://main.qcloudimg.com/raw/15cd2745ad1a5eb5708cc822d4a55cfa.png)
4. 在弹出的“绑定后端服务”对话框中，目标类型选择“云函数 SCF”，选择命名空间、函数名和版本/别名，设置权重后，单击【确认】。
![](https://main.qcloudimg.com/raw/9d26cf3049532375b08f42c8d57c3792.png)
5. 返回“监听器管理”页签，在“转发规则详情”区域显示负载均衡已绑定的云函数，即已创建 CLB 触发器。
![](https://main.qcloudimg.com/raw/074f018af5f3772714710e32ef7fcee0.png)
>? 您还可以选择在 SCF 控制台创建 CLB 触发器，从而将负载均衡 CLB 与云函数 SCF 绑定，详情请参见 [创建触发器](https://cloud.tencent.com/document/product/583/30230#.E9.80.9A.E8.BF.87.E6.8E.A7.E5.88.B6.E5.8F.B0.E5.AE.8C.E6.88.90.E8.A7.A6.E5.8F.91.E5.99.A8.E5.88.9B.E5.BB.BA)。

## 结果验证
1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf)，在左侧导航栏单击【函数服务】。
2. 在“函数服务”页面的列表中，单击刚才创建的函数名。
3. 在函数页面，单击左侧列表的【触发管理】。
4. 在“触发管理”页面的触发器中，单击访问路径。
![](https://main.qcloudimg.com/raw/d576617f76fa4c9849d196e735dfff85.png)
5. 在浏览器里打开该访问路径，若显示 “Hello CLB”，则说明函数已成功部署。
![](https://main.qcloudimg.com/raw/618b179b55682ff690d5c95b6a260016.png)


## 相关文档
[创建 SCF 函数](https://cloud.tencent.com/document/product/583/37509)
