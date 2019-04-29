## 概述

本文将为您介绍在使用 CLS API 时候会出现的公共返回头部（Response Header），下文提到的头部会在之后的具体 API 文档中不再赘述。

## 返回头部列表

响应头的说明如下：

| HTTP Header名称   | 描述                                |
| --------------- | --------------------------------- |
| Content-Length  | 响应的 Body 长度                       |
| Content-Type    | 响应的 Body 格式，目前支持 application/json |
| x-cls-requestid | 服务端针对本次请求标示的唯一 ID                 |
