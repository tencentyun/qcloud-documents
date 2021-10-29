您可以通过本文了解页面测速、接口测试等信息。



## 页面测速

Aegis 小程序 SDK 会自动收集页面性能数据并上报。包括：
1. 程序启动时间。
2. 代码注入时间。
3. 页面首次渲染时间。
4. 路由切换时间。


<dx-alert infotype="notice" title="">
获取页面性能数据依赖小程序的 Performance API，请保证基础库版本大于 `2.11.0`。
QQ 小程序目前暂时不支持 Performance API，所以不会上报页面性能数据。
</dx-alert>


## 接口测速

>? 打开方式：初始化时传入配置 `reportApiSpeed: true`

Aegis 通过劫持 `wx.request || qq.request` 进行接口测速。
