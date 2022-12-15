## 操作场景

本文介绍如何在 Kong 云原生 API 网关上通过 Kong IP Restriction 插件实现 IP 访问控制，包括以下两种场景：
- 配置 IP 黑/白名单列表进行访问控制
- 配置 IP 黑/白名单 CIDR 段进行访问控制

   

## 前置条件

- 已购买 Kong 网关实例，[操作文档](https://cloud.tencent.com/document/product/1364/72495)。
- 配置了后端（Service）以及路由（Route）。

   

## 操作步骤

### 场景一：配置 IP 黑/白名单列表进行访问控制

本场景操作步骤以黑名单 IP 列表为例，指导如何拒绝某个（些）IP 访问，白名单配置与之类似。

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse/kong)，进入需要配置限流插件的 Kong 网关实例详情页，在**配置管理**页查看管理控制台登录方式。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/296cd720bc50aba0da782189d28d0073.jpg">
2. 登录 Konga 管理控制台，进入需要 IP 限制的 **Route 详情页**，单击 **Add Plugin** 按钮创建插件。
   ![](https://qcloudimg.tencent-cloud.cn/raw/e61863ce0ae7ba44dc19c9f1f2b4cc3e.png)
2. 在插件市场的 Security 分组中选择 IP Restriction 插件，单击 Add Plugin。
   ![](https://qcloudimg.tencent-cloud.cn/raw/b9e8bf2e4076cf6c1540a66f72cd5c81.png)
4. 插件配置中填写需要配置限制的 IP 配置，并保存
 - `allow`：填写允许访问的IP，多个 IP 需要填写多个。
 - `deny`：填写拒绝访问的IP，多个 IP 需要填写多个。
 - `consumer`：填写需要应用访问控制的 Consumer ID，如空缺，表示该 IP 访问控制应用于所有 consumer。
<dx-alert infotype="notice" title="">
     **allow 和deny 两者至少配置一项。**
</dx-alert>
<img src = "https://qcloudimg.tencent-cloud.cn/raw/ebdf544eebde990150aa455a2744c0c9.png"> 
5. 返回 route 页面，确定该 route 已经绑定的创建的插件。
![](https://qcloudimg.tencent-cloud.cn/raw/73f36c07a931098487dac1365438bc98.png)
6. 发起 API 请求，该 IP 访问被限制。
<dx-codeblock>
:::  SH
HTTP/1.1 403 Forbidden
Connection: keep-alive
Content-Length: 48
Content-Type: application/json; charset=utf-8
Date: Mon, 25 Apr 2022 02:57:32 GMT
X-Kong-Response-Latency: 1

{
  "message":"Your IP address is not allowed"
}
:::
</dx-codeblock>




### 场景二：配置 IP 黑/白名单 CIDR 段进行访问控制

本场景操作步骤以白名单 IP CIDR 段为例，指导如何允许某个 IP 段的请求访问，黑名单配置与之类似。

1. 进入需要 IP 限制的 Route 详情页，单击 Add Plugin 按钮创建插件。
2. 插件配置中填写以下配置，并保存
   - `allow`：填写允许访问的 IP CIDR 段。
   - `deny`：填写拒绝访问的 IP CIDR 段。
   - `consumer`：填写需要应用访问控制的 Consumer ID，如空缺，表示该IP访问控制应用于所有 consumer。
<dx-alert infotype="notice" title="">
     **allow 和 deny 两者至少配置一项。**
</dx-alert>
<img src = "https://qcloudimg.tencent-cloud.cn/raw/1664c91ae502e2c60b66d1a8c89db97b.png"> 
3. 发起 API 请求，使用不在该 CIDR 段的IP访问，请求被拒绝。
<dx-codeblock>
:::  SH
HTTP/1.1 403 Forbidden
Date: Mon, 25 Apr 2022 03:06:58 GMT
Content-Type: application/json; charset=utf-8
Connection: keep-alive
Content-Length: 48
X-Kong-Response-Latency: 14

{
  "message":"Your IP address is not allowed"
}
:::
</dx-codeblock>



## 注意事项

当对一个 IP 同时应用了 allow 和 deny ，该 IP 会被限制访问。

  

## 参考

更多相关说明请参见 [Kong 插件文档](https://docs.konghq.com/hub/kong-inc/ip-restriction/)。