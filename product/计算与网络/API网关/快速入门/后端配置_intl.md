## Integrating Serverless Cloud Function 
If you do not enable the response integration (current usage mode) for requests from API Gateway to SCF, the request information will be assembled with a fixed structure when API Gateway sends the request to SCF. SCF receives this fixed structure. The returned result will be passed through without any processing.

Configuration instructions:
1. When you integrate an SCF with the backend, configure the functions you created on the SCF.

2. Configure the timeout, and click **Finish**.
![SCF](//mc.qcloudimg.com/static/img/23145ace7ad407d718c62ff54d381f04/image.png)

If you enable the response for requests from API Gateway to SCF, API Gateway will assemble the request with a fixed structure when sending it to the SCF, and the SCF also returns a fixed structure. Then API Gateway maps the result returned by the SCF to such locations as statusCode, header and body before returning the result to the client.
![](https://main.qcloudimg.com/raw/dc157e3bc40ffd6c7daff5f62766b1ab.png)

In this case, you must return data in the following format to API Gateway for parsing:
```
{ "isBase64Encoded": true|false,
    "statusCode": httpStatusCode,
    "headers": { "headerName": "headerValue", ... },
    "body": "..."
}
```
The structure format of requests from API Gateway to SCF is as follows:
```
{
  
  "requestContext": {
    "serviceId": "123456",
    "path": "/{proxy+}",
    "method": "POST",
    "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
    "identity": {
      "secretId": "abdcdxxxxxxxsdfs",
      "sourceIp": "10.0.2.14"
    },
    "sourceIp": "10.0.2.14",
    "stage": "prod"
  },
  
  "headers": {
    "Accept-Language": "en-US,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
    "User-Agent": "Custom User Agent String"
  },
  "body": "{\"test\":\"body\"}",

  "pathParameters": {
    "proxy": "path/to/resource"
  },
  "queryStringParameters": {
    "foo": "bar"
  },
  "headerParameters":{
    "Refer": "10.0.2.14"
  },
  
  "stageVariables": {
    "baz": "qux"
  },
  
  "path": "/path/to/call"
  "method": "POST",
}
```




## Integrating HTTP 
If your business is deployed in another Cloud or in your local server and is open with HTTP, select the HTTP integration for the backend.
Configuration instructions:
1. To integrate HTTP, you must select HTTP or HTTPS for Backend Type.

2. Enter the backend address, which starts with `http://` or `https://` and does not include the path behind, such as `http://api.myservice.com` or `http://108.160.162.30`.

3. Enter the backend path starting with /, such as `/path` or `/path/{petid}`.

4. Select the request method. The request methods for the frontend and the backend can be different.

5. Set the backend timeout.

6. Set the backend parameters that map the frontend.

7. Click **Finish**.
![Backend configuration](https://i.imgur.com/pQfgDqp.png)

#### API Gateway backend integrates CLB resources in a VPC

When you want to integrate the backend with CLB in a VPC, the frontend configuration is the same as other API configuration methods, and the backend configuration method is as follows:

1. In the backend configuration, select the VPC to be integrated.
![](https://main.qcloudimg.com/raw/15e6d1daba72708d28747fa38ad1dcfd.png)

2. Select CLB in the VPC. API Gateway only supports integrating CLB in a VPC. Other cloud resources in the VPC will be supported soon.
![](https://main.qcloudimg.com/raw/0be3289e9aa42e8cef8bf0062a1a00bf.png)

3. Enter `http://vip+port` or `https://vip+port` at the backend address. The requests we send to CLB will be HTTP requests or HTTPS requests depending on the content you entered. The VIP is that of CLB, which can be found in the basic information of application-based private network CLB.
![](https://main.qcloudimg.com/raw/dda0cba1faf5a0276c9dab5dff1e75f5.png)

4. Select a listening type.

	**If you select the CLB listening type of HTTP/HTTPS**, you must configure the backend path as the path configured in the CLB listener.

	The following figure shows the domain name and path configured in the CLB listener:
![](https://main.qcloudimg.com/raw/0343ecb570624f0c71f11e3ca0805a63.png)

	The following shows the backend path in API Gateway, which must be consistent with that in CLB.
![](https://main.qcloudimg.com/raw/4637b8ae237e84dc3632ee1a5abf36f4.png)

	You also need to configure the parameter host as the constant parameter and place it in the header. The parameter value is the domain name configured in the CLB listener.
![](https://main.qcloudimg.com/raw/d1d6bb3a99344099385dc8b19ee23386.png)

	**If you select the CLB listening type of TCP/UDP**, you must configure the backend path as the path required by the business in the CVM mounted on the CLB.

	If you configure the host verification in the CVM, you need to configure the parameter host as the constant parameter, and select the address to place parameter according to your own business, just like using a layer-7 listener.

	The subsequent configurations are the same as other API configurations.
>**Note:**
>When the backend integrates CLB, security groups on the CVM mounted to the backend should be open to the IP address ranges of 100.64.0.0/10 and 9.0.0.0/8.

## Integrating Mock 
Mock will return a response with fixed configurations for an API request. Mock is generally used for development test. It can complete the API configuration in advance and return responses when the backend service is not completely developed. When integrating MOCK, you only need to configure the returned data, and click **Finish**.
![mock](//mc.qcloudimg.com/static/img/59d198b75bc21d7af480656cf6ebcc62/image.png)

