<!-- 目录：/开发指南/在线视频剪辑/Web Iframe 集成概述 -->

## 界面形态
Web Iframe 集成模式中，业务前端以 Iframe 方式集成剪辑界面，剪辑界面负责剪辑轨道数据的编辑与预览，视频在云端合成。示例如下，红色区域内为智能创作剪辑页，其它为业务方界面。

<img src="https://qcloudimg.tencent-cloud.cn/raw/b9278016b712f6ae88435c5d0ec05ba0.png" width="960">

## 集成架构
业务架构图如下，虚线表示智能创作内部通信，实线表示与您的业务通信。

<img src="https://qcloudimg.tencent-cloud.cn/raw/83a7f4235f00cf2b2a85fe56989d2578.png" width="960">

整个业务系统涉及五部分，包括**智能创作前端**、**业务前端**、**业务后端**、**智能创作后端** 以及 **素材存储**。其中**智能创作前端**与**业务前端**使用 Javascript API 进行通信，**智能创作后端**与**业务后端**以云 API 进行通信。

## 业务流程
以腾讯云 VOD 的音视频剪辑为例按以下步骤介绍集成步骤：
1. **准备素材**：准备视频、音频、图片等素材。上传到腾讯云 VOD 。
2. **创建剪辑项目**：创建剪辑项目在业务前端将可以看到剪辑器界面，以及准备好的素材。
3. **编辑项目**：用户在剪辑器中剪辑预览。
4. **导出视频**：发起云端视频合成，生成视频。
5. **查看结果**：轮询任务，成功后，在 VOD 上查看结果。

<img src="https://qcloudimg.tencent-cloud.cn/raw/b1322033d1d03c332f28cedf5b0fd93c.png" width="960">

流程时序如下：

<img src="https://qcloudimg.tencent-cloud.cn/raw/1a4e5ef85ae324436d094e7ade26fbfa.png" width='960' />

>? 
> - 实线表示网络请求。
> - 虚线表示用户前端与 [智能创作剪辑 SDK](https://cloud.tencent.com/document/product/1156/65101#SDK_API) 的通信。

## 集成教程
接下来将通过具体案例，来介绍集成流程。分为如下几个步骤：
1. [准备工作](https://cloud.tencent.com/document/product/1156/65099)：开通腾讯云 VOD 服务、创建智能创作平台、密钥获取、准备示例视频等。
2. [后端集成](https://cloud.tencent.com/document/product/1156/65100)：搭建业务服务，为下一步前端集成提供必要的接口。
3. [前端集成](https://cloud.tencent.com/document/product/1156/65101)：集成智能创作剪辑页面，并和上一步已经搭建好的后端服务进行通信，完成前后端联调并导出视频。

## 集成 Demo

为方便业务集成参考，智能创作团队提供了集成 Demo，具体使用请参见 [在线编辑 Demo 使用说明](https://cloud.tencent.com/document/product/1156/71276)。
