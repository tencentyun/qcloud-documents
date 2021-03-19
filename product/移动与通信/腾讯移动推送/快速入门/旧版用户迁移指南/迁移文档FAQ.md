### 信鸽平台（https://xg.qq.com）的数据可以迁移到移动推送 TPNS 平台吗？
信鸽平台和移动推送 TPNS 平台是两个独立的平台，数据互不相通，不支持数据迁移。

### 迁移移动推送 TPNS 版本初期，做全量推送是否需要在2个平台操作？
因信鸽平台和移动推送 TPNS 平台是两个独立的平台，当升级移动推送 TPNS 版后，若您的 App 没有强制升级策略，App 覆盖需要一定时间，在新版本 App 覆盖量不足时，做全量推送，需要在信鸽和移动推送 TPNS 两个平台上都操作一次，为了避免重复推送，请您按照以下方法配置：
1. 接入 Android V1.1.5.5 及以上版本，并 [注销 Android 信鸽平台推送服务](https://cloud.tencent.com/document/product/548/41609#.E6.B3.A8.E9.94.80.E4.BF.A1.E9.B8.BD.E5.B9.B3.E5.8F.B0.E6.8E.A8.E9.80.81.E6.9C.8D.E5.8A.A1)。
2. 接入 iOS V1.2.5.3 及以上版本，并 [注销 iOS 信鸽平台推送服务](https://cloud.tencent.com/document/product/548/41610#.E6.B3.A8.E9.94.80.E4.BF.A1.E9.B8.BD.E5.B9.B3.E5.8F.B0.E6.8E.A8.E9.80.81.E6.9C.8D.E5.8A.A1)。


### 如何预估日联网设备月峰值？
日联网设备月峰值，指单日连接移动推送 TPNS 服务器的去重终端设备量（即移动推送 TPNS 可触达的设备量）在一个月内的最高值，一般是在 DAU（每日 App 前台活跃设备数）的3到5倍或 MAU（每月 App 前台活跃设备数）的1/3这个范围内，可以按照这个范围进行预估，平台支持即时升级套餐，超量后可以在 [控制台](https://console.cloud.tencent.com/tpns) 上直接升级。

### 移动推送 TPNS 版本的服务端 SDK 支持哪些语言？
目前仅支持 Java SDK，其他语言的服务端 SDK 暂时未上线。

### 移动推送 TPNS 版本支持哪些厂商通道？
目前 Android 侧支持小米、华为、魅族、vivo、OPPO 等国内主流厂商通道集成，境外支持 Google FCM 通道；iOS 支持 APNs 通道。

### 移动推送 TPNS 本如何添加子账号？
可以对子账号/协作者进行授权，授权后子账号/协作者可协助您使用移动推送 TPNS 服务，授权方法如下：

1. 进入访问管理控制台的 [策略](https://console.cloud.tencent.com/cam/policy) 页面。
2. 目前移动推送 TPNS 提供2种权限角色，您可在策略页面，搜索关键字 TPNS 进行查找。
![](https://main.qcloudimg.com/raw/8fc6c34081ceb2601687f5c4c733d35b.png)
3. 找到需要授权的预设策略，单击右侧操作列的【关联用户/组】，如下图所示：
![](https://main.qcloudimg.com/raw/c6b85e8c5210840e779b0d55fefd1691.png)
4. 在弹出的关联用户/用户组窗口，单击【切换用户组】>【用户】/【用户组】，如下图所示：
![](https://main.qcloudimg.com/raw/b0b9a631495ad64790f191574aa506f9.png)
5. 勾选要关联的用户/用户组，单击【确定】，完成关联用户操作。

### 预设策略说明

| 预设策略                                                     | 描述                                                         | 权限                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [QcloudTPNSFullAccess](https://console.cloud.tencent.com/cam/policy/detail/28456411&QcloudTPNSFullAccess&2) | 移动推送 TPNS 全局读写访问权限<br>一般分配给推送管理员使用 | <li>查看数据统计<li>创建产品<li>编辑产品信息<li>查询产品列表<li>删除产品<li>创建应用<li>编辑应用信息<li>删除应用<li>查询应用列表<li>更新厂商通道信息<li>更新推送证书<li>创建推送<li>查看推送记录<li>SDK 下载 |
| [QcloudTPNSReadOnlyAccess](https://console.cloud.tencent.com/cam/policy/detail/28459926&QcloudTPNSReadOnlyAccess&2) | 移动推送 TPNS 只读访问权限<br>一般分配给运营人员使用   | <li>查看数据统计<li>查询产品列表<li>查询应用列表<li>创建推送<li>查看推送记录<li>SDK 下载 |
