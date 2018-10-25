## Description

This document describes Common Request Headers to be used when using APIs. The headers described below will not be discussed in later API documents. <style rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>

### List of Request Headers

| Header Name           | Description                                       | Type     | Required   |
| ------------------ | ---------------------------------------- | ------ | ---- |
| Authorization      | Contain authentication information, signature information used to verify the validity of requests. This header is not required for files that can be read by public users. | String | No    |
| Content-Length     | HTTP request content length defined in RFC 2616 (bytes), commonly used in API operations of PUT type. | String | No    |
| Content-Type       | HTTP request content type defined in RFC 2616 (MIME), for example: text/plain | String | No   |
| Content-MD5        | 128-bit content MD5 check value encoded using Base64, defined in RFC 1864. This header is used to check whether the file content has changed. | String | No    |
| Date               | GMT time defined in RFC 1123, for example: Wed, 30 Mar. 2016 23:00:00 GMT. | String | No    |
| Expect             | If Expect: 100-continue is used, the request content will not be sent until the receipt of response from server. This option can be used to check whether a header is valid, without the need to send the data content. <br />Valid value: 100-continue. | String | No    |
| Host               | Request host, in a form of <BucketName>-<APPID>.cos.<Region>.myqcloud.com | String | Yes    |


