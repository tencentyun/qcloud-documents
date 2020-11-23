## 导出：wj-export
导出组件提供了视频导出的功能，内部复用了`wj-player`，针对小程序导出进行了专门处理。
>!受微信 Android 客户端 7.0.19 版本策略影响，导出表现偏慢，预计在11月底的版本修复。

### 使用方式
1. 配置 JSON 文件：
```
  {
      "usingComponents": {
        "export": "plugin://myPlugin/wj-export"
      }
    }
```
2. 在 wxml 中引入组件：
```wxml
  <export
      tracks="{{tracks}}"
      bindprogress="handleProgress"
      bindexportsuccess="handleExportSuccess"
      bindexportfail="handleExportFail"
      bindready="handleReady"
      bindthumbready="handleThumbReady"
      watermark="{{watermark}}"
      quality="{{quality}}"
      showloading="{{showloading}}">
      <button bindTap="startExport">导出视频</button>
  </export>
```

### 属性说明

| 属性名            | 类型                          | 默认值 | 说明                                                         | 必填 |
| ----------------- | ----------------------------- | ------ | ------------------------------------------------------------ | ---- |
| tracks            | Array&lt;Track&gt;                 | []     | 导出视频的轨道信息                                           | 是   |
| quality           | Enum('high', 'medium', 'low') | medium | 导出视频质量选项。提供 high，medium，low 三个选项。以标准16：9视频为例：<li/>high 导出分辨率为1080\*1920<li/>medium 导出分辨率为720\*1280<li/>low 导出分辨率为 540\*960 | 否   |
| showloading       | Boolean                       | false  | 是否显示默认的导出进度 toast，默认值：false                    | 否   |
| watermark         | String                        | -      | 水印地址，支持线上链接和本地临时地址 | 否   |
| watermarkX | Number | 15 | 水印基于左上角X偏移量 | 否 |
| watermarkY | Number | 15 | 水印基于左上角Y偏移量 | 否 |
| bindready         | Function                      | -      | 导出组件加载完成时触发                                       | 否   |
| bindexportstart   | Function                      | -      | 导出流程开始                                                 | 否   |
| bindprogress      | Function                      | -      | 导出进度更新<pre style="margin:0">e.detail =  {<br />progress: Number<br />} </pre>| 否   |
| bindexportsuccess | Function                      | -      | 导出成功<pre style="margin:0">{<br/> code: 0, //成功<br/>  tempFilePath: 'wxfile://xxx.mp4',<br/>  coverInfo: {<br/>    path: xxx,<br/>    width: 544,<br/>    height: 960<br/>  }, // 封面信息<br/>  video: {<br/>    width: '544', //视频分辨率<br/>    height: '960',<br/>   fps: 30, //帧率<br/>  }<br/>  duration: 3000 //单位 ms<br/>}</pre> | 否   |
| bindexportfail    | Function                      | -      | 导出失败<pre style="margin:0">{<br/>message: String,<br />error: errorStack<br />}</pre>| 否   |
| bindthumbready    | Function                      | -      | 默认封面图生成<pre style="margin:0">{<br/>path: String,<br/>height:1080,<br />width: 720<br/>}</pre> | 否   |

#### 添加水印
##### 线上地址（v1.5.0 之前版本需做以下配置，1.5.0 新增云函数支持，无需以下配置）
如果需要使用在线图片，请按如下步骤配置。
1. 在小程序根目录下引入 index.js，目录：`miniprogram/index.js`。
```
		module.exports = {
			downloadFile:wx.downloadFile
		}
```
2. 在`app.json`中将 downloadFile 方法导出到插件。
      ```json
        "plugins": {
          "myPlugin": {
            "provider": "wx76f1d77827f78beb",
            "version": "xxxx.xxx.xxx",
            "export": "index.js"
          }
        },
      ```
3. 进入小程序管理后台，将在线图片域名配置进`request`和`downloadFile`白名单即可。

##### 本地地址
传入`wxfile://`开头的本地临时地址即可。
>?导出组件提供了`slot 插槽`以定制导出组件的实际 UI，并监听内部冒泡的 tap 事件以触发导出流程；如果需要手动触发导出流程，可以使用`wx.selectComponent`获取组件实例并调用实例的`start`方法。

