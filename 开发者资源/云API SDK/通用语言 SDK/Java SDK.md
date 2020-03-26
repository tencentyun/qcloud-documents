本文主要介绍适用于 Java 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例，让 Java 开发者快速掌握如何调试和接入腾讯云产品 API。
支持 SDK 3.0 版本的云产品列表请参见 [SDK 简介](https://cloud.tencent.com/document/product/494/42698)。

## 依赖环境
- 依赖环境：JDK 7 及以上版本。
- 登录 [腾讯云控制台](https://console.cloud.tencent.com/) 开通相应云产品。
- 在访问管理控制台 >【[API密钥管理](https://console.cloud.tencent.com/cam/capi)】页面获取 SecretID 和 SecretKey。
 - SecretID 用于标识 API 调用者的身份。
 - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，**SecretKey 需妥善保管，避免泄露**。
- 获取调用地址（endpoint），endpoint 一般格式为`*.tencentcloudapi.com`，例如 CVM 的调用地址为`cvm.tencentcloudapi.com`，具体地址请参考各云产品说明。

## 获取安装

### 通过 Maven 安装（推荐）
[Maven](https://maven.apache.org) 是 Java 的依赖管理工具，支持您项目所需的依赖项，并将其安装到项目中。
1. 访问 [Maven 官网](https://maven.apache.org/) 下载对应系统 Maven 安装包进行安装。
2. 为您的项目添加 Maven 依赖项，只需在 Maven pom.xml 添加以下依赖项即可：
```xml
<dependency>
        <groupId>com.tencentcloudapi</groupId>
        <artifactId>tencentcloud-sdk-java</artifactId>
        <version>3.0.8</version><!-- 注：这里只是示例版本号，请到 https://mvnrepository.com/artifact/com.tencentcloudapi/tencentcloud-sdk-java 获取最新版本号 -->
</dependency>
```
3. 引用方法可参考 [示例](#example)。

### 通过源码包安装
1. 前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-java) 或者 [快速下载地址](https://tencentcloud-sdk-1253896243.file.myqcloud.com/tencentcloud-sdk-java/tencentcloud-sdk-java.zip) 下载源码压缩包。
2. 解压源码包到您项目合适的位置。
3. 需要将 vendor 目录下的 jar 包放在 Java 的可找到的路径中。
4. 引用方法可参考 [示例](#example)。

<span id="example"></span>
## 示例

本文以云服务器查询可用区接口为例，介绍 SDK 的基础用法，更多示例请参考 [examples 目录](https://github.com/TencentCloud/tencentcloud-sdk-java/tree/master/examples)。

```java
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
// 导入对应产品模块的 client
import com.tencentcloudapi.cvm.v20170312.CvmClient;
// 导入要请求接口对应的 request response 类
import com.tencentcloudapi.cvm.v20170312.models.DescribeZonesRequest;
import com.tencentcloudapi.cvm.v20170312.models.DescribeZonesResponse;

public class DescribeZones
{
    public static void main(String [] args) {
        try{
            // 实例化一个认证对象，入参需要传入腾讯云账户 secretId，secretKey
            Credential cred = new Credential("secretId", "secretKey");

            // 实例化要请求产品（以 CVM 为例）的 client 对象
            CvmClient client = new CvmClient(cred, "ap-guangzhou");

            // 实例化一个请求对象
            DescribeZonesRequest req = new DescribeZonesRequest();

            // 通过 client 对象调用想要访问的接口，需要传入请求对象
            DescribeZonesResponse resp = client.DescribeZones(req);

            // 输出 JSON 格式的字符串回包
            System.out.println(DescribeZonesRequest.toJsonString(resp));
        } catch (TencentCloudSDKException e) {
                System.out.println(e.toString());
        }

    }

}
```
## 相关配置
您可以通过以下方式指定代理：

**方式一**：指定代理访问（版本>=3.0.96），目前仅支持 HTTP 代理：
```
HttpProfile httpProfile = new HttpProfile();
httpProfile.setProxyHost("真实代理 IP");
httpProfile.setProxyPort(真实代理端口);
```
**方式二**：设置系统代理，请求发起前，您可以代码中设置：
```
System.setProperty("https.proxyHost", "真实代理 IP");
System.setProperty("https.proxyPort", "真实代理端口");
```
**方式三**：运行程序时在启动参数中设置。

## 其他问题
SDK 3.1.x版本中`Integer`字段的已改为`Long`类型，SDK 从3.0.x版本升级到3.1.x版本时需要重新编译项目。

## 旧版 SDK
我们推荐您使用新版 SDK， 如果需要旧版 SDK，请在您的 Maven pom.xml 添加以下依赖项即可：
```xml
<dependency>
<groupId>com.qcloud</groupId>
<artifactId>qcloud-java-sdk</artifactId>
<version>2.0.6</version>
</dependency>
```
