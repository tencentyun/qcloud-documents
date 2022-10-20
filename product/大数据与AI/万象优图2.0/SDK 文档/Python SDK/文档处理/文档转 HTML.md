## 简介

本文档提供关于文档预览同步请求的 API 概览以及 SDK 示例代码。

| API  |	说明  |
|----|-----|
| [文档转 HTML](https://cloud.tencent.com/document/product/436/54059)  | 文档转 HTML 功能支持对多种文档类型的文件生成 HTML 格式预览，满足 PC、App 等多个用户端的文档在线浏览需求，适用于在线教育、企业 OA、在线知识库、网盘文档预览等业务场景。 | 


## 文档转 HTML

#### 功能说明

支持对多种文档类型的文件生成 HTML 格式预览。

#### 方法原型

```py
def ci_doc_preview_html_process(self, Bucket, Key, SrcType=None, Copyable='1', DstType='html', HtmlParams=None, HtmlWaterword=None, HtmlFillStyle=None,
                                    HtmlFront=None, HtmlRotate=None, HtmlHorizontal=None, HtmlVertical=None, **kwargs):
```

#### 请求示例

```py
def ci_doc_preview_to_html_process():
    # 文档预览同步接口（生成html）
    response = client.ci_doc_preview_html_process(
        Bucket=bucket_name,
        Key='1.txt',
    )
    print(response)
    response['Body'].get_stream_to_file('result.html')
```

#### 参数说明

| 名称        | 参数说明                                                         | 类型   | 是否必选 |
| ----------- | ------------------------------------------------------------ | ------ | -------- |
| Bucket   | 对象所在存储桶  | String  | 是       |  
| Key      | 对象名  | String  | 是       |  
| SrcType | 指定目标文件类型，支持的文件类型请见 [文档转 HTML](https://cloud.tencent.com/document/product/436/54059) 文档   | String | 否 |
| Copyable          | 是否可复制。默认为可复制，填入值为1；不可复制，填入值为0     | String   | 否      | 
| DstType   | 转换输出目标文件类型，文档 HTML 预览固定为 html（需为小写字母）  | String  | 是       |  
| HtmlParams          | 自定义配置参数，json结构，需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/32832#.E4.BB.80.E4.B9.88.E6.98.AF-url-.E5.AE.89.E5.85.A8.E7.9A.84-base64-.E7.BC.96.E7.A0.81.EF.BC.9F) 的 Base64 编码，默认配置为：{ commonOptions: { isShowTopArea: true, isShowHeader: true } }，支持的配置参考 [自定义配置项说明](https://cloud.tencent.com/document/product/436/59408#.E8.87.AA.E5.AE.9A.E4.B9.89.E9.85.8D.E7.BD.AE.E9.80.89.E9.A1.B9)    | String   | 否   |
| HtmlWaterword          | 水印文字，需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/32832#.E4.BB.80.E4.B9.88.E6.98.AF-url-.E5.AE.89.E5.85.A8.E7.9A.84-base64-.E7.BC.96.E7.A0.81.EF.BC.9F) 的 Base64 编码，默认为空     | String  | 否      | 
| HtmlFillStyle          | 水印 RGBA（颜色和透明度），需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/32832#.E4.BB.80.E4.B9.88.E6.98.AF-url-.E5.AE.89.E5.85.A8.E7.9A.84-base64-.E7.BC.96.E7.A0.81.EF.BC.9F) 的 Base64 编码，默认为：rgba(192,192,192,0.6)  | String   | 否      | 
| HtmlFront          | 水印文字样式，需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/32832#.E4.BB.80.E4.B9.88.E6.98.AF-url-.E5.AE.89.E5.85.A8.E7.9A.84-base64-.E7.BC.96.E7.A0.81.EF.BC.9F) 的 Base64 编码，默认为：bold 20px Serif    | String   | 否      | 
| HtmlRotate          | 水印文字旋转角度，0 - 360，默认315度  | String   | 否      | 
| HtmlHorizontal          | 水印文字水平间距，单位 px，默认为50  | String | 否      | 
| HtmlVertical          | 水印文字垂直间距，单位 px，默认为100  | String | 否      | 









