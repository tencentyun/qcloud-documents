## 简介
* 欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK 3.0 是云 API 3.0 平台的配套工具。SDK 3.0 实现了统一化，各个语言版本的 SDK 具备使用方法相同、接口调用方式相同、错误码和返回包格式相同等优点。
* 本文以 Java SDK 3.0 为例，介绍如何使用、调试并接入腾讯云产品 API。
* 目前已支持云服务器 CVM、私有网络 VPC 、云硬盘 CBS 等 [腾讯云产品](https://cloud.tencent.com/document/sdk/Description)，后续会支持其他云产品接入。

## 依赖环境

* JDK 7版本及以上。
* 获取安全凭证。安全凭证包含 SecretId 及 SecretKey 两部分。SecretId 用于标识 API 调用者的身份，SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥。前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面，即可进行获取，如下图所示：
![](https://main.qcloudimg.com/raw/8ec140474be0ced1352695b372b2934d.png)
>!**您的安全凭证代表您的账号身份和所拥有的权限，等同于您的登录密码，切勿泄露他人。**
* 获取调用地址。调用地址（endpoint）一般形式为`*.tencentcloudapi.com`，产品的调用地址有一定区别，例如，云服务器的调用地址为`cvm.tencentcloudapi.com`。具体调用地址可参考对应产品的 [API 文档](https://cloud.tencent.com/document/api)。

## 安装 SDK[](id:p1)
### 方式一、通过 Maven 安装（推荐）
Maven 是 JAVA 的依赖管理工具，支持您项目所需的依赖项，并将其安装到项目中。
1. 请访问 [Maven官网](https://maven.apache.org/) 下载对应系统 Maven 安装包进行安装，关于 Maven 详细可参考 [Maven 官网](https://maven.apache.org/)。
2. 为您的项目添加 Maven 依赖项，只需在 pom.xml 中找到`<dependencies>`标签，在里面添加以下依赖项即可。您可以在 [Maven 仓库](https://search.maven.org/search?q=tencentcloud-sdk-java) 上找到最新的版本（最新版本是3.1.322）
```xml
<dependency>
     <groupId>com.tencentcloudapi</groupId>
     <artifactId>tencentcloud-sdk-java</artifactId>
     <!-- go to https://search.maven.org/search?q=tencentcloud-sdk-java and get the latest version. -->
     <!-- 请到https://search.maven.org/search?q=tencentcloud-sdk-java查询所有版本，最新版本如下 -->
     <version>3.1.322</version>
</dependency>
```
>!
>- 这里的版本号只是举例，您可以在 [Maven 仓库](https://search.maven.org/search?q=tencentcloud-sdk-java) 上找到最新的版本。
>- [Maven 仓库](https://search.maven.org/search?q=tencentcloud-sdk-java) 中显示的4.0.11是废弃版本，由于 Maven 索引更新问题尚未完全删除。
>- 若上面的引用方式会将腾讯云所有产品 SDK 下载到本地，可以将 artifactId 换成 tencentcloud-sdk-java-cvm/cbs/vpc 等，即可引用特定产品的 SDK，代码中使用方式和大包相同，可参考示例。最新版本也可在 [Maven仓库](https://search.maven.org/search?q=tencentcloud-sdk-java) 查询，可大大节省存储空间。
3. 设置镜像源以加快下载速度，编辑 maven 的 settings.xml 配置文件，在 mirrors 段落增加镜像配置：
```
    <mirror>
      <id>tencent</id>
      <name>tencent maven mirror</name>
      <url>https://mirrors.tencent.com/nexus/repository/maven-public/</url>
      <mirrorOf>*</mirrorOf>
    </mirror>
```

### 方式二、通过源码包安装
1. 前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-java) 下载源码压缩包。
2. 解压源码包到您项目合适的位置。
3. 需要将 vendor 目录下的 jar 包放在 java 可找到的路径中。
4. 引用方法可参考示例。

## 使用 SDK
以查询实例接口 DescribeInstances 为例：
<dx-codeblock>
::: 简化版 java
```java
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
import com.tencentcloudapi.cvm.v20170312.CvmClient;
import com.tencentcloudapi.cvm.v20170312.models.DescribeInstancesRequest;
import com.tencentcloudapi.cvm.v20170312.models.DescribeInstancesResponse;

public class DescribeInstances {
     public static void main(String[] args) {
         try {
             Credential cred = new Credential("secretId", "secretKey");
             CvmClient client = new CvmClient(cred, "ap-shanghai");

            DescribeInstancesRequest req = new DescribeInstancesRequest();
             DescribeInstancesResponse resp = client.DescribeInstances(req);

            System.out.println(DescribeInstancesResponse.toJsonString(resp));
         } catch (TencentCloudSDKException e) {
            System.out.println(e.toString());
         }
     }
}
```
:::
::: 详细版 java
```java
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
// 导入对应产品模块的client
import com.tencentcloudapi.cvm.v20170312.CvmClient;
// 导入要请求接口对应的request response类
import com.tencentcloudapi.cvm.v20170312.models.DescribeInstancesRequest;
import com.tencentcloudapi.cvm.v20170312.models.DescribeInstancesResponse;
import com.tencentcloudapi.cvm.v20170312.models.Filter;
//导入可选配置类
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;
import com.tencentcloudapi.common.profile.Language;
public class DescribeInstances {
     public static void main(String[] args) {
         try {
             // 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
             Credential cred = new Credential("secretId", "secretKey");
             // 实例化一个http选项，可选的，没有特殊需求可以跳过
             HttpProfile httpProfile = new HttpProfile();
             //  从3.1.16版本开始, 单独设置 HTTP 代理
             // httpProfile.setProxyHost("真实代理ip");
             // httpProfile.setProxyPort(真实代理端口);
             httpProfile.setReqMethod("GET"); // get请求(默认为post请求)
             httpProfile.setProtocol("https://");  // 在外网互通的网络环境下支持http协议(默认是https协议),请选择(https:// or http://)
             httpProfile.setConnTimeout(30); // 请求连接超时时间，单位为秒(默认60秒)
             httpProfile.setWriteTimeout(30);  // 设置写入超时时间，单位为秒(默认0秒)
             httpProfile.setReadTimeout(30);  // 设置读取超时时间，单位为秒(默认0秒)
             httpProfile.setEndpoint("cvm.ap-shanghai.tencentcloudapi.com"); // 指定接入地域域名(默认就近接入)
             // 实例化一个client选项，可选的，没有特殊需求可以跳过
             ClientProfile clientProfile = new ClientProfile();
             clientProfile.setSignMethod("HmacSHA256"); // 指定签名算法(默认为HmacSHA256)
             // 自3.1.80版本开始，SDK 支持打印日志。
             clientProfile.setHttpProfile(httpProfile);
             clientProfile.setDebug(true);
             // 从3.1.16版本开始，支持设置公共参数 Language, 默认不传，选择(ZH_CN or EN_US)
             clientProfile.setLanguage(Language.EN_US);
             // 实例化要请求产品(以cvm为例)的client对象,clientProfile是可选的
             CvmClient client = new CvmClient(cred, "ap-shanghai", clientProfile);
             // 实例化一个cvm实例信息查询请求对象,每个接口都会对应一个request对象。
             DescribeInstancesRequest req = new DescribeInstancesRequest();
             // 填充请求参数,这里request对象的成员变量即对应接口的入参
             // 你可以通过官网接口文档或跳转到request对象的定义处查看请求参数的定义
             Filter respFilter = new Filter(); // 创建Filter对象, 以zone的维度来查询cvm实例
             respFilter.setName("zone");
             respFilter.setValues(new String[] { "ap-shanghai-1", "ap-shanghai-2" });
             req.setFilters(new Filter[] { respFilter }); // Filters 是成员为Filter对象的列表
             // 通过client对象调用DescribeInstances方法发起请求。注意请求方法名与请求对象是对应的
             // 返回的resp是一个DescribeInstancesResponse类的实例，与请求对象对应
             DescribeInstancesResponse resp = client.DescribeInstances(req);
             // 输出json格式的字符串回包
             System.out.println(DescribeInstancesResponse.toJsonString(resp));
             // 也可以取出单个值。
             // 你可以通过官网接口文档或跳转到response对象的定义处查看返回字段的定义
             System.out.println(resp.getTotalCount());
         } catch (TencentCloudSDKException e) {
              System.out.println(e.toString());
         }
     }
}
```
:::
</dx-codeblock>

### 更多示例

您可以在 [github](https://github.com/tencentcloud/tencentcloud-sdk-java) 中的`examples`目录下获取更多详细的示例。

## 相关配置

### 代理[](id:p3)

从3.0.96版本开始，可以单独设置 HTTP 代理： 

```
HttpProfile httpProfile = new HttpProfile();
httpProfile.setProxyHost("真实代理ip");
httpProfile.setProxyPort(真实代理端口);
```

### 语言

从3.1.16版本开始，我们添加了对公共参数 Language 的支持，以满足部分产品国际化的诉求。和以前一样，Language 默认不传，行为由各产品接口自行决定，通常是中文的，但也有默认英文的。目前可选值为中文或者英文,通过如下方法设置：

```
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.Language;
...
    ClientProfile clientProfile = new ClientProfile();
    clientProfile.setLanguage(Language.ZH_CN);
```

### 支持 http

SDK 支持 http 协议和 https 协议，通过设置 HttpProfile 的 setProtocol() 方法可以实现协议间的切换：

```
      HttpProfile httpProfile = new HttpProfile();
      httpProfile.setProtocol("http://"); //http 协议
      httpProfile.setProtocol("https://"); //https 协议
```

## 支持打印日志
自3.1.80版本开始，SDK 支持打印日志。
首先，在创建 CLientProfile 对象时，设置 debug 模式为真，会打印 sdk 异常信息和流量信息。
```
      ClientProfile clientProfile = new ClientProfile();
      clientProfile.setDebug(true);
```

腾讯云 java sdk 使用 commons.logging 类进行打印日志，如下所示。

```
九月 10, 2020 5:14:30 下午 com.tencentcloudapi.cvm.v20170312.CvmClient info
信息: send request, request url: https://cvm.ap-shanghai.tencentcloudapi.com/?Nonce=367595572&Action=DescribeInstances&Filters.0.Values.1=ap-shanghai-2&Version=2017-03-12&Filters.0.Values.0=ap-shanghai-1&SecretId=AKIDziAMHwiVO0LPCizu61e1iCQP7YiaOX7Q&Filters.0.Name=zone&RequestClient=SDK_JAVA_3.1.129&Region=ap-shanghai&SignatureMethod=HmacSHA256&Timestamp=1599729270&Signature=DcGRPdquMZZRPj1NFXP5bsOGnRlaT2KXy7aegNhZa00%3D. request headers information: 
九月 10, 2020 5:14:32 下午 com.tencentcloudapi.cvm.v20170312.CvmClient info
信息: recieve response, response url: https://cvm.ap-shanghai.tencentcloudapi.com/?Nonce=367595572&Action=DescribeInstances&Filters.0.Values.1=ap-shanghai-2&Version=2017-03-12&Filters.0.Values.0=ap-shanghai-1&SecretId=AKIDziAMHwiVO0LPCizu61e1iCQP7YiaOX7Q&Filters.0.Name=zone&RequestClient=SDK_JAVA_3.1.129&Region=ap-shanghai&SignatureMethod=HmacSHA256&Timestamp=1599729270&Signature=DcGRPdquMZZRPj1NFXP5bsOGnRlaT2KXy7aegNhZa00%3D, response headers: Server: nginx;Date: Thu, 10 Sep 2020 09:14:32 GMT;Content-Type: application/json;Content-Length: 103;Connection: keep-alive;OkHttp-Selected-Protocol: http/1.1;OkHttp-Sent-Millis: 1599729271230;OkHttp-Received-Millis: 1599729272020;,response body information: com.squareup.okhttp.internal.http.RealResponseBody@8646db9
```
用户可以根据自己的需要配置日志打印类，如 log4j，配置方法如下:
+ 配置 pom 文件，设置 log4j 版本。
```
    <dependency>
      <groupId>log4j</groupId>
      <artifactId>log4j</artifactId>
      <version>1.2.17</version>
    </dependency>
```
+ 设置环境变量为 log4j，并创建 log 类。
```
System.setProperty("org.apache.commons.logging.Log", "org.apache.commons.logging.impl.Log4JLogger");
Log logger = LogFactory.getLog("TestLog");
logger.info("hello world");
```

## 旧版 SDK

我们推荐您使用新版 SDK，如果需要旧版 SDK，请在您的 Maven pom.xml 添加以下依赖项即可：

```xml
<dependency>
<groupId>com.qcloud</groupId>
<artifactId>qcloud-java-sdk</artifactId>
<version>2.0.6</version>
</dependency>
```



## 常见问题
### 版本升级

请注意，从 3.0.x 版本升级到 3.1.x 版本有兼容性问题，对于 Integer 字段的使用修改为了 Long 类型，需要重新编译项目。

### 依赖冲突

目前，SDK 依赖 okhttp 2.5.0，如果和其他依赖 okhttp3 的包混用时，有可能会报错，例如:`Exception in thread "main" java.lang.NoSuchMethodError: okio.BufferedSource.rangeEquals(JLokio/ByteString;)Z`。原因是 okhttp3 依赖 okio 1.12.0，而 okhttp 依赖 okio 1.6.0，maven 在解析依赖时的规则是路径最短优先和顺序优先，所以如果 SDK 在 pom.xml 依赖中先被声明，则 okio 1.6.0 会被使用，从而报错。

在 SDK 没有升级到 okhttp3 前的解决办法：

1. 在 pom.xml 中明确指定依赖 okio 1.12.0 版本：
>?可能有其他包需要用到更高的版本，需要变通下取最高的可兼容版本，例如当其他包使用 okhttp4 时对应的可能是 okio 2.2.2。

```
    <dependency>
      <groupId>com.squareup.okio</groupId>
      <artifactId>okio</artifactId>
      <version>1.12.0</version>
    </dependency>
```

2. 将 SDK 放在依赖的最后（注意如果此前已经编译过，需要先删除掉 maven 缓存的 okhttp 包），以同时使用依赖 okhttp3 的 CMQ SDK 为例，形如（注意变通版本号）：
```
    <dependency>
      <groupId>com.qcloud</groupId>
      <artifactId>cmq-http-client</artifactId>
      <version>1.0.7</version>
    </dependency>
    <dependency>
      <groupId>com.tencentcloudapi</groupId>
      <artifactId>tencentcloud-sdk-java</artifactId>
      <version>3.1.59</version>
    </dependency>
```

### 证书问题

证书问题通常是客户端环境配置错误导致的。SDK 没有对证书进行操作，依赖的是 Java 运行环境本身的处理。出现证书问题后，可以使用`-Djavax.net.debug=ssl`开启详细日志辅助判断。

有用户报告使用 IBM JDK 1.8 出现证书报错：`javax.net.ssl.SSLHandshakeException: Received fatal alert: handshake_failure`，使用 Oracle JDK 后问题消失。

## Common Client

从 3.1.303 版本开始腾讯云 Java SDK 支持使用泛用性的 API 调用方式(Common Client)进行请求。您只需要安装  Common 包，即可向任何产品发起调用。

>?您必须明确知道您调用的接口所需参数，否则可能会调用失败。

目前仅支持使用 POST 方式，且签名方法必须使用签名方法 v3。详细使用请参阅示例：[使用 Common Client 进行调用](https://github.com/TencentCloud/tencentcloud-sdk-java/tree/master/examples/common/CommonClient)


## 支持重试请求

从 3.1.310 版本开始腾讯云 Java SDK 支持重试请求。对于每一个请求，您可以设置重试次数，如果接口请求未成功，就进行重试，直到请求成功或者达到重试次数为止。待设置的重试次数最大为10，最小为0，每次重试失败需要睡眠1秒钟。

详细使用请参阅示例：[使用 retry 进行重试请求](https://github.com/TencentCloud/tencentcloud-sdk-java/blob/master/examples/common/retry/Retry.java)。

## 凭证管理

腾讯云 Java SDK 目前支持以下几种方式进行凭证管理：

### 环境变量

默认读取环境变量 `TENCENTCLOUD_SECRET_ID` 和 `TENCENTCLOUD_SECRET_KEY` 获取 secretId 和 secretKey。相关代码如下：

```java
Credential cred = new EnvironmentVariableCredentialsProvider().getCredentials();
```

### 配置文件

配置文件路径要求为：

+ Windows: `c:\Users\NAME\.tencentcloud\credentials`
+ Linux: `~/.tencentcloud/credentials` 或 `/etc/tencentcloud/credentials`

配置文件格式如下：

```ini
[default]
secret_id = xxxxx
secret_key = xxxxx
```

相关代码如下：

```java
Credential cred = new ProfileCredentialsProvider().getCredentials();
```

### 角色扮演

有关角色扮演的相关概念请参阅：[腾讯云角色概述](https://cloud.tencent.com/document/product/598/19420)。

要使用此种方式，您必须在腾讯云访问管理控制台上创建了一个角色，具体创建过程请参阅：[腾讯云角色创建](https://cloud.tencent.com/document/product/598/19381)。

在您拥有角色后，可以通过持久密钥和 roleArn 获取临时凭证，SDK 会自动刷新临时凭证，相关代码如下：

```java
Credential cred = new STSCredential("secretId", "secretKey", "roleArn", "roleSessionName");
```

### 实例角色

有关实例角色的相关概念请参阅：[腾讯云实例角色](https://cloud.tencent.com/document/product/213/47668)。

在您为实例绑定角色后，您可以在实例中访问相关元数据接口获取临时凭证，SDK 会自动刷新临时凭证。相关代码如下：

```java
Credential cred = new CvmRoleCredential();
```

### 凭证提供链

腾讯云 Java SDK 提供了凭证提供链，它会默认以环境变量->配置文件->实例角色的顺序尝试获取凭证，并返回第一个获取到的凭证。相关代码如下：

```java
Credential cred = new DefaultCredentialsProvider().getCredentials();
```

凭证管理详细使用请参阅示例：[使用凭证提供链](https://github.com/TencentCloud/tencentcloud-sdk-java/blob/master/examples/common/credential_manager/CredentialManager.java)。
