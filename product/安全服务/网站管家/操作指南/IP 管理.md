## 功能简介
腾讯云 Web 应用防火墙 IP 管理功能，对经过 Web 应用防火墙防护域名的访问源 IP 进行状态查询和黑白名单设置，主要功能包括：IP 查询，IP 黑白名单设置和 IP 封堵状态查询。
- IP 查询，查询输入 IP 在防御域名中状态信息，包括是否在黑白名单中，是否处于封堵状态。
- IP 黑白名单设置，支持设置基于域名或全局的 IP 黑白名单规则，支持网段设置。
- IP 封堵状态，实时查看 CC 攻击、BOT 行为管理、自定义策略人机识别等源 IP 封堵状态信息。

## 配置步骤
- #### **示例一 IP 查询**
	1. 进入 [腾讯云 Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/overview)，选择【IP 管理】>【IP 查询】输入需要查询的 IP 地址查看该 IP 状态。
![](https://main.qcloudimg.com/raw/a33335fb6f7c7bd79b0f81889352bfea.png)
	2. 查询出的 IP 地址，可手动添加黑白名单。
![](https://main.qcloudimg.com/raw/648f80d08d263d6230aa8555b07505cc.png)
- #### **示例二 添加 IP 黑名单**
	1. 进入 [腾讯云 Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/overview)，选择【IP 管理】>【IP 黑白名单】进入配置页面。
>?IP 黑白名单模块，可以添加基于域名的黑白名单或基于全局的黑白名单，生效优先级说明如下：
>- 黑白名单的优先级仅低于 Web 应用防火墙自定义放行策略，高于其他检测逻辑。
>- IP 黑白名单优先级从高到低顺序：自定义策略放行＞全局白名单>域名白名单>域名黑名单>全局黑名单＞WAF 其他模块。
>
![](https://main.qcloudimg.com/raw/8d4b4b2248e8e8fd0b559350dfd12f3f.png)
**配置项说明：**
		- 类别：黑名单、白名单。
		- 来源：CC 防护、BOT、自定义规则。
		- 高级筛选：利用创建时间和有效截止时间进行 IP 信息筛选。
	2. 添加黑白名单。左上角选择需要添加防护的域名，单击【添加黑白名单】，选择黑名单添加需要加黑名单 IP 地址或者网段。
>!
>- 选择域名为 ALL 时，添加的 IP 地址或 IP 段为全局的黑白名单。
>- 各个版本每个域名规格限制为：
>高级版：1000条/域名，企业版：5000条/域名，旗舰版:20000条/域名，每个 IP 地址或者 IP 段占用一条额度。
>
![](https://main.qcloudimg.com/raw/e81a70518ef61d9c4b0b417ed365cd76.png)
	3. 黑白名单支持导入和筛选结果导出，导入 IP 信息时，请参考导出格式。
![](https://main.qcloudimg.com/raw/1cb1a2a169f996f6f70cbf52e7d0925e.png)
	4. 添加完成后，可以在 IP 查询中输入添加的源 IP，查询状态信息。
- #### **示例三 IP 封堵状态查询**
	1. 进入 [腾讯云 Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/overview)，选择【IP 管理】>【IP 封堵状态】进入查询页面。
	2. 在查询页面，可以查询自定义策略人机识别、BOT 拦截、CC 防护模块拦截的 IP 信息，同时可对查询结果进行导出，对单个 IP 进行加黑加白操作。
![](https://main.qcloudimg.com/raw/00fcb12635c94868e4636b2310acd84c.png)

