事件总线作为云上事件传递管道，只进行事件的筛选与路由分发，如果您需要对于事件进行记录或者存储，可以通过配置 **CLS 投递目标**实现。


## 权限说明

为保证日志正常查看，如果您是子账号，至少需要拥有日志服务 CLS 只读权限 `QcloudCLSReadOnlyAccess`。主账号为子账号授权方法请参见 [授权管理](https://cloud.tencent.com/document/product/598/10602)。


## 功能介绍

目前支持**默认日志集投递**与**自定义日志集投递**两种方式：

<dx-tabs>
::: 默认日志集投递
新建投递目标时，如不指定日志投递主题，将会使用默认投递日志能力。默认投递日志时，EB 将会为您开通日志服务，并将函数调用日志投递至 EB 专用日志集下的日志主题中，EB 专用日志集和日志主题分别以 `EB_logset` 和 `EB_logtopic` 为前缀命名，如不存在将自动创建。函数调用日志默认保留30天，您可在 [日志服务控制台](https://console.cloud.tencent.com/cls/logset) 查看及管理。
![](https://main.qcloudimg.com/raw/45cce17af24e5da13b140d2d84ae2d4a.png)

#### 计费说明
日志服务为独立计费产品，2021年10月22日起，EB 专用日志主题将提供独占免费额度，为1GB数据量，30天存储，具体额度如下：
<table>
<thead>
<tr>
<th>计费项</th>
<th>额度/天</th>
</tr>
</thead>
<tbody><tr>
<td>写流量</td>
<td>256MB</td>
</tr>
<tr>
<td>索引流量</td>
<td>1GB</td>
</tr>
<tr>
<td>日志存储</td>
<td>7.5GB</td>
</tr>
<tr>
<td>索引存储</td>
<td>30GB</td>
</tr>
<tr>
<td>分区</td>
<td>1个</td>
</tr>
</tbody></table>
此免费额度为 EB 专用日志主题独享，扣费顺序为<b>全网默认免费额度 > EB 日志集独享免费额度 > 正常按量扣费</b>。
:::
::: 自定义日志集投递
新建投递目标时，如需指定日志投递主题，可选择使用日志自定义投递能力。在使用日志自定义投递能力之前，需保证账号已经开通 [日志服务](https://cloud.tencent.com/product/cls)。
![](https://main.qcloudimg.com/raw/444aff04bb19953334ab5ea50c85eb30.png)

#### 计费说明
日志服务为独立计费产品，绑定自定义日志集后，扣费规则以日志服务侧为准，详情可参见 [日志服务计费详情](https://cloud.tencent.com/document/product/614/45802)。
:::
</dx-tabs>









## 配置说明

1. **查看和管理日志服务**
创建完成后，您可在**事件规则** > **事件目标**下，查看绑定的日志集与日志主题，并单击前往日志服务控制台查看和管理日志。
EB 专用日志集在日志服务控制台已用 EB 字样进行标记，如有事件持久化存储等需求，均可在日志服务控制台完成进一步配置管理。
![](https://main.qcloudimg.com/raw/0f05c49bf231bbe4de8175d0bfd41f18.png)
2. **索引管理**
日志检索依赖日志主题的索引配置，对于默认日志集，EB 会自动为您完成索引配置，目前支持的索引字段如下：
>! 如果您选择自定义日志集，**请保证您的日志集也配置下列索引**，否则可能导致事件投递后无法在日志服务侧查询。
<table>
<thead>
<tr>
<th>字段名称</th>
<th>字段类型</th>
<th>分词符</th>
<th>包含中文</th>
</tr>
</thead>
<tbody><tr>
<td>sourceType</td>
<td>text</td>
<td>无</td>
<td>不包含</td>
</tr>
<tr>
<td>caller</td>
<td>text</td>
<td>无</td>
<td>不包含</td>
</tr>
<tr>
<td>eventbusId</td>
<td>text</td>
<td>无</td>
<td>不包含</td>
</tr>
<tr>
<td>status</td>
<td>text</td>
<td>无</td>
<td>不包含</td>
</tr>
<tr>
<td>specversion</td>
<td>text</td>
<td>无</td>
<td>不包含</td>
</tr>
<tr>
<td>id</td>
<td>text</td>
<td>无</td>
<td>不包含</td>
</tr>
<tr>
<td>type</td>
<td>text</td>
<td>无</td>
<td>不包含</td>
</tr>
<tr>
<td>source</td>
<td>text</td>
<td>无</td>
<td>不包含</td>
</tr>
<tr>
<td>subject</td>
<td>text</td>
<td>无</td>
<td>不包含</td>
</tr>
<tr>
<td>region</td>
<td>text</td>
<td>无</td>
<td>不包含</td>
</tr>
<tr>
<td>datacontenttype</td>
<td>text</td>
<td>无</td>
<td>不包含</td>
</tr>
<tr>
<td>tags</td>
<td>text</td>
<td>无</td>
<td>不包含</td>
</tr>
<tr>
<td>data</td>
<td>text</td>
<td>无</td>
<td>不包含</td>
</tr>
<tr>
<td>time</td>
<td>text</td>
<td>无</td>
<td>不包含</td>
</tr>
</tbody></table>

