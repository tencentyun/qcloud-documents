本文只列出 PaaS 服务相关返回码及其对应的计费关系， SaaS 服务的返回码及其他对应计费关系请查阅 [SaaS 错误码](https://cloud.tencent.com/document/product/1007/47912)。

## 人脸核验类
下表仅列出了活体人脸核身、活体人脸比对、照片人脸核身和身份证人像照片验真接口的收费返回码，其他未收费的接口错误码请参阅对应接口文档，完整错误码对照表请参考 API3.0 文档 > [错误码](https://cloud.tencent.com/document/product/1007/31332)。

| 返回码 | 含义                         | 是否收费 |
| ------ | ---------------------------- | -------- |
| Succcess | 检测通过 | 是 |
| FailedOperation.IdNameMisMatch|	姓名和身份证号不一致，请核实后重试。  | 是       |
|FailedOperation.IdPhotoPoorQuality	|证件图片分辨率太低，请重新上传。|是|
| FailedOperation.LifePhotoDetectFaces	|检测到多张人脸。|是    |
| FailedOperation.LifePhotoDetectFake	|实人比对没通过。|是   |
|FailedOperation.LifePhotoDetectNoFaces	|未能检测到完整人脸。| 是|
| FailedOperation.CompareFail	|比对失败。|是    |
| FailedOperation.CompareLowSimilarity	|比对相似度未达到通过标准。|是 |

## 要素类
身份证要素、银行卡要素和运营商要素的接口错误码及对应计费关系，请参阅各自接口文档。
