API 监控为您提供 HTTP Code 成功率、API 请求耗时等调用情况监控，本文将为您介绍如何 API 监控。
## 操作前提
已完成 [应用接入](https://cloud.tencent.com/document/product/1464/58145)。

## 操作步骤 
1. 登录 [前端性能监控控制台](https://console.cloud.tencent.com/rum)。
2. 在左侧菜单栏中单击 **API 监控**。
3. 进入 API 监控页面即可查看 API 性能情况。

### 汇总分析
展示 API 性能关键指标变化趋势图，包括 API 耗时、成功率等。
- 单击上方的图例可取消或展示对应的数据。
- 支持按时间段或近14天粒度展示变化趋势图。
- 在曲线中拖动鼠标可展示某一时刻 API 耗时。
- 鼠标移动到圆形位置并左右拖动圆形，可调整图表时间跨度。
![](https://main.qcloudimg.com/raw/8f598b372c090dcd109bc61ea51d0502.png)

### 页面分析
该页面展示各页面接口平均耗时情况。
![](https://main.qcloudimg.com/raw/467ce76fb4c9fdddb2d64ca877755dec.png)

###  TOP 视图
- API 请求 TOP 视图，按接口耗时排序展示 API 请求情况，最多可展示1000个 API。
- HTTP Status Code 40x TOP 视图：按 HTTP Status Code 40x 错误数排序展示，最多可展示1000个 API。
- HTTP Status Code 50x TOP 视图：按 HTTP Status Code 50x 错误数排序展示，最多可展示1000个 API。
![](https://main.qcloudimg.com/raw/5c2419b94cebd5d61e0a1252bd9de8af.png)

### 其它视图
|视图名称|说明 |
|---------|---------|
| 网络/平台视图 | 用饼图形式展示来自各区域的 API 请求数量、占比及平均耗时 。其中网络包括3G、4G、WIFI 等，平台包括 Macos、Windows、IOS 等|
|HTTP 响应码视图|用饼图形式展示各 HTTP 响应码的错误数量、占比及平均耗时。 |
| retcode 视图 |用饼图形式展示各 retcode 码的错误数量、占比及平均耗时。|
| ISP 视图| 用饼图形式展示来自各运营商的 API 请求数量、占比及平均耗时。运营商包括移动，电信、联通等。| 
| 地区视图 | 用饼图形式展示来自各区域的 API 请求数量、占比及平均耗时。 | 
|品牌/机型视图|用饼图形式展示来自手机品牌/机型的 API 请求数量、占比及平均耗时。|
|浏览器视图|用饼图形式展示来自各浏览器的 API 请求数量、占比及平均耗时。|
|Version 视图| 用饼图形式展示来自各应用版本的 API 请求数量、占比及平均耗时。您可以通过在接入应用时的 new Aegis 传入 version 来自定义研发相关的版本信息，默认使用 SDK 的版本。|
|Ext1 视图、Ext2 视图、Ext3 视图|自定义视图，由您自定义上报时传入参数。详情请参见 [接入指南](https://cloud.tencent.com/document/product/1464/58548)。|


