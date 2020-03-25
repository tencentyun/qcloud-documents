## PostgreSQL for Serverless 简介
PostgreSQL for Serverless 是一款基于 PostgreSQL 数据库实现的按需分配资源的数据库产品，其数据库将根据您的实际请求数来自动分配资源。

传统数据库实例需要根据业务实际使用情况来进数据库规格调整，而手动管理数据库容量需要占用宝贵的时间，也可能因为数据库资源的不饱和使用而造成浪费。
PostgreSQL for Serverless 仅需创建实例，即可正常使用，您无需关心数据库实例规格，仅需要在数据库处于活动状态期间按照实际用量进行付费。

## 系统架构
用户连接数据库后，通过 PostgreSQL for Serverless Proxy 层统一进行请求转发，然后进行数据操作。当用户请求数增加时，数据库将自动响应。当前设定单用户最高支持 QPS 40000/s。
![](https://main.qcloudimg.com/raw/84020ccedd2a1fee8fef2635cea898ba.png)


