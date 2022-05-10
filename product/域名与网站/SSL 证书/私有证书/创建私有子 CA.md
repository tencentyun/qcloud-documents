## 操作场景
私有子 CA 是私有 CA 下的子证书，即中间证书，只有启用根 CA 后，您才可以启用根 CA 下的子 CA。本文将指导您购买创建私有 CA 后如何启用私有子 CA。

## 使用说明
- 私有 CA 分为根 CA 和子 CA（即中间 CA），子CA 隶属于根 CA，根 CA 下可以包含多个子 CA。只有子 CA 可用于签发私有证书（包括服务端证书、客户端证书）。
- 首次创建私有 CA 时，您必须先创建根 CA。创建根 CA 后，您将会获得一个根 CA 和一个子 CA，且子 CA 默认包含10张证书资源（可以签发10张证书）。
- 后续您可以根据企业组织架构，在已有的根 CA 下继续创建多个子 CA（例如，为企业内不同部门分别创建对应的子 CA）或者在私有子 CA 下购买证书额度，增加子 CA 可以签发的证书数量。

## 操作步骤
1. 登录 SSL 证书 [私有 CA 控制台](https://console.cloud.tencent.com/private-ca)，进入 “私有 CA” 管理页面。
2. 选择对应的私有 CA，单击 <img src="https://qcloudimg.tencent-cloud.cn/raw/2a778da88f2967b7115274d776528941.png"/>，即可展开当前私有 CA 的所有子 CA。
3. 选择需要启用的子 CA，单击**启用**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/8749eeea797ad1a8a6fc471c2f33f154.png)
4. 在创建根 CA 页面，配置根 CA 的信息，单击**确定**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/4095cbb8f8c98a6a34d21378685a9762.png)
配置说明如下：
<table>
<thead>
  <tr>
    <th>配置信息 </th>
    <th>说明</th>
  </tr>
</thead>
<tbody>
 <tr>
    <td>中间 CA 名称 </td>
    <td>中间 CA 的名称。支持使用中文或者英文，可自定义。<br>示例：tencent。</td>
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
    <td>组织机构所在国家的ISO 3166代码。下拉选取即可。<br>示例：默认为中国。</td>
  </tr>
  <tr>
    <td>省</td>
    <td>组织机构所在城市名称。支持使用中文或者英文。<br>示例：广东省。</td>
  </tr>
  <tr>
    <td>市</td>
    <td>示例：深圳市。</td>
  </tr>
  <tr>
    <td>有效期</td>
    <td>该 CA 的有效时长。可选项：所有小于根 CA 有效期(如：5年、10年、15年等)、和根 CA 保持一致。</td>
  </tr>
</tbody>
</table>
5. 在弹出的提示对话框中，单击**确定**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/be23e65cf6fd8b4355bb30479678da16.png)

## 后续步骤
依次启用根 CA 和子 CA 后，可以通过已启用的子 CA 申请私有 SSL 证书。具体操作请参见 [申请私有证书](https://cloud.tencent.com/document/product/400/72334)。
