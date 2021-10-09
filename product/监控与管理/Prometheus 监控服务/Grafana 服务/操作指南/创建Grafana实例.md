本文将指导您如何新建 Grafana 实例。

>?目前处于内测阶段，每个主账号可以申请一个实例。

## 操作步骤

1. 登录 [云监控 Grafana 服务控制台](https://console.cloud.tencent.com/monitor/grafana)。
2. 单击**新建**，根据页面提示，配置以下信息：
<img src = "https://main.qcloudimg.com/raw/54eecac8c024f52947b83ad032c650e6.png">
<table>
<tr>
<th>类别</th>
<th>是否必选</th>
<th>配置说明</th>
</tr>
<tr>
<td>计费模式</td>
<td>是</td>
<td>目前仅支持试用版。</td>
</tr>
<tr>
<td>实例名称</td>
<td>是</td>
<td>用户自定义 Grafana 实例名称。</td>
</tr>
<tr>
<td>可用区域</td>
<td>是</td>
<td>根据您云产品所在区域选择。处于不同地域的云产品内网不通；选择最靠近您客户的地域，可降低访问时延，创建成功后不支持切换地域。</td>
</tr>
<tr>
<td>网络</td>
<td>是</td>
<td>表示在腾讯云上构建的逻辑隔离的网络空间，一个私有网络由至少一个子网组成。系统会为您在每个地域提供的默认私有网络和子网。如现有的私有网络/子网不符合您的要求，可以参考文档 <a href = "https://cloud.tencent.com/document/product/215/36515">新建私有网络</a> 和 <a href = "https://cloud.tencent.com/document/product/215/36517">新建子网</a> 进行创建。</td>
</tr>
<tr>
<td>用户名</td>
<td>是</td>
<td>默认为：admin 。暂不支持更改。</td>
</tr>
<tr>
<td>密码</td>
<td>是</td>
<td>定义 Grafana 登录密码。密码长度为8到16位，且需要至少包含大写字母、小写字母、数字和符号（如-!@#$%^&*+=_;:.?）四类中的其中三类。</td>
</tr>
<tr>
<td>外网访问</td>
<td>是</td>
<td>定义是否允许外网访问 Grafana 。</td>
</tr>
<tr>
<td>标签	</td>
<td>否</td>
<td>设置标签之后可以用于从不同维度对资源分类管理。具体可参考 <a href = "https://cloud.tencent.com/document/product/213/19548">标签说明</a>。</td>
</tr>
</table>

3.填写完成后，单击**立即购买**即可。