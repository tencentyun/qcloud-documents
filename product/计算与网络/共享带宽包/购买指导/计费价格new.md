本文为您介绍不同带宽类型的共享带宽包的计费价格。

## 带宽类型
共享带宽包按照带宽类型，可分为如下类型的带宽包：
<table>
<tr><th width="30%">带宽类型</th><th>说明</th></tr>
<tr><td><a href="#bgp">常规 BGP 带宽包</a></td><td>普通 BGP IP 线路类型的带宽包。可手动创建。</td></tr>
<tr><td><a href="#cn2">精品 BGP 带宽包</a></td><td>使用专属线路的精品 BGP IP 线路类型的带宽包。可手动创建。</td></tr>
<tr><td><a href="#anycast">Anycast 加速 BGP 带宽包</a></td><td>采用 Anycast 加速 BGP IP 线路类型的带宽包。自动创建，不支持手动创建。</td></tr>
<tr><td><a href="#singleip">移动/联通/电信带宽包</a></td><td>通过单个网络运营商访问公网，静态单线 IP 线路类型的带宽包。自动创建，不支持手动创建。

<dx-alert infotype="explain" title="">
自2022年06月01日00时00分起，静态单线 IP（移动/电信/联通共享带宽包）将支持按天结算，如有疑问请咨询<a href="https://cloud.tencent.com/online-service">  在线支持</a>，给您带来不便，敬请谅解。
</dx-alert>


</td></tr>
</table>

## [常规 BGP 带宽包](id:bgp)
>? 目前仅标准账户类型支持预付费带宽包，传统账户类型需升级后才能使用，升级详情请参见  [账户类型升级说明](https://cloud.tencent.com/document/product/1199/49090#judge)。
### 预付费带宽包
<table>
<thead>
<tr>
<th align="left">地域</th>
<th align="left" width="35%">单价（元/Mbps/月）</th>
</tr>
</thead>
<tbody><tr>
<td align="left">中国大陆
</td>
<td align="left">80</td>
</tr>
<tr>
<td align="left">东京、新加坡、曼谷、雅加达、孟买、法兰克福
</td>
<td align="left">80</td>
</tr>
<tr>
<td align="left">硅谷、弗吉尼亚
</td>
<td align="left">90</td>
</tr>
<tr>
<td align="left">中国香港、中国台北、首尔、莫斯科、圣保罗、多伦多
</td>
<td align="left">100</td>
</tr>
</tbody></table>

### 后付费带宽包
<table>
<thead>
<tr>
<th align="left">地域</th>
<th align="left" width="35%">单价（元/Mbps/月）</th>
</tr>
</thead>
<tbody><tr>
<td align="left">除圣保罗以外的其他地域
</td>
<td align="left">108</td>
</tr>
<tr>
<td align="left">圣保罗
</td>
<td align="left">138</td>
</tr>
</tbody></table>

## [精品 BGP 带宽包](id:cn2)
>?
>- 目前仅标准账户类型支持精品 BGP 带宽包，传统账户类型需升级后才能使用，升级详情请参见 [账户类型升级说明](https://cloud.tencent.com/document/product/1199/49090)。如需体验，请提交 [内测申请](https://cloud.tencent.com/apply/p/224jt7718s8)。
>- 仅中国香港地域支持精品 BGP IP。
>

### 预付费带宽包
<table>
<thead>
<tr>
<th align="left">地域</th>
<th align="left" width="35%">单价（元/Mbps/月）</th>
</tr>
</thead>
<tbody><tr>
<td align="left">中国香港
</td>
<td align="left">380</td>
</tr>
</tbody></table>

### 后付费带宽包
<table>
<thead>
<tr>
<th align="left">地域</th>
<th align="left" width="35%">单价（元/Mbps/月）</th>
</tr>
</thead>
<tbody><tr>
<td align="left">中国香港
</td>
<td align="left">580</td>
</tr>
</tbody></table>

## [Anycast 加速 BGP 带宽包](id:anycast)
>?计费详情请参见 [Anycast 公网加速购买指南](https://cloud.tencent.com/document/product/644/12617)。
<table>
<tr>
<th align="left"rowspan="2">Anycast EIP 所属地域</th>
<th align="left" width="35%" colspan="4">加速地域（单价：元/Mbps/月）</th>
</tr>
<tr>
<td align="left">亚太</td>
<td align="left">欧洲</td>
<td align="left">北美</td>
<td align="left">南美</td>
</tr>
<tr>
<td align="left">亚太（中国香港、新加坡、曼谷、孟买、首尔、东京）</td>
<td align="left">108</td>
<td align="left">108</td>
<td align="left">108</td>
<td align="left">288</td>
</tr>
<tr>
<td align="left">欧洲（法兰克福、莫斯科）</td>
<td align="left">108</td>
<td align="left">108</td>
<td align="left">108</td>
<td align="left">168</td>
</tr>
<tr>
<td align="left">北美（硅谷）</td>
<td align="left">108</td>
<td align="left">108</td>
<td align="left">108</td>
<td align="left">168</td>
</tr>
<tr>
<td align="left">南美（圣保罗）</td>
<td align="left">288</td>
<td align="left">168</td>
<td align="left">168</td>
<td align="left">138</td>
</tr>
</table>

## [移动/联通/电信带宽包](id:singleip)
>?
>- 自2022年06月01日00时00分起，静态单线 IP（电信/联通/移动共享带宽包）将支持按天结算，如有疑问请咨询[ 在线支持](https://cloud.tencent.com/online-service)，给您带来不便，敬请谅解。
>- 目前仅广州、上海、南京、济南、杭州、福州、北京、石家庄、武汉、长沙、成都、重庆地域支持静态单线 IP 线路类型，其他地域支持情况请以控制台页面为准。
>- 该功能处于内测阶段，如需体验，请提交[ 内测申请](https://cloud.tencent.com/apply/p/6nzb3jwbsk)。广州、上海、南京、北京、成都、重庆地域暂未开放申请，如需使用，请联系您的商务经理。
>- 按月结算计费方式仅限月消费大于10万元的客户申请，可联系您的商务经理开通，或提 [工单申请](https://console.cloud.tencent.com/workorder/category)。
>

### 按日结算[](id:arjs)
<table>
<tr>
<th>地域</th><th>移动带宽包价格<br/>（单位：元/Mbps/天）</th><th>联通带宽包价格<br/>（单位：元/Mbps/天）</th><th>电信带宽包价格<br/>（单位：元/Mbps/天）</th>
</tr>
<tr>
<td>广州、上海、北京</td><td>1.8</td><td>2.2</td><td>2.2</td>
</tr>
<tr>
<td>成都</td><td>1.6</td><td>1.8</td><td>1.8</td>
</tr>
<tr>
<td>重庆</td><td>1.6</td><td>1.2</td><td>1.2</td>
</tr>
<tr>
<td>南京、济南</td><td>0.9</td><td>1.2</td><td>1.2</td>
</tr>
<tr>
<td>杭州</td><td>0.9</td><td>1.2</td><td>2.2</td>
</tr>
<tr>
<td>福州、石家庄、武汉、长沙</td><td>0.9</td><td>1.2</td><td>1.2</td>
</tr>
</table>

### 按月结算

<table>
<tr>
<th>地域</th><th>移动带宽包价格<br/>（单位：元/Mbps/月）</th><th>联通带宽包价格<br/>（单位：元/Mbps/月）</th><th>电信带宽包价格<br/>（单位：元/Mbps/月）</th>
</tr>
<tr>
<td>广州、上海</td><td>47</td><td>47</td><td>47</td>
</tr>
<tr>
<td>北京</td><td>44</td><td>44</td><td>44</td>
</tr>
<tr>
<td>成都</td><td>45</td><td>45</td><td>45</td>
</tr>
<tr>
<td>重庆</td><td>26</td><td>26</td><td>26</td>
</tr>
<tr>
<td>南京</td><td>22</td><td>25</td><td>23</td>
</tr>
<tr>
<td>济南</td><td>19</td><td>17</td><td>18</td>
</tr>
<tr>
<td>杭州</td><td>20</td><td>29</td><td>40</td>
</tr>
<tr>
<td>福州</td><td>10</td><td>19</td><td>21</td>
</tr>
<tr>
<td>石家庄</td><td>15</td><td>25</td><td>25</td>
</tr>
<tr>
<td>武汉</td><td>14</td><td>19</td><td>21</td>
</tr>
<tr>
<td>长沙</td><td>15</td><td>25</td><td>25</td>
</tr>
</table>


## 相关文档
[计费模式](https://cloud.tencent.com/document/product/684/51876)
