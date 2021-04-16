您可以通过编写云函数 SCF 来实现 Web 后端服务，然后使用负载均衡 CLB 绑定云函数 SCF 并对外提供服务。
>? 负载均衡 CLB 绑定云函数 SCF 功能目前处于内测阶段，如需使用，请提交 [内测申请](https://cloud.tencent.com/apply/p/h2r3ix3s5vs)。
>

## 背景信息
[云函数（Serverless Cloud Function，SCF）](https://cloud.tencent.com/document/product/583)是腾讯云为企业和开发者们提供的无服务器执行环境，帮助您在无需购买和管理服务器的情况下运行代码。在您创建完云函数后，可以通过创建 CLB 触发器将云函数与事件进行关联。CLB 触发器会将请求内容以参数形式传递给云函数，并将云函数返回作为响应返回给请求方。

## 使用场景
<dx-accordion>
::: 典型场景一：秒杀/抢购活动
秒杀&抢购活动中，对整体资源的应用弹性的要求较高，而且和业务的主干场景联系较为紧密。云函数 SCF 一般是业务系统中较为独立的模块，便于迁移和改造。您可以通过负载均衡 CLB 无缝支持云函数，对于按调用次数的收费场景，整体计费和迁移成本都会比较低。同域名下，还可以轻松解决跨资源共享（CORS）跨域问题。
![](https://main.qcloudimg.com/raw/9407d48ee26c116a59c26c83e3f8c9db.png)
:::
::: 典型场景二：辅助系统架构
企业的非主干 WEB 业务，例如订单系统、采集系统、BI 分析等对削峰填谷比较敏感的非主干场景，使用云函数 SCF 结合负载均衡 CLB ，整体迁移成本会比较低且迁移收益大。
![](https://main.qcloudimg.com/raw/414fc87fbcc391912d42261a8347bf15.png)
:::
::: 典型场景三：动静态业务分离
当业务请求量较大时，可以通过区分网站的静态和动态请求，有针对性地对其进行分发处理，有效减少后端负载压力。其中动态请求可以通过单独部署负载均衡及关联云函数 SCF 服务进行处理，静态内容可以通过接入 CDN 服务，结合对象存储进行优化，提升加载速度。
![](https://main.qcloudimg.com/raw/910ee56aac139ead66be7dae556ca6e2.png)
:::
::: 典型场景四：同域名的地域级访问服务
业务对地域要求较高时，可以通过负载均衡 CLB 对云函数 SCF 做地域级访问划分。
:::
</dx-accordion>

## 限制说明
- 仅广州、深圳金融、上海、上海金融、北京、成都、中国香港、新加坡、孟买、东京、硅谷地域支持绑定 SCF。
- 仅标准账户类型支持绑定 SCF，传统账户类型不支持。建议升级为标准账户类型，详情可参见 [账户类型升级说明](https://cloud.tencent.com/document/product/1199/49090)。 
- 传统型负载均衡不支持绑定 SCF。
- 基础网络类型不支持绑定 SCF。
- 仅支持跨 VPC 绑定 SCF，不支持跨地域绑定。
- 目前仅 IPv4、IPv6 NAT64 版本的负载均衡支持绑定 SCF，IPv6 版本的暂不支持。
- 仅七层（HTTP、HTTPS）监听器支持绑定 SCF，四层（TCP、UDP、TCP SSL）监听器和七层 QUIC 监听器不支持。


## 前提条件
1. [创建负载均衡实例](https://cloud.tencent.com/document/product/214/6149)
2. [配置 HTTP 监听器](https://cloud.tencent.com/document/product/214/36384) 或 [配置 HTTPS 监听器](https://cloud.tencent.com/document/product/214/36385)

## 操作步骤
1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb)。
2. 在“实例管理”页面的“负载均衡”页签中，单击目标实例右侧“操作”列的【配置监听器】。
3. 在 HTTP/HTTPS 监听器列表中，选择需要绑定云函数 SCF 的监听器，分别单击目标监听器左侧的【+】和展开的域名左侧的【+】，然后选中展开的 URL 路径，单击【绑定】。
![](https://main.qcloudimg.com/raw/15cd2745ad1a5eb5708cc822d4a55cfa.png)
4. 在弹出的“绑定后端服务”对话框中，目标类型选择“云函数 SCF”，选择命名空间、函数名和版本/别名，设置权重后，单击【确认】。
![](https://main.qcloudimg.com/raw/12286261c9c84316b4634fce0ee5aa96.png)
5. 返回“监听器管理”页签，在“转发规则详情”区域单击函数名。
![](https://main.qcloudimg.com/raw/2da69c0e92fe34a744a48c4a8c7cdb05.png)
6. 在“函数代码”页签，编辑函数代码。需要按照特定响应集成格式返回，详情请参见 [集成响应](https://cloud.tencent.com/document/product/583/52635#.E9.9B.86.E6.88.90.E5.93.8D.E5.BA.94)。
![](https://main.qcloudimg.com/raw/d0560171044434579e07b8dbcc963c10.png)
>? 您还可以选择在 SCF 控制台创建 CLB 触发器，从而将负载均衡 CLB 与云函数 SCF 绑定，详情请参见 [创建触发器](https://cloud.tencent.com/document/product/583/30230#.E9.80.9A.E8.BF.87.E6.8E.A7.E5.88.B6.E5.8F.B0.E5.AE.8C.E6.88.90.E8.A7.A6.E5.8F.91.E5.99.A8.E5.88.9B.E5.BB.BA)。

## 相关文档
[创建 SCF 函数](https://cloud.tencent.com/document/product/583/37509)
