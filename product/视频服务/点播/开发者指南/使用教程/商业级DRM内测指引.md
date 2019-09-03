为了满足视频平台 DRM 版权保护的需要，云点播目前提供了 [HLS 普通加密](https://cloud.tencent.com/document/product/266/9638) 方案。

但是，HLS 普通加密方案在集成和使用上有一定的复杂性，主要原因如下：

* 处理解密密钥：您的密钥服务需要对 [获取视频解密密钥](https://cloud.tencent.com/document/product/266/9643) 中获取的解密密钥进行缓存。
* 维护密钥获取地址：您需要调用 [创建 HLS 普通加密模板](https://cloud.tencent.com/document/product/266/35167) 等接口新增或修改密钥获取的地址。
* 传递身份验证信息：客户端向您的获取密钥服务请求解密密钥时，您需要验证来源用户的身份。

另外，HLS 普通加密是一种基础的 DRM 版权保护形式，在安全性上有以下缺点：

* 密钥明文暴露易遭窃取。
* 获取密钥地址易遭篡改。
* 无法指定密钥有效期。

因此，HLS 普通加密方案在易用性与安全性上亟待提升。

## 易用与安全的 DRM

商业级 DRM 是一类利用 License 实现高安全级别的版权保护系统。终端播放视频时，必须先获取 License（License 中包含解密密钥、密钥有效期及终端信息等），然后使用 License 中的密钥解密播放视频。

使用商业级 DRM 保护视频，有以下优势：

* 视频内容加密：采用 CENC 对内容加密，播放需要密钥解密。
* 密钥不可见：密钥本身被加密，仅 OS 中的解密模块能读取密钥。
* License 终端绑定：License 仅对单个终端有效，其他终端无法使用。
* License 支持过期：支持指定 License 的有效期。
* 解码过程安全：支持硬件级（TEE）解密和解码。
* 知名版权方认证：好莱坞和迪士尼认证。

云点播提供了“**转码打包 + 内容加密 + License 生成 + 密钥管理 + 解密播放**”的一站式解决方案。该方案无需您管理和维护解密密钥，只需按照云点播定义的方式对播放者授权，即可完成一整套解密播放流程，帮助您轻松实现高级别的安全保障。

## 使用商业级 DRM

- **开通**
云点播商业级 DRM 目前处于内测阶段，如果您希望体验使用，请先提交 [工单](https://cloud.tencent.com/document/product/266/19905#.E5.B7.A5.E5.8D.95.E7.B3.BB.E7.BB.9F)，由我们为您进行必要的配置。
>! 如果您需要播放 FairPlay 方式加密的视频，请参见 [ASK 和 FPS 证书](https://cloud.tencent.com/document/product/266/34102#ask-.E5.92.8C-fps-.E8.AF.81.E4.B9.A6) 完成 ASk 和 FPS 证书设置。
- **加密**
如果您需要对云点播中的视频进行加密，请参见 [视频加密](https://cloud.tencent.com/document/product/266/34072)。
- **播放**
加密后的视频，**必须使用 V3 版本超级播放器播放**：
	* [iOS V3 超级播放器](https://cloud.tencent.com/document/product/266/35585)
	* [Android V3 超级播放器](https://cloud.tencent.com/document/product/266/35584)
	* [Web V3 超级播放器](https://cloud.tencent.com/document/product/266/35586)
	
- **入门教程**
我们建议您在接入时使用 SimpleAES 方式加密（该加密方式的门槛远低于 FairPlay 和 PlayReady，且能适配大部分终端与播放器）。
请您阅读并实践 [DRM 入门教程-SimpleAES](https://cloud.tencent.com/document/product/266/35578)，完整学习接入与使用流程。

## 商业级 DRM 收费说明

使用云点播商业级 DRM 后，产生的费用主要由以下部分组成：

* 转码费用：自适应码流中各个流的转码费用，单价请参见 [价格表](https://cloud.tencent.com/document/product/266/14666#.E6.99.AE.E9.80.9A.E8.BD.AC.E7.A0.81)。
* 加密费用：自适应码流中各个流的加密费用，单价为0.015元/分钟/流。
* 获取 License 费用：播放加密视频时获取 License 的次数，单价为5.6元/千次。

例如，一位 [日结](https://cloud.tencent.com/document/product/266/14666) 用户使用转自适应码流模板 ID 为21的模板，对一个时长为1小时30分的视频进行 [视频加密](https://cloud.tencent.com/document/product/266/34072)。加密后的自适应码流包含6个规格的流（240p，480p，720p，1080p，1440p和2160p）。而且，这个视频被3万个终端解密播放（等同于获取 License 共3万次）。则费用的构成是：

* 转码费用：（0.016 + 0.016 + 0.0325 + 0.063 + 0.136 + 0.278）x 90 = 48.735元
* 加密费用：6 x 0.015 x 90 = 8.1元
* 获取 License 费用：5.6 x 30 = 168元

所以上述案例中，使用 DRM 的收费总计是：48.735 + 8.1 + 168 = 224.835元。