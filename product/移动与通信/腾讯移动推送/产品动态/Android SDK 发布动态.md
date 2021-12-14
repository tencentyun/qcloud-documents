
## 2021年09月

<table>
	<tr>
		<th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
	</tr>
	<tr>
        <td>SDK 1.2.7.1 版本发布</td>
	<td>修复：偶现的跨进程存储不一致问题</td>
        <td>2021-09-1</td><td><li>使用新增的应用内消息能力时，请注意高版本安卓使用 WebView 的兼容性，参考 <a href="https://cloud.tencent.com/document/product/548/36659#.E5.BA.94.E7.94.A8.E5.86.85.E6.B6.88.E6.81.AF.E5.B1.95.E7.A4.BA">Android 接口文档</a></li>
<li><a href="https://console.cloud.tencent.com/tpns/sdkdownload">SDK 下载</a></li>
<li><a href="https://cloud.tencent.com/document/product/548/56364">Android SDK 升级指南</a></li></td>
    </tr>
<tr>
</table>

## 2021年08月

<table>
	<tr>
		<th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
	</tr>
	<tr>
        <td>SDK 1.2.7.0 版本发布</td><td>
		<li>  新增：新增应用内消息展示
		<li>  优化：推送服务注册流程优化
		<li>  修复：同意隐私协议前获取设备型号问题</td>
        <td>2021-08-27</td><td><li>使用新增的应用内消息能力时，请注意高版本安卓使用 WebView 的兼容性，参考 <a href="https://cloud.tencent.com/document/product/548/36659#.E5.BA.94.E7.94.A8.E5.86.85.E6.B6.88.E6.81.AF.E5.B1.95.E7.A4.BA">Android 接口文档</a></li>
<li><a href="https://cloud.tencent.com/document/product/548/56364">Android SDK 升级指南</a></li></td>
    </tr>
<tr>
</table>

## 2021年07月

<table>
	<tr>
		<th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
	</tr>
	<tr>
        <td>SDK 1.2.6.0 版本发布</td><td><li> 新增：接口调用 API 支持限频
<li>  新增：FCM 前台通知、TPNS 本地通知支持通知渠道配置
<li>  优化：优化长连接重连策略
<li>  优化：优化日活，启动上报
<li>  优化：SDK 日志放置在隐藏目录下
<li>  优化：默认关闭联合保活，如需开启请参考 Android 常见问题文档
		<li>  修复：修复 IPv6 请求失败</td>
        <td>2021-07-06</td><td><li>
<a href="https://console.cloud.tencent.com/tpns/sdkdownload">SDK 下载</a></li>
<li><a href="https://cloud.tencent.com/document/product/548/36674">Android 常见问题</a></li></td>
    </tr>
<tr>
</table>

## 2021年05月

<table>
	<tr>
		<th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
	</tr>
	<tr>
        <td>SDK 1.2.5.0 版本发布</td><td><li> 新增：新增标签查询接口
<li>  新增：新增手机号码绑定接口，用于普通短信及智能短信发送
<li>  新增：推送服务长连接支持 SSL 加密通信
<li>  新增：账号绑定接口升级，新增多种预设账号类型
<li>  修复：“清除全部通知”接口兼容清除小米厂商推送通知（MIUI 11 及以下版本小米设备）
<li>  修复：支持荣耀手机应用角标展示</td>
        <td>2021-05-26</td><td><li> 由于 Jcenter 下线，您可能遇到 SDK 依赖拉取问题，请参考 <a href="https://cloud.tencent.com/document/product/548/56364">Android SDK 升级指南</a> 配置依赖仓库镜像源</li>
<li> 新增的标签查询接口，需要注意在继承 <code>XGPushBaseReceiver</code> 的实现类中增加实现方法 <code>onQueryTagsResult</code></li></td>
    </tr>
<tr>
</table>

## 2021年02月

<table>
	<tr>
		<th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
	</tr>
	<tr>
        <td>SDK 1.2.3.1 版本发布</td><td>修复：修复华为禁用组件逻辑错误</td>
        <td>2021-02-04</td><td>-</td>
    </tr>
<tr>
</table>

## 2021年01月
   <table>
<tr>
    <th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
</tr>
        <td>SDK 1.2.3.0 版本发布</td>
<td><li>优化：网络通讯协议支持消息二次加密处理
<li>优化：终端账号、标签、属性设置接口简化
<li>新增：通知回调携带 traceId、templateId 字段
<li>新增：支持新荣耀手机角标逻辑
<li>修复：检查网络连接状态时偶发的 ANR 问题</td>
        <td>2021-01-27</td>
        <td>-</td>
    </tr>
<tr>
        <td>SDK 1.2.2.4 版本发布</td>
<td><li>修复：FCM 通知 intent 字符串内特殊字符处理问题<li>修复：其他已知问题</td>
        <td>2021-01-18</td>
        <td>-</a></td>
    </tr>
</table>



## 2020年11月

<table>
<tr>
    <th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
</tr>
<tr>
        <td>SDK 1.2.2.0 版本发布</td>
       <td><li> 优化：统一账号、标签操作接口命名<li> 优化：优化 SDK 内部错误码上报<li> 优化：FCM 通道协议升级，FCM 通道通知弹出支持 FCM 系统接管<li> 新增：支持 TPNS 通道通知小图标染色<li> 新增：网络通信支持 GZIP 压缩<li>修复：多线程环境下可能出现的 Service 解绑异常</td>
        <td>2020-11-26</td>
        <td>-</td>
    </tr>
        <tr>
        <td>SDK 1.2.1.3 版本发布</td>
       <td><li>内部逻辑优化<li>此版本起正式支持华为推送 V5 版本 SDK，请参考 <a href="https://cloud.tencent.com/document/product/548/45909">华为通道 V5 接入 SDK</a> 更新集成配置</td>
        <td>2020-11-11</td>
        <td>-</td>
    </tr>
</table>


## 2020年10月

<table>
<tr>
    <th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
</tr>
        <tr>
        <td>SDK 1.2.1.1 版本发布</td>
				<td><li>新增<b>用户属性</b>相关接口，用于个性化推送</li> <li>新增<b>应用内消息</b>功能，以及若干应用内消息模板</li><li>SO 文件优化更新</li><li>SDK 内部优化</li></td>
        <td>2020-10-12</td>
        <td>-</td>
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
        <td>SDK 1.2.0.3 版本发布</td>
       <td>修复已知问题 </td>
        <td>2020-07-30</td>
        <td>-</a></td>
    </tr>
<tr>
        <td>SDK 1.2.0.2 版本发布</td>
       <td>内部逻辑优化 </td>
        <td>2020-07-01</td>
        <td>-</td>
    </tr>
</table>

## 2020年06月

<table>
<tr>
    <th width=20%>动态名称</th>
    <th width=44%>动态描述</th>
    <th width=16%>发布时间</th>
    <th width=20%>相关文档</th>
</tr>
<tr>
        <td>SDK 1.2.0.1 版本发布</td>
       <td><li> 支持统计厂商通道通知点击事件 </li> <li> 丰富通知自定义样式</li> <li> 升级 OPPO 推送 SDK V2.1.0</li> </td>
        <td>2020-06-23</td>
        <td>此版本较旧版本有包名变更，请注意参考最新<a href="https://cloud.tencent.com/document/product/548/36652"> 集成文档 </a>变更相关配置：
<li>自动集成：注意混淆配置</li>
<li>手动集成：注意 so 文件、manifest 文件、混淆配置</li></td>
    </tr>
    <tr>
        <td>SDK 1.1.6.3 版本发布</td>
        <td> 第三方厂商通道集成优化</td>
        <td>2020-06-04</td>
        <td><a href="https://console.cloud.tencent.com/tpns/sdkdownload">-</a></td>
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
        <td>SDK 1.1.6.1 版本发布</td>
        <td>修复 HTTPS 证书校验漏洞</td>
        <td>2020-04-28</td>
        <td>-</a></td>
    </tr>
    <tr>
        <td>SDK 1.1.6.0 版本发布</td>
        <td><li> 优化加密协议 </li> <li> 优化网络连接</li> <li> 支持华为角标设置</li> <li> 升级小米推送 SDK v3.7.5，魅族推送 SDK v3.9.0 </li><li> 支持 Realme 和黑鲨手机厂商通道</li><li> 去除调用灯塔获取 QIMEI 相关信息</li></td>
        <td>2020-04-21</td>
        <td><a href="https://cloud.tencent.com/document/product/548/43693">角标适配指南</a></td>
    </tr>
    <tr>
        <td>SDK 1.1.5.5 版本发布</td>
        <td>解决 App上架 GooglePlay 会出现 DCL 违规问题</li></td>
        <td>2020-04-02</td>
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
        <td>SDK 1.1.5.4 版本发布</td>
        <td><li> 网络连接优化</li> <li> 增加账号类型</li> <li> 安全告警修复</li> <li> 兼容信鸽平台版本升级</li><li>获取 QIMEI 信息的功能</li><li>增加关闭联合保活功能</li></td>
        <td>2020-03-06</td>
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
        <td>SDK 1.1.5.3 版本发布</td>
        <td><li> 网络优化</li> <li> 安全告警优化</li></td>
        <td>2020-01-14</td>
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
        <td>SDK 1.1.5.2 版本发布</td>
        <td>优化错误监控</td>
        <td>2019-12-19</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SDK 1.1.5.1 版本发布</td>
        <td>优化 crash 监控</td>
        <td>2019-12-12</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SDK 1.1.5.0 版本发布</td>
        <td><li> 优化华为推送</li> <li> 升级 OPPO 推送 SDK v2.0.2</li></td>
        <td>2019-12-04</td>
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
        <td>SDK 1.1.4.0 版本发布</td>
        <td><li> 增加内部错误上报</li> <li> 华为推送 V3 兼容</li> <li> 一加手机厂商兼容</li></td>
        <td>2019-11-21</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SDK 1.1.3.2 版本发布</td>
        <td>数据统计优化</td>
        <td>2019-11-13</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SDK 1.1.3.1 版本发布</td>
        <td>网络优化</td>
        <td>2019-11-11</td>
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
        <td>SDK 1.1.3.0 版本发布</td>
        <td><li> 数据上报优化</li> <li> 日志优化，增加用户上报本地日志功能</li> <li> 增加 API 链式调用</li> <li> 系统内部性能优化，资源释放优化</li></td>
        <td>2019-10-31</td>
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
        <td>SDK 1.1.2.1 版本发布</td>
        <td><li> 通知栏展示优化</li> <li> 部分 API 接口 优化</li> <li> 增加音频富媒体</li> <li> SDK 内部优化</li></td>
        <td>2019-09-27</td>
        <td><a href="https://cloud.tencent.com/document/product/548/36652#.E9.9B.86.E6.88.90.E6.96.B9.E6.B3.95">音视频富媒体配置方法</a></td>
    </tr>
</table>

