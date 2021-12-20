Aegis SDK 使用 flog 管理离线日志，用户只需要简单配置就可以使用


1. 在 SDK 中开启离线日志参数。
<dx-codeblock>
:::  js
new Aegis({
  id: '', // 用户在TAM平台上申请的上报key
  uin: 'xxxx', // 必须有 uin 才可以上报离线日志，如果一开始获取不到，后面可以通过 setConfig 设置
  offlineLog: true, // 开启离线日志
})
:::
</dx-codeblock>
离线日志开启后，用户的日志就会被收集到浏览器的 IndexedDB 中，但是并不会实时上报，需要开发者对用户 UIN 进行监听。
2. 进入 [前端性能监控控制台](https://console.cloud.tencent.com/rum) **离线日志**页面，单击**设置离线监听**，输入对应用户的 UIN 进行监听。
![](https://main.qcloudimg.com/raw/12e4608aee8a33e681132f4677fdc727.png)
3. 当用户下次打开页面或者代码中执行 setConfig 的时候，用户将日志上报到 RUM 服务端，并且用户侧会发两个接口：
	-  `aegis.qq.com/collect/offlineAuto` ：判断是否要发送离线日志，并且返回加密 token。
	-   `aegis.qq.com/collect/offlineLog` ：上报当前用户 indexedDB 中存放的离线日志。
4. 单击下拉菜单，选择对应的离线日志，单击**搜索**查看日志。
![](https://main.qcloudimg.com/raw/7b103d2881ba0e6f8521ec9800ebbc76.png)
