[](id:toc)
通过阅读本文，你可以了解在您现有的 Android / iOS 原生开发项目中，集成腾讯云IM Flutter 的方法。

采用混合开发方案，即将Flutter模块，嵌入您的原生开发APP项目中。

**可在很大程度上，降低您的工作量，快速在双端原生APP中，植入IM通信能力。**

![](https://qcloudimg.tencent-cloud.cn/raw/af577f9cc3b02a1a02312f17cc92aa7d.png)

## 环境要求

| 环境  | 版本 |
|---------|---------|
| Flutter | IM SDK 最低要求 Flutter 2.2.0版本，TUIKit 集成组件库最低要求 Flutter 2.10.0 版本。|
|Android|Android Studio 3.5及以上版本，App 要求 Android 4.1及以上版本设备。|
|iOS|Xcode 11.0及以上版本，请确保您的项目已设置有效的开发者签名。|

## 前置知识点

在开始前，您首先需要了解腾讯云IM Flutter的SDK构成及使用方式。

主要包括两个SDK：[无UI版本](https://cloud.tencent.com/document/product/269/68823#.E7.AC.AC.E4.BA.94.E9.83.A8.E5.88.86.EF.BC.9A.E8.87.AA.E5.AE.9E.E7.8E.B0-ui-.E9.9B.86.E6.88.90)及[含UI组件库](https://cloud.tencent.com/document/product/269/70747)。本文将以 [含UI组件库（TUIKit）](https://cloud.tencent.com/document/product/269/70747) 为例，介绍混合开发方案。

**关于腾讯云IM Flutter详细用法，可从我们的 [快速入门文档](https://cloud.tencent.com/document/product/269/68823) 看起。**

## 混合开发选型

我们推荐您使用Flutter Module方式进行混合开发集成。在Native原生项目中，构建Flutter引擎，来承载Flutter中的IM及Calling模块。

对于Flutter引擎的创建管理，目前两种方式：单Flutter引擎及多Flutter引擎。、、

| 引擎模式 | 介绍 | 优点 | 缺点 |
|---------|---------|---------|---------|
| 单Flutter引擎 | IM Chat模块和Calling模块在同一个Flutter引擎中承载。 | 方便，所有Flutter代码统一维护。 | 由于Calling插件，在有电话呼入时，需要自动展示来电页面。如果在同一个引擎中，需要强制跳转用户当前页面。 |
| 多Flutter引擎 | IM Chat模块和Calling模块分别承载于不同的Flutter引擎中，使用Flutter引擎组来统一管理这两个。 | 文本3 | 文本3 |

