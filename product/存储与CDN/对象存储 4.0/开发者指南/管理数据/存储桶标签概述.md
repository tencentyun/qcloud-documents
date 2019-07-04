## 概述

存储桶标签是一个键值对（key = value），由标签的键（key）和标签的值（value）与“=”相连组成，例如 group = IT。它可以作为管理存储桶的一个标识，便于用户对存储桶进行分组管理。您可以对指定的存储桶进行标签的设定、查询和删除操作。

## 规格与限制

>!存储桶标签暂不支持中文标签，我们将尽快支持该特性，如有疑问，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 咨询。

### 标签键限制

- 以 qcs:、project、项目等开头的标签键为系统预留标签键，系统预留标签键禁止创建。
- 支持 UTF-8 格式表示的字符、空格和数字以及特殊字符 `+ - = ._ : / @ `。
- 标签键长度为0 - 127个字符（采用 UTF-8 格式）。
- 标签键区分英文字母大小写。

### 标签值限制

- 支持 UTF-8 格式表示的字符、空格和数字以及特殊字符`+ - = ._ : / @`。
- 标签值长度为0 - 255个字符 （采用 UTF-8 格式）。
- 标签值区分英文字母大小写。

### 标签数量限制

- 存储桶维度：一个资源最多10个不同的存储桶标签。
- 标签维度：
 - 单个用户最多1000个不同的 key。 
 - 一个 key 最多有1000个 value。
 - 同个存储桶下不允许有多个相同的 key。

## 使用方法

您可以通过控制台、API 的方式设置存储桶标签。

### 使用对象存储控制台

您如需使用对象存储控制台设置存储桶标签，请参阅 [设置存储桶标签](https://cloud.tencent.com/document/product/436/34830) 控制台指南文档。

### 使用 REST API

您可以直接通过以下 API 管理存储桶标签：

- [PUT Bucket tagging](https://cloud.tencent.com/document/product/436/34838)
- [GET Bucket tagging](https://cloud.tencent.com/document/product/436/34837)
- [DELETE Bucket tagging](https://cloud.tencent.com/document/product/436/34836)

