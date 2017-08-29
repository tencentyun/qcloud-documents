# Java SDK
## 简介
欢迎使用腾讯云开发者工具套件（SDK）。为方便 JAVA 开发者调试和接入腾讯云产品 API，这里向您介绍适用于 Java 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例。让您快速获取腾讯云 Java SDK 并开始调用。

## 依赖环境
1.  依赖环境：JDK 7 版本及以上
2. 从 [腾讯云控制台](https://console.qcloud.com) 开通相应产品，
3. [获取 SecretID、SecretKey](https://console.qcloud.com/capi) 以及调用地址（endpoint），endpoint 一般形式为`*.api.qcloud.com`，如CVM 的调用地址为 `cvm.api.qcloud.com`，具体参考各产品说明。
4. 下载相关资料并做好相关文件配置。

## 获取安装
安装 Java SDK 前，先获取安全凭证。在第一次使用云API之前，用户首先需要在腾讯云控制台上申请安全凭证，安全凭证包括 SecretID 和 SecretKey, SecretID 是用于标识 API 调用者的身份，SecretKey是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。

### 获取 JAR 包安装
1. 打开腾讯云为您提供的 JAVA SDK JAR包下载地址，[获取 jar包地址 >>](https://mvnrepository.com/artifact/com.qcloud/qcloud-java-sdk)
2. 进入 jar 包的版本列表，选择相应的版本
3. 单击 "Download (JAR)" 下载 jar 包
4. 将 jar 包引用到您的项目
5. 配置方法可参考 Demo.java 示例配置和引用源码

### 通过 GitHub 获取源码安装
打开腾讯云为您提供的 JAVA SDK GitHub 地址，[获取 GitHub 资源 >>](https://github.com/QcloudApi/qcloudapi-sdk-java)。
1. 在 `qcloudapi-sdk-java`的 github 地址上下载源码
2. 解压源码到您项目合适的位置
3. 配置方法可参考 Demo.java 示例配置和引用源码

### 通过 maven 获取安装
通过 Maven 获取安装是使用 JAVA SDK 的推荐方法（关于 Maven 的介绍详见 [Maven 官方网站](https://maven.apache.org/)）。
1. 下载并安装 Maven。下载 Maven 可以单击 [下载 Maven >>](https://maven.apache.org/download.cgi)，安装Maven可参考 [官网 Maven 安装](https://maven.apache.org/install.html)
2. 为您的项目添加 Maven 依赖项，详情请参阅 [查看 maven 依赖项](https://mvnrepository.com/artifact/com.qcloud/qcloud-java-sdk)

以 2.0.1 版本的 JAVA SDK 为例，只需在 pom.xml 添加以下依赖项即可：
```
<dependency>
<groupId>com.qcloud</groupId>
<artifactId>qcloud-java-sdk</artifactId>
<version>2.0.1</version>
</dependency>
```
3.运行 maven 命令获取 sdk 后，配置方法可参考 Demo.java 示例配置和引用源码。

## 入门 DEMO
以 CVM 查看实例列表（DescribeInstances）为例：
```
import java.util.TreeMap;

import com.qcloud.QcloudApiModuleCenter;
import com.qcloud.Module.Cvm;
import com.qcloud.Utilities.Json.JSONObject;

public class Demo {
 public static void main(String[] args) {
  /* 如果是循环调用下面举例的接口，需要从此处开始你的循环语句。切记！ */
  TreeMap<String, Object> config = new TreeMap<String, Object>();
  config.put("SecretId", "你的secretId");
  config.put("SecretKey", "你的secretKey");
  /* 请求方法类型 POST、GET */
  config.put("RequestMethod", "GET");
  /* 区域参数，可选: gz:广州; sh:上海; hk:香港; ca:北美;等。 */
  config.put("DefaultRegion", "gz");

  /*
   * 你将要使用接口所在的模块，可以从 官网->云 API 文档->XXXX 接口->接口描述->域名
   * 中获取，比如域名：cvm.api.qcloud.com，module 就是 new Cvm()。
   */
  /*
   * 示例：DescribeInstances 
   * 的 API 文档地址：https://www.qcloud.com/document/product/213/9388
   */
  QcloudApiModuleCenter module = new QcloudApiModuleCenter(new Cvm(),
    config);

  TreeMap<String, Object> params = new TreeMap<String, Object>();
  /* 将需要输入的参数都放入 params 里面，必选参数是必填的。 */
  /* DescribeInstances 接口的部分可选参数如下 */
  params.put("offset", 0);
  params.put("limit", 3);
  /*在这里指定所要用的签名算法，不指定默认为 HmacSHA1*/
  //params.put("SignatureMethod", "HmacSHA256");
  
  /* generateUrl 方法生成请求串,可用于调试使用 */
  //System.out.println(module.generateUrl("DescribeInstances", params));
  String result = null;
  try {
   /* call 方法正式向指定的接口名发送请求，并把请求参数 params 传入，返回即是接口的请求结果。 */
   result = module.call("DescribeInstances", params);
   JSONObject json_result = new JSONObject(result);
   System.out.println(json_result);
  } catch (Exception e) {
   System.out.println("error..." + e.getMessage());
  }

 }
}
```