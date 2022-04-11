## 操作场景
私有子 CA 是私有 CA 下子证书，即中间证书，只有启用根 CA 后，您才可以启用根 CA 下的子 CA。本文将指导您购买私有 CA 服务后如何开启其私有子 CA。

## 使用说明
- 私有 CA 分为根 CA 和子 CA（即中间 CA），子 CA 隶属于根 CA，根 CA 下可以包含多个子 CA。只有子 CA 可用于签发私有证书（包括服务端证书、客户端证书）。
- 首次创建私有 CA 时，您必须先创建根 CA。创建根 CA 后，您将会获得一个根 CA 和一个子 CA，且子 CA 默认包含10张证书资源（可以签发10张证书）。
- 您可以根据企业组织架构，在已有的根 CA 下继续创建多个子 CA（例如，为企业内不同部门分别创建对应的子 CA）或者在私有子 CA 下购买证书，增加子 CA 可以签发的证书数量。

## 操作步骤
1. 登录 [SSL 证书私有 CA 管理控制台](https://console.cloud.tencent.com/private-ca)，选择您需要开启的私有子 CA，并单击**启用**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/38532156e5cb79bb27907c32e960b5d7.png)
2. 在创建根 CA 页面，配置根 CA 的信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/1b8053ae2c6d501f959f6c00407cd3d1.png)
配置说明如下：
<table>
<thead>
   <tr>
    <th>配置信息</th>
    <th>填写说明</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>根 CA 名称</td>
    <td>根 CA 的名称，支持使用中文或者英文，可自定义。<br>示例：tencent。</td>
  </tr>
  <tr>
    <td>通用名称</td>
    <td>该 CA 关联的组织机构的通用名称（或简称）。支持使用中文或者英文。<br>示例：腾讯云。</td>
  </tr>
  <tr>
    <td>组织</td>
    <td>该 CA 关联的组织机构的名称。支持使用中文或者英文。<br>示例：腾讯云计算北京有限责任公司。</td>
  </tr>
  <tr>
    <td>部门</td>
    <td>该 CA 关联的组织部门的名称。支持使用中文或者英文。<br>示例：IT部。</td>
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
3. 配置完成后，单击**确定**。
4. 在弹出的提示框中，单击**确定**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/4e67209eb962ccbbaf5c28039c9e8d63.png)

## 后续步骤
您依次启用根 CA 和子 CA 后，可以通过已启用的子 CA 申请私有 SSL 证书。详情请参见 [申请私有证书](https://cloud.tencent.com/document/product/400/72334)。
