若您不再使用弹性公网 IP（EIP），可在控制台将其释放，释放后将不再收取 EIP 的任何费用。

## 前提条件
释放 EIP 前，需要先解绑 EIP，详情请参见 [解绑 EIP](https://cloud.tencent.com/document/product/1199/41703)。

## 费用说明
释放 EIP 后，不同类型账户的费用说明如下：
<table>
<thead>
<tr>
<th width="20%">账户类型</th>
<th width="15%" align="center">计费模式</th>
<th>计费说明</th>
</tr>
</thead>
<tbody><tr>
<td>传统账户类型</td>
<td align="center">-</td>
<td rowspan="2">EIP 不收取任何费用。</td>
</tr>
<tr>
<td rowspan="4">标准账户类型</td>
<td align="center">按流量</a></td>

</tr>
<tr>
<td align="center">包月带宽</a></td>
<td>将 EIP 退还后，将按资源包使用比例退还您的费用，具体步骤请参见 <a href="https://cloud.tencent.com/document/product/1199/43137#33" target="_blank">退还包月带宽 EIP</a>。退还后 EIP 将进入回收状态并保留7天，若期间未进行续费，7天后将自动释放该 EIP。</td>
</tr>
<tr>
<td align="center">按小时带宽</a></td>
<td>EIP 不收取 IP 资源费用，且停止收取公网网络费用。</td>
</tr>
</tbody></table>

## 操作步骤
1. 登录 [公网 IP 控制台](https://console.cloud.tencent.com/cvm/eip)。
2. 在公网 IP 页面顶部，选择需要释放的 EIP 地域，并在对应 EIP 所在行的操作栏下，选择**更多** > **释放**。
3. 在弹出的“确定释放所选EIP?”窗口中，勾选**确定释放以上 IP**，单击**释放**。
> ?找回公网 IP 地址有相应的限制条件，请参见 [使用限制](https://cloud.tencent.com/document/product/1199/41708#.E4.BD.BF.E7.94.A8.E9.99.90.E5.88.B6)，因此 EIP 释放后可能无法找回。
>
![](https://main.qcloudimg.com/raw/9151d8f9623b09ddae25e2e019b7a835.png)

## 后续步骤
- 若需要找回使用过、且当前未分配给其他用户的公网 IP 地址，请参见 [找回公网 IP 地址](https://cloud.tencent.com/document/product/1199/41708)。

