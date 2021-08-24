## 现象描述
登录腾讯云 [DNS 解析 DNSPod 控制台](https://console.cloud.tencent.com/cns) ，进入域名解析列表， 即可查看解析状态，包含以下5种常见状态：

![](https://main.qcloudimg.com/raw/6ccb73d1f176256ddad924518ab0c370.png)
<table>
<thead>
  <tr>
    <th>解析状态</th>
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
    <td>未添加正确且有效的解析记录。</td>
  </tr>
  <tr>
    <td>已封禁</td>
    <td>该域名已被举报封禁，如有问题，可加入 <a href="https://cloud.tencent.com/document/product/242/57608#DNSPod">DNSPod 官方用户群</a> 进行咨询。</td>
  </tr>
</tbody>
</table>

若显示以下几种状态，则建议您调整为正常解析状态：
- 暂停解析。
- 域名 DNS 未修改。
- 待添加解析记录。
- 已封禁。

## 解决办法
### 暂停解析
如您设置解析状态为暂停解析，现需要重新开启，可参考 [暂停或启用解析记录](https://cloud.tencent.com/document/product/302/42165) 进行调整。

### 域名 DNS 未修改
DNS 地址未修改会影响解析生效，请前往域名注册商处修改 DNS 服务器，如您的域名在腾讯云注册，可参考 [修改域名 DNS 服务器](https://cloud.tencent.com/document/product/302/5518) 进行调整。

### 待添加解析记录
解析记录中，无解析记录值。需对域名添加正确且有效的解析记录，才可以正常使用。设置解析记录请参考 [各记录类型说明及规则](https://cloud.tencent.com/document/product/302/38661)。

### 已封禁
该域名已被举报封禁，如有问题，可加入 [DNSPod 官方用户群](https://cloud.tencent.com/document/product/242/57608#DNSPod) 进行咨询。
