## Description

This document describes Common Response Headers that will appear when using APIs. The headers described below will not be explained in later API documents.

##  List of Response Headers

| Header Name         | Description                                       | Type     |
| ---------------- | ---------------------------------------- | ------ |
| Content-Length   | HTTP request content length defined in RFC 2616 (Bytes)            | String |
| Content-Type     | HTTP request content type defined in RFC 2616 (MIME)          | String |
| Connection       | Declare connection status between client and server. <br />Enumerated values: keep-alive, close | Enum   |
| Date             | Response time of the server, subject to the GMT time defined in RFC 1123.        | String |
| Etag             | ETag (Entity Tag) is an information tag used to identify Object content upon creation of Object. This parameter may return values other than MD5, depending on different situations of the requests. ETag value can be used to check whether the Object content has changed.  | String |
| Server           | Name of the server that created the request. Default value: tencent-cos              | String |
| x-cos-request-id | When a request is sent, the server will automatically generate an ID for the request.                 | String |
| x-cos-trace-id   | When a request encounters an error, the server will automatically generate an ID for the error.               | String |


