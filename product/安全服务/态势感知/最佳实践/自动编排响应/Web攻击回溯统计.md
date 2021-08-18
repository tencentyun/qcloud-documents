本文档将为您介绍当遭受 Web 攻击时，安全运营中心将如何通过自动化编排响应进行防护。
## 背景信息
安全运营中心会联动 [Web 应用防火墙](https://cloud.tencent.com/document/product/627)（WAF），将您的服务遭受到 Web 攻击进行搜集上报。自动化编排响应会自动帮助您将遭受到的 Web 攻击，以丰富的统计报表形式展示出来，并对遭受攻击的域名做进一步防护，对攻击 IP 做封禁。

### WAF 巡检报表剧本
攻击者对您的 Web 服务等进行攻击时，安全编排协助您对 WAF（Web 应用防火墙） 拦截攻击日志进行多维度的统计，并定期提供详细的报表信息，使得您对自己 Web 服务的安全情况有全面认知，同时帮助您做相应拦截处理。

### 响应流程
统计类剧本是针对某一时间段内，某一类安全事件进行统计分析并输出报表。WAF 巡检报表剧本通过对来源 WAF 的全部安全事件，每天进行一次巡检分析，通过获取统计时间范围及事件名称，统计 TOP5 攻击源 IP 及查询其威胁情报，统计 TOP5 域名被访问次数、统计 TOP5 被攻击域名及查询域名源站 IP、安全访问策略信息，排查出恶意 IP 并提供修复建议，输出巡检报表。

下图为 WAF 巡检报表剧本的响应图谱，右侧为图谱每个节点的节点类型、节点描述、输入参数及输出参数等信息。
![](https://main.qcloudimg.com/raw/fe98006fb24a8a22605c8c3b4b6250ca.png)
## 前提条件
- 自动编排响应功能目前正在试用中，获得内测邀请的用户可获得免费试用资格，您可通过 [申请内测](https://cloud.tencent.com/apply/p/w5svog9t1nj) 进行使用。
- 使用 WAF 巡检报表剧本需先开通 [Web 应用防火墙](https://buy.cloud.tencent.com/buy/waf) 服务。


## 操作步骤
1. 登录 [安全运营中心控制台](https://console.cloud.tencent.com/ssav2/soar)，在左侧导航中，单击【自动化编排响应】。
2. 在自动编排响应页面，单击 WAF 巡检报表剧本，查看剧本详情。
3. 在剧本详情页，可查看 WAF 巡检报表剧本的剧本类型、最近运行时间、针对事件、事件来源及剧本描述等信息。
>?封禁次数是通过该剧本封禁 IP 的次数。
>
![](https://main.qcloudimg.com/raw/48e4852972e158607c08f4e464a16901.png)
	- **昨日 Web 攻击事件概况**：您可查看昨日 Web 攻击事件占比及发生次数。
	<img src="https://main.qcloudimg.com/raw/1a0d5dfa5b0a35647a2f3e1c3d323801.png" style="zoom:65%;" />
	- **昨日 TOP5 攻击源 IP**：您可查看昨日攻击次数最多的5个攻击源 IP 的攻击次数和来源城市。
	<img src="https://main.qcloudimg.com/raw/a07e5e55353d9fb235f18377bfa88bec.png" style="zoom:65%;" />
	- **昨日 TOP5 被攻击域名**：您可查看昨日被攻击次数最多的5个域名及其被攻击次数。
	<img src="https://main.qcloudimg.com/raw/760a02f0fd99f90d98a53c5b5c6bec05.png" style="zoom:65%;" />
	- **昨日 TOP5 域名访问次数**：您可查看昨日被访问次数最多的5个域名及其被访问次数。
	<img src="https://main.qcloudimg.com/raw/c478ff19a9b286602b8e3ef59eefdd9c.png" style="zoom:65%;" />
	- **昨日 TOP5 攻击源 IP 威胁情报查询情况**：您可查看昨日被攻击次数最多的5个攻击源 IP 的攻击次数、判定结果及置信度。
	![](https://main.qcloudimg.com/raw/0ce96b82ee1d147f853ac7827682fc4f.png)
	- **最新巡检报表**：您可查看最新生成5份巡检报表。列表包括生成时间、报表名称、报表统计时间范围、统计分析事件数及操作。
		- 单击【查看全部】，可前往报表中心的报表列表查看全部报表。
		- 单击【报表名称】，可查看报表详情。
		- 单击【统计分析事件数】，可前往安全事件的事件列表，查看当前时间段统计分析的事件。
		- 单击【响应详情】，可查看生成该份报表的具体响应详情并进行相应的处理。
![](https://main.qcloudimg.com/raw/370f6745c218f3dcc68e9722054e7b0d.png)
4. **查看报表响应详情**。
	1. 在 WAF 巡检报表剧本详情页的最新巡检报表右侧操作栏，单击【响应详情】。
	2. 在响应详情页，可查看该时间段通过 WAF 巡检报表剧本已经响应的动作节点、当前事件的响应状态、响应时长、每一个动作清单节点的详情。
![](https://main.qcloudimg.com/raw/1b61664c963b82a3623a33d3feebdf78.png)
	3. 在报表响应详情左上角，单击【后续操作建议】，您可根据实际业务需求和建议方案进行处理。
![](https://main.qcloudimg.com/raw/23b423152f6ee875da235ee60b37b928.png)
	4. 当前后续操作建议为封禁 TOP5 恶意 IP，拦截方式支持“云防火墙”和 “WEB 应用防火墙”，如需封禁您可根据实际业务需求，选择拦截方式和拦截截止时间。
	![](https://main.qcloudimg.com/raw/051338d0185beec8aada874b7abcf998.png)
5. 查看报表，WAF 巡检报表可统计每天的 Web 攻击事件概况、攻击者概况及受害者概况。
	- **方式1**：您可在报表中心的 [报表列表](https://console.cloud.tencent.com/ssav2/report) 中，查看该剧本已生成的全部报表。
	![](https://main.qcloudimg.com/raw/b8556d68636e1d35f04437a9c5d0b5f0.png)
	- **方式2**：您可在报表响应详情的最新巡检报表中，查看该剧本已生成的最新报表。
![](https://main.qcloudimg.com/raw/8e78c1d585928380d715026b372fc900.png)

