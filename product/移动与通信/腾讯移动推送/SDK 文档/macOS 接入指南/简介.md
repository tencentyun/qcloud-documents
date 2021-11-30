
macOS 端实现推送消息的服务涉及三个角色：终端应用（Client App），APNs（Apple Push Notification service），移动推送 TPNS 服务器（TPNS Provider）。在使用移动推送 TPNS 服务实现给客户端推送消息，需要这三个角色在整个流程中相互配合，任何一个角色出现异常都可能会导致消息无法推送。

## 文件组成
-  XG_SDK_Cloud_macOS.framework (主SDK文件)
-  XGMTACloud_macOS.framework （“点击上报”组件）

## 版本说明
- 支持 macOS 10.8+。
- 针对 macOS10.14+ 以上版本。
 - 需要额外引入 UserNotification.framework。
 - 建议使用 Xcode 10.0+。

## 主要功能
macOS SDK 是移动推送 TPNS 服务为客户端实现消息推送而提供给开发者的接口，主要负责完成：
- 设备 Token 的自动化获取和注册，降低接入门槛。
- 账号、标签与设备的绑定接口，以便开发者实现特定群组的消息推送，丰富推送方式。
- 点击量上报，统计消息被用户点击的次数。

### TPNS macOS 与 iOS 的差异

- 功能差异 
>! 以下特性由于苹果官方不支持，因此 macOS SDK 未提供。
>
<table>
<thead>
	<tr><th>功能描述</th><th>iOS</th><th>macOS</th><th>说明</th></tr>
</thead>
<tbody>
	<tr>
		<td>通知扩展插件</td><td>✓</td><td>×</td><td>macOS 不支持通知扩展插件，不支持富媒体通知，不支持离线抵达统计</td>
	</tr>
	<tr><td>自定义通知声音</td><td>✓</td><td>×</td><td>macOS 不支持自定义通知声音</td></tr>
	<tr><td>静默消息</td><td>✓</td><td>×</td><td>macOS 不支持静默消息</td></tr>
	<tr><td>通知分组</td><td>✓</td><td>×</td><td>macOS 不支持通知分组</td></tr>
</tbody>
</table>
- 使用 Mac Catalyst 构建的 App 推荐使用 TPNS iOS SDK
- Big Sur 系统（11.3及以下）开发环境无法获取 DeviceToken
此为苹果官方 Bug，已在11.4修复。
