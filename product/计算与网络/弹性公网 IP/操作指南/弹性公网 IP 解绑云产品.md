您可以随时将弹性公网 IP（EIP）与云资源解绑，解绑后您可以将其与其他云资源重新绑定。若不再需要使用该 EIP，请及时将其释放，以免产生不必要的 IP 资源费。

## 费用说明
将 EIP 解绑云资源后，不同类型账户的费用说明如下：
<table>
<thead>
<tr>
<th>账户类型</th>
<th align="center">计费模式</th>
<th>计费说明</th>
</tr>
</thead>
<tbody><tr>
<td>传统账户类型</td>
<td align="center">-</td>
<td rowspan="2">EIP 仅收取 <a href="https://cloud.tencent.com/document/product/1199/51694" target="_blank">IP 资源费用</a>。</td>
</tr>
<tr>
<td rowspan="4">标准账户类型</td>
<td align="center">按流量</td>

</tr>
 <tr>
<td align="center">包月带宽</td>
<td rowspan="2">EIP 不收取 IP 资源费用，仅收取 <a href="https://cloud.tencent.com/document/product/1199/51693" target="_blank">公网网络费用</a>。</td>
</tr> 
<tr>
<td align="center">按小时带宽</td>
</tr>
</tbody></table>

## 操作场景
- 若 EIP 绑定的 CVM 实例发生故障，需快速恢复服务，则可先解绑再重新绑定到健康的 CVM 实例上。 
- 若不再需要 EIP 为云资源提供公网通信服务时，可将云资源与 EIP 解绑。

## 操作步骤
1. 登录 [公网 IP 控制台](https://console.cloud.tencent.com/cvm/eip)。
2. 在公网 IP 页面顶部，选择需要解绑云资源的 EIP 的地域，并在对应 EIP 所在行的操作栏下，单击**更多** > **解绑**。
3. 在弹出的“解绑EIP”窗口中，确认解绑信息，单击**确定**。
> ?
> - NAT 网关至少需绑定一个 EIP，因此，若与 EIP 解绑的云资源为 NAT 网关，且该 EIP 为 NAT 网关绑定的唯一 EIP，则无法解绑。
> - 对于传统账户类型，可以在解绑时勾选**解绑时免费分配普通公网 IP**。
>
![](https://main.qcloudimg.com/raw/1b08a8d041eaf1a22d801ff268b9dd5f.png)
4. 在弹出的提示框中，单击**确定**，即可完成与云资源的解绑。

## 后续步骤
- 若需要为已解绑云资源的 EIP 重新绑定其他云资源，请参见 [EIP 绑定云资源](https://cloud.tencent.com/document/product/1199/41702)。
- 若需要释放处于闲置（未绑定）状态的 EIP，请参见 [释放 EIP](https://cloud.tencent.com/document/product/1199/41704)。
