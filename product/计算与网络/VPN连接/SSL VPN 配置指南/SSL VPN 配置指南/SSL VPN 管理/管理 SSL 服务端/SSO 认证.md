若您通过 [自助 Portal](https://self-service-test.vpn.woa.com/) 下载 SSL 客户端配置，可以在 SSL 服务端开启 SSO 认证。
>?目前 SSO 身份认证功能灰度中，仅支持圣保罗，如有需要，请提交 [工单申请](https://console.cloud.tencent.com/workorder/category)。
>

## 前提条件
在 [数字身份管控平台](https://console.cloud.tencent.com/eiam) 已创建 [用户组](https://cloud.tencent.com/document/product/1442/55067)、添加了相应的 [用户](https://cloud.tencent.com/document/product/1442/55066) 并配为用户组配置 [应用授权](https://cloud.tencent.com/document/product/1442/55069)。


## 在创建 SSL 服务端过程中开启
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **SSL 服务端**，进入管理页面。
3. 在 SSL 服务端管理页面，单击**新建**。
4. 在弹出的**新建 SSL 服务端**对话框中，**认证方式**选择**证书认证** + **身份认证**，然后选择 EIAM 应用。
<table>
<tr>
<th>参数名称</th>
<th>参数说明</th>
</tr>
<tr>
<td>协议</td>
<td>服务端传输协议</td>
</tr>
<tr>
<td>端口</td>
<td>填写 SSL 服务端用于数据转发的端口</td>
</tr>
<tr>
<td>认证算法</td>
<td>目前支持 SHA1 和 MD5 两种认证算法</td>
</tr>
<tr>
<td>加密算法</td>
<td>目前支持 AES-128-CBC、AES-192-CBC 和 AES-256-CBC 加密算法</td>
</tr>
<tr>
<td>是否压缩</td>
<td>否</td>
</tr>
<tr>
<td>认证方式</td>
<td><ul><li>证书认证：该认证方式默认 SSL 服务端可被 SSL 客户端全量访问</li><li>证书认证 + 身份认证：该认证方式仅允许在控制策略中的访问策略连接，您可选择为特定用户组或全部用户配置访问策略，勾选后需要选择对应的 EIAM 应用</li></ul></td>
</tr>
<tr>
<td>EIAM 应用</td>
<td>EIAM 是在 <a href="https://console.cloud.tencent.com/eiam">数字身份管控平台</a> 所创建的用于访问控制的应用</td>
</tr>
<tr>
<td>访问控制</td>
<td>SSL 服务端访问控制开关</td>
</tr>
</table>
5. **访问控制**按需**开启**，详情请参见 [开启访问控制](https://cloud.tencent.com/document/product/554/75188)。

## 在 SSL 服务端创建完成后开启
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **SSL 服务端**，进入管理页面。
3. 在 SSL 服务端管理页面，单击具体的实例名称。
4. 在实例详情页的**基本信息**页签的**服务端配置**区域单击**编辑**。
5. **认证方式**选择**证书认证** + **身份认证**，并选择 EIAM 应用，然后单击**保存**。
