

您可以在域名管理页面，对域名的防护策略进行修改。

## 应用场景

融合腾讯云 Web 防火墙 AI+规则的 Bot 爬虫防护功能，面向全量加速请求进行行为分析，对友好及恶意的 Bot 爬虫进行甄别，支持自定义策略管理。

## 防护配置
购买 BOT 防护功能的用户，可登录 SCDN 控制台，进入 BOT 防护管理**防护配置**页面，开启/关闭 BOT 防护。
![](https://main.qcloudimg.com/raw/67676c436c3ba06f00af16919848ace7.jpg)

### 公开类型策略配置

SCDN ⽬前提供12个已知公开的 BOT ⼤类，超过1000+的 BOT ⼦类，包括搜索引擎、测速⼯具、内容聚合、扫描和⽹⻚爬⾍等类别。⽤户可以根据⾃身需求对公开 BOT 类别设置防护动作（放⾏、监控、拦截），防护引擎将对命中公开类型的 BOT 请求进⾏相应处理。进入 **BOT 爬虫防护** > **公开类型**页面，默认展示 BOT **公开类型**列表，页面操作说明如下：

- 单击**设为监控**：若访问域名出现该 BOT 行为将触发 BOT 监控。
- 单击**设为拦截**：若访问域名出现该 BOT 行为将触发 BOT 拦截。
![](https://main.qcloudimg.com/raw/2fcafb6d30907b70ae4301cb519e66c3.jpg)
- 单击**复制**：可以将当前域名的公开类型 BOT 设置信息复制到其他开启了 BOT 防护的域名，最多可选20个域名。
![](https://main.qcloudimg.com/raw/ca320efc0c3885bd919f532ceea71b27.jpg)

### 协议特征策略配置

安全加速支持17种协议特征 BOT 防护规则配置。
![](https://main.qcloudimg.com/raw/981b6f76ed5127037449cc209082f0d0.jpg)
**策略分类**：分为 User-Agent 类别、HTTP 头部、HTTP 协议特征。
**执行动作**：协议特征策略开启时默认动作为“放行”，可通过右侧操作栏进行设置为“拦截”或者“监控”。
**策略开关**：默认为关闭。您可根据业务需求开启单项协议特征策略。

### 自定义会话规则配置

安全加速支持用户可自定义配置BOT会话特征规则，进入**自定义会话规则**页面。
![](https://main.qcloudimg.com/raw/a4f94e47abf82eac7420b56e95141e34.jpg)
**策略名称**：策略名称和描述信息。
**匹配条件**：策略匹配条件内容，1条策略最多可以添加10个匹配条件，匹配条件之间是“与”的关系。
**执行动作**：策略动作信息，展示添加策略时设置的动作信息，可通过右侧操作栏进行修改。
**操作**：对策略进行编辑或删除操作。单击**编辑**可进行规则内容修改。
**策略开关**：展示添加策略时设置的开关状态信息。
**批量操作**：支持批量编辑自定义会话特征（如，统一修改执行动作、复制到其他已开启 BOT 防护的域名等）。

![](https://main.qcloudimg.com/raw/fa4a1245a0444d59322b7e2b61152775.jpg)
单击【新增配置】：添加自定义会话特征。
![](https://main.qcloudimg.com/raw/0a0206a5aa6898e5128bc28f13c45522.jpg)

⾃定义会话特征匹配条件说明如下：

<table>
<thead>
<tr>
<th>分类</th>
<th>过滤条件</th>
<th>条件说明</th>
</tr>
</thead>
<tbody><tr>
<td rowspan = "6">会话特征</td>
<td>会话平均速度</td>
<td>为会话请求总次数 / 会话持续时间，单位为：次/分钟。</td>
</tr>
<tr>
<td>会话窗口速度</td>
<td>每2分钟（窗口）内的会话访问速度，单位为：次/分钟。</td>
</tr>
<tr>
<td>会话总次数</td>
<td>一个 BOT 会话发生的总访问次数。</td>
</tr>
<tr>
<td>会话持续时间</td>
<td>BOT 会话的持续时间。</td>
</tr>
<tr>
<td>会话存在 Robots.txt</td>
<td>会话请求中访问 Robots.txt 文件。</td>
</tr>
<tr>
<td>会话发生在凌晨</td>
<td>会话请求发生在凌晨2:00 - 5:00之间。</td>
</tr>
<tr>
<td rowspan = "5">请求特征</td>
<td>请求最多的 URL</td>
<td>会话请求中，请求最多的 URL。</td>
</tr>
<tr>
<td>URL 重复比</td>
<td>会话请求中 URL 重复比例，取值范围0 - 1，根据实际业务情况，进行参数配置，过高或过低为疑似异常（根据实际情况进行判断）。</td>
</tr>
<tr>
<td>URL 种类</td>
<td>会话请求中 URL 去重后条目数。</td>
</tr>
<tr>
<td>请求最多的参数</td>
<td>会话请求出现最多的参数，包括 GET 请求参数（Query 内容）或 POST 请求参数（Body 内容）。</td>
</tr>
<tr>
<td>参数重复比</td>
<td>会话请求中 GET 请求参数（Query 内容）或 POST 请求参数（Body 内容）重复比例，取值范围0 - 1，根据实际业务情况，进行参数配置，过高或过低疑似异常（根据实际情况进行判断）。</td>
</tr>
<tr>
<td rowspan = "6">COOKIE</td>
<td>COOKIE 存在性</td>
<td>会话请求中，判断 HTTP 头部字段是否存在 COOKIE。</td>
</tr>
<tr>
<td>请求最多的 COOKIE</td>
<td>会话请求中， 出现最多的 COOKIE。</td>
</tr>
<tr>
<td>COOKIE 重复比</td>
<td>会话请求中 COOKIE 的重复比例，取值范围0 - 1。</td>
</tr>
<tr>
<td>COOKIE 存在比</td>
<td>会话请求中 COOKIE 存在比例，取值范围0 - 1。</td>
</tr>
<tr>
<td>COOKIE 滥用</td>
<td>多种不同的 UA 使用相同的 COOKIE。</td>
</tr>
<tr>
<td>COOKIE 种类</td>
<td>会话请求中 COOKIE 去重后的数目。</td>
</tr>
<tr>
<td rowspan = "6">Referer</td>
<td>Referer 存在性</td>
<td>会话请求中，判断 HTTP 头部字段是否存在 Referer。</td>
</tr>
<tr>
<td>请求最多的 Referer</td>
<td>会话请求中，HTTP Referer 字段出现最多的值。</td>
</tr>
<tr>
<td>Referer 重复比</td>
<td>会话请求中 Referer 的重复比例，取值范围0 - 1，对浏览器访问有效，过高疑似异常（根据实际情况进行判断）。</td>
</tr>
<tr>
<td>Referer 存在比</td>
<td>会话请求中 Referer 存在比例，取值范围0 - 1，对浏览器访问有效，过低疑似异常（根据实际情况进行判断）。</td>
</tr>
<tr>
<td>Referer 滥用</td>
<td>多种不同的 UA 使用相同的 Referer。</td>
</tr>
<tr>
<td>Referer 种类</td>
<td>会话请求中 Referer 去重后的数目。</td>
</tr>
<tr>
<td rowspan = "6">UA</td>
<td>UA存在性</td>
<td>会话请求中，判断 HTTP 头部字段是否存在 User-Agent。</td>
</tr>
<tr>
<td>请求最多的 UA</td>
<td>会话请求中，HTTP User-Agent 字段出现最多的值。</td>
</tr>
<tr>
<td>UA 存在比</td>
<td>会话请求中 UA 的存在比例，取值范围0 - 1，过低疑似异常（根据实际情况进行判断）。</td>
</tr>
<tr>
<td>UA 种类</td>
<td>会话请求中 UA 去重后的数目，过多疑似异常（根据实际情况进行判断），对非代理 IP 有效。</td>
</tr>
<tr>
<td>UA 类型</td>
<td>UA 类型为浏览器。UA 类型为移动端。UA 类型游戏终端或电视终端。UA 类别为公开 BOT 类型。UA 类别为未公开 BOT 类型。UA 类别为自动化工具。UA 类别为未知类型。UA 类别为公开扫描器。UA 类别为开发框架。UA 类别为语言 HTTP 库。</td>
</tr>
<tr>
<td>UA 随机性指数</td>
<td>会话请求中 UA 的随机分布情况，取值范围0 -1，指数越高越异常。 参考值阈值：超过0.6疑似异常，指数超过0.92基本确定为异常。</td>
</tr>
<tr>
<td rowspan = "6">其他 HTTP 头部</td>
<td>Accept 存在性</td>
<td>会话请求中判断 HTTP 头部字段是否存在 Accept 字段。</td>
</tr>
<tr>
<td>Accept-Language 存在性</td>
<td>会话请求中判断 HTTP 头部字段是否存在 Accept-Language 字段。</td>
</tr>
<tr>
<td>Accept-Encoding 存在性</td>
<td>会话请求中判断 HTTP 头部字段是否存在 Accept-Encoding 字段。</td>
</tr>
<tr>
<td>Connectiton 存在性</td>
<td>会话请求中判断 HTTP 头部字段是否存在 Connectiton 字段。</td>
</tr>
<tr>
<td>请求方法占比</td>
<td>会话请求中判断请求使用方法。</td>
</tr>
<tr>
<td>返回状态码比例</td>
<td>会话请中 WAF 返回给客户状态码比例。</td>
</tr>
</tbody></table>
