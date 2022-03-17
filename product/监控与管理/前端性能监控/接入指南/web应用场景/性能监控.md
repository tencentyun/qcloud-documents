您可以通过本文了解页面测速、接口测试、资源测速的统计方式和传入配置等信息。


## 页面测速
<dx-alert infotype="explain" title="">
RUM 默认为您开启页面测速功能。
</dx-alert>


当您成功安装和初始化 SDK 后，Aegis 实例默认会上报以下指标：  

**1. DNS查询**：domainLookupEnd - domainLookupStart；  
**2. TCP连接**：connectEnd - connectStart；  
**3. SSL建连**：requestStart - secureConnectionStart；  
**4. 请求响应**：responseStart - requestStart；  
**5. 内容传输**：responseEnd - responseStart；  
**6. DOM解析**：domInteractive - domLoading；  
**7. 资源加载**：loadEventStart - domInteractive；  
**8. 首屏耗时**：监听页面打开3s内的 **首屏** DOM 变化，并认为 DOM 变化数量最多的那一刻为首屏框架渲染完成时间（SDK 初始化后 setTimeout 3s 收集首屏元素，由于 JS 是在单线程环境下执行，收集时间点可能大于 3s）；  
**9. 页面完加载时间**：为1-7项（DNS 查询、 TCP 连接、SSL 建连、请求响应、内容传输、DOM 解析、资源加载）时间总和；  

<dx-alert infotype="explain" title="">
1-7 项页面打开性能指标计算说明可从 [PerformanceTiming](https://developer.mozilla.org/zh-CN/docs/Web/API/PerformanceTiming) 获取。首屏耗时对应的 DOM 元素，可以通过打印 aegis.firstScreenInfo 查看。如果 DOM 元素不能代表首屏，可以添加属性 <code>&lt;div AEGIS-FIRST-SCREEN-TIMING&gt;&lt;/div&gt;</code>，把某个元素识别为首屏关键元素，SDK 认为只要用户首屏出现此元素就是首屏完成。也可以添加属性 <code>&lt;div AEGIS-IGNORE-FIRST-SCREEN-TIMING&gt;&lt;/div&gt;</code>，把该 DOM 列入黑名单。
</dx-alert>


根据以上数据，前端性能监控为用户绘制了页面加载瀑布图

![](https://main.qcloudimg.com/raw/c2bdd61387f8bf433d28825e645129ab.png)

<dx-alert infotype="explain" title="">
 在服务端场景，瀑布图会出现首屏时间大于 DOM 解析的情况，这是由于移动端设备兼容性问题，有些设备无法获取到 DNS 查询、TCP 连接、SSL 建连时间，这三个指标汇总后的平均值偏小，导致除了首屏时间外的其他指标都往左偏移。
</dx-alert>

## 接口测速


<dx-alert infotype="explain" title="">
打开方式：初始化时传入配置 `reportApiSpeed: true`  
</dx-alert>

Aegis 通过劫持 `XHR` 及 `fetch` 进行接口测速。

## 资源测速
<dx-alert infotype="explain" title="">
打开方式：初始化时传入配置 `reportAssetSpeed: true`  
</dx-alert>

Aegis 通过浏览器提供的 `PerformanceResourceTiming` 进行资源测速。

