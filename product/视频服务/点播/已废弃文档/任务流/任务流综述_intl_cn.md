## 任务流简介

不同的业务场景，要求我们对视频文件进行不同的处理。比如一家游戏直播网站，会将直播的内容录制成为点播视频，然后转码，再截取图片作为封面；而一个做教育视频的网站，则是在服务端上传完视频后进行转码，同时对视频进行打水印或加密以保护产权。对于某个特定的场景，视频处理流程一般是固定的，如果开发者对每一个视频的每一次处理都分别调用一次服务端 API，那么开发过程会变得很复杂。
为了解决这一问题，云点播提供了 ***视频处理任务流*** 机制：云点播根据最常用的业务场景，预先将一系列具体的视频处理流程定义为任务流，开发者只需要调用相关的任务流接口即可对指定视频进行一系列的处理操作，而无需分别调用独立的视频处理接口。

## 任务流示意图
任务流机制的实现基于[视频处理参数模版](/document/product/266/10383)，他们之间的关系举例如下：
1. 任务流：转码
![](//mc.qcloudimg.com/static/img/e7abf100655ab5766d3c8fe5c77365dc/image.jpg)

2. 任务流：采样截图
![](//mc.qcloudimg.com/static/img/4f8d2128622783736aeb4b5a00b050ae/sample.jpg)

3. 任务流：转码-水印-采样截图 
![](//mc.qcloudimg.com/static/img/2eae18c9ab9e90171e95227b8a108341/r.jpg)


## 预设任务流 
云点播的预设任务流包括下述几种使用场景。

| 场景 | 使用方式 | 示例 |
|---------|---------|---------|
| 服务端上传 | 在发起上传API中携带任务流参数：procedure。详情见[VOD发起上传API](/document/product/266/9756) |procedure=[QCVB_SimpleProcessFile](/document/product/266/10277)(1,0,0,0)| 
| 客户端上传 | 在上传签名中携带任务流参数：procedure。详情见[客户端上传签名](/document/product/266/9221) | procedure=[QCVB_SimpleProcessFile](/document/product/266/10277)(1,0,0,0)|
| 直播录制 | 推流时携带任务流参数：vod_procedure | vod_procedure=[QCVB_SimpleProcessFile](/document/product/266/10277)(1,0,0,0)|

## 对已有视频进行处理

### 依照指定任务流处理视频
参见文档[依照指定流程处理视频文件](/document/product/266/9045)

### 对视频文件进行处理
参见文档[对视频文件进行处理](/document/product/266/9642)

## 获取任务流结果
1. 任务流状态变更（或者处理完成）会触发[事件通知-任务流状态变更通知](/document/product/266/9636)。APP后台可据此监听任务流的执行状态。
2. 任务流执行完毕之后，任务结果可以从[GetVideoInfo](/document/product/266/8586)中获取。
