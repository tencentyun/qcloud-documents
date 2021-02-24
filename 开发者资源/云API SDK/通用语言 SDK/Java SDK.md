## 简介
* 欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK 3.0 是云 API 3.0 平台的配套工具。SDK 3.0 实现了统一化，各个语言版本的 SDK 具备使用方法相同、接口调用方式相同、错误码和返回包格式相同等优点。
* 本文以 Java SDK 3.0 为例，介绍如何使用、调试并接入腾讯云产品 API。
* 目前已支持云服务器 CVM、私有网络 VPC 、云硬盘 CBS 等 [腾讯云产品](https://cloud.tencent.com/document/sdk/Description)，后续会支持其他云产品接入。

## 依赖环境

* JDK 7版本及以上。
* 获取安全凭证。安全凭证包含 SecretId 及 SecretKey 两部分。SecretId 用于标识 API 调用者的身份，SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥。前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面，即可进行获取，如下图所示：
![](https://main.qcloudimg.com/raw/78145f9e6a830a188304991552a5c614.png)
>!**您的安全凭证代表您的账号身份和所拥有的权限，等同于您的登录密码，切勿泄露他人。**
* 获取调用地址。调用地址（endpoint）一般形式为`*.tencentcloudapi.com`，产品的调用地址有一定区别，例如，云服务器的调用地址为`cvm.tencentcloudapi.com`。具体调用地址可参考对应产品的 [API 文档](https://cloud.tencent.com/document/api)。

## 安装 SDK[](id:p1)

### 通过 Maven 安装（推荐）

Maven 是 JAVA 的依赖管理工具，支持您项目所需的依赖项，并将其安装到项目中。关于 Maven 详细可参考 [Maven 官网](https://maven.apache.org/)。

1. 为您的项目添加 Maven 依赖项，只需在 pom.xml 中找到`<dependencies>`标签，在里面添加以下依赖项即可。
>!
>- 这里的版本号只是举例，您可以在 [Maven 仓库](https://search.maven.org/search?q=tencentcloud-sdk-java) 上找到最新的版本。
>- [Maven 仓库](https://search.maven.org/search?q=tencentcloud-sdk-java) 中显示的4.0.11是废弃版本，由于 Maven 索引更新问题尚未完全删除。

	```xml
<dependency>
    <groupId>com.tencentcloudapi</groupId>
    <artifactId>tencentcloud-sdk-java</artifactId>
    <!-- go to https://search.maven.org/search?q=tencentcloud-sdk-java and get the latest version. -->
    <!-- 请到 https://search.maven.org/search?q=tencentcloud-sdk-java 查询最新版本 -->
    <version>3.1.87</version>
</dependency>
```
2. 设置镜像源以加快下载速度。
```xml
<repositories>
	<repository>
      <id>nexus-tencentyun</id>
      <name>Nexus tencentyun</name>
      <url>https://mirrors.tencent.com/nexus/repository/maven-public/</url>
	</repository>
</repositories>
```

示例如下图所示：
![](https://main.qcloudimg.com/raw/cc7027bc9fc9c7863121c2dfdeda3185.png)  

3. 在命令端进入到 “G:\maven-demo”（示例项目根路径）：
```bash
#  创建JAR/WAR包如在 pom.xml 中定义提及的包。
G:\maven-demo>mvn package
```


## 使用 SDK

### 示例1：查询可用区（DescribeZones）

以 [查询可用区](https://cloud.tencent.com/document/product/213/15707) 接口为例，创建`DescribeZones.java`文件（例如上述 Maven 安装示例中的`G:\maven-demo\src\main\java\com\Demo\App.java`），并写入以下代码：

```java
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
import com.tencentcloudapi.common.profile.ClientProfile;
// 导入对应产品模块的 client
import com.tencentcloudapi.cvm.v20170312.CvmClient;
// 导入要请求接口对应的 request response 类
import com.tencentcloudapi.cvm.v20170312.models.DescribeZonesRequest;
import com.tencentcloudapi.cvm.v20170312.models.DescribeZonesResponse;
//导入可选配置类
import com.tencentcloudapi.common.profile.HttpProfile;

public class DescribeZones{
    public static void main(String [] args) {
        try{
            // 实例化一个认证对象，入参需要传入腾讯云账户 secretId、secretKey
            Credential cred = new Credential("secretId", "secretKey");
            
            // 实例化要请求产品（以 cvm 为例）的 client 对象
            CvmClient client = new CvmClient(cred, "ap-guangzhou");
            
            // 实例化一个请求对象
            DescribeZonesRequest req = new DescribeZonesRequest();
            
            // 通过 client 对象调用想要访问的接口，需要传入请求对象
            DescribeZonesResponse resp = client.DescribeZones(req);
            
            // 输出 json 格式的字符串回包
            System.out.println(DescribeZonesRequest.toJsonString(resp));
        } catch (TencentCloudSDKException e) {
            System.out.println(e.toString());
        }
    }
} 
```

通过命令端运行 java 项目：

```bash
# 进入到 maven-demo 目录下：编译
G:\maven-demo>mvn compile
# 在项目根目录下生成了 target 文件夹，里面存放了 class 文件。运行示例中的 DescribeZones
# *示例中的凭证需要换成真实值，更要注意凭证的保密性*
G:\maven-demo>mvn exec:java -Dexec.mainClass="com.Demo.DescribeZones"
# 运行成功！注意，不能直接用 java 命令运行（除非指定 classpath），因为项目依赖了外部 jar 包。
```

### 示例2：查看实例列表（DescribeInstances）

以 [查看实例列表](https://cloud.tencent.com/document/product/213/15728) 接口为例，创建`DescribeInstances.java`文件并写入以下代码：

```java
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
// 导入对应产品模块的 client
import com.tencentcloudapi.cvm.v20170312.CvmClient;
// 导入要请求接口对应的 request response 类
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
            // 实例化一个认证对象，入参需要传入腾讯云账户 secretId、secretKey，此处还需注意密钥对的保密
            Credential cred = new Credential("secretId", "secretKey");

            // 实例化一个 http 选项，可选的，没有特殊需求可以跳过
            HttpProfile httpProfile = new HttpProfile();
            //  从3.1.16版本开始, 单独设置 HTTP 代理
            // httpProfile.setProxyHost("真实代理ip");
            // httpProfile.setProxyPort(真实代理端口);
            httpProfile.setReqMethod("GET"); // get 请求(默认为post请求)
            httpProfile.setProtocol("https://");  // 在外网互通的网络环境下支持 http 协议（默认是 https 协议），请选择(https:// or http://)
            httpProfile.setConnTimeout(30); // 请求连接超时时间，单位为秒（默认60秒）
            httpProfile.setWriteTimeout(30);  // 设置写入超时时间，单位为秒（默认0秒）
            httpProfile.setReadTimeout(30);  // 设置读取超时时间，单位为秒（默认0秒）
            httpProfile.setEndpoint("cvm.ap-shanghai.tencentcloudapi.com"); // 指定接入地域域名（默认就近接入）

            // 实例化一个 client 选项，可选的，没有特殊需求可以跳过
            ClientProfile clientProfile = new ClientProfile();
            clientProfile.setSignMethod("HmacSHA256"); // 指定签名算法（默认为 HmacSHA256）
            // 自3.1.80版本开始，SDK 支持打印日志。
            clientProfile.setHttpProfile(httpProfile);
            clientProfile.setDebug(true);
            // 从3.1.16版本开始，支持设置公共参数 Language, 默认不传，选择（ZH_CN or EN_US）
            clientProfile.setLanguage(Language.EN_US);
            // 实例化要请求产品（以 cvm 为例）的 client 对象，clientProfile 是可选的
            CvmClient client = new CvmClient(cred, "ap-shanghai", clientProfile);

            // 实例化一个 cvm 实例信息查询请求对象，每个接口都会对应一个 request 对象。
            DescribeInstancesRequest req = new DescribeInstancesRequest();

            // 填充请求参数，这里 request 对象的成员变量即对应接口的入参
            // 您可以通过官网接口文档或跳转到 request 对象的定义处查看请求参数的定义
            Filter respFilter = new Filter(); // 创建 Filter 对象, 以 zone 的维度来查询 cvm 实例
            respFilter.setName("zone");
            respFilter.setValues(new String[] { "ap-shanghai-1", "ap-shanghai-2" });
            req.setFilters(new Filter[] { respFilter }); // Filters 是成员为Filter对象的列表

            // 通过 client 对象调用 DescribeInstances 方法发起请求。注意请求方法名与请求对象是对应的
            // 返回的 resp 是一个 DescribeInstancesResponse 类的实例，与请求对象对应
            DescribeInstancesResponse resp = client.DescribeInstances(req);

            // 输出 json 格式的字符串回包
            System.out.println(DescribeInstancesResponse.toJsonString(resp));

            // 也可以取出单个值。
            // 您可以通过官网接口文档或跳转到 response 对象的定义处查看返回字段的定义
            System.out.println(resp.getTotalCount());
        } catch (TencentCloudSDKException e) {
            System.out.println(e.toString());
        }
    }
}
```

### 更多示例

您可以在 [github](https://github.com/tencentcloud/tencentcloud-sdk-java) 中的`examples`目录下获取更多详细的示例。



## 相关配置

### 代理配置[](id:p3)

从3.0.96版本开始，可以单独设置 HTTP 代理： 

```
HttpProfile httpProfile = new HttpProfile();
httpProfile.setProxyHost("真实代理ip");
httpProfile.setProxyPort(真实代理端口);
```

### 语言

从3.1.16版本开始，我们添加了对公共参数 Language 的支持，以满足部分产品国际化的诉求。和以前一样，Language 默认不传，通常是中文的，但也有默认英文的。目前可选值为中文（zh-CN）或者英文（en-US），通过如下方法设置： 

```java
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
首先，在创建 CLientProfile 对象时，设置 debug 模式为真,会打印sdk异常信息和流量信息。
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

### 更新仓库 pom.xml 文件里面的依赖失败

可能是因为本机配置了代理，而工具在更新时未进行代理的配置导致，按照上文在命令端更新依赖，如果还是失败，这时候需要看是否因为网络不通还是防火墙拦截。

### 运行示例失败

`[TencentCloudSDKException]message:java.net.ConnectException-Connection timed out: connect requestId:`这里需要排查：是否本机配置了代理，而未在代码中加入代理，代理的加入可参考上文的 [代理配置](#p3)。

### 版本升级

请注意，从3.0.x版本升级到3.1.x版本有兼容性问题，对于 Integer 字段的使用修改为了 Long 类型，需要重新编译项目。

### 依赖冲突

目前，SDK 依赖 okhttp 2.5.0，如果和其他依赖 okhttp3 的包混用时，有可能会报错：如`Exception in thread "main" java.lang.NoSuchMethodError: okio.BufferedSource.rangeEquals(JLokio/ByteString;)Z`。

原因是 okhttp3 依赖 okio 1.12.0，而 okhttp 依赖 okio 1.6.0，maven 在解析依赖时的规则是路径最短优先和顺序优先，所以如果 SDK 在 pom.xml 依赖中先被声明，则 okio 1.6.0 会被使用，从而报错。

在 SDK 没有升级到 okhttp3 前的解决办法：
1. 在 pom.xml 中明确指定依赖 okio 1.12.0 版本（注意可能有其他包需要用到更高的版本，变通下取最高版本即可）。
2. 将 SDK 放在依赖的最后（注意如果此前已经编译过，则需要先删除掉 maven 缓存的 okhttp 包），以同时使用依赖 okhttp3 的 CMQ SDK 为例，形如（注意变通版本号）： 
```xml
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






