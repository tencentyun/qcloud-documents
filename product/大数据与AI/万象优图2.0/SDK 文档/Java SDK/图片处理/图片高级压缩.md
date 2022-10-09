## 简介

本文档提供关于图片高级压缩的 API 概览以及 SDK 示例代码。


<table>
<thead>
<tr>
<th align="left" width="15%">API</th>
<th align="left">操作描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/460/60526">图片高级压缩</a></td>
<td align="left">图片高级压缩可以更加高效地将图片转换为 TPG 或 HEIF 等高压缩比格式，有效降低图片传输链路及加载耗时，降低带宽及流量成本。</td>
</tr>
</tbody></table>

### 示例代码

[//]: # ".cssg-snippet-process-with-pic-operation"
```java
GetObjectRequest getObj = new GetObjectRequest(bucketName, key);
// 这里是图片压缩参数，具体请参考数据万象API，这里仅是示例
String compress = "imageMogr2/format/tpg";
getObj.putCustomQueryParameter(compress, null);
```
