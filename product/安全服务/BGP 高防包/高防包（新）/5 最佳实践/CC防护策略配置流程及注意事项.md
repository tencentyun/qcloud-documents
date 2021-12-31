
DDoS 高防包提供针对 CC 攻击的防护功能，策略包括防护等级、清洗阈值、精准防护、CC 频率限制等。业务完成接入后，您可以参考本文介绍的 CC 攻击防护策略配置流程，进行相关的配置，更好地保护您的业务。
## 配置步骤
1. 登录 [DDoS 高防包管理控制台](https://console.cloud.tencent.com/ddos/antiddos-native/config/web)，在左侧导航中，单击**防护配置**。
2. 在左侧的列表选中高防包 ID，如“bgp-000000co”，在右侧的顶部单击**域名防护**。
3. **CC 防护清洗阈值设置**。在“CC 防护等级”卡片中，设置清洗阈值。
>?
>- 清洗阈值是 DDoS 高防的 CC 防护开关，具体的阈值可以设置为正常业务峰值的1.5倍。
>- 如果没有设置具体的阈值，高防包将不会触发清洗动作，即 CC 防护为关闭状态。当存在 CC 攻击时，控制台所配置的防护等级、精准防护、CC 频率限制相关策略也不会生效，详细说明请参见 [防护等级与清洗阈值](https://cloud.tencent.com/document/product/1021/43921)。
>
![](https://main.qcloudimg.com/raw/5124b42408fc51d1bcf60748ed95beb5.png)
4. **CC 防护等级设置**。
	1. 在“CC 防护等级”卡片中，单击**设置**，进入 CC 防护等级页面。
	2. 在 CC 防护等级页面，可以新建防护等级，或对已创建的防护等级进行编辑。
>?防护等级为 DDoS 高防开启 CC 防护且遭受攻击触发清洗动作时，对流量检测的严格程度，分为三种等级：宽松、适中、严格，可根据攻击情况进行选择，详细说明请参见 [防护等级与清洗阈值](https://cloud.tencent.com/document/product/1021/43921)。
>
![](https://main.qcloudimg.com/raw/2338bb1e9aa7f0bdfad011a00198d935.png)
5. **精准防护策略配置**。
攻击发生时，建议通过网络抓包、中间件访问日志、其他防护设备等途径获取攻击请求的具体信息，并结合业务确定攻击特征，完成精准防护策略的配置。
开启精确访问控制后，您可以对常见的 HTTP 字段（例如 URI、UA、Cookie、Referer 及 Accept 等）做条件组合防护策略，筛选访问请求，并对命中条件的请求设置人机校验或丢弃的策略动作。
	1. 在 [防护配置](https://console.cloud.tencent.com/ddos/antiddos-native/config/web) 页面，单击“精准防护”卡片中的**设置**，进入精准防护规则列表。
![](https://main.qcloudimg.com/raw/bbae63161780d3079dc0d6a1f15e265b.png)
	2. 单击**新建**，创建精准防护规则，填写相关字段，填写完成后，单击**确定**即可。详细配置说明，请参见 [精准防护](https://cloud.tencent.com/document/product/1021/43924)。
>!
>- 如果同一条策略中，存在多个 HTTP 字段时，需所有条件都满足才能匹配到此条策略。
>- DDoS 高防包暂不支持 HTTPS 业务的精准防护配置，[DDoS 高防 IP](https://cloud.tencent.com/document/product/1014/44102) 可支持 HTTPS 业务的精准防护配置。
>
![](https://main.qcloudimg.com/raw/96ef4496f8c562e7979f0266a2d228a5.png)
**字段说明：**
<table>
<thead>
<tr>
<th>字段</th>
<th>字段描述</th>
</tr>
</thead>
<tbody><tr>
<td>uri</td>
<td>访问请求的 URI 地址。</td>
</tr>
<tr>
<td>ua</td>
<td>发起访问请求的客户端浏览器标识等相关信息。</td>
</tr>
<tr>
<td>cookie</td>
<td>访问请求中的携带的 Cookie 信息。</td>
</tr>
<tr>
<td>referer</td>
<td>访问请求的来源网址，即该访问请求是从哪个页面跳转产生的。</td>
</tr>
<tr>
<td>accept</td>
<td>发起访问请求的客户端希望接受的数据类型。</td>
</tr>
<tr>
<td>匹配条件</td>
<td>人机校验和丢弃，<ul><li>丢弃：不做人机识别，直接丢弃。 </li><li> 人机校验：采用通过算法进行人机识别。</li></ul></td>
</tr>
</tbody></table>
6. **CC 频率限制**。
DDoS 高防为已接入防护的网站业务提供频率控制防护策略，支持限制源 IP 的访问频率。您可以自定义频率控制规则，检测到单一源 IP 在短期内异常频繁地访问某个页面时，将设置人机校验或丢弃策略。
	1. 在 [防护配置](https://console.cloud.tencent.com/ddos/antiddos-native/config/web) 页面，单击“CC 频率限制”卡片中的**设置**，进入精准防护规则列表。
![](https://main.qcloudimg.com/raw/531db6c64dfa2ca3f292bd2b0624f3e7.png)
	2. 单击**新建**，创建频率控制规则，填写相关字段，单击**确定**即可。详细配置说明，请参见 [频率控制](https://cloud.tencent.com/document/product/1021/43925)。
>!
>- 在配置针对 URI 的 CC 频率限制策略时，需首先配置“/”目录的频率限制，且匹配模式必须设置为等于，配置“/”目录后,才能设置其他目录的 URI 访问频率限制。
>- 配置“/”目录的频率限制的具体效果体现为在单位时间内，单个源 IP 请求此域名的“/”目录频率超过阈值，则触发相应的策略动作（人机校验或丢弃）。
>- 每个域名在配置“/”目录的频率限制策略后，其他目录的检测时间必须保持一致。
>- 当请求 URI 中存在不固定字符串时，可通过匹配模式包含配置来解决，即对 URI 中相同的前缀进行匹配。
 >
![](https://main.qcloudimg.com/raw/cebb1aba5a363f6ba31a88478dff64b7.png)
**字段说明：**
<table>
<thead>
<tr>
<th>字段</th>
<th>字段描述</th>
</tr>
</thead>
<tbody><tr>
</tr>
<tr>
<td>Cookie</td>
<td>访问请求中的携带的 Cookie 信息。</td>
</tr>
<tr>
<td>User-Agent</td>
<td>发起访问请求的客户端浏览器标识等相关信息。</td>
</tr>
<tr>
<td>Uri</td>
<td>访问请求的 URI 地址。</td>
</tr>
<tr>
<td>频率限制策略</td>
<td>人机校验和丢弃，<ul><li>丢弃：不做人机识别，直接丢弃。 </li><li> 人机校验：采用通过算法进行人机识别。</li></ul></td>
</tr>
<tr>
<td>检查条件</td>
<td>根据业务情况设置访问频次。建议输入正常访问次数的2倍 - 3倍，例如，网站人平均访问20次/分钟，可配置为40次/分钟 - 60次/分钟，可依据被攻击严重程度调整。</td>
</tr>
<tr>
<td>惩罚时间</td>
<td>最长为一天。</td>
</tbody></table>
