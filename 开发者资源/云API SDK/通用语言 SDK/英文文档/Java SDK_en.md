
## Overview
Welcome to use Tencent Cloud Software Development Kit (SDK). To help JAVA developers debug and connect to the Tencent Cloud product API, here we introduce the Tencent Cloud SDK suitable for Java, and provide a simple example of getting started with the SDK. Then, you can quickly get the Tencent Cloud Java SDK and start calling.

## Supported Environment
1. Supported environment: JDL 7 or above
2. Activate the corresponding product on [Tencent Cloud Console](https://console.cloud.tencent.com).
3. [Get SecretID, SecretKey](https://console.cloud.tencent.com/capi) and the URL for calling (endpoint). The general form of endpoint is `*.api.qcloud.com`, for example, the endpoint for CVM is `cvm.api.qcloud.com`. For more information, please see product descriptions.
4. Download the relevant information and configure the relevant files.

## Installation
Before installing Java SDK, you should obtain the security credential first. Before calling the Cloud API for the first time, you need to apply for a security credential on the Tencent Cloud console. A security credential consists of a SecretID, which is used to identify an API caller, and a SecretKey, which is used to encrypt the signature string and the key used to verify the signature string on the server end. You must keep your SecretKey strictly confidential to avoid disclosure.

### Obtaining Jar Package for Installation
1. Click on the download address of JAVA SDK JAR package provided by Tencent Cloud. [Get jar package address >>](https://mvnrepository.com/artifact/com.qcloud/qcloud-java-sdk)
2. Enter the list of the jar package versions, and select the appropriate one
3. Click **Download (JAR)** to download the jar package
4. Reference the jar package to your project
5. You can refer to Demo.java example and reference source code for configuration

### Obtaining Source Code via GitHub for Installation
Click on the GitHub address of JAVA SDK provided by Tencent Cloud. [Get GitHub resources >>](https://github.com/QcloudApi/qcloudapi-sdk-java).
1. Download source code from the Github address of `qcloudapi-sdk-java`
2. Extract the source code to the proper location of your project
3. You can refer to Demo.java example and reference source code for configuration

## Installing via Maven
Installing via Maven is recommended for JAVA SDK. For more information on Maven, please see the [Maven official website](https://maven.apache.org/).
1. Download and install Maven. Click [Download Maven >>](https://maven.apache.org/download.cgi) to download Maven, and install Maven by referring to the [installation method on official website](https://maven.apache.org/install.html).
2. To add Maven dependency to your project, please see [View Maven Dependency](https://mvnrepository.com/artifact/com.qcloud/qcloud-java-sdk) for details.

To take Java SDK version 2.0.1 as an example, you only need to add the following dependencies in pom.xml:
```
<dependency>
<groupId>com.qcloud</groupId>
<artifactId>qcloud-java-sdk</artifactId>
<version>2.0.1</version>
</dependency>
```
3. After getting the SDK by executing the maven command, you can refer to Demo.java example and reference source code for configuration.

## Quick Start Demo
Take CVM's "View Instance List" (DescribeInstances) as an example:
```
import java.util.TreeMap;

import com.qcloud.QcloudApiModuleCenter;
import com.qcloud.Module.Cvm;
import com.qcloud.Utilities.Json.JSONObject;

public class Demo {
 public static void main(String[] args) {
  /* Remember to start your loop statement from here if you cyclically call the APIs in the following example. Keep in mind! */
  TreeMap<String, Object> config = new TreeMap<String, Object>();
  config.put("SecretId", "Your secretId");
  config.put("SecretKey", "Your secretKey");
  /* Request methods: POST, GET */
  config.put("RequestMethod", "GET");
  /* Region parameter. Available values: gz: Guangzhou; sh: Shanghai; hk: Hong Kong; ca: North America; etc. */
  config.put("DefaultRegion", "gz");

  /*
   * You can get the module to which the API belongs from Tencent Cloud website -> Cloud API documentation -> XXXX API -> API Description-> Domain name.
   * For example, you can get the module "new Cvm()" from the domain name "cvm.api.qcloud.com".
   */
  /*
   * Example: DescribeInstances 
   * URL for API documentation: https://cloud.tencent.com/document/product/213/9388
   */
  QcloudApiModuleCenter module = new QcloudApiModuleCenter(new Cvm(),
    config);

  TreeMap<String, Object> params = new TreeMap<String, Object>();
  /* Place the parameters to be entered into params. The required parameters are mandatory. */
  /* Some of the optional parameters for the API DescribeInstances are as follows */
  params.put("offset", 0);
  params.put("limit", 3);
  /* Specify the signature algorithm to be used here, otherwise the default is HmacSHA1. */
  //params.put("SignatureMethod", "HmacSHA256");
  
  /* Generate the request string using generateUrl method, which can be used for debugging. */
  //System.out.println(module.generateUrl("DescribeInstances", params));
  String result = null;
  try {
   /* Send a formal request to the specified API using call method, and pass the request parameter params. Then, the request result of the API is returned. */
   result = module.call("DescribeInstances", params);
   JSONObject json_result = new JSONObject(result);
   System.out.println(json_result);
  } catch (Exception e) {
   System.out.println("error..." + e.getMessage());
  }

 }
}
```

