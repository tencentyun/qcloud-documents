## 简介
欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK3.0 是云 API3.0 平台的配套工具。目前已经支持 cvm、vpc、cbs 等产品，后续所有的云服务产品都会接入进来。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，统一的错误码和返回包格式这些优点。
为方便 JAVA 开发者调试和接入腾讯云产品 API，这里向您介绍适用于 Java 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例。让您快速获取腾讯云 Java SDK 并开始调用。
## 支持的产品

|产品名称|支持JAVA SDK3.0|
|----|------|
|云服务器 (CVM)|是|
|云硬盘 (CBS) |是|
|私有网络 (VPC)|是|
|云数据库(CDB)|是|
|批量计算|是|
|云数据库 MariaDB|是|
|无服务器云函数|是|
|分布式数据库 DCDB|是|
|物联网套件|是|
|渠道合作伙伴|是|
| Web漏洞扫描  | 是  |
|腾讯机器翻译|是|
|云数据库 PostgreSQL|是|

## 依赖环境
1. 依赖环境：JDK 7 版本及以上。
2. 从 [腾讯云控制台](https://console.cloud.tencent.com/) 开通相应产品。
3. 获取 SecretID、SecretKey 以及调用地址（endpoint），endpoint 一般形式为*.tencentcloudapi.com，如 CVM 的调用地址为 cvm.tencentcloudapi.com，具体参考各产品说明。

## 获取安装
安装 Java SDK 前，先获取安全凭证。在第一次使用云 API 之前，用户首先需要在腾讯云控制台上申请安全凭证，安全凭证包括 SecretID 和 SecretKey， SecretID 是用于标识 API 调用者的身份，SecretKey是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。
### 通过 Maven 安装(推荐)
通过 Maven 获取安装是使用 JAVA SDK 的推荐方法，Maven 是 JAVA 的依赖管理工具，支持您项目所需的依赖项，并将其安装到项目中。关于 Maven 详细可参考 Maven 官网 。
1. 请访问 [Maven官网](https://maven.apache.org/) 下载对应系统 Maven 安装包进行安装。
2. 为您的项目添加 Maven 依赖项，只需在 Maven pom.xml 添加以下依赖项即可：
```xml
<dependency>
        <groupId>com.tencentcloudapi</groupId>
        <artifactId>tencentcloud-sdk-java</artifactId>
        <version>3.0.1</version>
</dependency>
```
3. 引用方法可参考示例。

### 通过源码包安装
1. 前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-java) 下载源码压缩包。
2. 解压源码包到您项目合适的位置。
3. 需要将 vendor 目录下的 jar 包放在 java 的可找到的路径中。
4. 引用方法可参考示例。

## 示例
以查询可用区接口为例:
```java
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
// 导入对应产品模块的client
import com.tencentcloudapi.cvm.v20170312.CvmClient;
// 导入要请求接口对应的request response类
import com.tencentcloudapi.cvm.v20170312.models.DescribeZonesRequest;
import com.tencentcloudapi.cvm.v20170312.models.DescribeZonesResponse;

public class DescribeZones
{
    public static void main(String [] args) {
        try{
            // 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
            Credential cred = new Credential("secretId", "secretKey");

            // 实例化要请求产品(以cvm为例)的client对象
            CvmClient client = new CvmClient(cred, "ap-guangzhou");

            // 实例化一个请求对象
            DescribeZonesRequest req = new DescribeZonesRequest();

            // 通过client对象调用想要访问的接口，需要传入请求对象
            DescribeZonesResponse resp = client.DescribeZones(req);

            // 输出json格式的字符串回包
            System.out.println(DescribeZonesRequest.toJsonString(resp));
        } catch (TencentCloudSDKException e) {
                System.out.println(e.toString());
        }

    }

}
```
您可以在 [github仓库](https://github.com/tencentcloud/tencentcloud-sdk-java) 中 examples 目录下找到更详细的示例。
## 旧版 SDK
我们推荐您使用新版 SDK， 如果需要旧版 SDK，请在您的 Maven pom.xml 添加以下依赖项即可：
```xml
<dependency>
<groupId>com.qcloud</groupId>
<artifactId>qcloud-java-sdk</artifactId>
<version>2.0.6</version>
</dependency>
```
