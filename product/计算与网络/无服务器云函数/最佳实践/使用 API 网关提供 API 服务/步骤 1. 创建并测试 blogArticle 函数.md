在此部分中，将创建一个函数来实现博客文章的 API 响应，并通过控制台调用来测试函数。

## 创建 blogArticle 云函数
1 . 登录[无服务器云函数控制台](https://console.cloud.tencent.com/scf)，在【广州】地域下单击【新建】按钮。

2 . 进入函数配置部分，函数名称填写`blogArticle`，剩余项保持默认，单击【下一步】。

3 . 进入函数代码部分，执行方法填写`index.main_handler`，代码窗口内贴入如下代码，单击【下一步】。

```
# -*- coding: utf8 -*-
import json

testArticleInfo=[
    {"id":1,"category":"blog","title":"hello world","content":"first blog! hello world!","time":"2017-12-05 13:45"},
    {"id":2,"category":"blog","title":"record info","content":"record work and study!","time":"2017-12-06 08:22"},
    {"id":3,"category":"python","title":"python study","content":"python study for 2.7","time":"2017-12-06 18:32"},
]

def main_handler(event,content):
    if "requestContext" not in event.keys():
        return {"errorCode":410,"errorMsg":"event is not come from api gateway"}
    if event["requestContext"]["path"] != "/article/{articleId}" and event["requestContext"]["path"] != "/article":
        return {"errorCode":411,"errorMsg":"request is not from setting api path"}
    if event["requestContext"]["path"] == "/article" and event["requestContext"]["httpMethod"] == "GET": #获取文章列表
        retList = []
        for article in testArticleInfo:
            retItem = {}
            retItem["id"] = article["id"]
            retItem["category"] = article["category"]
            retItem["title"] = article["title"]
            retItem["time"] = article["time"]
            retList.append(retItem)
        return retList
    if event["requestContext"]["path"] == "/article/{articleId}" and event["requestContext"]["httpMethod"] == "GET": #获取文章内容
        articleId = int(event["pathParameters"]["articleId"])
        for article in testArticleInfo:
            if article["id"] == articleId:
                return article
        return {"errorCode":412,"errorMsg":"article is not found"}
    return {"errorCode":413,"errorMsg":"request is not correctly execute"}
```
4 . 进入触发方式部分，由于 API 网关触发的配置位于 API 网关中，此处暂时不添加任何触发方式，单击【完成】按钮。


**注意**

保存文章的数据结构使用 testArticleInfo 变量进行保存和模拟，此处在实际应用中通常为从数据库中或者文件中读取。

## 测试 blogArticle 云函数

在创建函数时，通常会使用控制台或 API 先进行测试，确保函数输出符合预期后再绑定触发器进行实际应用。

1 . 在刚刚创建的函数详情页中，单击【测试】按钮；

2 . 在测试模版内选择【API Gateway 测试模版】，并修改模版成为如下内容，此内容为测试获取文章列表的 API。

```
{
  "requestContext": {
    "serviceName": "testsvc",
    "path": "/article",
    "httpMethod": "GET",
    "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
    "identity": {
      "secretId": "abdcdxxxxxxxsdfs"
    },
    "sourceIp": "10.0.2.14",
    "stage": "prod"
  },
  "headers": {
    "Accept-Language": "en-US,en,cn",
    "Accept": "text/html,application/xml,application/json",
    "Host": "service-3ei3tii4-251000691.ap-guangzhou.apigateway.myqloud.com",
    "User-Agent": "User Agent String"
  },
  "pathParameters": {
  },
  "queryStringParameters": {
  },
  "headerParameters":{
    "Refer": "10.0.2.14"
  },
  "path": "/article",
  "httpMethod": "GET"
}
```

其中 `requestContext` 内的 `path`，`httpMethod`字段，外围的`path`，`httpMethod` 字段，均修改为我们设计的 API 路径 `/article` 和方法 `GET`。

3 . 单击【运行】按钮，观察运行结果。运行结果应该为成功，且返回内容应该为如下所示的文章概要内容。

```
[{"category": "blog", "time": "2017-12-05 13:45", "id": 1, "title": "hello world"}, {"category": "blog", "time": "2017-12-06 08:22", "id": 2, "title": "record info"}, {"category": "python", "time": "2017-12-06 18:32", "id": 3, "title": "python study"}]
```

4 . 修改测试模版成为如下内容，此内容为测试获取文章内容的 API。

```
{
  "requestContext": {
    "serviceName": "testsvc",
    "path": "/article/{articleId}",
    "httpMethod": "GET",
    "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
    "identity": {
      "secretId": "abdcdxxxxxxxsdfs"
    },
    "sourceIp": "10.0.2.14",
    "stage": "prod"
  },
  "headers": {
    "Accept-Language": "en-US,en,cn",
    "Accept": "text/html,application/xml,application/json",
    "Host": "service-3ei3tii4-251000691.ap-guangzhou.apigateway.myqloud.com",
    "User-Agent": "User Agent String"
  },
  "pathParameters": {
    "articleId":"1"
  },
  "queryStringParameters": {
  },
  "headerParameters":{
    "Refer": "10.0.2.14"
  },
  "path": "/article/1",
  "httpMethod": "GET"
}
```

其中 `requestContext` 内的 `path`，`httpMethod`字段，外围的`path`，`httpMethod` 字段，均修改为我们设计的 API 路径 `/article/{articleId}`和实际请求路径 `/article/1` ，方法为`GET`， `pathParameters` 字段内应该为 API网关内抽取出来的参数和实际值`"articleId":"1" ` 。

5 . 单击【运行】按钮，观察运行结果。运行结果应该为成功，且返回内容应该为如下所示的文章详细内容。

```
{"category": "blog", "content": "first blog! hello world!", "time": "2017-12-05 13:45", "id": 1, "title": "hello world"}
```

