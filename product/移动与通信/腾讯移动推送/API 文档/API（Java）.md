## SDK 说明

本 SDK 提供 TPNS 服务端接口的 Java 封装，与移动推送 TPNS 后台通信。使用时引用 XingeApp 包即可，本 SDK 封装的主要是 V3 推送相关接口。

## 集成方式

Maven  依赖引用方式：

```
<dependency>
            <groupId>com.github.xingePush</groupId>
            <artifactId>xinge</artifactId>
            <version>1.2.4</version>
</dependency>
```

## 使用方法

### XingeApp 接口说明

该类提供与 TPNS 后台交互的接口。由 XingeApp.Builder 进行构建，对应参数如下

| 参数名         | 类型    | 必需 | 默认值                     | 参数描述                                                     |
| -------------- | ------- | ---- | -------------------------- | ------------------------------------------------------------ |
| appId          | Integer | 是   | 无                         | 推送目标 accessID（可在 [产品管理](https://console.cloud.tencent.com/tpns) 页面获取） |
| secretKey      | String  | 是   | 无                         | 推送密钥                                                     |
| proxy          | Proxy   | 否   | Proxy.NO\_PROXY            | 如果需要设置代理可以设定该参数                               |
| connectTimeOut | Integer | 否   | 10s                        | 链接超时时间设置                                             |
| readTimeOut    | Integer | 否   | 10s                        | 请求超时时间设置                                             |
| domainUrl      | String  | 否   | https://openapi.xg.qq.com/ | 请求接口服务域名地址，默认为请求信鸽平台的接口地址。使用时需要根据您产品的服务接入点选择 [请求服务地址](https://cloud.tencent.com/document/product/548/49157) |

### 示例

```java
XingeApp xingeApp = new XingeApp.Builder()
        .appId(appid)
        .secretKey(secretKey)
        .domainUrl(“https://api.tpns.tencent.com/”)    
        .build();

PushAppRequest pushAppRequest = new PushAppRequest();
//完善PushAppRequest  消息
... 
JSONObject ret =  xingeApp.pushApp(pushAppRequest );
```

### pushAppRequest 接口说明

该类提供封装好的推送消息体，各参数说明及使用方法可参考 [推送接口说明](https://cloud.tencent.com/document/product/548/39064)。

### Android 单设备推送示例

```java
public JSONObject pushTokenAndroid() {
        PushAppRequest pushAppRequest = new PushAppRequest();
        pushAppRequest.setAudience_type(AudienceType.token);
        pushAppRequest.setPlatform(Platform.android);
        pushAppRequest.setMessage_type(MessageType.notify);
        Message message = new Message();
        message.setTitle("title");
        message.setContent("content");
        pushAppRequest.setMessage(message);
        MessageAndroid messageAndroid = new MessageAndroid();
        message.setAndroid(messageAndroid);
        ArrayList<String> tokenList = new ArrayList();
        tokenList.add("04cac74a714f61bf089********63d880993");
        pushAppRequest.setToken_list(tokenList);
        return this.xingeApp.pushApp(pushAppRequest);
    }
```

### Android 单账号推送示例

```java
public JSONObject pushAccountAndroid() {
        PushAppRequest pushAppRequest = new PushAppRequest();
        pushAppRequest.setAudience_type(AudienceType.account);
        pushAppRequest.setPlatform(Platform.android);
        pushAppRequest.setMessage_type(MessageType.notify);
        pushAppRequest.setAccount_push_type(1);
        Message message = new Message();
        message.setTitle("title");
        message.setContent("content");
        MessageAndroid messageAndroid = new MessageAndroid();
        message.setAndroid(messageAndroid);
        pushAppRequest.setMessage(message);
        ArrayList<String> accountList = new ArrayList();
        accountList.add("123");
        pushAppRequest.setAccount_list(accountList);
        return this.xingeApp.pushApp(pushAppRequest);
    }
```

### Android 标签推送示例

```java
public JSONObject pushTagAndroid() {
        PushAppRequest pushAppRequest = new PushAppRequest();
        pushAppRequest.setAudience_type(AudienceType.tag);
        pushAppRequest.setPlatform(Platform.android);
        pushAppRequest.setMessage_type(MessageType.notify);
        Message message = new Message();
        message.setTitle("title");
        message.setContent("content");
        MessageAndroid messageAndroid = new MessageAndroid();
        message.setAndroid(messageAndroid);
        pushAppRequest.setMessage(message);
        ArrayList<String> tagList = new ArrayList();
        tagList.add("tag");
        TagListObject tagListObject = new TagListObject();
        tagListObject.setTags(tagList);
        tagListObject.setOp(OpType.OR);
        pushAppRequest.setTag_list(tagListObject);
        return this.xingeApp.pushApp(pushAppRequest);
    }
```

### Android 全部设备推送示例

```java
public JSONObject pushAllAndroid() {
        PushAppRequest pushAppRequest = new PushAppRequest();
        pushAppRequest.setAudience_type(AudienceType.all);
        pushAppRequest.setPlatform(Platform.android);
        pushAppRequest.setMessage_type(MessageType.notify);
        Message message = new Message();
        message.setTitle("title");
        message.setContent("content");
        MessageAndroid messageAndroid = new MessageAndroid();
        message.setAndroid(messageAndroid);
        pushAppRequest.setMessage(message);
        return this.xingeApp.pushApp(pushAppRequest);
    }
```

### 推送应答示例

```java
{"result":"{}","environment":"","push_id":"1328245138690125824","err_msg":"NO_ERROR","err_msg_zh":"","ret_code":0,"seq":0}
```

## 服务端返回码

ret_code 含义可参考 [服务端错误码](https://cloud.tencent.com/document/product/548/39080)。

## 常见问题

1. 接口返回错误码10101或403是什么原因，如何解决？
   答：请检查应用 AccessID 与 SecretKey 是否匹配，domainUrl 与产品 [服务接入点](https://cloud.tencent.com/document/product/548/49157) 是否匹配。
2. 接口返回错误码1008007，参数校验失败如何解决？
   答：请参考 [推送示例](https://cloud.tencent.com/document/product/548/39064#ios-.E5.8D.95.E8.AE.BE.E5.A4.87.E6.8E.A8.E9.80.81.E8.AF.B7.E6.B1.82.E6.B6.88.E6.81.AF)，检查参数填写是否缺失或字段类型填写有误。
