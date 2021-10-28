精品 BGP IP 线路类型的 EIP 使用专属线路，避免绕行国际运营商出口，网络延时更低。
>?
>- 目前仅标准账户类型支持精品 BGP IP，传统账户类型需升级后才能使用，升级详情请参见 [账户类型升级说明](https://cloud.tencent.com/document/product/1199/49090)。
>- 仅香港地域支持精品 BGP IP，价格详情请参见 [精品 BGP 带宽包](https://cloud.tencent.com/document/product/684/15255#cn2)。
>- 如需体验，请提交 [内测申请](https://cloud.tencent.com/apply/p/224jt7718s8)。

## 操作步骤
### 步骤一：创建精品 BGP 带宽包[](id:step1)
创建精品 BGP IP 线路类型的 EIP 前，需先创建精品 BGP 带宽包。
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)，单击左侧导航栏的**共享带宽包**。
2. 在“共享带宽包”页面顶部，选择中国香港地域，单击左上角的**新建**。
3. 在“新建共享带宽包”对话框中，输入名称，选择“精品 BGP”线路类型和计费模式后，单击**确定**。
<img src="https://main.qcloudimg.com/raw/13c8828b8542400e779b37735c4d59f7.png" width="53%" />

### 步骤二：创建精品 BGP IP 线路类型的 EIP[](id:step2)
创建精品 BGP IP 线路类型的 EIP，并将此 EIP 加入已创建好的精品 BGP 带宽包。
1. 登录 [公网 IP 控制台](https://console.cloud.tencent.com/cvm/eip)。
2. 在“公网 IP”页面顶部，选择中国香港地域，单击左上角的**申请**。
3. 在弹出的“申请 EIP”对话框中，配置以下参数。
<p><img src="https://main.qcloudimg.com/raw/48149cb4930c63296402c71a1eae7c80.png" width="50%" /></p>
<table>
<thead>
<tr>
<th width="20%">参数</th>
<th width="80%">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>IP 地址类型</td>
<td>选择精品 BGP IP。
</td>
</tr>
<tr>
<td>计费模式</td>
<td>精品 BGP IP 仅支持共享带宽包计费模式。
</td>
</tr>
<tr>
<td>共享带宽包</td>
<td>请在下拉列表中选择 <a href="#step1">步骤一</a> 已创建的共享带宽包。
</td>
</tr>
<tr>
<td>带宽上限</td>
<td>请按需设置带宽上限，合理分配带宽资源。</td>
</tr>
<tr>
<td>数量</td>
<td>请按需选择申请的数量且确保 EIP 总数未超过产品总配额，详情请参见 <a href="https://cloud.tencent.com/document/product/1199/41648?!#.E9.85.8D.E9.A2.9D.E9.99.90.E5.88.B6">配额限制</a>。</td>
</tr>
<tr>
<td><span>名称</span></td>
<td>EIP 实例名称，非必填。</td>
</tr>
<tr>
<td>标签</td>
<td>如需添加标签可在此进行添加，可通过标签进行权限管理。</td>
</tr>
</tbody></table>


### 步骤三：绑定云资源
1. 登录 [公网 IP 控制台](https://console.cloud.tencent.com/cvm/eip)，并选择中国香港地域。
2. 在目标 EIP 实例右侧的操作栏下，选择**更多** > **绑定**。
3. 在弹出的“绑定资源”窗口中，选择需绑定的云资源类型和云资源，单击**确定**。
>?
>- 若标准账户类型的 CVM 实例已存在普通公网 IP，则需先释放普通公网 IP，才能绑定 EIP。
>- EIP 绑定 CVM 实例的数量限制，根据 CVM 实例 CPU 配置的差异有所不同，请参见 <a href="https://cloud.tencent.com/document/product/1199/41648">使用限制</a>。
>
<img src="https://main.qcloudimg.com/raw/57d265084f2ee8d52bc1cdce6bf08e60.png" width="60%" />
4. 在弹出的“确认绑定”对话框中，单击**确定**，即可完成与云资源的绑定。

