## Overview

This document describes public request headers to be used when using CLS APIs. The headers described below will not be discussed in subsequent API documents.

## List of Public Request Headers

| HTTP Header Name | Description |
| ------------------- | ------------------------------------------------------------ |
| Host | The request host name, which is different for each region. For example, it is ap-shanghai.cls.myqcloud.com for Shanghai. |
| Authorization | Signature content. For more information on how to compute the signature, please see [Request Signature](/document/product/614/12445). |
| Content-Length | Length of the request Body. If there is no Body, this header can be ignored. |
| Content-Type | Format of the request Body (application/json, application/x-protobuf), which can be selected according to the detailed API documentation. If there is no Body, this header can be ignored. |
| Content-MD5 | MD5 of the request Body. If there is no Body, this header can be ignored. The calculation result supports lowercase letters. |
| x-cls-compress-type | Compression method (lz4) used by the request Body, which is only used by the log upload API. If there is no compression, this header can be ignored. |


