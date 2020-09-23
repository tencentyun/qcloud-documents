# Demo体验与源码解读

本章内容，将结合插件提供的一些组件，指引你完成一个简单的视频编辑demo小程序。

## demo介绍

部分功能界面截图如下：

<figure class="third">
    <image src="https://cdn.cdn-go.cn/mp-video-edit-static/latest/images/outside1.jpeg" width="200">
    <image src="https://cdn.cdn-go.cn/mp-video-edit-static/latest/images/outside3.jpeg" width="200">
    <image src="https://cdn.cdn-go.cn/mp-video-edit-static/latest/images/outside2.jpeg" width="200">
</figure>

### 功能支持

1. 视频拍摄
2. 视频裁切
3. 音乐，滤镜，特效，文字 添加
4. 视频导出

这些功能将使用到微剪插件提供的如下组件：
1. 播放器 `wj-player`
2. 照相机 `wj-camera`
3. 裁切器 `wj-clipper`
4. 导出 `wj-export`
5. 文字编辑 `wj-textEditor`

## 环境准备

### 步骤1：注册腾讯云账号
 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。 

### 步骤2：注册小程序账号
 登录 [微信公众平台](https://mp.weixin.qq.com/)，选择【帐号分类】>[【小程序】](https://mp.weixin.qq.com/cgi-bin/wx?token=&lang=zh_CN)，按接入流程注册小程序，并记录小程序的 appid。 

### 步骤3：申请插件权限
1. 在小程序管理后台的【设置】>【第三方设置】中选择【添加插件】。
2. 在弹出的面板中搜索"微剪"，选中插件并添加。


### 步骤4：购买插件使用权限
1. 登录云点播控制台，选择[【微剪插件】](https://console.cloud.tencent.com/vod/license/wecut)。
2. 根据页面提示填入小程序的 appid 等信息。

## 下载

1. 单击[ demo源码下载 ](https://imgcache.qq.com/operation/dianshi/other/demo_zip.724601d25ee9eb8b2abccf64a5855fd7ee301812.zip) 可以下载到demo小程序源码(带注释)。

2. 使用小程序 [开发者工具](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html) 打开，使用手机扫一扫即可体验

## 源码解读

### 1.工程结构

<image src="https://cdn.cdn-go.cn/mp-video-edit-static/latest/images/outside_code.png" width="600">

demo主要以微剪插件为核心，集成了一个简单的视频剪辑小程序。使用到了所有插件提供的核心组件，支持视频拍摄 => 裁切 => 编辑 => 导出 全流程。

### 2.模块介绍

此小程序按照页面功能共划分为4个核心页面模块。

1. 拍摄
2. 视频裁切
3. 视频编辑
4. 导出

#### 拍摄模块

拍摄页核心代码位于 `pages/demo/index`, 核心功能借助插件的`wj-camera`组件。

拍摄组件支持：
1. 拍摄视频
2. 选择视频
3. 选择图片

选择或者拍摄完视频之后，`wj-camera`组件会自动生成media track提供给裁切页使用。

拍摄完成后将进入 `下一步`, 进入视频裁切页。

#### 裁切模块

裁切页的核心代码位于 `pages/demo/preview`, 核心功能借助插件的`wj-clipper` 和 `wj-player`组件。

裁切组件支持：
1. 单段视频时长选择
2. 多段视频组合时长选择

进入裁切页之后，裁切器会自动生成缩略图以及拖拽式seek游标，于是就可以进行视频的时长选择了。在视频的裁切过程中，可以通过`wj-player`组件实时查看视频裁切状态。

同样的，当你裁切好视频之后，`wj-clipper`会自动生成调整之后的media track。

接下来点击`下一步`,将进入视频编辑页。


#### 视频编辑模块

视频编辑页核心代码位于 `pages/demo/edit`, 核心功能借助插件的`wj-player`组件。

编辑支持功能：
1. 音乐
2. 滤镜
3. 特效
4. 添加文字

小程序的编辑能力主要依赖于`wj-player`组件的核心方法`updateData`。
利用这个方法可以对视频进行各种编辑。

对于播放器编辑功能的使用，核心代码位于`pages/demo/edit/components`文件下面，里面分别对应了几种进行编辑的逻辑。

1. 音乐: `pages/demo/edit/components/music-list`
2. 滤镜: `pages/demo/edit/components/filter-list`
3. 特效: `pages/demo/edit/components/effect-list`
4. 文字: `pages/demo/edit/index`

文字编辑这里借助了插件提供的`wj-texteditor`,此组件可以帮助你生成文字，以及选择文字颜色和背景颜色。

视频编辑完成之后，点击`下一步`，进入导出页。

#### 导出模块

导出页核心代码位于 `pages/demo/export`, 核心功能借助插件的`wj-export`组件。

导出插件支持： 
1. 视频导出
2. 视频封面生成
3. 水印添加
4. 导出进度百分比

借助`wj-export`组件，你会发现视频的导出异常简单，只需要引入一个标签，写几行简单的js就可以完成视频导出这样的复杂功能了。js位于 `pages/demo/export/index.js`。


以上就是demo的功能以及代码介绍，建议下载代码进行阅读。这里仅仅只是抛砖引玉，实际上利用插件可以做出非常炫酷的效果。
