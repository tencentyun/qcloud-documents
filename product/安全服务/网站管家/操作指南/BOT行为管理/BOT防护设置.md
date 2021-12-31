## 功能简介
通过 BOT 防护配置，用户可以根据 BOT 会话行为特征设置 BOT 对抗策略，对 BOT 行为进行动作处理，并结合 BOT 详情进行观察和分析，根据详情提供的会话状态信息进行精细化策略设置，保护网站核心接口和业务的安全。BOT 防护设置支持公开类型和自定义会话策略两大类防护策略。
### 公开类型
WAF 提供12个已知公开的 BOT 大类，超过1000+的 BOT 子类，包括搜索引擎、测速工具、内容聚合、扫描和网页爬虫等类别。用户可以根据自身需求对公开 BOT 类别设置防护动作（放行、监控、拦截），WAF 将对命中公开类型的 BOT 请求进行相应处理。
### 自定义会话策略
WAF 自定义会话策略提供协议特征、IP 情报特征和自定义会话特征三种类型特征，每种类型特征包含多个判定维度，用户可以根据业务实际情况和 BOT 详情信息，设置自定义会话策略和处理动作（放行、监控、验证码、重定向和拦截），WAF 将命中的自定义防护策略的 BOT 请求进行相应处理。
>!
>- 只有 WAF 企业版和旗舰版支持 BOT 行为管理，高级版用户建议升级到企业版或旗舰版。
>- BOT 会话：统计 IP 到域名的访问请求，会话之间每个请求最长间隔为20分钟，若超过20分钟则记录为一个新会话。

## 使用说明
### BOT 功能开关
登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/bot2/config)，在左侧导航栏中，选择【BOT 行为管理】>【BOT 防护设置】，进入 BOT 策略设置页面。
![](https://main.qcloudimg.com/raw/078750ac49ea99153f3f81461f8611b4.png)
**字段说明：**
- **域名：**同步【Web 应用防火墙】>【[防护配置](https://console.cloud.tencent.com/guanjia/waf/config)】添加到 WAF 的防护域名，且支持排序。
- **BOT 流量分析开关：**默认关闭，可以根据需要开启.
>!当且仅当域名 WAF 开关为开启时，BOT 流量分析功能生效。
- **WAF 开关：**同步【Web 应用防火墙】>【[防护配置](https://console.cloud.tencent.com/guanjia/waf/config)】域名防护列表的开关状态。
- **操作：**单击【防护设置】，设置 BOT 防护策略。

### 公开类型设置
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/bot2/config)，在左侧导航栏中，选择【BOT 行为管理】>【BOT 防护设置】，找到需要操作的域名，在右侧操作栏，单击【防护设置】。
2. 进入防护设置页面，单击【公开类型】，进入相应列表页。
![](https://main.qcloudimg.com/raw/6edeebf8857429080854621877506d76.png)
**参数说明：**
	- **BOT 分类：**WAF 支持12个公开类别识别，如搜索引擎、测速工具、内容聚合、扫描和网页爬虫等。
	- **BOT 种类数：**每个分类包含的 BOT 种类数量。
	- **动作：**公开类型支持的动作类型，默认为监控，支持设置为放行或拦截，可通过右侧操作栏进行设置。拦截结果可在【[攻击日志](https://console.cloud.tencent.com/guanjia/tea-attacklog)】中查看，拦截 IP 的实时信息可在【[IP 封堵状态](https://console.cloud.tencent.com/guanjia/ip/record)】中查看。
	- **操作：**进行公开类型的动作设置，详情请参见 [动作类型说明](#dzlx)。
3. 在页面左上角，单击【复制】，可将当前域名的公开类型 BOT 设置信息复制到其他域名，其他域名的公开类型 BOT 设置信息将会被覆盖。
![](https://main.qcloudimg.com/raw/10b603c0a8050db3005feb8ead2a20ac.png)

### 自定义会话策略
#### 协议特征
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/bot2/config)，在左侧导航栏中，选择【BOT 行为管理】>【BOT 防护设置】，找到需要操作的域名，在右侧操作栏，单击【防护设置】。
2. 进入防护设置页面，选择【自定义会话策略】>【协议特征】，进入相应列表页。
![](https://main.qcloudimg.com/raw/d9779127d93f5c8b1640d68a436c72ad.png)
	- **字段说明：**
		- **策略名称：**协议特征字段。
		- **动作：**协议特征策略默认动作，默认为监控，可通过右侧操作栏进行设置。
		- **策略开关：**默认为关闭。
		- **修改时间：**策略最近一次被修改的时间。
		- **操作：**单击【编辑】进行动作设置，动作支持放行、监控、验证和拦截，详情请参见 [动作类型说明](#dzlx)。动作设置后，拦截结果可在【[攻击日志](https://console.cloud.tencent.com/guanjia/tea-attacklog)】中查看，拦截 IP 的实时信息可在【[IP 封堵状态](https://console.cloud.tencent.com/guanjia/ip/record)】中查看。
	- **协议特征策略名称如下：**
<table>
<tr><th>协议特征类别</th><th>策略名称</th></tr>
<tr><td rowspan="7">User-Agent 类别</td><td>User-Agent 为空或不存在。</td></tr>
<tr><td>User-Agent 类别为 BOT。</td></tr>
<tr><td>User-Agent 类别为 Unknown BOT。</td></tr>
<tr><td>User-Agent 类别为 HTTP Library。</td></tr>
<tr><td>User-Agent 类别为 Tools。</td></tr>
<tr><td>User-Agent 类别为 Framework。</td></tr>
<tr><td>User-Agent 类别为 Scanner。</td></tr>
<tr><td rowspan="8">HTTP 头部</td><td>Referer 为空或不存在.</td></tr>
<tr><td>Referer 滥用(多个 UA 使用相同 Referer)。</td></tr>
<tr><td>Cookie 滥用(多个 UA 使用相同 Cookie)。</td></tr>
<tr><td>Cookie 为空或不存在。</td></tr>
<tr><td>Connection 为空或不存在。</td></tr>
<tr><td>Accept 为空或不存在。</td></tr>
<tr><td>Accept-Language 为空或不存在。</td></tr>
<tr><td>Accept-Enconding 为空或不存在。</td></tr>
<tr><td rowspan="2">HTTP 协议特征</td><td>使用 HTTP HEAD 方法</td></tr>
<tr><td>HTTP 协议版本为1.0或者更低。</td></tr>
</table>

#### IP 情报特征
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/bot2/config)，在左侧导航栏中，选择【BOT行为管理】>【BOT防护设置】，找到需要操作的域名，在右侧操作栏，单击【防护设置】。
2. 进入防护设置页面，选择【自定义会话策略】>【IP 情报特征】，进入相应列表页。
![](https://main.qcloudimg.com/raw/aca75a58890ae8efc4a7c79bf5a10dd4.png)
	- **字段说明：**
		- **策略名称：**IP 情报策略字段名称。
		- **动作：**情报特征策略默认动作，默认为监控，可通过右侧操作栏进行设置。
		- **策略开关：**默认为关闭，其中腾讯云 WAF 用于检查客户域名健康状态的拨测服务，建议保持开启。
		- **修改时间：**策略最近一次被修改的时间。
		- **操作：**单击【编辑】进行动作设置，动作支持放行、监控、验证码和拦截，详情请参见 [动作类型说明](#dzlx)。
>!用于检查客户域名健康状态的拨测服务，请勿设置为拦截。
	- **IP 情报特征策略名称如下：**
<table>
<tr><th>情报特征类别</th><th>情报策略名称</th></tr>
<tr><td >拨测</td><td>腾讯云 WAF 拨测。</td></tr>
<tr><td rowspan="11">IDC-IP 库</td><td>IDC-IP 库  腾讯云。</td></tr>
<tr><td>IDC-IP 库  阿里云。</td></tr>
<tr><td>IDC-IP 库  华为云。</td></tr>
<tr><td>IDC-IP 库  金山云。</td></tr>
<tr><td>IDC-IP 库  Ucloud。</td></tr>
<tr><td>IDC-IP 库  百度云。</td></tr>
<tr><td>IDC-IP 库  京东云。</td></tr>
<tr><td>IDC-IP 库  青云。</td></tr>
<tr><td>IDC-IP 库  AWS。</td></tr>
<tr><td>IDC-IP 库  Azure。</td></tr>
<tr><td>IDC-IP 库  Google。</td></tr>
</table>

#### 自定义会话特征
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/bot2/config)，在左侧导航栏中，选择【BOT行为管理】>【BOT防护设置】，找到需要操作的域名，在右侧操作栏，单击【防护设置】。
2. 进入防护设置页面，选择【自定义会话策略】>【自定义会话特征】，进入相应列表页。
![](https://main.qcloudimg.com/raw/1453fca7d60c9922a5eea34b4f93264a.png)
	- **字段说明：**
		- **序号：**策略自增序号。
		- **策略名称/描述：**策略名称和描述信息。
		- **匹配条件：**策略匹配条件内容，1条策略最多可以添加10个匹配条件，匹配条件之间是“与”的关系。
		- **动作：**策略动作信息，展示添加策略时设置的动作信息，可通过右侧操作栏进行设置。
		- **策略开关：**展示添加策略时设置的开关状态信息。
		- **修改时间：**最近一次添加或修改策略的时间。
		- **操作：**对策略进行编辑或删除操作。单击【编辑】进行动作设置，动作支持放行、监控、验证码、重定向和拦截，详情请参见 [动作类型说明](#dzlx)。
3. 添加自定义会话特征，在列表左上方单击【添加】，进入自定义会话特征界面。
![](https://main.qcloudimg.com/raw/6cc9181fb5f37b66c1d0f5aa8fb0da66.png)
>?策略优先级按照数字大小生效，数字越小，代表这条规则的执行优先级越高。优先级默认为100，相同优先级下，创建时间越晚，优先级越高。
>
	- **字段说明：**
		- **策略名称：**策略名称字段。
		- **策略描述：**策略描述字段。
		- **策略开关：**策略开关状态，默认开启。
		- **匹配条件：**设置 BOT 策略的匹配条件，最多可以设置10个匹配条件，各个条件之间是“与”的关系。鼠标悬停具体的匹配条件时，可以查看相应的条件说明。
		- **执行动作：**设置执行动作。
	- [**动作类型说明：**](id:dzlx)
	<table>
<tr><th  >动作类型</th><th>说明</th></tr>
<tr><td>放行</td><td>符合匹配条件的会话请求将被放行，放行不记录日志。</td></tr>
<tr><td>监控</td><td>符合匹配条件的会话请求将会被监控记录日志，可在 BOT 详情的自定义类型中查看监控的会话信息。</td></tr>
<tr><td>验证码</td><td>仅用于浏览器访问场景，符合匹配条件的会话请求将进行验证码挑战，若挑战失败，执行拦截动作。若挑战成功，惩罚时长内正常访问。</td></tr>
<tr><td>重定向</td><td>符合匹配条件的会话请求执行重定向，并且指定惩罚时长，将请求重定向到指定 URL，但只支持重定向到当前域名下的 URL。</td></tr>
<tr><td>拦截</td><td>符合匹配条件的会话请求将执行拦截，可设置惩罚时长，取值为：5分钟 - 10080分钟（7天），拦截结果可在【<a href = "https://console.cloud.tencent.com/guanjia/tea-attacklog">攻击日志</a>】中查看，拦截 IP 的实时信息可在【<a href = "https://console.cloud.tencent.com/guanjia/ip/record">IP 封堵状态</a>】中查看。</td></tr>
</table>
	- **自定义会话特征匹配条件说明如下：**
	<table>
<tr><th width=100px>分类</th><th width=150px>过滤条件</th><th>条件说明</th></tr>
<tr><td rowspan="6">会话特征</td><td>会话平均速度</td><td> 为会话请求总次数 / 会话持续时间，单位为：次/分钟。</td></tr>
<tr><td>会话窗口速度</td><td>每2分钟（窗口）内的会话访问速度，单位为：次/分钟。</td></tr>
<tr><td>会话总次数</td><td>一个 BOT 会话发生的总访问次数。</td></tr>
<tr><td>会话持续时间</td><td>BOT 会话的持续时间。</td></tr>
<tr><td>会话存在 Robots.txt</td><td>会话请求中访问 Robots.txt 文件。</td></tr>
<tr><td>会话发生在凌晨</td><td>会话请求发生在凌晨2:00 - 5:00之间。</td></tr>
<tr><td rowspan="3">IP 特征</td><td>访问源 IP</td><td>访问源 IP。</td></tr>
<tr><td>IP 类型</td><td>IP 的类型信息，类型为 IDC 或基站(运营商基站)，当 IP 为 IDC 类型时疑似存在异常。</td></tr>
<tr><td>IP 所有者</td><td>IP 所有者信息，例如 tencent.com，可以在 BOT 详情中查看，当 IP 类型为 IDC 时有效。</td></tr>
<tr><td rowspan="5">请求特征</td><td>请求最多的 URL</td><td>会话请求中，请求最多的 URL。</td></tr>
<tr><td>URL 重复比</td><td>会话请求中 URL 重复比例，取值范围0 - 1，根据实际业务情况，进行参数配置，过高或过低为疑似异常（根据实际情况进行判断）。</td></tr>
<tr><td>URL 种类</td><td>会话请求中 URL 去重后条目数。</td></tr>
<tr><td>请求最多的参数</td><td>会话请求出现最多的参数，包括 GET 请求参数（Query 内容）或 POST 请求参数（Body 内容）。</td></tr>
<tr><td>参数重复比</td><td>会话请求中 GET 请求参数（Query 内容）或 POST 请求参数（Body 内容）重复比例，取值范围0 - 1，根据实际业务情况，进行参数配置，过高或过低疑似异常（根据实际情况进行判断）。</td></tr>
<tr><td rowspan="6">COOKIE</td><td>COOKIE 存在性</td><td>会话请求中，判断 HTTP 头部字段是否存在 COOKIE。</td></tr>
<tr><td>请求最多的 COOKIE</td><td>会话请求中， 出现最多的 COOKIE。</td></tr>
<tr><td>COOKIE 重复比</td><td>会话请求中 COOKIE 的重复比例，取值范围0 - 1。</td></tr>
<tr><td>COOKIE 存在比</td><td>会话请求中 COOKIE 存在比例，取值范围0 - 1。</td></tr>
<tr><td>COOKIE 滥用</td><td>多种不同的 UA 使用相同的 COOKIE。</td></tr>
<tr><td>COOKIE 种类</td><td>会话请求中 COOKIE 去重后的数目。</td></tr>
<tr><td rowspan="6">Referer</td><td>Referer 存在性</td><td>会话请求中，判断 HTTP 头部字段是否存在 Referer。</td></tr>
<tr><td>请求最多的 Referer</td><td>会话请求中，HTTP Referer 字段出现最多的值。</td></tr>
<tr><td>Referer 重复比</td><td>会话请求中 Referer 的重复比例，取值范围0 - 1，对浏览器访问有效，过高疑似异常（根据实际情况进行判断）。</td></tr>
<tr><td>Referer 存在比</td><td>会话请求中 Referer 存在比例，取值范围0 - 1，对浏览器访问有效，过低疑似异常（根据实际情况进行判断）。</td></tr>
<tr><td>Referer 滥用</td><td>多种不同的 UA 使用相同的 Referer。</td></tr>
<tr><td>Referer 种类</td><td>会话请求中 Referer 去重后的数目。</td></tr>
<tr><td rowspan="6">UA</td><td>UA存在性</td><td>会话请求中，判断 HTTP 头部字段是否存在 User-Agent。</td></tr>
<tr><td>请求最多的 UA</td><td>会话请求中，HTTP User-Agent 字段出现最多的值。</td></tr>
<tr><td>UA 存在比</td><td>会话请求中 UA 的存在比例，取值范围0 - 1，过低疑似异常（根据实际情况进行判断）。</td></tr>
<tr><td>UA 种类</td><td>会话请求中 UA 去重后的数目，过多疑似异常（根据实际情况进行判断），对非代理 IP 有效。</td></tr>
<tr><td>UA 类型</td><td><ul><li>UA 类型为浏览器。</li>
<li>UA 类型为移动端。</li>
<li>UA 类型游戏终端或电视终端。</li>
<li>UA 类别为公开 BOT 类型。</li>
<li>UA 类别为未公开 BOT 类型。</li>
<li>UA 类别为自动化工具。</li>
<li>UA 类别为未知类型。</li>
<li>UA 类别为公开扫描器。</li>
<li>UA 类别为开发框架。</li>
<li>UA 类别为语言 HTTP 库。</li><ul></td></tr>
<tr><td>UA 随机性指数 </td><td>会话请求中 UA 的随机分布情况，取值范围0  -1，指数越高越异常。<br>参考值阈值：超过0.6疑似异常，指数超过0.92基本确定为异常。</td></tr>
<tr><td rowspan="7">其他 HTTP 头部</td><td>Accept 存在性</td><td>会话请求中判断 HTTP 头部字段是否存在 Accept 字段。</td></tr>
<tr><td>Accept-Language 存在性</td><td>会话请求中判断 HTTP 头部字段是否存在 Accept-Language 字段。
</td></tr>
<tr><td>Accept-Encoding 存在性</td><td>会话请求中判断 HTTP 头部字段是否存在 Accept-Encoding 字段。</td></tr>
<tr><td>Connectiton 存在性</td><td>会话请求中判断 HTTP 头部字段是否存在 Connectiton 字段。</td></tr>
<tr><td>请求方法占比 </td><td>会话请求中判断请求使用方法。</td></tr>
<tr><td>HTTP 协议版本占比</td><td>会话请求中判断请求使用的 HTTP 协议版本比例。
</td></tr>
<tr><td>返回状态码比例</td><td>会话请中 WAF 返回给客户状态码比例。
</td></tr>
<tr><td rowspan="7">高级特征</td><td>预测标签</td><td>算法自动预测的疑似行为，不一定所有会话都有预测值，预测标签可能结果如下：
<ul><li>疑似无规律爬虫。</li>
<li>疑似规律性爬虫。</li>
<li>疑似登录行为，缺失用户值。</li>
<li>疑似登录行为，缺失用户参数。</li>
<li>疑似登录行为，缺失用户和密码。</li>
<li>疑似登录行为，缺失登录动作。</li>
<li>疑似暴力破解。</li>
<li>疑似撞库攻击。</li>
<li>疑似刷短信接口。</li> 
<li>疑似刷验证码接口。</li> 
<li>疑似恶意注册。</li> 
<li>疑似接口重复访问。</li> </ul></td></tr>
<tr><td>BOT 得分</td><td>BOT 智能分析引擎对会话给出的 BOT 得分，得分越高判定为 BOT 可能性越大，参考值为5。</td></tr>
<tr><td>AI 模型检出</td><td>AI 行为分析模型检测结果，结果为 AI 模型检出时，疑似异常。</td></tr>
<tr><td>公开 BOT 伪造</td><td>会话请求伪造为公开 BOT 类型，例如，使用百度爬虫的 UA，但 IP 不是百度的 IP。</td></tr>
<tr><td>敏感接口访问</td><td>判断是否对敏感接口（如短信接口、注册接口、登录接口等）进行访问。</td></tr>
<tr><td>时序行为异常指数</td><td>一种时序行为异常检测算法，指数越小越异常。<br>参考值阈值：小于0.5疑似异常，小于0.24基本确定为异常。</td></tr>
<tr><td>时序熵异常指数</td><td>一种时序行为熵检测算法，指数越小越异常。参考值阈值为0.5 ，小于0.5疑似异常。</td></tr>
</table>
