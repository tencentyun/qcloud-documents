照相机 **wj-camera** 组件提供用户拍摄（前置、后置），访问相册增加 Clip（图片、视频），展示已选 Clip 列表，删除 Clip（单个删除、整体删除）等基本功能，是 Clip 的入口组件。
>?1.4.0 版本开始组件支持多段拍摄，设置倒计时等。

## 使用方式
1. 配置 JSON 文件：
```json
  {
      "usingComponents": {
        "wj-camera": "plugin://myPlugin/wj-camera"
      }
  }
```
2. 在 wxml 中引入组件：
```html
  <wj-camera bindmediachanged="onMediaChanged" clips="{{clips}}"></wj-camera>
```

## 属性说明

| 属性名           | 类型          | 默认值                  | 说明                                                   | 是否必填 |
| ---------------- | ------------- | ----------------------- | ------------------------------------------------------ | -------- |
| settings         | Object        | 参见 [settings 默认值](#camera_settings) | 设置                                                   | 否       |
| clips            | Array&lt;clip&gt;	 | []  | 初始 Clip，具体详情请参见 [clip 结构](#camera_clip)                           | 否       |
| mode            | String | simple  | simple：简单模式 </br> advanced：高级模式，支持滤镜 | 否       |
| countdown            | Number | 0  | 拍摄倒计时 | 否       |
| filter            | String | 空  | advanced 模式下使用的滤镜名称 | 否       |
| bindready        | Function      | -                       | 组件加载完成回调                                       | 否       |
| bindtapstartrecord        | Function      | -                       | 拍摄按钮点击事件                       | 否       |
| bindtapstoprecord       | Function      | -                       | 停止按钮点击事件                       | 否       |
| bindswipetoright       | Function      | -                       | 右划事件（仅 advanced 模式有效）                       | 否       |
| bindswipetoleft       | Function      | -                       | 左划事件（仅 advanced 模式有效）                      | 否       |
| bindmediachanged | Function      | -                       | 选择 Clip 的回调<pre style="margin:0" />`e.detail = {track: Array<Track>`}</pre> | 否       |

### settings 默认值<span id="camera_settings"></span>
```
  {
      videoMaxDuration: 30, // 拍摄时长限制（秒）
      clipMaxDuration: 60, // 裁切时长限制（秒）
      imgDisplayDuration: 3, // 单张图片默认展示时间（秒）
      allMediaNum: 9, // 可选Clip（图片+视频）数量限制
      videoMediaNum: 5, // 可选Clip（视频）数量限制
      defaultBgColor: '#ff584c', // 录制按钮默认状态背景色
      defaultBdColor: 'rgba(255,88,76,0.5)', // 录制按钮默认状态外边框颜色
      recordBgColor: '#fff', // 录制按钮录制状态外边框颜色
      chooseVideoIcon: './images/choose_video.png', // 选择按钮
      switchDirectionIcon: './images/switch_camera.png', // 切换按钮
      deleteRecord: './images/delete_record.png', // 拍摄界面删除按钮
      completeRecord: './images/complete_record.png' // 完成拍摄按钮
  }
```

###  clip 结构<span id="camera_clip"></span>
```
  {
    type: "image" // Clip类型：image 、video
    duration: 3 // Clip时长
    height: 200 // Clip尺寸
    width: 200 // Clip尺寸
    tempFilePath: "http://tmp/wx76f1d77827f78beb.o6zAJs6MVPjJua9TiSq8YEZReGyE.awQ1B4forrYi5f8e3e782e61d8c3a6d7b38c77946914.png" // Clip临时地址
    tempThumbPath: "http://tmp/wx76f1d77827f78beb.o6zAJs6MVPjJua9TiSq8YEZReGyE.xROdutgzbxe8f6504bf32111715b890a1eea74f8f8db.jpg" // Clip缩略图地址（可选，video类型Clip必须）
  }
```

#### 说明
- 主界面底部三个操作按钮，分别为：切换摄像头方向、拍摄、跳转相册。
- 1.4.0 版本开始支持多段拍摄，中途单击拍摄按钮会暂停并保存，再次单击继续拍摄。单击右侧【删除】可删除已拍摄片段，单击【完成】结束拍摄。
- 拍摄总时长受 **小程序平台限制，最大值为 30s**。
- 视频 Clip 数量最大值为5，Clip（图片+视频）数量最大值为9。
- Clip 展示页展示已选择或已拍摄 Clip，单击 Clip 右上角的【删除】可删除单个 Clip；单击空白处可删除全部 Clip。
- 小程序平台限制，无法在插件中直接调用`wx.navigateTo`实现页面跳转，只能使用 [navigator 组件](https://developers.weixin.qq.com/miniprogram/dev/component/navigator.html) ，故我们预留了一个`slot 插槽`供用户实现个性化跳转需求，使用方式如下：
```
  <wj-camera bindmediachanged="onMediaChanged" clips="{{clips}}">
      <view 
        class="next-btn" 
        hover-class="hover-btn" 
        catchtap="onClickNext">
          <navigator data-source="jump" url="页面路由" hover-class="none">
            <text>下一步</text>
          </navigator>
      </view>
  </wj-camera>
```
