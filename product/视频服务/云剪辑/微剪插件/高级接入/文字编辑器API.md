文字编辑 **wj-textEditor** 组件是一个简单的模拟原生输入框的组件，用于向视频中添加文本贴纸。支持动态修改文本的颜色、背景色及字体（1.4.0 版本新增），提供实时预览功能。

## 使用方式
1. 配置 JSON 文件：
```json
  { 
    "usingComponents": {
      "wj-textEditor": "plugin://myPlugin/wj-textEditor"
    }
  }
```
2. 在 wxml 中引入组件：
```wxml
  <wj-textEditor value="{{textValue}}" bindconfirm="onConfirmText"/>
```
3. 字体的下载需要借助小程序的 loadFontFace 方法，需要在`index.js`中，将 loadFontFace 方法通过 exports 输出。
```
module.exports = {
  downloadFile:wx.downloadFile,
  loadFontFace:wx.loadFontFace
}
```
在`app.json`中将 loadFontFace 方法导出到插件。
```json
"myPlugin": {
  "provider": "wx76f1d77827f78beb",
  "version": "1.4.3",
  "export": "index.js"
}
```
4. 在您的小程序开发者后台，配置`reuqest`和`downloadFile`加入域名 `https://cdn.cdn-go.cn`当中。

## 属性说明

| 属性名      | 类型     | 默认值           | 备注                                                         | 必填 |
| ----------- | -------- | ---------------- | ------------------------------------------------------------ | ---- |
| show       | Boolean   | false           | 是否显示输入组件                                                    | 是   |
| value       | String   | 空               | 文本内容                                                     | 否   |
| color       | String   | #fff             | 字体颜色，标准 css 颜色值，默认白色                            | 否   |
| bgColor     | String   | transparent      | 背景色，标准 css 颜色值，默认透明                              | 否   |
| fontStyle     | Object   | {fontfamily:'moren',fonturl:''}      |  {fontfamily:字体名称标识（字母）,fonturl:字体文件地址}  | 否   |
| colorList   | Array    | 组件默认颜色集合 | [{key：唯一标识，value：标准 css 颜色值}]                      | 否   |
| fontList   | Array    | 组件默认字体集合 | [{name: 字体名称（汉字）,family: 字体名称标识（字母） ,url: 字体文件地址}]                      | 否   |
| bindconfirm | Function | -                | 用户输入完成：<pre style="margin:0">e.detail = { value: 文本内容, <br/>color: 文本颜色, <br/>bgColor: 背景色, <br/>showTextBg: 是否显示背景色 <br/>family: 字体名称,<br/>fontUrl: 字体文件地址,<br/>fontloaded: 是否已下载字体文件<br/>} </pre>| 否   |
| bindclose   | Function | -                | 用户取消输入                                                 | 否   |

## 操作说明
输入文字，单颜色列表实时更换文本颜色，单击左侧 T 图标实时更换背景颜色。
>?
>- 1.4.0 版本开始支持修改字体。
- 1.4.3 版本优化了字体缓存的逻辑，请避免使用`wx:if`控制`wj-textEditor`的显示，推荐使用`show`属性来控制以达到更好的加载性能。

