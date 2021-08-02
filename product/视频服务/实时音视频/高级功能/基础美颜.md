TRTC 提供了美颜滤镜功能以及美颜插件的集成，通过美颜滤镜或者插件，可以实现自然的美颜效果。

## 开启美颜
您可以 [单击此处](https://web.sdk.qcloud.com/trtc/webrtc/test/latest/beauty/index.html) 体验 Web 端美颜效果。

## 前提条件
Web 平台美颜插件支持以下浏览器：
<table>
<tr><th>浏览器</th><th>版本</th></tr>
<tr>
<td>Chrome</td><td>65+</td>
</tr><tr>
<td>Firefox</td><td>70+</td>
</tr><tr>
<td>Safari</td><td>12+</td>
</tr><tr>
<td>Edge</td><td>80+</td>
</tr><tr>
<td>移动端浏览器</td><td>不支持</td>
</tr><tr>
<td>微信内嵌网页</td><td>不支持</td>
</tr></table>

使用 `RTCBeautyPlugin` 时，请将 TRTC Web SDK 升级到 4.11.1 及以上版本。
在项目中安装 [RTCBeautyPlugin](https://www.npmjs.com/package/rtc-beauty-plugin) 插件。
```shell
npm install rtc-beauty-plugin
```

## 集成说明
### 步骤1：创建 RTCBeautyPlugin 实例

一个 RTCBeautyPlugin 实例只能用来处理一条本地音视频流。

```javascript
const beautyPlugin = new RTCBeautyPlugin();

// 调节美颜插件的美颜程度（ 0 - 1 ）
beautyPlugin.setBeautyParam({ beauty: 0.5, brightness: 0.5, ruddy: 0.5 });
```

### 步骤2：使用 RTCBeautyPlugin 的实例处理需要发布的流

```javascript
// 生成美颜后的流
const beautyStream = beautyPlugin.generateBeautyStream(localStream);

// 发布经过美颜后的流
await client.publish(beautyStream);
```

### 步骤3：通话结束后，销毁美颜插件

在通话结束之后，可以销毁美颜插件，避免内存占用和性能消耗。

```javascript
// 通话结束
await client.leave();

// 销毁插件，释放内存
beautyPlugin.destory();
```

## 注意事项
1. 一个 `RTCBeautyPlugin` 实例只能处理一条本地流。
2. 使用 `replaceTrack` 等操作会导致您的 `localStream` 美颜效果消失，请酌情使用。


