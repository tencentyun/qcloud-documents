本文介绍通过 TDSQL-C MySQL 版控制台创建 Serverless 集群的操作。

## 前提条件
购买前需要实名认证，请参见 [实名认证指引](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤
1. 登录 [购买页](https://buy.cloud.tencent.com/cynosdb?regionId=8)，完成**数据库配置**设置。
<table>
<thead><tr><th width=13%>参数</th><th>说明</th></tr></thead>
<tbody>
<tr>
<td>数据库引擎</td>
<td>选择 MySQL。</td></tr>
<tr>
<td>计算计费模式</td>
<td>选择 Serverless 模式。</td></tr>
<tr>
<td>地域</td>
<td>选择您的数据库部署地域。<dx-alert infotype="explain" title="">
目前 Serverless 仅支持广州、上海、北京、南京地域，如以上地域不满足您的需求，可 [提交工单](https://console.cloud.tencent.com/workorder/category)。
</dx-alert></td></tr>
<tr>
<td>主可用区</td>
<td>选择部署可用区，对应地域下的可用区分布您可以实际购买页为准。</td></tr>
<tr>
<td>多可用区部署</td>
<td>当前 Serverless 实例不支持多可用区部署。</td></tr>
<tr>
<td>网络</td>
<td>出于性能安全考虑，目前仅支持私有网络（VPC），云服务器需要与 TDSQL-C 在同一 <a href="https://cloud.tencent.com/document/product/215">VPC</a> 下方可通信。</td></tr>
<tr>
<td>兼容数据库</td>
<td>支持 MySQL 5.7、8.0。</td></tr>
<tr>
<td>算力配置</td>
<td>选择算力配置 CCU（CynosDB Compute Unit）上下限，实例会根据选择资源范围自动进行弹性扩缩容。<dx-alert infotype="explain" title="">
CCU（CynosDB Compute Unit）为 Serverless 的计算计费单位，一个 CCU 近似等于1个 CPU 和 2GB 内存的计算资源，每个计费周期的 CCU 使用数量为：数据库所使用的 CPU 核数 与 内存大小的1/2 二者中取最大值。算力配置可参考 [产品算力配置](https://cloud.tencent.com/document/product/1003/71887#CYNOSSLPZ)。
</dx-alert></td></tr>
<tr>
<td>自动暂停</td>
<td>配置实例自动暂停时间，在设定时间内无连接访问数据库会自动暂停实例，实例暂停后计算将不再计费。</td></tr>
<tr>
<td>存储计费模式</td>
<td>Serverless 版本默认存储模式为按量计费模式。</td></tr>
</tbody></table>
2. 选择实例数量，Serverless 服务支持批量购买同规格多个实例，然后单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/70e331d8851e9e7698a597ee8eab1df4.png)
3. 完成**基础信息**设置和**高级配置**设置，确认费用后单击**立即购买**。
 - **基础信息**
<table>
<thead><tr><th width=13%>参数</th><th>说明</th></tr></thead>
<tbody><tr>
<td>集群名</td>
<td>可选择创建后命名或立即命名。支持长度小于60的中文、英文、数字、<code>-</code>、<code>_</code>、<code>.</code>。</td></tr>
<tr>
<td>管理员用户名</td>
<td>默认为 root。</td></tr>
<tr>
<td>密码</td>
<td>8 - 64个字符，包含大小写英文字母、数字和符号 <code>~!@#$%^&amp;*_-+=|\(){}[]:;'&lt;&gt;,.?/</code> 中的任意三种。</td></tr>
<tr>
<td>默认字符集</td>
<td>支持 UTF8、GBK、LATIN1、UTF8MB4。</td></tr>
<tr>
<td>自定义端口</td>
<td>默认为3306，支持自定义输入。</td></tr>
</tbody></table>
 - **高级配置**
<table>
<thead><tr><th width=13%>参数</th><th>说明</th></tr></thead>
<tbody><tr>
<td>安全组</td>
<td>选择或新建安全组。</td></tr>
<tr>
<td>参数模板</td>
<td>选择或新建参数模板。</td></tr>
<tr>
<td>表名大小写敏感</td>
<td>可选择为不敏感或敏感。</td></tr>
<tr>
<td>指定项目</td>
<td>为您要新建的集群指定所属项目。</td></tr>
<tr>
<td>告警策略</td>
<td>选择或新建告警策略。</td></tr>
<tr>
<td>标签</td>
<td>添加标签，方便您进行资源分类和管理。</td></tr>
<tr>
<td>协议条款</td>
<td>阅读并勾选协议条款。</td></tr>
</tbody></table>
4. 购买成功后，返回集群列表，待集群状态显示为**运行中**，即可正常使用。

