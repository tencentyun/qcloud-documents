

构建专属图标库前，如果您还不了解如何通过设计工具插件端 Adobe Illustration、Sketch、Adobe XD 及图标网站，上传 svg 文件，希望以下内容对您有所帮助。

## 导出 SVG 前的准备

在导出 SVG 之前，先按照以下三个原则对图标进行处理：
- 闭合：图标路径锚点要处于封闭状态。
<img src="https://cdn.codesign.qq.com/hcimages/202111/6b178251-d2cb-4bc5-a255-ddb8c5aa8838.png" width="60%">

- 合并：如果有多个图形进行组合，要对图形合并扩展。
<img src="https://cdn.codesign.qq.com/hcimages/202111/28a97f40-5edd-4612-9e67-1e1fbbde9e49.png" width="60%">

- 轮廓化：要将描边转化为闭合图形，填充颜色。
<img src="https://cdn.codesign.qq.com/hcimages/202111/37914696-6026-4ae1-a814-2ff647a7b929.png" width="60%">

**关于多色图标**

团队图标库支持多色图标、多图层图标与多路径图标上传，上传时尽可能对同颜色的形状进行轮廓化处理
<img src="https://cdn.codesign.qq.com/hcimages/202111/fab988b3-9d15-4bb6-b3f9-cf88daca5528.png" width="60%">


## 从 Adobe Illustration 导出 SVG

Illustrator 导出 SVG 时，需要设置参数，有以下两种导出方法：

## 使用「资源导出」功能
>?Illustrator CC 2018 及之后的版本提供「资源导出」功能，方便导出各种格式资源。

点击 Illustrator 内容栏上的文件 > 导出 > 导出为 多种屏幕所用格式。
<img src="https://cdn.codesign.qq.com/hcimages/202111/26f9dd53-e49e-45ea-9ab2-ac228e9adc3b.png" width="60%">

在设置窗口中，选择导出格式为「SVG」后，要点击 ⚙ 进行设置。
<img src="https://cdn.codesign.qq.com/hcimages/202111/4ceaac8d-8ee9-4f4e-9874-f05a10823d89.png" width="60%">

在格式设置中进行以下设置（这个设置是会保留的，只要设置一次以后都会默认这个设置）：
- 样式 - 内联样式
- 图像 - 保留
- 缩小&响应 - 不勾选

点击储存设置后进行导出。
<img src="https://cdn.codesign.qq.com/hcimages/202111/ff9334b7-28b4-487d-bc82-95c9250fad72.png" width="60%">

## 使用「存储为」功能

>?由于每次导出后都需要重新设置选项，所以不推荐使用这个方法。

点击 Illustrator 内容栏上的文件>储存为
<img src="https://cdn.codesign.qq.com/hcimages/202111/2cefe46c-ea1e-45e7-b48c-4c8c7beb1054.png" width="60%">

选择格式 SVG，根据自己的资源情况来判断是否使用画板
<img src="https://cdn.codesign.qq.com/hcimages/202111/75be6e7e-08a5-445e-89ab-292a197b7a25.png" width="60%">

在弹出的选项菜单中，按照下图中的选项进行配置，顺利导出正确的 SVG
<img src="https://cdn.codesign.qq.com/hcimages/202111/854c815d-ac63-4da8-9ab1-0664d3fd3948.png" width="60%">


## 从 Sketch 导出 SVG

Sketch 中已经默认对 SVG 做了一些设置，只要格式选择 SVG ，即可顺利导出。
<img src="https://cdn.codesign.qq.com/hcimages/202111/9edd9b6d-3a56-4390-b6db-36c7681615b2.png" width="60%">


## 从 Adobe XD 导出 SVG

点击 Adobe XD 内容栏左上角的导出>所选内容
<img src="https://cdn.codesign.qq.com/hcimages/202111/118d5259-d6c9-434d-9b84-a91da0d7367a.png" width="60%">

选择格式 SVG，点击导出即可。
<img src="https://cdn.codesign.qq.com/hcimages/202111/9af4f977-84e2-4880-8db4-5652473f6812.png" width="60%">


## SVG 文件上传

点击进入图标库，点击左上角「新建图标库」按钮。
<img src="https://cdn.codesign.qq.com/hcimages/202111/56461152-99b6-4a03-b7b5-e8305bd2e0d3.png" width="60%">


根据项目或团队情况填写名称和简介，其中：
- iconfont 前缀 可以填写项目或团队的英文简写
- iconfont family 可以填写项目或团队的英文简写+ font
<img src="https://cdn.codesign.qq.com/hcimages/202111/25ec4914-26ec-4acd-968d-1b9893a95a77.png" width="60%">


点击立即创建，创建完成后会自动跳转详情页，点击左上角按钮可以上传 SVG 文件；
<img src="https://cdn.codesign.qq.com/hcimages/202111/b175ed57-ec15-4794-8b2f-f62c5afbb74b.png" width="60%">


在上传页可以通过拖拽批量上传 SVG 文件；
<img src="https://cdn.codesign.qq.com/hcimages/202111/c327e5f2-1ea4-4d38-8e23-1f2b2b7885b2.png" width="60%">


上传后在图标预览区确认上传的图标是否出现异常情况，如果发生图标变形错位，需要检查一下图标的路径锚点和导出设置是否符合「闭合」、「合并」、「轮廓化」。

同时确认一下要上传到的图标库是否符合预期，根据情况可以选择：
- 去除颜色上传 - 图标将被统一填充为 `#000000`
- 保留颜色上传 - 将保留图标的原始配色

<img src="https://cdn.codesign.qq.com/hcimages/202111/763fe9ff-86c8-4c70-8a9a-5816060470f8.png" width="60%">
