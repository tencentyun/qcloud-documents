本章内容，将结合插件提供的一些组件，指引您快速搭建一个简单的视频编辑 Demo 小程序。

## Demo 介绍
### 效果展示
部分功能界面截图如下：
<figure class="third">
    <image src="https://main.qcloudimg.com/raw/cb6d8301c6e6e238390af3e7111672fc.png" width="200"/>
    <image src="https://main.qcloudimg.com/raw/cca34aef6ca4defbbab0f6de3c7ad363.png" width="200"/>
    <image src="https://main.qcloudimg.com/raw/8af6a657387e167fdb74b0e592aef11b.png" width="200"/>
</figure>



### 功能支持
微剪插件支持**视频拍摄**、**视频裁切**、**添加音乐、滤镜、特效、文字效果**及**视频导出**功能，并为实现上述功能相应提供如下组件：
- 播放器 `wj-player`
- 照相机 `wj-camera`
- 裁切器 `wj-clipper`
- 文字编辑 `wj-textEditor`
- 导出 `wj-export`


## 环境准备
- 登录  [微信公众平台](https://mp.weixin.qq.com/)，注册微信小程序并获得小程序的 appid。
- 获得微剪插件使用权限。

>? 具体操作请参见 [准备工作](https://cloud.tencent.com/document/product/1156/45645)。


<span id="download"></span>
## Demo 下载
1. 单击 [GitHub](https://github.com/tencentyun/weijian-sdk/tree/master/outside-demo)，可以查看带注释的 Demo 小程序源码。
2. 使用小程序 [开发者工具](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html) 打开，使用手机扫一扫即可体验。


## 源码解读

### 工程结构
Demo 主要以微剪插件为核心，集成了一个简单的视频剪辑小程序。使用到了所有插件提供的核心组件，可实现【视频拍摄】>【裁切】>【 编辑】>【导出】全流程。
![](https://main.qcloudimg.com/raw/2353fa0bf67cff7ed55cc80c022de384.png)

### 模块介绍
此小程序按照页面功能共划分为4个核心页面模块：
- [拍摄模块](#shoot)
- [视频裁切模块](#cut)
- [视频编辑模块](#edit)
- [导出模块](#export)



#### <span id="shoot">拍摄模块</span>
- 拍摄模块支持**拍摄视频**、**选择视频**和**选择图片**功能。
- 拍摄页核心代码位于 `pages/demo/index`，核心功能借助插件的 `wj-camera` 组件。
- 选择或者拍摄完视频后，`wj-camera` 组件会自动生成 `media track` 提供给裁切页使用。

>? 拍摄完成后单击【下一步】，进入视频裁切页。

#### <span id="cut">裁切模块</span>
- 裁切模块支持**单段视频时长选择**和**多段视频组合时长选择**功能。
- 裁切页的核心代码位于 `pages/demo/preview`，核心功能借助插件的 `wj-clipper` 和 `wj-player`组件。
- 进入裁切页后，裁切器会自动生成缩略图以及拖拽式 seek 游标，可选择视频的时长。
- 视频的裁切过程中，您可通过 `wj-player` 组件实时查看视频裁切状态。
- 裁切好视频后，`wj-clipper` 会自动生成调整之后的 `media track`。

>? 视频裁切完成后单击【下一步】，进入视频编辑页。


#### <span id="edit">视频编辑模块</span>
- 视频编辑模块支持**添加音乐、滤镜、特效、文字**功能。
- 视频编辑页核心代码位于 `pages/demo/edit`，核心功能借助插件的 `wj-player` 组件。
- 小程序的编辑能力主要依赖于 `wj-player` 组件的核心方法 `updateData`。
- 播放器编辑功能的核心代码是在 `pages/demo/edit/components` 文件下，可对各相应功能的逻辑进行编辑：
	- 音乐：`pages/demo/edit/components/music-list`
	- 滤镜：`pages/demo/edit/components/filter-list`
	- 特效：`pages/demo/edit/components/effect-list`
	- 文字：`pages/demo/edit/index`
- 文字编辑功能借助插件的 `wj-texteditor`，此组件可实现生成文字，及选择文字颜色和背景颜色功能。

>? 视频编辑完成后单击【下一步】，进入导出页。

#### <span id="export">导出模块</span>
- 导出模块支持**视频导出**、**视频封面生成**、**水印添加**和**导出进度百分比**功能。
- 导出页核心代码位于 `pages/demo/export`, 核心功能借助插件的`wj-export`组件。
- 借助 `wj-export` 组件，只需引入一个标签和编写一个 js 文件即可实现视频导出功能。
	>? 示例 js 文件位于 `pages/demo/export/index.js`。


以上就是 Demo 的功能及代码介绍，建议 [下载](#download) 代码进行阅读。
