## 简介

数据万象依托对象存储（Cloud Object Storage，COS）提供数据处理服务，您可通过 COS 控制台和 SDK 快速调用数据万象的功能，例如内容审核、媒体处理等。本文介绍通过 COS 使用数据万象的注意事项和使用流程。

>? 使用数据万象服务会产生一定的数据处理费用，存储和部分流量费用则由 COS 收取，详情请参见 [计费说明](https://cloud.tencent.com/document/product/436/16871)。
>

## 前提条件

- 需开通 COS 服务并创建存储桶。如未开通，请访问 [COS 控制台](https://console.cloud.tencent.com/cos5)，按照界面提示进行开通并创建存储桶。
- 需开通数据万象服务。如未开通，请访问 [数据万象控制台](https://console.cloud.tencent.com/ci)，按照界面提示进行开通。


## 操作步骤

1. 在 COS 控制台 [创建存储桶](https://cloud.tencent.com/document/product/436/13309)，并向存储桶中 [上传待处理的文件](https://cloud.tencent.com/document/product/436/13321)。
2. 在 COS 控制台左侧导航栏中，单击【存储桶列表】，找到已创建的存储桶，单击其存储桶名称，进入存储桶的管理页面。
3. 在存储桶的管理页面，使用数据万象的全量处理能力。如下所示：
 - [内容审核](https://cloud.tencent.com/document/product/436/54402)
 - [数据处理](https://cloud.tencent.com/document/product/436/42892)
 - [数据工作流](https://cloud.tencent.com/document/product/436/53966)
4. COS SDK 也集成了数据万象的处理能力，调用方式请参见 [COS SDK 文档](https://cloud.tencent.com/document/product/436/6474)。
