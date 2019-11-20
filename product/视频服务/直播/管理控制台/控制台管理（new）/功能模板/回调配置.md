本文档介绍如何通过 [云直播控制台](https://console.cloud.tencent.com/live) 创建回调配置。创建成功后，还需到对应的推流域名下关联 [回调配置](https://cloud.tencent.com/document/product/267/35254)，关联成功后约5分钟 - 10分钟生效。用户也可以通过 API 对直播频道创建回调模板，详细请参见 [创建回调模板](https://cloud.tencent.com/document/api/267/32637)。


## 创建回调模板
登录云直播控制台后，在左侧菜单栏选择【功能模板】>[【回调配置】](https://console.cloud.tencent.com/live/config/callback)，单击 【+】创建回调模板，在回调设置弹框中填写完成回调信息，单击【保存】即可。
![](https://main.qcloudimg.com/raw/ed2b4c922fab3274133b0b3edbf6b6a8.png)
>?
>- **回调密钥**即为客户自定义的一串字符，由大小写字母及数字组成的，最多32个字符。
>- 回调密钥的使用请参见 [事件消息通知参数说明](https://cloud.tencent.com/document/product/267/32744#.E4.BA.8B.E4.BB.B6.E6.B6.88.E6.81.AF.E9.80.9A.E7.9F.A5.E5.8F.82.E6.95.B0.E8.AF.B4.E6.98.8E)。
>- 回调协议请参见 [事件消息通知协议](https://cloud.tencent.com/document/product/267/32744#.E4.BA.8B.E4.BB.B6.E6.B6.88.E6.81.AF.E9.80.9A.E7.9F.A5.E5.8D.8F.E8.AE.AE)。

## 关联域名
创建好回调模板后，需在[【域名管理】](https://console.cloud.tencent.com/live/domainmanage)选择对应的推流域名，进入【模板配置】为该域名指定回调模板。
![](https://main.qcloudimg.com/raw/f48bb63190e06a421e78a00cdffe9b06.png)
>?
>- 如果您需要解绑回调配置，在【模板配置】中，单击【编辑】，取消相应模板的勾选，然后单击【保存】，即可将该模板与域名取消关联。
>- 控制台的回调模板管理为域名维度，暂时无法取消关联接口创建的规则，如果是通过直播回调相关接口关联指定流的，则需要通过调用 [删除回调模板](https://cloud.tencent.com/document/product/267/32635) 解除关联。
