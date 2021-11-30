>!本文档是旧版加密文档，已不再推荐使用。强烈建议您使用 [最新的点播加密方案](https://cloud.tencent.com/document/product/266/43632)。

云点播转码平台在对视频进行 HLS 普通加密时，会将获取解密密钥的 URL 写入 M3U8 视频文件的`EXT-X-KEY`标签中，详细请参见 [HLS 普通加密](https://cloud.tencent.com/document/product/266/9638)。

HLS 普通加密模板，包含`definition`（唯一的模板 ID）和`get_key_url`（获取解密密钥的 URL）参数。如果您需要新增、修改或查询 HLS 普通加密模板，请参考以下 HLS 普通加密模板管理 API：

* [创建 HLS 普通加密模板](https://cloud.tencent.com/document/product/266/35167)
* [更新 HLS 普通加密模板](https://cloud.tencent.com/document/product/266/35168)
* [查询 HLS 普通加密模板](https://cloud.tencent.com/document/product/266/35169)

>?HLS 普通加密模板管理仅提供云点播 API 2017 接口。


