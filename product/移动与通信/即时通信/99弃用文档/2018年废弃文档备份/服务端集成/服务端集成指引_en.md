## 1. Overview

[REST APIs](/doc/product/269/REST%20API简介) provided by IM are used to manage the App data. For more information on the REST APIs provided by IM, please see [REST API List](/doc/product/269/REST%20API接口列表).

This document describes how to manage data via REST API, and you will learn:

1. What to do before calling REST API.
2. How to debug REST API using:
	2.1 IM REST API debugging tools;
	2.2 Postman;
	2.3 PHP Server SDK tools.
3. How to call REST API on the server, including
	3.1 Integrating PHP Server SDK in PHP.

## 2. What is REST API?

REST API provided by Tencent Cloud is HTTP management API that serves as an entry for managing the App backend. For more information, please see [REST API Overview](/doc/product/269/REST%20API简介).

## 3. Preconditions

To call REST API, you must
1. Create an App in IM. For more information, please see [App Access Guide](/doc/product/269/App%20Access%20Guide).
2. Specify an admin account for your App. For more information, please see [Set admin account for App](/doc/product/269/%E8%AE%BE%E7%BD%AEApp%E7%AE%A1%E7%90%86%E5%91%98).

>**Note: The App admin account is required for calling REST API. Otherwise, errors may occur.**

## 4. Calling Method

For more information on the request URL, request method and packet format for REST API, please see [REST API Overview](/doc/product/269/REST%20API简介). For more information on available REST APIs, please see [REST API List](/doc/product/269/REST%20API接口列表).

The document describes how to call REST API by using:
1. IM REST API debugging tools;
2. Postman;
3. REST API debugging tools from PHP Server SDK.

The section of "Example" uses specific cases to introduce the various methods for calling REST API.

## 5. Example

This document uses a complete example to demonstrate various calling methods, as shown in the following procedure:
1. Import the account to IM (using IM REST API debugging tools).
2. Set basic information for the imported account (using Postman).
3. Create a group including initial group members (using the tools in PHP Server SDK).

### 5.1 Preparation: Obtain the Signature of the App Admin Account

Ensure the existence of the App admin account. Go to the App console and click "App Configuration":
![](//avc.qcloud.com/wiki2.0/im/imgs/20151118091132_40174.png)
After that, check "Account System Integration" to ensure the App admin account is used in the follow-up process (assume the App admin account is "myadmin"):
![](//avc.qcloud.com/wiki2.0/im/imgs/20151118091144_80129.png)
Generate usersig for the App admin account:
1. To generate usersig on Linux, please see [Generate and Verify sig on Linux](/doc/product/269/TLS%E5%90%8E%E5%8F%B0API%E4%BD%BF%E7%94%A8%E6%89%8B%E5%86%8C#2-linux.E5.B9.B3.E5.8F.B0).
2. To generate usersig on Windows, please see [Generate and Verify sig on Windows](/doc/product/269/TLS%E5%90%8E%E5%8F%B0API%E4%BD%BF%E7%94%A8%E6%89%8B%E5%86%8C#3-windows.E5.B9.B3.E5.8F.B0).


For example, the generation command on Windows is:
```
.\tls_licence_tools.exe gen .\keys\private_key sig 3600 1400000478 myadmin
```
After the generation of usersig, you can call REST API.

### 5.2 Import the Account to IM (using IM REST API debugging tools)

This section describes how to use [IM REST API debugging tools](https://avc.cloud.tencent.com/im/APITester/APITester.html#v4/im_open_login_svc/account_import) to import an account with a user name of lilei.

(The account of lilei needs to be imported to IM because it does not exist in IM but needs to be set with information and created with a group in the follow-up process.)

On the [IM REST API Debugging Tools](https://avc.cloud.tencent.com/im/APITester/APITester.html), enter the calling parameters as follows:
![](//avc.qcloud.com/wiki2.0/im/imgs/20151210075829_46289.jpg)
Click "Submit" to view the response packet, as shown below:
![](//avc.qcloud.com/wiki2.0/im/imgs/20151124085151_48669.png)
Now, the account of lilei is imported to IM.

### 5.3 Set basic information for the imported account (using Postman)

This section describes how to use [Postman](https://www.getpostman.com/) to call the API v4/profile/portrait_set to set the basic information for the account imported in the previous section. To put it specifically, set the user lilei' name to "Li Lei".

**Install Postman**

>Note: You need to visit Google App store before installing Postman. If you cannot visit Google websites on your network, we recommend that you use IM REST API debugging tools.

Postman is a powerful Chrome extension for debugging web pages and sending HTTP requests. To install it, open the Chrome browser, search Postman in the Chrome App store, and then "Add to Chrome", as shown below:

After the installation, Postman displays in Chrome Apps, as shown below:

![](//avc.qcloud.com/wiki2.0/im/imgs/20151118091341_82635.png)

**Set user basic information**

Open Postman and enter the parameters as follows:

1. Request method: POST.
2. Request URL: ```https://console.tim.qq.com/v4/profile/portrait_set```.
3. Click "Params" on the right side of the address bar, and enter the request parameters in the following parameter list. For the meaning of the parameters, please see Descriptions of REST API Parameters.
4. Click Body.
5. Click raw to enter the text request packet (in JASON format).
6. Enter the request packet.

As shown in the figure below:

![](//avc.qcloud.com/wiki2.0/im/imgs/20151210080319_84233.jpg)

After all the request parameters are entered, click "Send" on the upper right corner to send the request, and you will receive the following response (Note: Select JSON in the red box):

![](//avc.qcloud.com/wiki2.0/im/imgs/20151118091506_85927.png)

Now, you can call REST API to set user information via Postman.

### 5.4 Create a group including initial group members (using the tools in PHP Server SDK)
This section describes how to use [PHP Server SDK](/doc/product/269/PHP%20Server%20SDK) to call the API v4/group_open_http_svc/create_group to create a group. To put it specifically, create a group called "MyFirstGrouplilei" and set the group owner to "lilei".

[PHP Server SDK](/doc/product/269/PHP%20Server%20SDK) is an integrated REST API SDK provided by IM for PHP backend service. Common REST APIs are wrapped into PHP functions by this SDK. To download and integrate PHP Server SDK, please see [PHP Server SDK](/doc/product/269/PHP%20Server%20SDK).

After downloading and deploying the PHP Server SDK, you need to modify the request paramters of REST API in TimRestApiConfig.json:

![](//avc.qcloud.com/wiki2.0/im/imgs/20151123113238_10213.jpg)

Private_pem_path is the path to the App private key files.

Use the following command to create a group:

```
php TimRestApiGear.php group_open_http_svc create_group Public MyFirstGroup lilei
```

The output is as follows:

![](http://avc.qcloud.com/wiki2.0/im/imgs/20151210080556_60961.png)

The group is created and you can view the group on the "Group Management" page from the App console:

![](//avc.qcloud.com/wiki2.0/im/imgs/20151118095659_40610.png)

## 6. Call REST API in the Backend Service
Calling REST API in the backend service is essentially to initiate HTTPS POST requests. Server SDK provided by IM is used to wrap the calling of REST API. Developers can integrate it to your server codes.

1. [PHP Server SDK](/doc/product/269/PHP%20Server%20SDK);
1. [Node.js Server SDK](/doc/product/269/4287#1-.E5.8A.9F.E8.83.BD.E8.AF.B4.E6.98.8E);
1. Java Server SDK (coming soon).
1. Golang Server SDK (coming soon).

