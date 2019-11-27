## 功能简介
腾讯云 Web 应用防火墙（网站管家） BOT 行为管理能够对友好及恶意机器人程序进行甄别分类，并采取针对性的流量管理策略，如放通搜索引擎类机器人流量，而对恶意数据爬取商品信息流量采取不响应或减缓响应或差异化响应策略，能够应对恶意机器人程序爬取带来的资源消耗，信息泄露及无效营销问题，同时也保障友好机器人程序（如搜索引擎，广告程序）的正常运行。
## 配置案例
### BOT 概览
登录 [Web 应用防火墙（网站管家）控制台](https://console.cloud.tencent.com/guanjia)，在左侧导航栏中，选择【BOT 行为管理】>【BOT 概览】，进入 BOT 概览页面，可通过页面左上方的下拉框选择域名。该页面展示所选域名的请求次数统计图和 BOT 类型比例图（以测试域名为例，图中红色标识 BOT 请求，绿色标识总请求、正常请求和 BOT 请求之和）。
 ![](https://main.qcloudimg.com/raw/f2375e94212b934c65049222d38d17a6.png)
**字段说明：**
 - 已知类型 BOT：   是指公开的 BOT 类型，例如搜索引擎。
 - 未知类型 BOT：   是指未公开的 BOT 类型。
 - 自定义类型 BOT： 是指用户自己配置的 BOT 类型。

### BOT 设置
登录 [Web 应用防火墙（网站管家）控制台](https://console.cloud.tencent.com/guanjia/bot/strategy/know) ，在左侧导航栏中，选择【BOT 行为管理】>【BOT 设置】，进入BOT策略设置页面。
- **已知类型预设**
单击【已知类型预测】，进入已知类型预设界面，展示的信息有 BOT 类型、BOT 种类数、动作以及操作，操作选项有【监控】和【拦截】。
![](https://main.qcloudimg.com/raw/8ac91e7749fd9c55d49cc987e3975345.png)
**动作说明：**
 - 监控动作：监控正常请求中是否存在恶意的 BOT 行为，但不进行拦截。
 - 拦截动作：对检测到的恶意 BOT 行为进行拦截，拦截的源 IP 将会添加到域名防护列表中防护配置的 [自定义策略](https://console.cloud.tencent.com/guanjia/waf/config/rule/a.qcloudwaf.com) 中，默认拦截时间为1天，拦截时间可在自定义策略中进行修改。

- **自定义策略**
	1. 单击【自定义策略】，进入自定义策略界面，单击【添加策略】。
![](https://main.qcloudimg.com/raw/c00919465e8c6261729ea403f9ed76ab.png)
	2. 在添加策略页面，填写相关信息。填写 “策略名称” 和 “策略描述”，选择一个 “匹配字段”，此处以 “请求路径” 为例，逻辑符号选择【包含】，填写路径内容为 “/admin” ，执行动作选择【监控】，策略开关选择【开启】，单击【确定】后即添加成功。配置说明请参见表格 [自定义策略配置说明](#peizhi)
![](https://main.qcloudimg.com/raw/a424f2a447bc9f13a4721bef6f2bbdff.png)
>!每条自定义策略最多可添加 10 个条件，条件之间是 **“与”** 的关系，即满足全部条件才会生效。
 >
 **动作说明：**  
 - 监控动作：监控正常请求中，是否存在恶意的 BOT 行为，但不进行拦截。
 - 拦截动作：对检测到的恶意 BOT 行为进行拦截，拦截的源 IP 将会添加到域名防护列表中防护配置的 [自定义策略](https://console.cloud.tencent.com/guanjia/waf/config/rule/a.qcloudwaf.com) 中，默认拦截时间为1天，拦截时间可在自定义策略中进行修改。
 - 放行动作：不进行监控，也不拦截。

### BOT 详情
1. 登录 [Web 应用防火墙（网站管家）控制台](https://console.cloud.tencent.com/guanjia/bot/unknow/unknow) ， 在左侧导航栏中，选择【BOT 行为管理】>【BOT 详情】，此页面共有【未知类型】、【已知类型】和【自定义类型】三个选项卡，此处以【自定义类型】为例，进行配置说明，如需了解某 BOT 详情，可单击该条数据后的【查看详情】。
 ![](https://main.qcloudimg.com/raw/c13bf2b7bd7a76ed3eb373fc9824919c.png)
2. 进入 BOT 类型详情页面
 ![6](https://main.qcloudimg.com/raw/3c8c880b17fb94def64e4c2616ae6644.png)
 **字段说明：**
 - IP 类型：idc 为互联网数据中心，bs 为基站。
 - 行为信息熵：0.5 为参考值，值越小说明行为越异常。
 - 监控动作：监控正常请求中是否存在恶意的 BOT 行为，但不进行拦截。
 - 拦截动作：对检测到的恶意 BOT 行为进行拦截，拦截的源 IP 将会添加到域名防护列表中防护配置的 [自定义策略](https://console.cloud.tencent.com/guanjia/waf/config/rule/a.qcloudwaf.com) 中，默认拦截时间为1天，拦截时间可在自定义策略中进行修改。
 >!
	-  BOT 的 AI 模型会学习数据访问模式，当数据达到一定数量会生成模型。
	-  AI 模型的学习过程取决于网站类型和访问流量，正常的情况下学习周期为两周。



<span id="peizhi"></span>
### 自定义策略配置说明

| 匹配字段 | 逻辑符号 | 匹配内容 |
|---------|---------|---------|
| 存在 referer | 存在或不存在 | - |
| 请求速率 | 大于 | 次 / 分 |
| 请求次数	 | 大于 | 次 |
| referer 内容 | 包含 | 例如 no-referrer-when-downgrade |
| 存在 UA | 存在或不存在 | - |
| UA 内容 | 包含 | 例如 Mozilla |
| UA 类型 | 属于 | 自行勾选 |
| 请求参数 | 包含 | 例如 15 |
| 请求路径 | 包含 | 例如 /admin |
| IP 范围 | 包含 | 支持单个 IP、IP 段 |


[上一步：地域封禁](https://cloud.tencent.com/document/product/627/14704)
