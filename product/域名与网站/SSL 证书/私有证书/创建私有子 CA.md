## 创建私有子CA
私有子CA是私有CA下子证书，即中间证书，只有启用根CA后，您才可以启用根CA下的子CA。本文将指导您购买创建私有 CA后如何创建其私有子CA。

## 使用说明
- 私有CA分为根CA和子CA（即中间CA），子CA隶属于根CA，根CA下可以包含多个子CA。只有子CA可用于签发私有证书（包括服务端证书、客户端证书）。
- 首次创建私有CA时，您必须先创建根CA。创建根CA后，您将会获得一个根CA和一个子CA，且子CA默认包含10张证书资源（可以签发10张证书）。
后续您可以根据企业组织架构，在已有的根CA下继续创建多个子CA（例如，为企业内不同部门分别创建对应的子CA）或者在私有子CA下购买证书，增加子CA可以签发的证书数量。

## 操作步骤
1. 登录 [SSL 证书私有CA管理控制台](https://console.cloud.tencent.com/private-ca),在私有CA处下方私有子CA处单击**启用**。

![](https://qcloudimg.tencent-cloud.cn/raw/38532156e5cb79bb27907c32e960b5d7.png)


2. 在创建根 CA 页面，配置根 CA 的信息。
![](https://qcloudimg.tencent-cloud.cn/raw/1b8053ae2c6d501f959f6c00407cd3d1.png)

配置说明如下：
<table>
<thead>
  <tr>
    <th>中间 CA 名称 </th>
    <th>中间 CA 的名称。支持使用中文或者英文，可自定义。<br>示例：tencent。</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>通用名称</td>
    <td>该CA关联的组织机构的通用名称（或简称）。支持使用中文或者英文。<br>示例：腾讯云。</td>
  </tr>
  <tr>
    <td>组织</td>
    <td>该CA关联的组织机构的名称。支持使用中文或者英文。<br>示例：腾讯云计算北京有限责任公司。</td>
  </tr>
  <tr>
    <td>部门</td>
    <td>该CA关联的组织部门的名称。支持使用中文或者英文。<br>示例：IT部。</td>
  </tr>
  <tr>
    <td>国家代码</td>
    <td>组织机构所在国家在联合国注册的国家代码。支持使用中文或者英文。<br>示例：CHN。</td>
  </tr>
  <tr>
    <td>省</td>
    <td>组织机构所在城市名称。支持使用中文或者英文。
示例：广东省。</td>
  </tr>
  <tr>
    <td>市</td>
    <td>深圳市</td>
  </tr>
  <tr>
    <td>有效期</td>
    <td>该CA的有效时长。可选项：5年、10年、15年、20年。</td>
  </tr>
</tbody>
</table>

3.单击**确认**，并在提示对话框，单击**确定**。

![](https://qcloudimg.tencent-cloud.cn/raw/570e24d2f5d4c098a4fec7206b2e360d.png)

## 后续步骤
您依次启用根CA和子CA后，可以通过已启用的子CA申请私有 SSL 证书。详情参见：[申请私有证书]()。