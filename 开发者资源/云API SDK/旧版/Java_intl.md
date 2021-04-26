We provide Java based SDK to make it easy for developers to debug and access Cloud API.

Download from: https://github.com/QcloudApi/qcloudapi-sdk-java

The qcloudapi-sdk-java SDK is designed to make it easy for java developers to use Tencent Cloud API in their codes.

## 1. Resources
For details, refer to API common parameters, overview and error codes in different modules. For instance, [CVM API Common Parameters](http://cloud.tencent.com/document/api/213/6976), [CVM API Overview](http://cloud.tencent.com/doc/api/229/API%E6%A6%82%E8%A7%88) and [CVM API Error Codes](http://cloud.tencent.com/doc/api/229/%E9%94%99%E8%AF%AF%E7%A0%81).

## 2. Quick Start
1) [Get Security Credential](https://console.cloud.tencent.com/capi). Before calling the Cloud API for the first time, you need to apply for a security credential on the Tencent Cloud console. A security credential consists of a SecretId, which is used to identify an API caller, and a SecretKey, which is used to encrypt the signature string and verify the string on the server. You must keep your SecretKey strictly confidential to avoid disclosure.

2) [Download SDK](https://github.com/QcloudApi/qcloudapi-sdk-java), and put it in your program directory. For details, refer to the example below.

## 3. Example
**DescribeInstances API**
```
public class Demo {
public static void main(String[] args) {
    /* Remember to start your loop statement from here if you cyclically call the  following API. */
    TreeMap<String, Object> config = new TreeMap<String, Object>();
    config.put("SecretId", "Your secretId");
    config.put("SecretKey", "Your secretKey");
    /* Request methods: POST, GET */
    config.put("RequestMethod", "GET");
    /* Available region parameters: gz: Guangzhou; sh: Shanghai; hk: Hong Kong; ca: North America */
    config.put("DefaultRegion", "gz");

    /*
     * You can get the module to which the API belongs from Tecent Cloud website -> Cloud API documentation -> XXXX API-> Description-> Domain.
     * For instance, you can get the module "new Cvm()" from the domain "cvm.api.qcloud.com".
     */
    /*
     *API documentation address of DescribeInstances
     *: http://cloud.tencent.com/wiki/v2/DescribeInstances
     */
    QcloudApiModuleCenter module = new QcloudApiModuleCenter(new Cvm(),config);
    TreeMap<String, Object> params = new TreeMap<String, Object>();
    /* Put the parameters to be entered into params. The required parameters are mandatory. */
    /* Some of the optional parameters for DescribeInstances API are as follows */
    params.put("offset", 0);
    params.put("limit", 3);
    /* Generate the request string using generateUrl method, but not send it. The following line of code may be deleted in formal request. */
    // System.out.println(module.generateUrl("DescribeInstances", params));

    String result = null;
    try {
        /* Send a formal request to the specified API using call method, and input the request parameter params. Then, the request result of the API will be returned. */
        result = module.call("DescribeInstances", params);
        JSONObject json_result = new JSONObject(result);
        System.out.println(json_result);
    } catch (Exception e) {
        System.out.println("error..." + e.getMessage());
    }
}
}
```
