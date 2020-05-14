<head><link rel="stylesheet" href="https://doc-archer-1255486055.cos.ap-nanjing.myqcloud.com/archer.css"></head>
弹性公网 IP（EIP）是可以独立购买和持有的公网 IP 地址资源，您可根据如下操作申请 EIP。

## 操作步骤
1. 登录 [EIP 控制台](https://console.cloud.tencent.com/cvm/eip)。
2. 在 EIP 管理页面，选择【地域】，单击【申请】。
3. 在弹出的“申请EIP”窗口中，请按照您的账户类型，分别进行如下操作：
>? 若您无法确定账户类型，请参见 [如何判断账户类型](https://cloud.tencent.com/document/product/1199/41692#judge)。
>
<div class="codetab">
 <input type="radio" name="tabs3" id="tab31" class="tab-switch" checked="">
<label for="tab31" class="tab-label">非带宽上移账户</label>
<input type="radio" name="tabs3" id="tab32" class="tab-switch">
 <label for="tab32" class="tab-label">带宽上移账户</label>
<div id="tab-content31" class="tab-content" style="padding:0 10px;">
<p><ul>
<li>IP 地址类型：请选择常规 IP。</li>
<li>数量：请按需选择申请的数量且确保 EIP 总数未超过产品总配额，详情请参见 <a href="https://cloud.tencent.com/document/product/1199/41648?!#.E9.85.8D.E9.A2.9D.E9.99.90.E5.88.B6">配额限制</a>。</li>
<li>标签：如需添加标签可在此进行添加，可通过标签进行权限管理。</li>
</ul></p>
</div>
 <div id="tab-content32" class="tab-content" style="padding:0 10px;">
<p><ul>
<li>IP 地址类型：请选择常规 IP。</li>
<li>计费模式：支持按流量、包月带宽、按小时带宽三种计费模式，详情请参见 <a href="https://cloud.tencent.com/document/product/1199/41692#net">公网网络计费</a>。	</li>
<li>带宽上限：请按需设置带宽上限，合理分配带宽资源。</li>
<li>包月时长：该选项仅适用计费模式为包月带宽的 EIP，请按需选择包月带宽的购买时长。</li>
<li>自动续费：该选项仅适用计费模式为包月带宽的 EIP，若勾选此选项，账户余额足够时，EIP 到期后将按月自动续费。</li>
<li>数量：请按需选择申请的数量且确保 EIP 总数未超过产品总配额，详情请参见 <a href="https://cloud.tencent.com/document/product/1199/41648?!#.E9.85.8D.E9.A2.9D.E9.99.90.E5.88.B6">配额限制</a>。</li>
<li>标签：如需添加标签可在此进行添加，可通过标签进行权限管理。</li>
</ul>
</p></div>
</div>
4. 单击【确定】，完成 EIP 的申请。
5. 在列表中，即可查看已申请的 EIP，此时处于未绑定状态。
>?建议您及时为处于未绑定状态的 EIP 绑定云资源，保障 IP 资源的合理利用，节省 IP 资源费，IP 资源费按小时计费，精确到秒级，不足一小时，按闲置时间占比收取费用。
>
![](https://main.qcloudimg.com/raw/9492216f61d10704015dac0cf217bd01.png)

## 后续步骤
- 若需要为 EIP 绑定云资源，请参见 [EIP 绑定云资源](https://cloud.tencent.com/document/product/1199/41702)。
