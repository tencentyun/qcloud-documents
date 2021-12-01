## 投递描述

CMQ 通过发送 POST 请求将主题消息推送到订阅的 HTTP Endpoint 端，消息格式支持两种：JSON 格式和 SIMPLIFIED 精简格式。

- JSON 格式：推送的 HTTP 请求 Body 包含消息的正文和消息的属性信息。**Content-type 为 text/plain**。
- SIMPLIFIED 格式：推送的 HTTP 请求 Body 即为消息正文，而 msgId 等信息会在 HTTP 请求 Header 中传递给订阅方。

订阅方的 HTTP 服务返回标准的 2xx 响应（如200），代表投递成功，否则为投递失败，并触发重试投递策略；超时不响应，CMQ 也会认为失败，同样触发重试投递策略，检测超时时间约为15秒。

## 投递的 HTTP 请求 Header

| 参数名称          | 描述                     |
| :---------------- | :----------------------- |
| x-cmq-request-id  | 此次推送消息的 requestId |
| x-cmq-message-id  | 此次推送消息的 msgId     |
| x-cmq-message-tag | 此次推送消息的消息标签   |

## 投递的 HTTP 请求 Body

在 JSON 格式下，HTTP Body 包含消息的正文和消息的属性信息。

| 参数名称         | 类型   | 描述                       |
| :--------------- | :----- | :------------------------- |
| TopicOwner       | String | 被订阅的主题拥有者的 APPID |
| topicName        | String | 主题名称                   |
| subscriptionName | String | 订阅名称                   |
| msgId            | String | 消息 ID                    |
| msgBody          | String | 消息正文                   |
| publishTime      | Int    | 消息的发布时间             |

在 SIMPLIFIED 格式下，HTTP Body 即为发布者发布的消息正文。

## 投递的 HTTP 请求响应

订阅方 HTTP 服务正常处理投递消息，返回 2xx 响应；其他响应码或者超时不响应，当作错误，并触发重试投递策略。

## 请求示例

本示例中，订阅的 HTTP Endpoint 为`http://test.com/cgi`。
JSON 格式：

```js
POST /cgi HTTP/1.1
Host: test.com
Content-Length: 761
Content-Type: text/plain
User-Agent: Qcloud Notification Service Agent
x-cmq-request-id: 2394928734
x-cmq-message-id: 6942316962
x-cmq-message-tag: a, b

{"TopicOwner":100015036,"topicName":"MyTopic","subscriptionName":"mysubscription","msgId":"6942316962","msgBody":"test message","publishTime":11203432}
```

SIMPLIFIED 格式：

```js
POST /cgi HTTP/1.1
Host: test.com
Content-Length: 123
Content-Type: text/plain
User-Agent: Qcloud Notification Service Agent
x-cmq-request-id: 2394928734
x-cmq-message-id: 6942316962
x-cmq-message-tag: a, b

test message
```



## 订阅消息示例

如下为订阅消息 Demo，投递消息均为 POST 方法，因此只需重写 do_POST 方法即可。
本示例会打印接收到的 HTTP POST 请求内容，并将 post data json 反序列化，实现遍历打印请求数据。

```java
#!/usr/bin/python
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import json
class TestHTTPHandle(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.getheader('content-length',0))
        post_body = self.rfile.read(content_len)
        print "receive cmq topic publisher request:"
        print self.headers
        print post_body
        post_data = json.loads(post_body)
        for k,v in post_data.iteritems():
                print "key:%s value:%s" % (k,v)
        #response http status 200     
        self.send_response(200)
        self.end_headers()
        self.wfile.write('ok')
def start_server(port):
        http_server = HTTPServer(('0.0.0.0', int(port)),TestHTTPHandle)
        http_server.serve_forever()
if __name__ == '__main__':
        start_server(80)
```
