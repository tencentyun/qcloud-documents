In this section, you will create a function to achieve API response regarding blog articles, and test the function by calling it through the console.

## Creating a blogArticle SCF
1. Log in to the [Serverless Cloud Function Console](https://console.cloud.tencent.com/scf). Select **Guangzhou** from the region list and click **Create**.

2. In the **Function configuration** section, enter `blogArticle` as the function name, leave all the other configuration options unchanged, and then click **Next**.

3. In the **Function code** section, enter `index.main_handler` as the execution method and paste the following codes into the code window, and then click **Next**.

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
        return json.dumps({"errorCode":410,"errorMsg":"event is not come from api gateway"})
    if event["requestContext"]["path"] != "/article/{articleId}" and event["requestContext"]["path"] != "/article":
        return json.dumps({"errorCode":411,"errorMsg":"request is not from setting api path"})
    if event["requestContext"]["path"] == "/article" and event["requestContext"]["httpMethod"] == "GET": #Obtain the article list
        retList = []
        for article in testArticleInfo:
            retItem = {}
            retItem["id"] = article["id"]
            retItem["category"] = article["category"]
            retItem["title"] = article["title"]
            retItem["time"] = article["time"]
            retList.append(retItem)
        return json.dumps(retList)
    if event["requestContext"]["path"] == "/article/{articleId}" and event["requestContext"]["httpMethod"] == "GET": #Obtain the article content
        articleId = int(event["pathParameters"]["articleId"])
        for article in testArticleInfo:
            if article["id"] == articleId:
                return json.dumps(article)
        return json.dumps({"errorCode":412,"errorMsg":"article is not found"})
    return json.dumps({"errorCode":413,"errorMsg":"request is not correctly execute"})
```
4. In the **Triggering method** section, you do not need to add any trigger method because the API gateway trigger is configured in the API gateway. Click **Complete**.


**Note**

The data structure of articles can be saved and simulated using the variable testArticleInfo. Usually, data structures are read from databases or files.

## Testing the blogArticle SCF

When a function is created, it is generally tested through the console or API, to ensure the function output meets the expectation, and then you can bind it to a trigger for practical application.

1. In the details page of the function you just created, click **Test**.

2. Select **API Gateway Test Template** from the test templates. Modify it as follows to test the API for obtaining the article list.

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

In the code above, the `path` and `httpMethod` fields in `requestContext`, as well as the peripheral `path` and `httpMethod` fields are modified as `/article` (the API path we design) and `GET`.

3. Click **Run** to view the results. The running result should be successful, and the content returned should be the basic information of articles as shown below.

```
[{"category": "blog", "time": "2017-12-05 13:45", "id": 1, "title": "hello world"}, {"category": "blog", "time": "2017-12-06 08:22", "id": 2, "title": "record info"}, {"category": "python", "time": "2017-12-06 18:32", "id": 3, "title": "python study"}]
```

4. Modify the test template as follows to test the API for obtaining article contents.

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

The `path` and `httpMethod` fields in `requestContext` are modified as `/article/{articleId}` (the API path we design) and `GET`. The peripheral `path` and `httpMethod` fields are modified as `/article/1` (the actual request path) and `GET`. The `pathParameters` field should be `"articleId":"1"`, the parameter and the actual value extracted from the API gateway.

5. Click **Run** to view the results. The running result should be successful, and the content returned should be the detailed content of articles as shown below.

```
{"category": "blog", "content": "first blog! hello world!", "time": "2017-12-05 13:45", "id": 1, "title": "hello world"}
```


