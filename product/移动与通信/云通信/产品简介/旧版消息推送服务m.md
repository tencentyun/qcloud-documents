## 消息推送服务简介

消息推送服务是基于云通信IM的通信架构实现的一组REST API，用以支持APP应用的全员推送、标签推送等消息推送需求，客户端可通过SDK在线推送、离线推送（Android后台通知和APNS）接收推送的消息。客户端IMSDK目前支持Android、iOS和Windows平台。目前，消息推送服务仅支持独立模式帐号。

![](//mccdn.qcloud.com/static/img/e18924a4def3891ca2bb7c365928f2ec/image.png)

## 消息推送服务提供的基础能力

1. 支持APP内用户全员推送消息；
1. 支持指定用户标签推送消息；
1. 支持APNS推送。

## 我们的优势

消息推送服务基于客户端imsdk + 云通信IM后台，在消息能力和系统可用性上有可靠保证：

1. 基于imsdk，保证消息可达，可简单为应用提供消息广播能力； 
1. 支持为每个用户最多10个推送标签，各标签可分别设置，互不影响；
1. 标签推送支持多个标签的and/or逻辑选择推送；
1. 支持只推在线用户，同时支持最长7天的消息离线存储；
1. 支持自定义消息。

## 相关API
1. [推送](http://cloud.tencent.com/doc/product/269/%E6%8E%A8%E9%80%81) ；
1. [查询推送任务状态](http://cloud.tencent.com/doc/product/269/%E6%9F%A5%E8%AF%A2%E6%8E%A8%E9%80%81%E4%BB%BB%E5%8A%A1%E7%8A%B6%E6%80%81) ；
1. [设置标签](http://cloud.tencent.com/doc/product/269/%E8%AE%BE%E7%BD%AE%E6%A0%87%E7%AD%BE) ；
1. [删除标签](http://cloud.tencent.com/doc/product/269/%E5%88%A0%E9%99%A4%E6%A0%87%E7%AD%BE)  ；
1. [获取用户标签](http://cloud.tencent.com/doc/product/269/%E8%8E%B7%E5%8F%96%E7%94%A8%E6%88%B7%E6%A0%87%E7%AD%BE) 。

