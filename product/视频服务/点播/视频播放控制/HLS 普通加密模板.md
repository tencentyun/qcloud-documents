点播转码平台在对视频进行 HLS 普通加密时，会将获取解密密钥的 URL 写入视频文件 m3u8 文件的 EXT-X-KEY 标签中（详细请参见 [点播平台发起视频加密转码](https://cloud.tencent.com/document/product/266/9638)）。

HLS 普通加密模板，包含了一个唯一的模板 ID（definition）和“获取解密密钥的 URL”（get_key_url）参数。如果您需要新增、修改或查询 HLS 普通加密模板，请参考以下 HLS 普通加密模板管理 API：

* [创建 HLS 普通加密模板](https://cloud.tencent.com/document/product/266/35167)。
* [更新 HLS 普通加密模板](https://cloud.tencent.com/document/product/266/35168)。
* [查询 HLS 普通加密模板](https://cloud.tencent.com/document/product/266/35169)。

>?HLS 普通加密模板管理仅提供云点播 API 2017 接口。
