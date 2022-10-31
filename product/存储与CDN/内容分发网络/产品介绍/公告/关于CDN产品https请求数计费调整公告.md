## 调整说明
腾讯云 CDN 产品将增加 HTTPS 请求数的增值服务计费，定价如下：

|HTTPS 请求数（万次）|	价格（元/万次）|
|-|-|
|0 - 300（含）|	免费|
|大于 300	|0.05|

- 每个账号每个月有300万（含）次 HTTPS 请求数的免费额度，CDN 产品仅对超出免费额度的 HTTPS 请求数进行计费，价格按0.05元/万次请求数进行收取。
- 免费额度在每个自然月内有效，未用尽部分会在次月1日0点失效，并同时重新获取新的300万次免费额度。
- 示例1：若您在9月6日开始启用 CDN 产品的 HTTPS 服务，并在9月6日-9月30日共产生了200万次 HTTPS 请求数，因未超过免费额度，则9月 HTTPS 请求数费用为0。免费额度中剩余未使用的100万次请求数在10月1日0点后失效，并会同时获取新的300万次免费额度。
- 示例2：若您在9月6日开始启用 CDN 产品的 HTTPS 服务，并在9月6日-9月30日共产生了400万次 HTTPS 请求数，其中300万次为免费额度不计费。超出的100万次按0.05元/万次计费，则9月 HTTPS 请求数费用为：100万次 \* 0.05元/万次 = 5元。在10月1日0点后获取新的300万次免费额度。


## 调整范围
加速类型为「内容分发网络 CDN」域名所产生的 HTTPS 请求数，不包含加速类型为「全站加速网络 ECDN」的域名：

<table>
<thead>
<tr>
<th colspan="2">加速类型</th>
<th>是否收 HTTPS 费用</th>
</tr>
</thead>
<tbody><tr>
<td>内容分发网络 CDN</td>
<td>CND 网页小文件</td>
<td>是</td>
</tr>
<tr>
<td>内容分发网络 CDN</td>
<td>CND 下载大文件</td>
<td>是</td>
</tr>
<tr>
<td>内容分发网络 CDN</td>
<td>CND 音视频点播</td>
<td>是</td>
</tr>
<tr>
<td>全站加速网络 ECDN</td>
<td>ECDN 动静加速</td>
<td>否</td>
</tr>
<tr>
<td>全站加速网络 ECDN</td>
<td>ECDN 动态加速</td>
<td>否</td>
</tr>
</tbody></table>

在域名列表可查看域名归属的加速类型，如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/c9c1b644518e5ab5244d3052740c95cb.png)

## 调整时间
北京时间2023年1月5日0:00:00起。

## 账单影响
CDN 产品开启 HTTPS 服务的用户会产生 HTTPS 请求数费用，包括小时结、月结用户，产生的费用可通过账单查询：
1. 小时结用户：小时结账单上仅展示付费的 HTTPS 请求数，免费额度的 HTTPS 请求数和费用不体现在账单上。
2. 月结用户：月结账单同时展示免费额度的 HTTPS 数和付费的 HTTPS 请求数及费用。

所有用户都可以在控制台的服务概览「CDN 总请求数」查询时间范围产生的总 HTTPS 请求数（包括免费和付费的请求数）。

## FAQ
### 什么情况会产生 HTTPS 计费？

当您完成域名的证书配置，即开启了 HTTPS 服务能力。若 HTTPS 请求数每月超出免费额度，超出的部分会产生 HTTPS 费用，下图为已开启 HTTPS 服务的配置。
![](https://qcloudimg.tencent-cloud.cn/raw/141511f8fdaf61622ed9d9f5f8bdae10.png)

### 如何查询 HTTPS 请求数量？
CDN 控制台可提供 HTTPS 请求数量，具体操作步骤如下：
1. 登录控制台 ，单击服务概览的 **CDN 总请求数**进入查询。
![](https://qcloudimg.tencent-cloud.cn/raw/b3f6442ff6edf4c63846d55170776c39.png)
2. 在访问监控详情页面选择您要查询的时间段，「HTTP 协议」下拉框选择为“HTTPS”、单击**查询**按钮，可查询时间段的 HTTPS 总请求数，如图：
![](https://qcloudimg.tencent-cloud.cn/raw/d64d75e860ccfd59dd977e0c3207ad28.png)


### 如何关闭 HTTPS 计费？

关闭域名的证书配置，则不会产生 HTTPS 请求数费用。但关闭域名的证书配置，就无法提供 HTTPS 服务，可能影响终端用户的 HTTPS 请求。
关闭操作如下：
1. 登录 CDN 控制台，选择菜单**域名管理**，选择要关闭的域名，单击**管理**操作。
![](https://qcloudimg.tencent-cloud.cn/raw/433d61bdbb26d47dd4081d3c2c202afa.png)
选择 **HTTPS 配置**页面，操作**删除**，等待配置部署完成。
![](https://qcloudimg.tencent-cloud.cn/raw/d305c912dc59cdb4e68d94f035aabd20.png)

