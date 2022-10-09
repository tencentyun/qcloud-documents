
## 显示模式

通过初始化配置选项类，开启不同的显示模式：
```plaintext
var demo = COSDocPreviewSDK.config({
    mode: 'normal', 
})
```

配置选项说明如下：

| mode 选项值        | 说明                  | 是否默认选项                                                         | 
| ----------- | ------------------------------------------------------------ | -------------- | 
| normal   | 普通模式，展示所有功能界面                         | 是 | 
| simple  | 极简模式，不显示头部和工具栏                 | 否 | 
 
## 自定义配置选项

初始化 JS-SDK 时，通过分别配置不同文档对应的配置选项，可以开启或关闭文档中的特定配置以及控制文档打开时的状态。
```plaintext
COSDocPreviewSDK.config({
    //通用选项，适用于所有类型的文档。
    commonOptions: {
      isShowTopArea: false, //隐藏顶部区域（头部和工具栏）。
      isShowHeader: false //隐藏头部区域。

    },
    //WORD文档相关配置。
    wordOptions: {
      isShowDocMap: false,
      isBestScale: true
    },
    //PDF文档相关配置。
    pdfOptions: {
      isShowComment: true,
      isInSafeMode: false
    },
    //演示文档相关配置。
    pptOptions: {
      isShowBottomStatusBar: true
    }
})
```

- 通用配置项：commonOptions
<table>
	<tr><th>配置项</th><th>说明</th><th>默认值</th></tr>
	<tr><td>isShowTopArea</td><td>是否显示顶部区域（头部和工具栏）</td><td>false</td></tr>
	<tr><td>isShowHeader</td><td>是否显示头部区域</td><td>false</td></tr>
	<tr><td>isBrowserViewFullscreen</td><td>是否在浏览器区域全屏</td><td>false</td></tr>
	<tr><td>isIframeViewFullscreen</td><td>是否在 iframe 区域内全屏</td><td>false</td></tr>
</table>
- 文字文件配置项：wordOptions
<table>
	<tr><th>配置项</th><th>说明</th><th>默认值</th></tr>
	<tr><td>isShowDocMap</td><td>是否开启目录功能，默认开启</td><td>true</td></tr>
	<tr><td>isBestScale</td><td>打开文档时，默认以最佳比例显示（适用于 PC）</td><td>true</td></tr>
	<tr><td>isShowBottomStatusBar</td><td>是否展示底部状态栏（适用于 PC）</td><td>false</td></tr>
</table>
- PDF 配置项：pdfOptions
<table>
	<tr><th>配置项</th><th>说明</th><th>默认值</th></tr>
	<tr><td>isShowComment</td><td>是否显示注解，默认显示</td><td>true</td></tr>
	<tr><td>isInSafeMode</td><td>是否处于安全模式（安全模式下不能划选文字，不能复制以及不能通过链接跳转），默认不是安全模式</td><td>false</td></tr>
	<tr><td>isShowBottomStatusBar</td><td>是否展示底部状态栏（适用于 PC）</td><td>false</td></tr>
</table>
- 演示文件配置项：pptOptions
<table>
	<tr><th>配置项</th><th>说明</th><th>默认值</th></tr>
	<tr><td>isShowBottomStatusBar</td><td>是否展示底部状态栏（适用于 PC）</td><td>false</td></tr>
</table>


## 组件状态设置

可以通过 commandBars 选项来隐藏或禁用页面的组件。

```plaintext
COSDocPreviewSDK.config({
    //通用选项，适用于所有类型的文档。
    commandBars: [
      {
        cmbId: 'Print', // 组件ID
        attributes: {
          visible: false, // 组件是否显示，默认为true。false：隐藏组件；true：显示组件
          enable: false, // 禁用或者开启组件，默认为true
        },
      },
    ]
})
```

目前可用的组件列表如下：

<table>
	<tr><th>组件ID</th><th>说明</th><th>适用范围</th></tr>
	<tr><td>Print</td><td>打印功能，和 ctrl+P 打印快捷键</td><td>所有文档</td></tr>
	<tr><td>MobileHeader</td><td>客户端的顶部工具栏</td><td>所有文档</td></tr>
	<tr><td>WriterHoverToolbars</td><td>客户端的底部工具栏</td><td>文字文件</td></tr>
	<tr><td>DownloadImg</td><td>双击图片下载按钮图标</td><td>演示文件</td></tr>
	<tr><td>PlayComponentToolbar</td><td>全屏播放时右上角工具栏</td><td>演示文件</td></tr>
	<tr><td>PlayContextCheckImage</td><td>播放时右键 - 查看原图</td><td>演示文件</td></tr>
	<tr><td>FloatMenuCheckImage</td><td>选中图片时浮动菜单栏 - 查看原图</td><td>演示文件</td></tr>
	<tr><td>WPPMobileCommentButton</td><td>客户端底部工具栏的评论按钮</td><td>演示文件</td></tr>
	<tr><td>PDFMobilePageBar</td><td>客户端的页码</td><td>PDF文件</td></tr>
</table>
