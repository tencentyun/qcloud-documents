## 2021年09月

<table>
 <tr>
 <th width=20%>动态名称 </th>
 <th width=44%>动态描述 </th>
 <th width=16%>发布时间 </th>
 <th width=20%>相关文档 </th>
 </tr>
<tr>
 <td>SDK 1.3.4.1 版本发布 </td>
 <td>  
  <li> 优化：提升了通知栏状态的准确性</li>
  <li> 增加：修改了应用内消息 API 接口</li>
 </td>
 <td>2021-09-10</td>
 <td><a href="https://console.cloud.tencent.com/tpns/sdkdownload">SDK 下载</a></td>
 </tr>
</table>

## 2021年08月

<table>
 <tr>
	 <th width=20%>动态名称 </th>
	 <th width=44%>动态描述 </th>
	 <th width=16%>发布时间 </th>
	 <th width=20%>相关文档 </th>
 </tr>
 <tr>
	 <td>SDK 1.3.4.0 版本发布 </td>
	 <td>  
		 <li>修复：修复了长链接多次重连后，网络连接偶尔失效的问题</li>
		 <li> 修复：修复了 App 跳转导致 TPNS 在线状态偶尔不准确的问题</li>
		 <li>增加：增加了使用应用内消息作为补推的能力</li>
	 </td>
	 <td>2021-08-26</td>
	 <td><li><a href="https://console.cloud.tencent.com/tpns/sdkdownload">SDK 下载</a></li>
		<li><a href="https://cloud.tencent.com/document/product/548/56433">升级指南 </a></li>
	 </td>
 </tr>
 </table>


## 2021年07月

<table>
 <tr>
	 <th width=20%>动态名称 </th>
	 <th width=44%>动态描述 </th>
	 <th width=16%>发布时间 </th>
	 <th width=20%>相关文档 </th>
 </tr>
 <tr>
	 <td>SDK 1.3.3.0 版本发布 </td>
	 <td>  
		<li> 修复：修复了集群切换没有实时生效的问题</li>
		<li> 修复：修复了 tag 接口频繁调用时，绑定不准确的问题</li>
		<li> 优化：升级 SDK deployment target 到 9.0</li>
		<li> 优化：提升了"账号绑定"和"注册回调"的性能</li>
		<li> 新增：新增了对 RestApi 的 show_type 字段的支持，App 前台时可以不展示通知</li>
		<li> 新增：新增了长连接可支持 SSL 的能力</li>
		<li> 新增：对 App 启动类型，能区分是由"点击通知"拉起</li>
	 </td>
	 <td>2021-07-06</td>
	 <td><a href="https://console.cloud.tencent.com/tpns/sdkdownload">SDK 下载</a></td>
 </tr>
 </table>
 
## 2021年06月

<table>
 <tr>
	 <th width=20%>动态名称 </th>
	 <th width=44%>动态描述 </th>
	 <th width=16%>发布时间 </th>
	 <th width=20%>相关文档 </th>
 </tr>
	 <tr>
	 <td>SDK 1.3.2.1 版本发布 </td>
	 <td>  
			<li> 修复：Xcode 12.5下，引用 TPNSInAppMessage.framework 的兼容性问题</li>
			<li> 修复：用户 iCloud 备份还原，两台设备具有同样 TPNS Token 问题</li>
			<li> 优化：接入点切换后，原接入点日志不上报</li>
			<li> 增加：新增手机号码绑定接口，用于普通短信及智能短信发送</li>
			<li> 增加：Demo 演示了"用户允许协议"后才进行 Push 通知弹窗的方法</li>
			<li> 增加：对 startXGWithAccessID 接口的错误调用，进行了日志提示</li>
			<li> 增加：对第三方 SDK 对 appdelegate 的 hook 冲突，进行了日志提示</li>
			<li> 删除：若干在生产环境下，不必要的日志提示</li>
	 </td>
	 <td>2021-06-01</td>
	 <td><a href="https://cloud.tencent.com/document/product/548/56433">升级指南 </a></td>
 </tr>
 </table>

## 2021年04月

<table>
 <tr>
	 <th width=20%>动态名称 </th>
	 <th width=44%>动态描述 </th>
	 <th width=16%>发布时间 </th>
	 <th width=20%>相关文档 </th>
 </tr>
 <tr>
	 <td>SDK 1.3.1.1 版本发布 </td>
	 <td>修复：GCDAsync 库可能导致的编译冲突 </td>
	 <td>2021-04-19 </td>
	 <td>-</li> </td>
 </tr>
 <tr>
	 <td>SDK 1.3.1.0 版本发布 </td>
	 <td>  
		<li>修复：TPNS 自建通道和 APNs 通道的播放声音规则不一致问题</li>
		<li>修复：切换集群时，云控下发加密字段失效的问题</li>
		<li>修复：偶现的统计日志上报失败问题</li>
		<li>修复：覆盖消息功能，带 thread-id 的通知可能覆盖失败的问题</li>
		<li>优化：部分错误日志的提示文案</li>
		<li>优化：提高终端对 TPNS Token 的环境校验的准确性</li>
		<li>优化：自动补发在 TPNS 网络连接失败时设置的角标数</li>
		<li>优化："静默消息"的抵达上报更及时</li>
		<li>增加：查询标签功能</li>
		<li>增加：申请通知权限的回调</li>
		<li>增加：TPNS 通道支持 thread_id 消息分组</li>
		<li> 增加：Demo 新增全球集群切换的示例代码</li>
		<li>增加：TPNS 网络连接的建连成功和断开回调</li>
	</td>
	 <td>2021-04-12 </td>
	 <td>-</td>
 </tr>
 </table>

## 2021年01月

<table>
 <tr>
 <th width=20%>动态名称 </th>
 <th width=44%>动态描述 </th>
 <th width=16%>发布时间 </th>
 <th width=20%>相关文档 </th>
 </tr>
 <tr>
 <td>SDK 1.3.0.0 版本发布 </td>
 <td> <li> 修复：多线程时和低内存下的小概率 crash 的问题
<li>优化：减少不必要的 MQTT 网络超时检测
<li>优化：“抵达”的上报支持更高性能的方式
<li>优化：减少“应用内消息”插件包体积
<li>优化：对获取 TPNS token 的请求进行加密
<li> 增加：账号、标签、用户属性接口的参数检查逻辑和错误回调
<li>删除：账号类型枚举，由业务自己定义 
</td>
 <td>2021-01-25 </td>
 <td>-</li> </td>
 </tr>
 </table>


## 2020年11月

<table>
 <tr>
 <th width=20%>动态名称 </th>
 <th width=44%>动态描述 </th>
 <th width=16%>发布时间 </th>
 <th width=20%>相关文档 </th>
 </tr>
 <tr>
 <td>SDK 1.2.9.0 版本发布 </td>
 <td> <li>修复：富媒体通知可能下载图片失败的问题
 <li>修复：App 在后台时，TPNS 通道可能在线的问题
 <li>修复：1.2.5.2以前版本，可能出现 TPNS token 重复的问题
 <li>修复：可能建立长连接失败的问题
 <li>修复：“应用内消息”和个别 SDK 命名冲突的问题
 <li>优化：本地缓存的性能
 <li>优化：App 通知开关状态的上报时机
 <li>优化：弱网下的长连接处理机制
 <li>优化：账号相关接口
 <li>优化：TPNS Demo 的代码示例
 <li> 增加：本地通知功能
 <li>增加：对 IPv6 的支持
 <li>删除：对免费版的兼容代码 </td>
 <td>2020-11-25 </td>
 <td> - </td>
 </tr>
 </table>


## 2020年10月

<table>
 <tr>
 <th width=20%>动态名称 </th>
 <th width=44%>动态描述 </th>
 <th width=16%>发布时间 </th>
 <th width=20%>相关文档 </th>
 </tr>
 <tr>
 <td>SDK 1.2.8.1 版本发布 </td>
 <td>修复已知问题 </td>
 <td>2020-10-29 </td>
 <td>- </td>
 </tr>
 </table>



## 2020年09月

<table>
<tr>
    <th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
</tr>
    <tr>
        <td>SDK 1.2.8.0 版本发布</td>
				<td><li> 新增「<b>用户属性</b>」相关接口，用于个性化推送</li><li> 新增「<b>应用内消息</b>」功能，以及若干应用内消息模板</li><li>支持通过 TPNS 通道下发消息</li><li>修复已知问题</li></td>
        <td>2020-09-27</td>
        <td>-</li></td>
    </tr>        
</table>


## 2020年07月

<table>
<tr>
    <th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
</tr>
    <tr>
        <td>SDK 1.2.7.2 版本发布</td>
        <td><li> 增加自定义事件上报功能</li><li> 提升“抵达数”上报的成功率</li><li>修复已知问题</li></td>
        <td>2020-07-23</td>
        <td>-</a></li></td>
    </tr>        
</table>



## 2020年05月

<table>
<tr>
    <th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
</tr>
    <tr>
        <td>SDK 1.2.6.1 版本发布</td>
        <td><li> 提升稳定性，修复已知问题</li><li> 优化接入，新增注册回调方法</li><li>新增 TPNS 通道，若 APNs 通道下发消息失败，将通过 TPNS 通道进行消息补发</li><li>优化数据统计</li></td>
        <td>2020-05-06</td>
        <td><a href="https://cloud.tencent.com/document/product/548/36663#.E8.B0.83.E8.AF.95.E6.96.B9.E6.B3.95">注册回调方法</a></li></td>
    </tr>        
</table>


## 2020年04月

<table>
<tr>
    <th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
</tr>
    <tr>
        <td>SDK 1.2.5.4 版本发布</td>
        <td>提升稳定性，修复已知问题</li></td>
        <td>2020-04-22</td>
        <td>-</td>
    </tr>
</table>


## 2020年03月

<table>
<tr>
    <th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
</tr>
    <tr>
        <td>SDK1.2.5.3 版本发布</td>
        <td><li> 支持对信鸽免费集群进行反注册token，防止重复推送</li><li>新增支持在通知扩展中对重复的消息进行替换</li></td>
        <td>2020-03-19</td>
        <td><a href="https://cloud.tencent.com/document/product/548/36668#.E6.B3.A8.E9.94.80.E4.BF.A1.E9.B8.BD.E5.B9.B3.E5.8F.B0.E6.8E.A8.E9.80.81.E6.9C.8D.E5.8A.A1">注销信鸽平台推送服务</a></td>
    </tr>
    <tr>
        <td>SDK 1.2.5.2 版本发布</td>
        <td><li> 提升精准推送，新增账号类型的枚举</li><li>提升稳定性，优化日志IO异常和iOS10接收消息回调异常的问题</li></td>
        <td>2020-03-06</td>
        <td>-</td>
    </tr>
</table>


## 2020年02月

<table>
<tr>
    <th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
</tr>
    <tr>
        <td>SDK 1.2.5.1 版本发布</td>
        <td><li> 简化接入，删除上报接口，SDK自动处理</li><li>提升稳定性，修复缓存模块引发的 Crash 问题</li></td>
        <td>2020-02-20</td>
        <td>-</td>
    </tr>
</table>


## 2020年01月

<table>
<tr>
    <th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
</tr>
    <tr>
        <td>SDK 1.2.4.9 版本发布</td>
        <td><li>提升稳定性，修复消息统计触发的崩溃问题和一处内存泄露问题</li> <li>优化提升 SDK 兼容性</li></td>
        <td>2020-01-06</td>
        <td>-</td>
    </tr>
</table>


## 2019年12月

<table>
<tr>
    <th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
</tr>
    <tr>
        <td>SDK 1.2.4.8 版本发布</td>
        <td>提升稳定性，修复消息统计触发的崩溃问题</li></td>
        <td>2019-12-24</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SDK 1.2.4.7 版本发布</td>
        <td> 提升稳定性，修复消息统计和日志记录触发的崩溃问题</li></td>
        <td>2019-12-19</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SDK 1.2.4.6 版本发布</td>
        <td><li> 优化 SDK 注册流程，提升注册成功率</li><li>优化富媒体推送，支持无后缀名的资源</li><li>修复其他已知问题</li></td>
        <td>2019-12-16</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SDK 1.2.4.5 版本发布</td>
        <td><li>SDK 增加 Crash 监控</li> <li>优化抵达数据统计</li><li>优化累计设备量统计</li><li>优化 SDK I/O 性能</li><li>优化提升 SDK 稳定性</li></td>
        <td>2019-12-12</td>
        <td>-</td>
    </tr>
</table>


## 2019年11月

<table>
<tr>
    <th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
</tr>
    <tr>
        <td>SDK 1.2.4.4 版本发布</td>
        <td> 优化 SDK 注册流程，提升通知消息触达</li></td>
        <td>2019-11-28</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SDK 1.2.4.3 版本发布</td>
        <td> 优化提升 SDK 兼容性</li></td>
        <td>2019-11-26</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SDK 1.2.4.2 版本发布</td>
        <td> 修复 SDK 获取 TPNS Token 的问题</li></td>
        <td>2019-11-22</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SDK 1.2.4.1 版本发布</td>
        <td><li> 新增日志上传接口</li><li> 优化提升 SDK 稳定性</li><li> 优化提升 SDK 兼容性</li></td>
        <td>2019-11-13</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SDK 1.2.4.0 版本发布</td>
        <td><li> 修复单账号绑定回调的问题</li><li> 提升 SDK 与第三方的兼容性</li><li> 新增区分设备推送环境，从而优化统计数据</li><li> 优化更换 App 信息的缓存逻辑</li><li> 提升 SDK 注册成功率</li></td>
        <td>2019-11-12</td>
        <td>-</td>
    </tr>
</table>


## 2019年10月

<table>
<tr>
    <th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
</tr>
    <tr>
        <td>SDK 1.2.3.0 版本发布</td>
        <td>修复一个当设备 Token 变化时出现的问题</li></td>
        <td>2019-10-21</td>
        <td>-</td>
    </tr>
</table>


## 2019年09月

<table>
<tr>
    <th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
</tr>
    <tr>
        <td>SDK 1.2.2.1 版本发布</td>
        <td>修复一个当 SDK 未启动完成就调用其他接口而产生的网络连接的问题</li></td>
        <td>2019-09-29</td>
        <td>-</td>
    </tr>
</table>


## 2019年08月

<table>
<tr>
    <th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
</tr>
    <tr>
        <td>SDK 1.2.2.0 版本发布</td>
        <td><li> 修复 iOS13上无法注册的问题</li><li>修复 App 状态切换时的网络连接的问题</li></td>
        <td>2019-08-28</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SDK 1.2.1.2 版本发布</td>
        <td><li> 修复点击数据统计问题</li><li> 修复标签绑定接口在网络连接状态变化时存在的问题</li></td>
        <td>2019-08-19</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SDK 1.2.1.0 版本发布</td>
        <td><li> 新增查询 TPNS 服务生成的 Token 接口</li><li> 修复单账号绑定失败的问题</li></td>
        <td>2019-08-08</td>
        <td>-</td>
    </tr>
</table>


## 2019年07月

<table>
<tr>
    <th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
</tr>
    <tr>
        <td>SDK 1.2.0.0 版本发布</td>
        <td><li> 新增独立上报数据 SDK</li><li> 优化终端注册服务</li><li> 更新 DeviceToken 解析逻辑</li></td>
        <td>2019-07-30</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SDK 1.1.0.1 版本发布</td>
        <td><li> 修复用户名和密码认证逻辑</li><li> 修复动态加载 SDK 的缺陷</li></td>
        <td>2019-07-25</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SDK 1.1.0.0 版本发布</td>
        <td><li> 增加 PushKit 插件</li><li> 优化 SDK 启动耗时</li></td>
        <td>2019-07-18</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SDK 1.0.1.0 版本发布</td>
        <td><li> 增加长连接的推送</li><li> 增加对 PushKit 的插件化支持，目前功能仅限注册，注销，上报</li></td>
        <td>2019-07-11</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SDK 1.0.0.0 版本发布</td>
        <td>初始版本</li></td>
        <td>2019-07-05</td>
        <td>-</td>
    </tr>
</table>

