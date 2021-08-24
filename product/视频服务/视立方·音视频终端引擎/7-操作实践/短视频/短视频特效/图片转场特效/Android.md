腾讯云视立方短视频 UGSV SDK 在4.9版本后增加了图片编辑功能，用户可以选择自己喜欢的图片，添加转场动画、BGM、贴纸等效果。 

## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | &#10003;  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。 

## 接口函数

<dx-codeblock>
::: java java
/*

 * bitmapList：转场图片列表,至少设置三张图片（tips：图片最好压缩到720P以下（参考 demo 用法），否则内存占用可能过大，导致编辑过程异常）
 * fps：转场图片生成视频后的 fps（15 - 30）
 * 返回值：
 *       0：设置成功；
 *      -1：设置失败，请检查图片列表是否存在
 */
public int setPictureList(List<Bitmap> bitmapList, int fps);

/*
 * type：转场类型，详情见 TXVideoEditConstants
 * 返回值：
 *       duration：转场视频时长（tips：同一个图片列表，每种转场动画的持续时间可能不一样，这里可以获取转场图片的持续时长）；
 */
public long setPictureTransition(int type)
:::
</dx-codeblock>

- 其中，setPictureList 接口用于设置图片列表，最少设置三张，如果设置的图片过多，要注意图片的大小，防止内存占用过多而导致编辑异常。
- setPictureTransition 接口用于设置转场的效果，目前提供了6种转场效果供用户设置，每种转场效果持续的时长可能不一样，这里可以通过返回值获取转场的时长。
- 需要注意接口调用顺序，先调用 setPictureList，再调用 setPictureTransition。
- 图片编辑暂不支持的功能：重复、倒放、快速/慢速。其他视频相关的编辑功能，图片编辑均支持，调用方法和视频编辑完全一样。

