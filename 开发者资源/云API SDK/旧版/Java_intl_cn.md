为方便Java开发者调试和接入云API， 我们提供了基于Java的SDK。

## 环境准备

1. 腾讯云Java SDK适用于JDK 7及以上版本。
2. [获取安全凭证](https://console.cloud.tencent.com/capi)。在第一次使用云API之前，用户首先需要在腾讯云控制台上申请安全凭证，安全凭证包括 SecretId 和 SecretKey, SecretId 是用于标识 API 调用者的身份，SecretKey是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。
3. 到[腾讯云控制台](https://console.cloud.tencent.com/)开通相应产品。

## SDK获取与安装

可以通过以下方式获取JAVA SDK，开发者可以结合自身的情况，选择SDK源码、添加maven依赖项或者使用jar包。

1. 获取源码
[从 Github 访问 >>](https://github.com/QcloudApi/qcloudapi-sdk-java)
[点击下载 Java SDK >>](https://mc.qcloudimg.com/static/archive/72dbc1a82ad8e18dead2e6dc07acd5d7/qcloudapi-sdk-java-master.zip)

2. maven
详情请点击查看[maven依赖项](https://mvnrepository.com/artifact/com.qcloud/qcloud-java-sdk)，以2.0.1版本的JAVA SDK为例，只需在pom.xml添加以下依赖项即可：
```
<dependency>
  <groupId>com.qcloud</groupId>
  <artifactId>qcloud-java-sdk</artifactId>
  <version>2.0.1</version>
</dependency>
```

3. 获取jar包
点击进入[jar包的版本列表](https://mvnrepository.com/artifact/com.qcloud/qcloud-java-sdk)，选择相应的版本，点击"Download (JAR)"下载jar包，再将jar包引用到你的项目即可。

## 示例

### 公共说明
见不同模块API的公共参数、API概览、错误码。如[云服务器API公共参数](http://cloud.tencent.com/document/api/213/6976)、[云服务器API概览](http://cloud.tencent.com/doc/api/229/API%E6%A6%82%E8%A7%88)、[云服务器API错误码](http://cloud.tencent.com/doc/api/229/%E9%94%99%E8%AF%AF%E7%A0%81)。



### 示例
**DescribeInstances 接口**
```
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
     * 你将要使用接口所在的模块，可以从 官网->云api文档->XXXX接口->接口描述->域名
     * 中获取，比如域名：cvm.api.qcloud.com，module就是new Cvm()。
     */
    /*
     * DescribeInstances
     * 的api文档地址：http://cloud.tencent.com/wiki/v2/DescribeInstances
     */
    QcloudApiModuleCenter module = new QcloudApiModuleCenter(new Cvm(),config);
    TreeMap<String, Object> params = new TreeMap<String, Object>();
    /* 将需要输入的参数都放入 params 里面，必选参数是必填的。 */
    /* DescribeInstances 接口的部分可选参数如下 */
    params.put("offset", 0);
    params.put("limit", 3);
    /* generateUrl 方法生成请求串，但不发送请求。在正式请求中，可以删除下面这行代码。 */
    // System.out.println(module.generateUrl("DescribeInstances", params));

    String result = null;
    try {
        /* call 方法正式向指定的接口名发送请求，并把请求参数params传入，返回即是接口的请求结果。 */
        result = module.call("DescribeInstances", params);
        JSONObject json_result = new JSONObject(result);
        System.out.println(json_result);
    } catch (Exception e) {
        System.out.println("error..." + e.getMessage());
    }
}
}
```
