## **操作场景**

gRPC 插件需要用户提供 .proto 文件描述 HTTP 到 gRPC 协议的转换规则，HttpRule 是此转发规则的语法。

## **前提条件**

HTTP 请求 Body 格式仅支持 JSON。HTTP 请求方法只支持 RESTful 的方法，支持的 HTTP 方法和 CRUD 对应关系如下表：

| **支持的HTTP 方法** | **HTTP方法对应的CURD** |
| ------------------- | ---------------------- |
| POST                | Create                 |
| GET                 | Read                   |
| PUT                 | Update/Replace         |
| PATCH               | Update/Modify          |
| DELETE              | Delete                 |

**后端支持的协议包括：**

- gRPC
- gRPCS

**后端类型支持包括：**

- 后端通道 （VPC 通道和 TKE 通道都支持）
- 内网 CLB
- 公网 URL 后端



## **原理说明**

HttpRule 定义的是 HTTP 和 gRPC 的映射关系。映射主要关心两个维度：**（1）gRPC 的 rpc 方法中，方法参数的值从哪里获取。**（**2） gRPC 的 rpc 方法中，返回的数据如何在 HTTP 的响应中返回。**

在 rpc 的方法定义内，加上一个 option (google.api.http) 就是 HttpRule 的映射语法了。

![](https://qcloudimg.tencent-cloud.cn/raw/cff6d62c07c0ed8966af5c9deab9e122.png)        

在 HhttpRule 中，HTTP 的方法，需要小写。一个 rpc 的方法，对应一个 HTTP 的请求（方法只有一种，除非使用 addtional_bindings, 后面会详细说明 addtional_bindings 的使用方法和使用场景）。

有 HttpRule 规则的 .proto 文件例子：

```java
syntax = "proto3";

option go_package = "google.golang.org/grpc/examples/helloworld/helloworld";
option java_multiple_files = true;
option java_package = "io.grpc.examples.helloworld";
option java_outer_classname = "HelloWorldProto";
import "google/api/annotations.proto";

package helloworld;
// 备注中文支持
// The greeting service definition.
service Greeter {
  // Sends a greeting
  rpc SayHello (HelloRequest) returns (HelloReply) {
    option (google.api.http) = {
        get: "/grpc_upstream/{name}"
        additional_bindings {
            get: "/grpc_upstream_tls/{name}"
        }
    };
  }
}

// The request message containing the user's name.
message HelloRequest {
  string name = 1;
}

// The response message containing the greetings
message HelloReply {
  string message = 1;
}
```

关键在于需要import相关的HttpRule的语法：import "google/api/annotations.proto";

除 HttpRule 的规则外，其他的所有语法均与 gRPC 服务的语法一致，因此用户只需要在原有的 gRPC 服务的 proto 文件中，加上HttpRule 规则即可。



### **本地检查 .proto 文件的语法合法性**

**如果上传的 .proto 文件有问题，可以在本地使用 protoc 工具校验，使用步骤如下：**

1. 下载文件 [googleapis.tar.gz](https://apigw-1300555551.cos.ap-nanjing.myqcloud.com/googleapis.tar.gz) 。
2. 解压 googleapis.tar.gz 到任意目录(比如 /tmp中)
3. 设置环境变量 GOOGLEAPIS_DIR：GOOGLEAPIS_DIR=/tmp/googleapis
4. 使用 protoc 工具验证.proto文件合法性（不能有报错和warning）：protoc --include_imports --include_source_info  --proto_path=${GOOGLEAPIS_DIR} --proto_path=. --descriptor_set_out=api_descriptor.pb ex   ample.proto



### **请求参数映射规则**

- **如果HttpRule中的body定义是是一个特定值（不是\* ）**

- - **参数是从path template中定义，就从请求的URL的Path中获取**
  - **body中定义的参数，就从请求的Body中获取**
  - **其他的参数则从请求URL的query参数中获取**

- **如果HttpRule中的body是\***

- - **所有的参数都不能从请求的URL的query参数中获取**
  - **只能从Body或URL Path中获取**

- **如果HttpRule中body没有定义**

- - **参数默认是从请求的URL的query参数中获取。**
  - **如果定义了参数是从URL的Path中获取，那么就根据path template的规则，从URL的Path中获取**



### **使用举例**

#### **1. 以GET请求的参数获取（默认是从query参数中获取，除非path template指定了）为例**

```java
service Messaging {
   rpc GetMessage(GetMessageRequest) returns (Message) {
     option (google.api.http) = {
         get:"/v1/messages/{message_id}"
     };
   }
 }
message GetMessageRequest {
   message SubMessage {
     string subfield = 1;
   }
   string message_id = 1;  // Mapped to URL path.
   int64 revision = 2;     // Mapped to URL query parameter `revision`.
   SubMessage sub = 3;     // Mapped to URL query parameter `sub.subfield`.
 }
```

GetMessageRequest中的message_id是从URL的Path获取，其他的参数，如revision和sub中的subfield都是从URL的query参数中获取。"/v1/messages/{message_id}" 中的{message_id}就是path template，指定了message_id的参数，是从URL的Path中获取。

HTTP请求的URL： /v1/messages/123456?revision=2&sub.subfield=foo，对应的gRPC请求就是：GetMessage(message_id: "123456" revision: 2 sub: SubMessage(subfield:"foo"))



#### **2. PATCH 请求参数从URL Path和Body中获取，注意 body为\*的时候，参数禁止从请求query参数中获取**



```java
 service Messaging {
   rpc UpdateMessage(Message) returns (Message) {
     option (google.api.http) = {
       patch: "/v1/messages/{message_id}"
       body: "*"
     };
   }
 }
 message Message {
   string message_id = 1;
   string text = 2;
 }
```

请求参数message_id是从请求URL的Path中获取，其他的参数（text），是从body中获取。注意，在body为*的情况下，参数是不会从请求的query 参数中获取的。

HTTP请求： PATCH /v1/messages/123456 { "text": "Hi!" } ，对应的gRPC请求为UpdateMessage(message_id: "123456" text: "Hi!") 

#### **3.  body不为\*的场景**

```java
 service Messaging {
   rpc UpdateMessage(UpdateMessageRequest) returns (Message) {
     option (google.api.http) = {
       patch: "/v1/messages/{message_id}"
       body: "message"
     };
   }
 }
 message UpdateMessageRequest {
   string message_id = 1;  // mapped to the URL
   Message message = 2;    // mapped to the body
 }
 
 message Message {
    string text = 1; // The resource content.
 }
```

HTTP请求： PATCH /v1/messages/123456 { "text": "Hi!" } ，对应的gRPC请求为UpdateMessage(message_id: "123456" text: "Hi!") 

#### **4.  additional_bindings 的使用场景**

additional_bindings 主要用于接口的兼容或者同一个 rpc 方法暴露两个 HTTP 请求的场景。

```java
 service Messaging {
   rpc GetMessage(GetMessageRequest) returns (Message) {
     option (google.api.http) = {
       get: "/v1/messages/{message_id}"
       additional_bindings {
         get: "/v1/users/{user_id}/messages/{message_id}"
       }
     };
   }
 }
 message GetMessageRequest {
   string message_id = 1;
   string user_id = 2;
 }
```



这样，就会有两个HTTP请求使用同一个rpc方法。请求映射如下：

HTTP请求：GET /v1/messages/123456 ， 对应gRPC请求是GetMessage(message_id: "123456") 。

HTTP请求：GET /v1/users/me/messages/123456 ， 对应gRPC请求是GetMessage(message_id: "123456")

详细的HttpRule规则见第三方文档：https://github.com/googleapis/googleapis/blob/master/google/api/http.proto

## **注意事项**

1. 一个 gRPC 后端插件只能上传一个 .proto 文件，因此用户需要把所有需要暴露的 rpc 方法，放到一个 .proto 文件中，并且加上HttpRule。

## **常见问题**

1. 保存gRPC后端插件的时候，报错**参数 `proto file format error` 格式错误，请修改后重新操作** 。原因是提交的.proto文件格式有问题，很可能是没有执行import HttpRule的文件。需要在.proto文件中加上 import "google/api/annotations.proto";   

2. **访问API网关提供的服务时候，报错：** **Api with grpc(s) backend needs GrpcGateway plugin be configured.  处理方法：绑定gRPC后端插件到此API上。**

![](https://qcloudimg.tencent-cloud.cn/raw/91c6ef7ac266b6286d26fad359549a5c.png)                      

修改后，成功访问的示例：

![](https://qcloudimg.tencent-cloud.cn/raw/6e6cb660c671dbee3f904fc8b9e3ce5d.png)

3. 访问API网关提供的服务时候，报错：failed to transcode .proto file Unknown path "/something" 。处理方法：因为.proto文件中HttpRule的option中定义的路径和你访问的路径不一致，需要检查一下.proto文件，改为一致即可。 ![](https://qcloudimg.tencent-cloud.cn/raw/fc261fed06f0c56b4624ef7b8558baea.png)                       

解决方法示例：

![](https://qcloudimg.tencent-cloud.cn/raw/0fe7d92702aeddc1c64ea0ae38ee9c70.png)        

修改后，成功访问的示例：

![](https://qcloudimg.tencent-cloud.cn/raw/6e6cb660c671dbee3f904fc8b9e3ce5d.png)        



