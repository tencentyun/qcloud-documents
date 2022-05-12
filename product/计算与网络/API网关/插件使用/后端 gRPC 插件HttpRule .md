## 操作场景

gRPC 插件需要用户提供 `.proto` 文件描述 HTTP 到 gRPC 协议的转换规则，HttpRule 是此转发规则的语法。

## 前提条件

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



## 原理说明

HttpRule 定义的是 HTTP 和 gRPC 的映射关系。映射主要关心两个维度：
- **gRPC 的 rpc 方法中，方法参数的值从哪里获取。**
- **gRPC 的 rpc 方法中，返回的数据如何在 HTTP 的响应中返回。**

在 rpc 的方法定义内，加上一个 option (google.api.http) 就是 HttpRule 的映射语法。
![](https://qcloudimg.tencent-cloud.cn/raw/cff6d62c07c0ed8966af5c9deab9e122.png)        
>?
>- 在 HhttpRule 中，HTTP 的方法，需要小写。一个 rpc 的方法，对应一个 HTTP 的请求。
>- 方法只有一种，除非使用 addtional_bindings，[下文](#addtional_bindings) 会详细说明 addtional_bindings 的使用方法和使用场景。
>
含 HttpRule 规则的 `.proto` 文件例子如下：
<dx-codeblock>
:::  java
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
:::
</dx-codeblock>

>!关键在于需要 import 相关的 HttpRule 的语法：import "google/api/annotations.proto"。除 HttpRule 的规则外，其他的所有语法均与 gRPC 服务的语法一致，因此用户只需要在原有的 gRPC 服务的 proto 文件中，加上 HttpRule 规则即可。



### 本地检查 .proto 文件的语法合法性

**如果上传的 .proto 文件有问题，可以在本地使用 protoc 工具校验，使用步骤如下：**

1. 下载文件 [googleapis.tar.gz](https://apigw-1300555551.cos.ap-nanjing.myqcloud.com/googleapis.tar.gz) 。
2. 解压 googleapis.tar.gz 到任意目录（例如 `/tmp` 中）。
3. 设置环境变量 GOOGLEAPIS_DIR：GOOGLEAPIS_DIR=/tmp/googleapis。
4. 使用 protoc 工具验证 `.proto` 文件合法性（不能有报错和 warning）：
<dx-codeblock>
:::  sh
protoc --include_imports --include_source_info  --proto_path=${GOOGLEAPIS_DIR} --proto_path=. --descriptor_set_out=api_descriptor.pb ex   ample.proto
:::
</dx-codeblock>




### 请求参数映射规则

- **如果 HttpRule 中的 body 定义是一个特定值（不是 \* ）**
 - **参数是从 path template 中定义，就从请求的 URL 的 Path 中获取。**
 - **body 中定义的参数，就从请求的 Body 中获取。**
 - **其他的参数则从请求 URL 的 query 参数中获取。**
- **如果 HttpRule 中的 body 是 \***
 - **所有的参数都不能从请求的 URL 的 query 参数中获取。**
 - **只能从 Body 或 URL Path中获取。**
- **如果 HttpRule 中 body 没有定义**
 - **参数默认是从请求的 URL 的 query 参数中获取。**
 - **如果定义了参数是从 URL 的 Path 中获取，那么就根据 path template 的规则，从 URL 的 Path 中获取。**



### 使用举例
1. 以 GET 请求的参数获取（默认是从 query 参数中获取，除非 path template 指定了）为例：
<dx-codeblock>
:::  java
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
:::
</dx-codeblock>
<ul><li>GetMessageRequest 中的 message_id 是从 URL 的 Path 获取，其他的参数，如 revision 和 sub 中的 subfield 都是从 URL 的 query 参数中获取。</li>
<li>"/v1/messages/{message_id}" 中的 {message_id} 就是 path template，指定 message_id 的参数，是从 URL 的 Path 中获取。</li>
<li>HTTP 请求的 URL： /v1/messages/123456?revision=2&sub.subfield=foo，对应的 gRPC 请求就是：GetMessage(message_id: "123456" revision: 2 sub: SubMessage(subfield:"foo"))。</li></ul>
2. PATCH 请求参数从 URL Path 和 Body 中获取，注意 body 为 \* 的时候，参数禁止从请求 query 参数中获取。
<dx-codeblock>
:::  java
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
:::
</dx-codeblock>
<ul><li>请求参数 message_id 是从请求URL的 Path 中获取，其他的参数（text），是从 body 中获取。注意，在 body 为 \* 的情况下，参数是不会从请求的 query 参数中获取的。</li>
<li>HTTP 请求： PATCH /v1/messages/123456 { "text": "Hi!" } ，对应的 gRPC 请求为 UpdateMessage(message_id: "123456" text: "Hi!") 。</li></ul>
3. body 不为 \* 的场景。
<dx-codeblock>
:::  java
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
:::
</dx-codeblock>
HTTP 请求： PATCH /v1/messages/123456 { "text": "Hi!" } ，对应的 gRPC 请求为 UpdateMessage(message_id: "123456" text: "Hi!") 。
4.  additional_bindings 的使用场景。
additional_bindings 主要用于接口的兼容或者同一个 rpc 方法暴露两个 HTTP 请求的场景。
<dx-codeblock>
:::  java
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
:::
</dx-codeblock>
这样，就会有两个 HTTP 请求使用同一个 rpc 方法。请求映射如下：
<ul><li>HTTP 请求：GET /v1/messages/123456 ， 对应 gRPC 请求是GetMessage(message_id: "123456") 。</li>
<li>HTTP 请求：GET /v1/users/me/messages/123456 ， 对应 gRPC 请求是GetMessage(message_id: "123456")。</li></ul>

>?详细的 HttpRule 规则，请参见 [第三方文档](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto)。

## 注意事项

一个 gRPC 后端插件只能上传一个 `.proto` 文件，因此用户需要把所有需要暴露的 rpc 方法，放到一个 `.proto` 文件中，并且加上 HttpRule。

## 常见问题

#### 保存 gRPC 后端插件的时候，报错**参数 `proto file format error` 格式错误，请修改后重新操作** 。
原因是提交的 `.proto` 文件格式有问题，很可能是没有执行 import HttpRule 的文件。需要在 `.proto` 文件中加上 import "google/api/annotations.proto"。


#### 访问 API 网关提供的服务时候，报错：Api with grpc(s) backend needs GrpcGateway plugin be configured.  
处理方法：绑定 gRPC 后端插件到此 API 上。
![](https://qcloudimg.tencent-cloud.cn/raw/91c6ef7ac266b6286d26fad359549a5c.png)                      
修改后，成功访问的示例：
![](https://qcloudimg.tencent-cloud.cn/raw/6e6cb660c671dbee3f904fc8b9e3ce5d.png)


#### 访问 API 网关提供的服务时候，报错：failed to transcode .proto file Unknown path "/something" 。

处理方法：因为 `.proto` 文件中 HttpRule 的 option 中定义的路径和您访问的路径不一致，需要检查一下 `.proto` 文件，改为一致即可。 
![](https://qcloudimg.tencent-cloud.cn/raw/fc261fed06f0c56b4624ef7b8558baea.png)                       
解决方法示例：
![](https://qcloudimg.tencent-cloud.cn/raw/0fe7d92702aeddc1c64ea0ae38ee9c70.png)        
修改后，成功访问的示例：
![](https://qcloudimg.tencent-cloud.cn/raw/6e6cb660c671dbee3f904fc8b9e3ce5d.png)        



