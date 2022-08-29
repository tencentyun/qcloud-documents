## 简介
**欢迎使用图像搜索 API [3.0 版本](https://cloud.tencent.com/product/api)。全新的 API 接口文档更加规范和全面，统一的参数风格和公共错误码，统一的 SDK/CLI 版本与 API 文档严格一致，给您带来简单快捷的使用体验。支持全地域就近接入让您更快连接腾讯云产品。更多腾讯云 API 3.0 使用介绍请查看：[快速入门](https://cloud.tencent.com/document/product/1278/46696)。**

图像搜索（Image Search）基于腾讯云的图像解决方案，集成了图像检索、超细粒度元素挖掘和图像匹配等技术，通过以图搜图的方式在用户自建图片库中快速检索出与输入图片相同或相似的图片集合，可应用于图片版权保护、电商侵权审核、相似素材查询、同款商品搜索与推荐等场景。

请您在使用图像搜索 API 前，确保已充分理图像搜索功能并完全同意图像搜索的计费规则，详情可参见 [计费概述](https://cloud.tencent.com/document/product/1589/74549)。
 
## 服务类型
- 相同图像搜索：针对全图的通用搜索。基于输入检索的图片，在用户自建图片库中搜索相同原图或相似图片集，并给出相似度打分，可支持经过裁剪、翻转、模糊、扭曲、滤镜调色、加水印等二次编辑后的图片搜索。
- 商品图像搜索：针对同款商品的搜索。基于输入检索的商品图片，可智能识别图片中的商品主体，在用户自建图片库中搜索相同或相似的商品图片，并给出相似度打分；如果输入检索的图片包含服饰类商品，可智能识别上衣、下装、裙装、鞋、包、配饰等多种服饰的类别、颜色以及其他特征属性。
- 相似图像搜索：针对图像元素或主体的搜索。针对输入检索的图片中包含的图案、花纹、logo等图像元素，在用户自建图片库中搜索与之相似的元素图片，并给出相似度打分。

## 图像搜索相关接口

- [创建图片库(CreateGroup)](https://cloud.tencent.com/document/api/865/63488)
- [创建图片(CreateImage) ](https://cloud.tencent.com/document/api/865/63487)
- [删除图片(DeleteImages)](https://cloud.tencent.com/document/api/865/63486)
- [查询图片库(DescribeGroups)](https://cloud.tencent.com/document/api/865/63485)
- [查询图片信息(DescribeImages)](https://cloud.tencent.com/document/api/865/63484)
- [检索图片(SearchImage)](https://cloud.tencent.com/document/api/865/63483)


## 调用方式
- [请求结构](https://cloud.tencent.com/document/api/865/35464)
- [公共参数](https://cloud.tencent.com/document/api/865/35465)
- [签名方法 v3](https://cloud.tencent.com/document/api/865/35466)
- [返回结果](https://cloud.tencent.com/document/api/865/35468)

## 数据结构

[数据结构](https://cloud.tencent.com/document/api/865/35474)

## 错误码

[错误码](https://cloud.tencent.com/document/api/865/35475)

