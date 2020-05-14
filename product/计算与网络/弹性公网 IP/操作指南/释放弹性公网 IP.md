若您不再需要使用弹性公网 IP（EIP），可在控制台将其释放，释放后将不再收取 EIP 的任何费用。

## 费用说明
释放 EIP 后，不同类型账户下的费用说明如下：
<table>
<thead>
<tr>
<th width="20%">账户类型</th>
<th width="15%" align="center">计费模式</th>
<th>计费说明</th>
</tr>
</thead>
<tbody><tr>
<td>非带宽上移账户</td>
<td align="center">-</td>
<td>EIP 不收取任何费用。</td>
</tr>
<tr>
<td rowspan="3">带宽上移账户</td>
<td align="center"><a href="https://cloud.tencent.com/document/product/1199/41692#1" target="_blank">按流量</a></td>
<td>EIP 不收取任何费用。</td>
</tr>
<tr>
<td align="center"><a href="https://cloud.tencent.com/document/product/1199/41692#2" target="_blank">按小时带宽</a></td>
<td>EIP 不收取 IP 资源费用，且停止收取公网网络费用。</td>
</tr>
<tr>
<td align="center"><a href="https://cloud.tencent.com/document/product/1199/41692#3" target="_blank">包月带宽</a></td>
<td>将 EIP 退还后，将按资源包使用比例退还您的费用，具体步骤请参见 <a href="https://cloud.tencent.com/document/product/1199/43137#33" target="_blank">退还包月带宽 EIP</a>。退还后 EIP 将进入回收状态并保留7天，若期间未进行续费，7天后将自动释放该 EIP。</td>
</tr>
</tbody></table>

## 操作步骤

1. 登录 [EIP 控制台](https://console.cloud.tencent.com/cvm/eip)。
2. 在 EIP 管理页面，选择需要释放的 EIP 地域，并在对应 EIP 所在行的操作栏下，选择【更多】>【释放】。
3. 在弹出的“确定释放所选EIP”窗口中，勾选【确定释放以上IP】，单击【释放】。
![](https://main.qcloudimg.com/raw/23eac37af5e7368b9429fac24c9686ee.png)

## 后续步骤
- 若需要找回使用过、且当前未分配给其他用户的公网 IP 地址，请参见 [找回公网 IP 地址](https://cloud.tencent.com/document/product/1199/41708)。

