所有相关问题先进行如下步骤进行初筛排查
1. 检查源站是否返回4XX，若存在，则源站问题。
2. 检查 CDN 加速状态是否运行正常。
3. 检查是否配置4XX缓存状态码。
4. 其他具体常见4XX如下步骤排查。

|状态码|状态码含义|处理建议|
|---|---|--|
|403|禁止访问|[单击查看详情](https://cloud.tencent.com/document/product/228/63824)|
|404|Not Found|[单击查看详情](https://cloud.tencent.com/document/product/228/63825)|
|410|太多请求|请检查回源 Host 是否正确|
|416|服务器无法处理所请求的数据区间|[单击查看详情](https://cloud.tencent.com/document/product/228/63827)|
|423|当前资源被锁定|[单击查看详情](https://cloud.tencent.com/document/product/228/63826)|



