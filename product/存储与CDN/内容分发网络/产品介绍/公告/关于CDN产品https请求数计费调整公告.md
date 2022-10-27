## 调整说明
腾讯云 CDN 加速产品增加 HTTPS 请求计费项，费用如下：



|HTTPS 请求数（万次）|	价格（元/万次）|
|-|-|
|0 - 300（含）|	0|
|> 300	|0.05|

即每个账号每个月将有300万（含）次请求数免费额度，超出后需进行计费，超出部分按0.05元/万次请求进行收取。
免费额度按自然月度累积计算，次月则重新获取300万免费额度。
示例：若您在9月20日开始使用 CDN，产生的 HTTPS 请求数，在9月20日-9月30日均可免费抵扣300万 HTTPS 请求数，超出则按0.05元/万次计费。在10月1日0点后，重新可免费抵扣300万 HTTPS 请求数。

## 调整范围
面向腾讯云 CDN 用户，加速类型为「内容分发网络 CDN」的域名，不包含加速类型为「全站加速网络 ECDN」的域名，如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/b6a9efebab2ce586e40e147c9f3f5257.png)
用户可以域名列表查看域名归属的加速类型，如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/c9c1b644518e5ab5244d3052740c95cb.png)

## 调整时间
北京时间2023年1月4日0:00:00起。

## 调整影响
HTTPS 计费面向 CDN 开启证书配置产生 HTTPS 服务的用户，包括小时结、月结用户，产生的费用可通过账单上体现：
1. 小时结用户，在账单上仅体现付费的 HTTPS 请求数，免费额度的 HTTPS 不体现在账单，可在控制台的服务概览「CDN 总请求数」查询时间范围产生的 HTTPS 总数。
2. 月结用户，月结用户的月结账单推体现免费额度的 HTTPS 数和需付费的 HTTPS 请求数。


## FAQ
### 什么情况会产生 HTTPS 计费？
当您的域名配置了证书且使用 HTTPS 请求服务，且 HTTPS 请求数每月超出300万次，则会产生 HTTPS 费用。
![](https://qcloudimg.tencent-cloud.cn/raw/c62ac55ed4a4a8e9174103cf3c8c47b2.png)

### 如何查询 HTTPS 请求数量？
CDN 控制台可提供 HTTPS 请求数量，具体操作步骤如下：
1. 登录控制台 ，单击服务概览的 **CDN 总请求数**进入查询。
![](https://qcloudimg.tencent-cloud.cn/raw/b3f6442ff6edf4c63846d55170776c39.png)
2. 在访问监控详情页面选择您要查询的时间段，「HTTP 协议」下拉框选择为“HTTPS”、单击**查询**按钮，可查询时间段的 HTTPS 总请求数，如图：
![](https://qcloudimg.tencent-cloud.cn/raw/d64d75e860ccfd59dd977e0c3207ad28.png)
3. 费用估算，根据查询的 HTTPS 请求数，您可以预估 HTTPS 请求数产生的大概费用，计算公式：**预计费用 =（总请求数-免费额度）/ 10000 \* 0.05（元）**。
**注：**免费额度按月计费，估算费用时 HTTPS 请求数的查询时间范围建议为一个月。

### 如何关闭 HTTPS 计费？
关闭域名的证书配置，则不产生 HTTPS 请求，但也影响 HTTPS 请求服务，即关闭域名的证书配置，则无法响应 HTTPS 请求服务。关闭操作如下：
1. 登录 CDN 控制台，选择菜单**域名管理**，选择要关闭的域名，单击**管理**操作。
![](https://qcloudimg.tencent-cloud.cn/raw/433d61bdbb26d47dd4081d3c2c202afa.png)
选择 **HTTPS 配置**页面，操作**删除**，等待配置部署完成。
2.  若关闭了证书配置且已配置强制跳转 HTTP->HTTPS，也需一起关闭，操作如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/d305c912dc59cdb4e68d94f035aabd20.png)
单击**配置状态**开关进行关闭，等待部署完成。
3. 若域名原来一直提供HTTPS服务，关闭证书后，为了避免HTTPS服务被拒绝，建议在「强制跳转」配置为Https->Http。
![](https://qcloudimg.tencent-cloud.cn/raw/eff783907062b745ecf1caa498795ad4.png)
