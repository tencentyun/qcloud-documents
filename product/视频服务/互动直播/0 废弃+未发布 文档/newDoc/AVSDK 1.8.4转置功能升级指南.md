## AVSDK 1.8.4转置功能升级指南

### 名词解释

* 转置：终端app根据手机的重力传感器的反馈，把采集的视频内容进行旋转，保持正向角度。

### 背景

由于视频采集端和播放端各自都有独立的角度变化，会造成视频播放的时候经常出现和采集端画面不一致的情况。这个看似简单的问题在叠加了前后摄像头切换、画面裁剪拉伸、录制、不同的播放要求等变量后，会变得异常复杂。

为了解决这个问题，AVSDK从1.8.2开始，逐步完善了对视频采集和播放的转置能力，在1.8.4版本中有了全面的解决方案。

此文档旨在为开发者提供从AVSDK当前版本升级到1.8.4中可能遇到的兼容性问题提供解决方案。

##### 如果您使用的是iLive SDK，则不需要考虑这个问题。

## 升级AVSDK 1.8.4可能遇到的转置兼容性问题

未开客户端转置以前的版本，观看AVSDK 1.8.4的版本开了客户端转置的视频时，视频有可能被拉伸或者旋转。


## 如何解决这个兼容性问题

### 一 从1.8.1之前的版本（包含1.8.1）升级：

不建议直接升级1.8.4, 需要先升级到1.8.2。步骤如下：

1. 升级AVSDK到1.8.2,并将转置开关设置为关(iOS把QAVMultiParam的autoRotateVideo为NO，Android设置AVRoomMulti.EnterParam.Builder.isDegreeFixed为false)
2. 参考附录中的指南升级ios OpenGL渲染代码。
3. 新app与线上使用AVSDK1.8.1的app进行联调，调试好渲染逻辑，并做好iOS/Android互看适配工作；
4. 待基于AVSDK 1.8.2版本的app普及后，启动AVSDK1.8.4的升级；
5. 在腾讯云后台提交[工单](https://console.cloud.tencent.com/workorder/category/create?level1_id=29&level2_id=37&level1_name=%E8%A7%86%E9%A2%91%E4%B8%8E%E9%80%9A%E4%BF%A1%E6%9C%8D%E5%8A%A1&level2_name=%E4%BA%92%E5%8A%A8%E7%9B%B4%E6%92%AD%20%20ILVB)，问题类型选择`其他问题`，问题描述填写`添加转置白名单申请-公司名-腾讯云账号(XXXXXXX)-申请白名单的sdkappid(XXXXXXX)`；
6. 待工单处理完毕，升级AVSDK 1.8.4,并做好iOS/Android互看适配工作，以及与线上版本兼容测试；
7. 待基于AVSDK 1.8.4版本的app普及后，提交[工单](https://console.cloud.tencent.com/workorder/category/create?level1_id=29&level2_id=37&level1_name=%E8%A7%86%E9%A2%91%E4%B8%8E%E9%80%9A%E4%BF%A1%E6%9C%8D%E5%8A%A1&level2_name=%E4%BA%92%E5%8A%A8%E7%9B%B4%E6%92%AD%20%20ILVB)，问题类型选择`其他问题`，问题描述填写`移除转置白名单申请-公司名-腾讯云账号(XXXXXXX)-申请白名单的sdkappid(XXXXXXX)`；



### 二 . 从1.8.2版本升级：

如果客户端的转置开关是关闭的(iOS把QAVMultiParam的autoRotateVideo为NO，Android设置AVRoomMulti.EnterParam.Builder.isDegreeFixed为false)，那么：

1. 在腾讯云后台提交[工单](https://console.cloud.tencent.com/workorder/category/create?level1_id=29&level2_id=37&level1_name=%E8%A7%86%E9%A2%91%E4%B8%8E%E9%80%9A%E4%BF%A1%E6%9C%8D%E5%8A%A1&level2_name=%E4%BA%92%E5%8A%A8%E7%9B%B4%E6%92%AD%20%20ILVB)，问题类型选择`其他问题`，问题描述填写`添加转置白名单申请-公司名-腾讯云账号(XXXXXXX)-申请白名单的sdkappid(XXXXXXX)`；
2. 待工单处理完毕，升级AVSDK 1.8.4，并参考附录中的指南升级ios OpenGL渲染代码。
3. 做好iOS/Android互看适配工作，以及与线上版本兼容测试；
5. 待基于AVSDK 1.8.4版本的app普及后，提交[工单](https://console.cloud.tencent.com/workorder/category/create?level1_id=29&level2_id=37&level1_name=%E8%A7%86%E9%A2%91%E4%B8%8E%E9%80%9A%E4%BF%A1%E6%9C%8D%E5%8A%A1&level2_name=%E4%BA%92%E5%8A%A8%E7%9B%B4%E6%92%AD%20%20ILVB)，问题类型选择`其他问题`，问题描述填写`移除转置白名单申请-公司名-腾讯云账号(XXXXXXX)-申请白名单的sdkappid(XXXXXXX)`；


否则：

1. 升级AVSDK 1.8.4，并参考附录中的指南升级ios OpenGL渲染代码；
2. 待基于AVSDK 1.8.4版本的app普及后，提交[工单](https://console.cloud.tencent.com/workorder/category/create?level1_id=29&level2_id=37&level1_name=%E8%A7%86%E9%A2%91%E4%B8%8E%E9%80%9A%E4%BF%A1%E6%9C%8D%E5%8A%A1&level2_name=%E4%BA%92%E5%8A%A8%E7%9B%B4%E6%92%AD%20%20ILVB)，问题类型选择`其他问题`，问题描述填写`移除转置白名单申请-公司名-腾讯云账号(XXXXXXX)-申请白名单的sdkappid(XXXXXXX)`；

### 三 . 从1.8.3版本升级：

1. 在腾讯云后台提交[工单](https://console.cloud.tencent.com/workorder/category/create?level1_id=29&level2_id=37&level1_name=%E8%A7%86%E9%A2%91%E4%B8%8E%E9%80%9A%E4%BF%A1%E6%9C%8D%E5%8A%A1&level2_name=%E4%BA%92%E5%8A%A8%E7%9B%B4%E6%92%AD%20%20ILVB)，问题类型选择`其他问题`，问题描述填写`查询转置白名单申请-公司名-腾讯云账号(XXXXXXX)-申请白名单的sdkappid(XXXXXXX)`；
2. 收到工单回复后，

**如果转置开关是打开的:**

* 升级AVSDK 1.8.4，并参考附录中的指南升级ios OpenGL渲染代码；
* 进行iOS/Android互看适配工作，以及与线上版本兼容测试；
* 测试完成后，升级AVSDK 1.8.4版本到现网；

**如果转置开关是关闭的:**

* 进行iOS/Android互看适配工作，以及与线上版本兼容测试；
* 测试完成后，升级AVSDK 1.8.4版本到现网；
* 待基于AVSDK 1.8.4版本的app普及后，提交[工单](https://console.cloud.tencent.com/workorder/category/create?level1_id=29&level2_id=37&level1_name=%E8%A7%86%E9%A2%91%E4%B8%8E%E9%80%9A%E4%BF%A1%E6%9C%8D%E5%8A%A1&level2_name=%E4%BA%92%E5%8A%A8%E7%9B%B4%E6%92%AD%20%20ILVB)，问题类型选择`其他问题`，问题描述填写`移除转置白名单申请-公司名-腾讯云账号(XXXXXXX)-申请白名单的sdkappid(XXXXXXX)`；

### 四 自定义采集与渲染

自定义采集注意点：

* ios调用fillExternalCaptureFrame时，SDK底层会自动补充角度值；
* Android刚需要自己手动填写角度值（具体值可参考[角度方案](https://github.com/tencentyun/qcloud-documents/blob/master/product/%E8%A7%86%E9%A2%91%E6%9C%8D%E5%8A%A1/%E4%BA%92%E5%8A%A8%E7%9B%B4%E6%92%AD/newDoc/%E8%A7%92%E5%BA%A6%E6%96%B9%E6%A1%88.md)）。**要保证在互通时画面方向正确，Android端首先参考[考角度方案](https://github.com/tencentyun/qcloud-documents/blob/master/product/%E8%A7%86%E9%A2%91%E6%9C%8D%E5%8A%A1/%E4%BA%92%E5%8A%A8%E7%9B%B4%E6%92%AD/newDoc/%E8%A7%92%E5%BA%A6%E6%96%B9%E6%A1%88.md)填对之后，这样SDK才不会将画面转置出错；**;
* 在不开转置情况下：fillExternalCaptureFrame里填入的角度值是多少，传给观众的值就是多少；
* 在开转置情况下：主播在fillExternalCaptureFrame之后，SDK还会对画面进行转置，并修改角度值为0, 然后上行视频数据包，这样传给观众的就一直是0, 观众端需要根据宽高来判断是否有横屏；

自定义渲染注意点：

* 因之前的的画面都带有角度值，业务方主要是根据角度值来确定画面方向。
* AVSDK1.8.4 在开转置之后，传入的方向始终为0, 那么用户需要根据画面的宽高比来确定是否为横竖屏：`宽>高为横屏`，`宽 < 高为竖屏`。用户要在之前适配好渲染逻辑的代码里面，补充好宽高比来确定是否为横竖屏逻辑。

**如果只做了自定义采集，但没有自定义渲染的用户，渲染部分还是可以参考附录中的指南升级ios OpenGL渲染代码**；

在确认好以上两部分修改后，做好与老版本的兼容测试，然后升级到现网。


## 附录 OpenGL代码升级指南

1. 更新[随心播](https://github.com/zhaoyang21cn/iOS_Suixinbo)代码，
2. 参考随心播opengl代码，替换以下内容
	
	![](https://mc.qcloudimg.com/static/img/94f24136772e38c77fe40a1968163539/mergeopengl.png)
	
3. 如果开发者的渲染代码已经自己修改过，那么参考2中替换项，并根据自身需要进行同步（核心逻辑在TCAVFrameDispatcher和AVGLCustomRenderView中）。