<!-- 目录：/开发指南/在线视频剪辑/Web Iframe 集成概述 -->

## 界面形态
Web Iframe 集成模式中，业务前端以 Iframe 方式集成剪辑界面。剪辑界面负责剪辑轨道数据的编辑与预览，视频在云端合成。示例如下，红色区域内为多媒体创作引擎剪辑页，其它为业务方界面。
![](https://qcloudimg.tencent-cloud.cn/raw/b9278016b712f6ae88435c5d0ec05ba0.png)

## 集成架构
业务架构图如下，虚线表示媒体创作引擎内部通信，实线表示与您的业务通信。
![](https://qcloudimg.tencent-cloud.cn/raw/a5268db0c5d6e8f4678f57cfc372d5e5.png)

整个业务系统涉及五部分，包括**多媒体创作引擎前端**、**业务前端**、**业务后端**、**多媒体创作引擎后端** 以及 **素材存储**。其中**多媒体创作引擎前端**与**业务前端**使用 Javascript API 进行通信，**多媒体创作引擎后端**与**业务后端**以云 API 进行通信。

## 业务流程
以腾讯云 VOD 的音视频剪辑为例按以下步骤介绍集成步骤：
1. **准备素材**：准备视频、音频、图片等素材。上传到腾讯云 VOD 。
2. **创建剪辑项目**：创建剪辑项目在业务前端将可以看到剪辑器界面，以及准备好的素材。
3. **编辑项目**：用户在剪辑器中剪辑预览。
4. **导出视频**：发起云端视频合成，生成视频。
5. **查看结果**：轮询任务，成功后，在 VOD 上查看结果。

![](https://qcloudimg.tencent-cloud.cn/raw/b1322033d1d03c332f28cedf5b0fd93c.png)

流程时序如下：

<img src="https://qcloudimg.tencent-cloud.cn/raw/1a4e5ef85ae324436d094e7ade26fbfa.png" width='960' />

>? 
> - 实线表示网络请求。
> - 虚线表示用户前端与 [媒体创作引擎剪辑 SDK](https://cloud.tencent.com/document/product/1156/43785#sdk-.E6.A6.82.E8.BF.B0) 的通信。

## 集成教程
接下来将通过具体案例，来介绍集成流程。分为如下几个步骤：
1. [准备工作](https://cloud.tencent.com/document/product/1156/65099)：密钥获取、云服务准备、示例视频准备等。
2. [后端集成](https://cloud.tencent.com/document/product/1156/65100)：搭建业务服务，为下一步前端集成提供必要的接口。
3. [前端集成](https://cloud.tencent.com/document/product/1156/65101)：集成多媒体创作引擎剪辑页面，并和上一步已经搭建好的后端服务进行通信，完成前后端联调并导出视频。

<!-- 4. [高级功能](TODO)：在完成基础教程的前提下，针对具体业务需求，进行更高级的业务开发。 -->

## 更多参考
相关 SDK 说明，请参见 [Web 在线编辑(Iframe集成)](https://cloud.tencent.com/document/product/1156/51217)。








