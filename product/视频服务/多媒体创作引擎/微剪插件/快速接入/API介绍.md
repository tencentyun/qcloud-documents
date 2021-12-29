快速接入会涉及两个组件，clip 组件和 export 组件，具体使用方式及组件 API 如下：

## clip 组件
clip 组件作为插件快速接入方式的入口组件，只需要将其引用到具体的业务 page 中即可，如下所示：

1. 在页面对应的配置文件 test.json 中加入以下代码，引入插件提供的 clip 组件。名称可自定义，以 my-clip 为例：
```
{
  "usingComponents": { 
    "my-clip": "plugin://myPlugin/clip" // “myPlugin”需与app.json中定义一致，“clip”为固定值
  }
}
```
2. 在页面的 wxml 文件中应用上述组件：
```
<view>
    <my-clip></my-clip>
</view>
```
3. clip 组件提供拍摄、相册及模板入口，默认为拍摄。若需要自定义初始模式，例如只保留拍摄和相册入口，且默认跳转相册，可通过注入配置的方式实现，如下所示：
>? 具体配置项请参见 [自定义配置](https://cloud.tencent.com/document/product/1156/53802) 中的配置项说明部分。
<dx-codeblock>
::: dart 
<!-- 初始化逻辑通常写在app.js中-->
const plugin = requirePlugin("myPlugin")

App({
  onLaunch: function () {
    if(plugin.initPlugin){
      const settings = {
        camera: {
          modeTypes: ['album', 'camera'], // 资源入口控制
          defaultMode: 'album', // 默认入口
        },
        // 其他配置项
      }     
		  plugin.initPlugin(settings)  // 手动初始化插件
  	}
  }
})
:::
</dx-codeblock>

## export 组件
导出组件作为插件的出口组件，用于将编辑好的视频导出至用户相册中，插件内置简单的导出页面可直接使用。若用户需要自定义导出页面UI，可以通过在目标页中引入 export 组件的方式实现，使用方式如下：

1. 在目标页面对应的配置文件 test.json 中加入以下代码引入插件提供的 export 组件，名称可自定义，如下以 my-export 为例：
```
{
  "usingComponents": {
    "my-export": "plugin://myPlugin/export" // “myPlugin”需与app.json中定义一致，“export”为固定值
  }
}
```
2. 在页面的 wxml 文件中应用上述组件：
```
<export
  showloading="{{false}}" // 导出时会自动显示loading，如不需要传false隐藏
  watermark="https://cdn-weijian-1258344699.file.myqcloud.com/images/watermark.png" //水印地址
  bindexportsuccess="handleExportSuccess" //返回导出的文件临时路径，供调用者使用
  bindprogress="handleProgress" // 导出进度更新，返回值0-100
  bindthumbready="handleThumbReady"> //导出页面预览图绘制完成回调
    	<button class="customContent">导出</button> // 自定义UI，由slot实现
</export>
```


#### 属性说明

| 属性名            | 类型                          | 默认值 | 说明                                                         | 必填 |
| ----------------- | ----------------------------- | ------ | ------------------------------------------------------------ | ---- |
| quality           | Enum('high', 'medium', 'low') | medium | 导出视频质量选项。提供 high，medium，low 三个选项。以标准16：9视频为例：<li/>high 导出分辨率为1080\*1920<li/>medium 导出分辨率为720\*1280<li/>low 导出分辨率为 540\*960 | 否   |
| showloading       | Boolean                       | false  | 是否显示默认的导出进度 toast，默认值：false                  | 否   |
| watermark         | String                        | -      | 水印地址，支持线上链接和本地临时地址                         | 否   |
| watermarkX        | Number                        | 15     | 水印基于左上角X偏移量                                        | 否   |
| watermarkY        | Number                        | 15     | 水印基于左上角Y偏移量                                        | 否   |
| bitrate           | Number                        | 2000     | 导出视频的比特率                                        | 否   |
| gop               | Number                        | 12     | 导出视频的 gop                                        | 否   |
| bindexportstart   | Function                      | -      | 导出流程开始                                                 | 否   |
| bindprogress      | Function                      | -      | 导出进度更新<pre style="margin:0">e.detail =  {<br />progress: Number<br />} </pre> | 否   |
| bindexportsuccess | Function                      | -      | 导出成功<pre style="margin:0">{<br/> code: 0, //成功<br/>  tempFilePath: 'wxfile://xxx.mp4',<br/>  coverInfo: {<br/>    path: xxx,<br/>    width: 544,<br/>    height: 960<br/>  }, // 封面信息<br/>  video: {<br/>    width: '544', //视频分辨率<br/>    height: '960',<br/>   fps: 30, //帧率<br/>  }<br/>  duration: 3000 //单位 ms<br/>}</pre> | 否   |
| bindexportfail    | Function                      | -      | 导出失败<pre style="margin:0">{<br/>message: String,<br />error: errorStack<br />}</pre> | 否   |
| bindthumbready    | Function                      | -      | 默认封面图生成<pre style="margin:0">{<br/>path: String,<br/>height:1080,<br />width: 720<br/>}</pre> | 否   |

