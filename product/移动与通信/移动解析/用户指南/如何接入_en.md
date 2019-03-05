>Note:
>For free edition and enterprise edition without using SDK, you need to **use LocalDNS resolution as an alternative** in connection process. For more information, please see [Best Practice](/doc/product/379/最佳实践).

### 1. Activate an Account
First, you need to activate HttpDNS service in the [Console](https://console.cloud.tencent.com/httpdns).
Currently, this service is only available to verified enterprise users.

> Note: Individual developers can access this service via free API. For more information, please see [API Documentation](https://cloud.tencent.com/document/product/379/3524).
Enterprise users can also use free API for testing first.

### 2. Use HttpDNS API to Resolve Domain Name
After the service is activated, authorization ID and Key are sent to your email.

After obtaining authorization ID and Key, you can request for resolution in the format of `http://119.29.29.29/d?dn=[the string to which domain name is encrypted]&id=[authorization ID]&ttl=1`.

For more information about the encryption method, please see [Encryption Guide](https://cloud.tencent.com/document/product/379/3530).

### 3. Client Modification
Modify the resolution method at the client end to HttpDNS resolution. Please note that you need to **use LocalDNS resolution as an alternative** in connection process. For more information, please see [Best Practice](/doc/product/379/最佳实践).

### 4. Apply for SDK (Optional)
Users of enterprise edition can also apply for SDK for connection. Tencent **MSDKDns** can be customized and called by being embedded in App directly. Besides, this proven and stable service is widely applied across various Tencent game clients.

For more information, please see the following documents:
[iOS SDK >>](https://cloud.tencent.com/document/product/379/6469)
[Android SDK >>](https://cloud.tencent.com/document/product/379/6470)

