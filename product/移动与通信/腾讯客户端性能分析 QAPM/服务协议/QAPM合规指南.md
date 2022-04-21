## 引言
根据监管部门要求，App 使用 SDK 时必须在其《隐私政策》中告知终端用户 SDK 提供者的名称、处理的个人信息类型、处理目的、处理方式、获取权限等信息（以下通称为“告知信息”），并且在终端用户未同意《隐私政策》前不得初始化任何 SDK 。

为了保证 App 接入QAPM SDK （以下通称为“本 SDK ”）的合规性，请App开发者/运营者（以下通称为“您”）务必按照《QAPM SDK 开发者合规指南》（以下通称为“本指南“）做好合规自查、进行相关信息披露和设置，避免被监管部门通报或下架您的 App。

## 一、请务必确保您已经将本 SDK 升级至满足监管新规的最新版本
请务必确保Android SDK 为5.0.7及以上版本，iOS SDK 为5.1.5及以上版本。因更新不及时产生的任何问题，由您自行解决并承担全部责任。

## 二、《隐私政策》中添加本 SDK 相关说明
请您确保您开发或运营的App有符合监管要求的《隐私政策》文本，同时请您根据App的实际情况，在App的《隐私政策》中明确告知终端用户您选择了本 SDK 作为合作方，其APP中使用了本 SDK 的相关产品及服务，并委托本 SDK 收集、使用、加工和处理终端用户的个人信息。
我们建议您在《隐私政策》的“数据共享与披露”章节中或者在《第三方个人信息共享清单》中披露告知信息，具体如下：
- **SDK 名称**：腾讯云客户端性能分析 QAPM SDK。
- **SDK 提供者名称**：腾讯云计算（北京）有限责任公司。
-  **SDK 处理目的：**监控和分析客户端的整体性能。
-  **SDK 处理方式**：收集客户端性能信息并经过加密处理后发送到 QAPM 的后台，生成辅助用户度量应用性能的指标数据和辅助用户分析性能问题的个例数据，以供第三方开发者查看。涉及到存储、计算分析和前端展示。
-  **SDK 个人信息类型**：
<table>
<thead>
<tr>
<th>SDK  类型</th>
<th>信息类型说明</th>
</tr>
</thead>
<tbody><tr>
<td>  iOS 与 Android 客户端 SDK</td>
<td><ul style="margin:0">
<li>设备信息（不同版本收集的设备信息有所不同）：<ul style="margin:0">
  <li>Android 版将获取手机型号、CPU信息、IP 地址、Wi-Fi参数、机型、系统版本、设备制造商、设备型号、屏幕分辨率、运行内存信息、运营商、电池温度、GPU、设备媒体的编码格式、设备最大显示的尺寸、设备全部显示尺寸、SD 卡信息。
  <li>iOS 版将获取 CPU 信息、IP 地址、电量、运营商、FPS、GPU、设备型号、系统版本、屏幕分辨率、运行内存信息、机身物理内存。</ul></li>
<li>用户行为信息：滑动事件、长按事件、触摸事件、点击事件、页面切换事件。</li>
<li>网络日志信息：浏览网址、网络传输速率数据、页面渲染数据。</li>
<li>应用性能信息：崩溃数据、启动信息、卡顿信息、内存监控数据。Android 版还将收集 ANR 数据、db 监控数据、io 监控数据。</li>
<li>设备标识符（第三方开发者自行生成并传入）、用户账号（第三方开发者自行生成并传入）。</li>
</ul></td>
</tr><tr>
<td>小程序 SDK</td>
<td><ul style="margin:0">
<li>设备信息：机型、系统版本、设备制造商、微信语言和版本、操作系统版本、客户端平台（Android、iOS、windows、Mac）、小程序基础库版本。</li>
<li>网络日志信息：运营商，网络 IP、网络状态。</li>
</ul></td>
</tr><tr>
<td>Web SDK</td>
<td><ul style="margin:0">
<li>设备信息：机型、系统版本、设备制造商、操作系统版本、客户端平台（Android、iOS、windows、Mac）、浏览器版本。</li>
<li>网络日志信息：运营商，网络 IP、网络状态。</li>
</ul></td>
</tr>
</tbody></table>
- **SDK 获取的权限**： 
  -   iOS 系统权限申请表
<table>
<thead>
<tr>
<th>所属权限组</th>
<th>子权限名称</th>
<th>申请目的</th>
</tr>
</thead>
<tbody><tr>
<td>连接网络信息</td>
<td>App   Transport Security Settings（连接网络）</td>
<td>用于获取到的数据正常上报到QAPM的后台。</td>
</tr>
</tbody></table>
  -   Android 系统权限申请表
<table>
<thead>
<tr>
<th>所属权限组</th>
<th>子权限名称</th>
<th>申请目的</th>
</tr>
</thead>
<tbody><tr>
<td>无</td>
<td>android.permission.INTERNET（网络权限）</td>
<td>用于获取到的数据正常上报到QAPM的后台。</td>
</tr>
<tr>
<td>无</td>
<td>android.permission.ACCESS_NETWORK_STATE（获取网络状态）</td>
<td>用于获取网络状态信息，判断当前网络是否可用。</td>
</tr>
<tr>
<td>无</td>
<td>android.permission.ACCESS_WIFI_STATE（获取Wifi状态）</td>
<td>用于获取Wifi的状态信息及WLAN热点信息，判断当前网络是否可用。</td>
</tr>
</tbody></table>

>? SDK 隐私政策请参见 [QAPM SDK 隐私政策声明](https://cloud.tencent.com/document/product/683/70822)。

**推荐条款示例**：
>我们为了实现监控和分析当前客户端的整体性能服务，集成了腾讯云客户端性能分析 QAPM SDK，需要收集、使用您的个人信息类型包括设备信息（Android 版将获取手机型号、CPU 信息、IP 地址、Wi-Fi 参数、机型、系统版本、设备制造商、设备型号、屏幕分辨率、运行内存信息、运营商、电池温度、GPU、设备媒体的编码格式、设备最大显示的尺寸、设备全部显示尺寸、SD 卡信息；iOS 版将获取 CPU 信息、IP 地址、电量、运营商、FPS、GPU、设备型号、系统版本、屏幕分辨率、运行内存信息、机身物理内存。）、用户行为信息（滑动事件、长按事件、触摸事件、点击事件、页面切换事件）、网络日志信息（浏览网址、网络传输速率数据、页面渲染数据）、应用性能信息（崩溃数据、启动信息、卡顿信息、内存监控数据，Android 版还将收集 ANR 数据、db 监控数据、io 监控数据）、设备标识符（第三方开发者自行生成并传入）、用户账号（第三方开发者自行生成并传入），及您的设备权限包括网络权限等权限。为便于您更好地理解腾讯云客户端性能分析 QAPM SDK个人信息处理规则，您可以访问 [QAPM SDK隐私保护指引](https://privacy.qq.com/document/preview/d53a0ded27a645d6addcf61f2b21abd0) 进行了解。


## 三、《隐私政策》弹出条件
您需要确保您的 App 有符合监管要求的《隐私政策》，且在终端用户首次启动 App 且 App 实际开始进行个人信息收集前弹出《隐私政策》并取得终端用户同意。终端用户进入 App 主功能界面后，通过4次以内的点击/滑动，能够访问到《隐私政策》。


## 四、请务必确保终端用户同意《隐私政策》后再初始化本 SDK
请您务必确保终端用户首次启动 App 时，通过弹窗等明显方式提示用户阅读您 App 的《隐私政策》并获得终端用户有效同意之后再初始化本 SDK。如果没有初始化本 SDK，将无法使用本 SDK 提供的服务。。

### Android 合规指引
QAPM Android SDK 不会采集 IMEI、MAC 等敏感数据，为了能够确定数据的唯一性，保证用户级指标的计算准确度，QAPM 开放以下接口供您将设备唯一标识符信息传入，调用方式可参考如下教程：
```java
// 当用户同意隐私政策协议后，方可正常初始化QAPM
if (isAgree) {    
  // 需要传入设备的唯一标识    QAPM.setProperty(QAPM.PropertyKeyDeviceId, "设备的唯一标识");    
  // 需要传入手机型号    
  QAPM.setProperty(QAPM.PropertyKeyModel, "填写手机型号");    
  // 正常初始化代码贴入，参考文档2.1部分
  初始化代码
}
```
>!
>- 初始化 QAPM Android SDK 之前需要确保用户已同意《隐私政策》，用户未同意《隐私政策》禁止初始化 QAPM Android SDK 。
>- 若传入的设备唯一标识是基于IMEI等不可变更性强的设备标识符信息生成的，需要确保已对相关信息进行不可逆的加密操作。
>- 如果设备唯一标识等信息未传入，则会影响用户级指标数据的计算，如用户崩溃率等数据有可能失真。
>-  如果未传入手机型号信息，则会影响根据手机型号聚类分析的准确度，无法根据手机型号维度聚合查看相关的崩溃率等指标。
>
在 AndroidManifiest.xml 中需要添加以下权限，若未配置可能无法正常使用 QAOM 相关功能。
```java
<!--上报信息所需-->
<uses-permission android:name="android.permission.INTERNET" />
<!--采集信息所需-->
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
```

### iOS 合规指引
QAPM iOS SDK 不会采集 UUID、Open UUID 等敏感数据，为了能够确定数据的唯一性，保证用户级指标的计算准确度，QAPM 开放以下接口由您将设备唯一标识符信息传入，调用方式可参考如下教程：
```
// 当用户授权后，方可正常初始化QAPM
if (isAgree) {
  [QAPMLaunchProfile setAppDidFinishLaunchBeginTimestamp];//启动耗时函数的第一个打点
  // 需要传入设备的唯一标识
  [QAPMConfig getInstance].deviceID = @"自定义deviceId";  
  // 可以上传设备唯一标识
  [QAPMConfig getInstance].userId = @"设置userId";  
  //您自行生成的用户账号，此接口可以多次在代码位置使用
  // 正常初始化代码贴入，参考文档2部分
}
```
>! 
>- 初始化 QAPM iOS SDK 之前需要确保用户已同意《隐私政策》，用户未同意《隐私政策》禁止初始化 QAPM。
>- 若传入的设备唯一标识是基于 UUID 等不可变更性强的设备标识符信息生成的，需要确保已对相关信息进行不可逆的加密操作。

### 小程序合规指引
1. 用户确保同意《隐私政策》之前，不初始化小程序 SDK 。
2. 在同意《隐私政策》之后，再调用初始化小程序 SDK 的方法 qapmMini SDK Start。

### Web 合规指引
1. 用户确保同意《隐私政策》之前，不初始化 Web 的 SDK。
2. 在同意《隐私政策》之后，再调用初始化 Web 的 SDK 的方法 qapmWeb SDK Start。

## 五、自定义字段功能使用说明
由于业务自身的特性不同，针对卡顿监控、ANR 监控、崩溃监控这三个功能，我们在本 SDK 的 Android 与 iOS 版中额外提供了自定义字段上报能力，您可以根据自身业务需要自行采集并通过本 SDK 上报若干信息至本 SDK 后台展示用以辅助分析问题，我们不会对该部分上报的信息进行分析，仅做传输、展示处理。若您使用了该能力，鉴于该部分信息的具体内容完全由您自行决定，请务必在您的隐私政策中说明需要采集的信息内容并履行相应的法律义务。




## 六、关闭本 SDK 
您可以告知终端用户选择关闭相应的权限，其个人信息将不会被本 SDK 处理与使用。
我们建议您在终端用户需要注销其个人信息时，您可以通过 [**腾讯云 QAPM**](https://yzf.qq.com/xv/web/static/chat/index.html?sign=37ef9b97d67d519574409ee64de3e23374aad371f460d716f55689f17061b9e422e908bdaa4cd5c7902d11ae7fb2e7b08314e07e) 直接联系我们进行处理，以便终端用户更便捷行使其权利。
