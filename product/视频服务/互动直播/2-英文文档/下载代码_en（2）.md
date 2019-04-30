# Download Code

## Overview
ILVB SDK for IE (referred to as ILiveSDK(IE) below) is an ILVB SDK on IE platform  that allows Interactive Live Video Broadcasting, joint broadcasting and basic IM (instant messaging) through ActiveX.

## Supported browsers
32-bit IE9, 32-bit IE10, IE11

## Download SDK and DEMO
The demo project is an ILVB application developed based on ILiveSDK (IE). The application is called "FreeShow" and can be interconnected with "FreeShow" on other terminals.   
You can [try it online](https://sxb.qcloud.com/webdemo/index.html).   
You can also download ILiveSDK (IE) and its demo at [github](https://github.com/zhaoyang21cn/ILiveSDK_Web_Demos). In addition to ILiveSDK (IE), API document, js API file and API call samples as shown below are also included:
  

File | Description | 
----|------|
/suixinbo | FreeShow demo project. You can open the index.html with IE.| 
iLiveSDK/iLiveSDK.cab | ILVB component. Business layer does not interact directly with this file | 
iLiveSDK/iLiveSDK.js | ILVB API, in which iLiveSDK.cab is wrapped to be called by business layer | 
/doc | Related documents  | 
/tools | Developer tools | 


## How to run the demo
Running the demo allows you to have an intuitive picture of the capabilities of ILiveSDK (IE). To run the demo, follow the steps below:

 1. Modify the appid and accountType in the FreeShow code to those of the developer. Find OnInit method in demo.js, locate `sdk = new ILiveSDK(1400027849, 11656, "iLiveSDKCom")` statement, and then replace the first two parameters with your own `SDKAppID` and` accountType`. For more information on how to obtain the two parameters, please see [Quick Configuration of Parameters]https://cloud.tencent.com/document/product/268/7599).
 2. Deploy the [FreeShow background code](https://github.com/zhaoyang21cn/SuiXinBoPHPServer) to your own server and modify the background key as described in the document.
 3. Open the index.html with IE and allow the usage of activeX control to go to the registration and login page.
 ! [Login Page](http://mc.qcloudimg.com/static/img/cf9dec67f37159dc9fec9d529dcf47f1/image.png)
 4. After login, you can see the list of rooms which are in the live broadcasting ("room" is a ILiveSDK concept and will be discussed in detail later). You can also create your own ILVB. [Room list page](http://mc.qcloudimg.com/static/img/82fcdb2dfad54efd80d3c9ed4b5c5d8a/image.png)
 5. When joining a room, you can see the live video, broadcast messages, current room members and so on. You can enable the camera for a live broadcasting, or send messages to other room members.  [Room](http://mc.qcloudimg.com/static/img/43f1047c1d00f70de63b9a287ff55973/image.png)

## Integrate iLiveSDK (IE) into your own project
Only javastript is required for integrating ILiveSDK (IE). To introduce SDK to your project, follow the steps below:

 1. Place the cab file and iLiveSDK.js anywhere on your PC.
 2. In the html page, add `
<object id="iLiveSDK" classid="CLSID:54E71417-216D-47A2-9224-C991A099C531" codebase="path/iLiveSDK.cab#version=version number"></object>`.
 3. In the html page, add js API file <script type="text/javascript" src="path/iLiveSDK.js"></script>.
 4. Call the APIs in iLiveSDK to implement the business requirements.

## SDK log location
The log is located at: %appdata%\Tencent\iLiveSDK (executed in the **Start** menu)

