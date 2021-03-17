DNS服务器状态提示“域名 DNS 未修改”？

## 现象描述

登录腾讯云 [DNSPod DNS 解析管理控制台](https://console.cloud.tencent.com/cns) ，进入域名解析列表， 即可查看到 DNS 服务器状态，主要分别包含如下四个状态：

![](https://main.qcloudimg.com/raw/6ccb73d1f176256ddad924518ab0c370.png)
<table>
<thead>
  <tr>
    <th>DNS服务器状态</th>
    <th>状态说明</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>正常解析</td>
    <td>当前域名使用的 DNS 服务器符合 DNSPod DNS 解析设置的 DNS 服务器。</td>
  </tr>
  <tr>
    <td>暂停解析</td>
    <td>当前域名的解析已被暂停。</td>
  </tr>
  <tr>
    <td>域名 DNS 未修改</td>
    <td>当前域名使用的 DNS 服务器不符合 DNSPod DNS 解析设置的 DNS 服务器。</td>
  </tr>
  <tr>
    <td>待添加解析记录</td>
    <td>需对域名添加正确且有效的解析记录，才可以正常使用。</td>
  </tr>
  <tr>
    <td>已封禁</td>
    <td>该域名已被举报封禁，如有问题，可提交工单申诉。</td>
  </tr>
</tbody>
</table>


若您的状态为以下状态，您可以参考以下方式进行解决：
- 域名 DNS 未修改。
- 待添加解析记录。
- 已封禁。

## 解决办法
- 域名 DNS 未修改。
DNS未修改会影响解析生效，请前往域名注册商处修改DNS服务器，使域名处设置的 DNS 服务器地址与 DNSPod DNS 解析设置的DNS 地址保持一致。详细操作可参考 [修改域名 DNS 服务器](https://cloud.tencent.com/document/product/302/5518)。

- 待添加解析记录。
解析记录中，无解析记录值。需对域名添加正确且有效的解析记录，才可以正常使用。设置详情可参考：[各记录类型说明及规则](https://cloud.tencent.com/document/product/302/38661)。

- 已封禁。
该域名已被举报封禁，如有问题，可访问 [在线客服](https://cloud.tencent.com/online-service?from=cns)  进行咨询。
