本文档以 Demo 为例，介绍如何将购买或自制的素材放入工程并使用。

## iOS
iOS 端 Demo 初始化资源包相关代码在 `BeautyViewModel.m`，贴纸素材列表的初始化方法是 **setupData**。

1. 将您的贴纸素材名称（目录名）放入 **_motion2DMenuIDS** 列表。
2. 将素材包拷贝到 Demo 工程中 **resources/2dMotionRes.bundle** 里，重新编译运行 Demo。

> ?贴纸所在的bundle只与展示位置有关，与贴纸类型无关。

## Android

Android 端 Demo 初始化资源包相关代码在 **XmagicResParser.java**，贴纸素材列表的初始化方法是 **parseMotion**。

1. 将您的贴纸素材名称（目录名）拼接到字符串 **motionResStr** 的任意位置（注意逗号）。
2. 将素材包拷贝到 Demo 工程中 **src/main/asstes/MotionRes/2dMotionRes** 目录下，重新编译运行 Demo。

#### 示例：
假设将您的贴纸素材文件夹命名为 **video_mymotion**，则需将：
```java
final String MotionResStr = "video_lianliancaomei:恋恋草莓," +
......
```
改为
```java
final String MotionResStr = "video_mymotion:我的贴纸," +
                            "video_lianliancaomei:恋恋草莓," +
......
```
> !素材包拷贝到其他 **xxxMotionRes** 目录均可，这个只影响贴纸在 Demo 中展示的位置，与贴纸本身的类型无关。

