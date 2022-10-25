## 为什么要对 API 进行容量保护？
由于 API 是面向程序自动化调度所设计的，因此容易受到自动化调度引发的网络攻击。

- 攻击者会试图重放并自动填充不同认证凭据的业务流量攻击，导致相关业务敏感数据的泄露造成业务损失。
- 利用自动化工具发起 Layer-7 的 DOS 攻击，通过不断地发起相关业务请求，通过高频次的调度占满服务器的带宽及上下游的计算、存储资源，造成业务平台不稳定。
- 攻击者通过利用自动化模糊测试的工具，对业务进行定向攻击绕过测试，用于绕过定向的安全防护。
- 攻击者通过编写自动化编程工具，将有资源额度的相关 API 进行资源耗尽攻击。


可以分为如下四个模块，对 API 进行业务防护。
- API 容量防护
- API 安全防护
- API 资产管理
- API 生命周期管理

本文将从 API 容量保护角度进行梳理。在开发的生命周期内，API 的开发运营人员在进行 API 开发及维护时，可以通过使用**缓存、降级、限流**措施用来保护及提高 API 系统容量的稳定性。
<dx-tabs>
::: 缓存
提升系统访问速度和增大系统处理容量。
:::
::: 降级
当服务出现问题或者影响到核心流程时，需要暂时屏蔽掉 API 的访问，待高峰或者问题解决后再打开。
:::
::: 限流
通过对并发访问/请求进行限速，或者对一个时间窗口内的请求进行限速来保护系统，一旦达到限制速率则可以拒绝服务、排队或等待、降级等处理。:::
</dx-tabs>


上述三种有效的防护手段措施可以在开发、运营部署的过程中进行实现，但是会消耗大量的人力资源成本及开发成本。并且在整个 API 安全的生命周期中，需要对所有的 API 资产进行对应的 API 容量保护。

因此需要对每一个 API 接口进行特定的业务改造，这个时候工程量就会呈指数级上涨。可以采用如下方式来对业务 API 进行快速的容量保护。


## 如何对 API 进行容量保护？
对 API 进行容量保护时，除了上述部分中描述的**缓存、降级、限流**可以通过自己开发运维外，还可以通过 Web 应用防火墙中的相关模块进行定向的 API 容量保护，本文将会以如下9种可在 Web 应用防火墙中保护的方法进行定向 API 的快速容量保护。

| 防护细项              | 防护实践内容                                            |
| ---------------------- | --------------------------------------------------- |
| API 内容缓存           | 静态 API 资源缓存                                   |
| API 访问降级           | 阻断 API 的异常流量保护业务系统稳定                 |
| API 限流               | 限制 API 整体访问请求流速                           |
| API 客户端调度访问限速 | 限制客户端调度 API 的访问速度                       |
| API 敏感调用保护       | 保护敏感 API 接口调度不被滥用，保证业务数据不被外泄 |
| API 资源调用保护       | 保护 API 强资源消耗接口调度不超限额                 |
| 关键 API 调用保护      | 在调度关键 API  的时候进行2fa/mfa/人机识别          |
| API 验签保护           | 验证客户端是否为真实客户端进行访问                  |
| API 异常访问源调度保护 | 保护 API 不被异常的访问资源访问                     |



## API 内容缓存
由于公共 API 的返回接口内容较为频繁，消耗资源较大，如果 API 返回内容在一段时间内都不会持续的更新，那么就可以对 API 的相关内容进行缓存，减少 API 服务端的计算资源、带宽资源的损耗。

此处可以使用  Web 应用防火墙中的 **[基础安全](https://console.cloud.tencent.com/guanjia/tea-baseconfig)** > **网页防篡改**模块对 API 内容进行快速缓存，对业务 API 进行特定的数据缓存，帮助业务系统快速内容缓存。
1. 在网页防篡改页面，单击**添加规则**，弹出添加防篡改规则弹窗。
2. 在添加防篡改规则对话框中，填写相关字段，设置完成后，单击**添加**。
![](https://qcloudimg.tencent-cloud.cn/raw/4ae95611eb90b72d8a2bd7086f17c0de.png)
  **字段说明：**
	- **规则名称**：防篡改规则名称，最长50个字符，可以在攻击日志中按照规则名称进行搜索。
	- **页面路径**：防篡改路径，需要进行防篡改保护的 URL，需要指定详细 URL，不支持路径配置。
>?
>- 指定页面仅限于.html、.shtml、.txt、.js、.css、.jpg、.png 等静态资源。
>- 添加规则后，用户第一次访问该页面，WAF 将会对页面进行缓存，后继访问的请求为 WAF 缓存页面。
3. 完成的防篡改规则后，规则默认启用。

##  API 流速限制
对 API 的流速限制分为两个部分：

### 对服务端 API 整体的流速限制
如果对服务端进行整体的 API 限速限流，容易导致部分客户端无法访问到业务信息。由于恶意流量在攻击时，流量数据会比较大，如果通过 API 后端服务限速，大多数访问流量信息基本都为异常访问用户，正常访问用户很少，容易造成大量正常用户的客诉。因此，建议对**客户端的调用进行流速限制，可以通过对客户端的限频或限速，来实现对 API 流速的限制**。

### 对客户端调用的流速限制
在 Web 应用防火墙中的，可以通过 CC 防护设置、BOT 管理进行对客户端的限流。

#### CC 防护设置
CC 防护功能可配置每个客户端的整体的访问频次，一旦客户端的访问频次超出限制的预期，则对其进行相关处置。

1. 在 [CC 防护页面](https://console.cloud.tencent.com/guanjia/tea-baseconfig)，单击**添加规则**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/e09b6939285958ecd663950ff2b4db6f.png" width=700px>
2. 在添加 CC 防护规则对话框中，配置相关参数，单击**确定**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/c78e84c47e8e51789afc471c270b9b4b.png" width=870px>

#### BOT 管理设置
通过配置 [BOT 管理](https://console.cloud.tencent.com/guanjia/tea-botconfig) > **自定义会话设置**中的会话平均速度条件，可以控制每个客户端的会话持续访问速度。

1. 在 BOT 管理页面的高级设置模块，单击自定义规则的**前往配置**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/1389b46be27345c459cadf7f2d829839.png"  width=700px>
2. BOT 自定义设置页面，单击**添加规则**，配置相关参数，单击**确定**即可。
<img src="https://qcloudimg.tencent-cloud.cn/raw/baf98c6ca169d3c9c6481d53ee1fd7c3.png"  width=870px>

#### Session 设置/会话设置
由于在现网环境下，IPv4 的 IP 数量越发紧张，目前很多 IP 运营商都会将客户端放置在 NAT IP 下，即一个 IP 下面有多个业务客户端。如果单纯对业务进行 IP 的限速，在面对 NAT IP 的情况下，容易触碰到业务配置的 IP 限频策略，导致误拦截的现象。如果业务配置限频过于宽松，又会使相关业务的限频拦截无法起到限流的效果。

因此，可以在 Web 应用防火墙中配置 Session 设置/会话设置，既可做到**自动分辨同一 IP 下的不同客户端，实现对单一客户端的业务限频**。

- **Session 设置**
 1.  登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/tea-overview)，在左侧导航栏选择**基础安全**。
 2. 在基础安全页面，左上角选择需要防护的域名，单击 **CC 防护**，进入 CC 防护页面。
 <img src="https://qcloudimg.tencent-cloud.cn/raw/5e4564d35c7388711034878864f189eb.png" width=700px>
 2. 在 SESSION 设置模块中，单击**设置**，设置 SESSION 维度信息。
<img src="https://qcloudimg.tencent-cloud.cn/raw/154dd23236f82de255052f8bfba0285b.png" width=700px>
 3. 在 SESSION 设置对话框，配置相关参数，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/90c67bcf884d1bb8935c99ba40fb56ad.png)
**参数说明：**
   - **SESSION 位置**：可选择 COOKIE、GET 或 POST，其中 GET 或 POST 是指 HTTP 请求内容参数，非 HTTP 头部信息。
   - **匹配说明**：位置匹配或者字符串匹配。
   - **SESSION 标识**：取值标识，32个字符以内。
   - **结束位置**：字符串或位置匹配的结束位置，1-2048以内的整数，并且最多只能提取128个字符。
- **会话设置**
 1. 在[ BOT 管理](https://console.cloud.tencent.com/guanjia/tea-botconfig) > **高级设置**模块，单击会话管理的**前往配置**。
 <img src="https://qcloudimg.tencent-cloud.cn/raw/6482e262a73a10a522fa51fd9e789e04.png" width=700px>
  2. 在会话管理页面，单击**添加配置**，配置相关参数，单击**确定**即可。
>?会话管理应为可持续性跟踪 tokenid ，例如登录后的 set-cookies 的值。
>
![](https://qcloudimg.tencent-cloud.cn/raw/ab5e7a5ca3c5a2e19b2f8fb8b7f6f766.png)
**参数说明：**
   - **Token 位置：**	可选择 HEADER、COOKIE、GET 或 POST，其中 GET 或 POST 是指 HTTP 请求内容参数，非 HTTP 头部信息。
   - **Token 标识：**取值标识。


### 控制客户端的 API 调用
每一个敏感的 API 都有应该存在调用次数限制，例如：在短信 API 服务中，如果不对其进行相关限制，攻击者会滥用 API 接口，消耗短信资源包，造成超额的计费账单。如果敏感 API 接口在客户端调用前，进行 2fa/mfa 或人机识别等验证，可以有效减少异常 API 调度。

在 Web 应用防火墙的 [BOT 管理](https://console.cloud.tencent.com/guanjia/tea-botconfig) > **自定义会话设置**中，通过简单的配置，实现对 API、客户端的次数调用，敏感 API 调用前，对其进行敏感操作保护。

#### 敏感 API 调度前进行人机识别
<img src="https://qcloudimg.tencent-cloud.cn/raw/93ecbd64daa25603f6dea1a55cade3a8.png"  width=870px>

#### 限制客户端在单一会话时间内的 API 调度总次数
<img src="https://qcloudimg.tencent-cloud.cn/raw/518766d2d84d78a87ba653d88d6c2a23.png"  width=870px>

### 如何进行客户端的 API 访问进行验签？
客户端的验签可以有很多种方式，包括但不限于：
- mtls。
- 客户端签名验证。
- 客户端数据挑战。

用户可以通过配置 mtls、客户端数据签名挑战等方式进行数据的加强验签。

在 Web 应用防火墙中，通过开启前端对抗功能，对客户端的 API 数据进行验签，并进行定向防重放功能。对抗 API 滥用有良好的效果，详细可以参见 [客户端风险识别](https://cloud.tencent.com/document/product/627/65690)。
![](https://qcloudimg.tencent-cloud.cn/raw/e2a850ae7190762f9b7848b116b37f3a.png)

