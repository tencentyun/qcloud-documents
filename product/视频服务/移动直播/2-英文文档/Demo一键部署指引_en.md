
Tencent Cloud's complete technical documents and source codes help you quickly build an audio and video mini program. As even good source codes and documents take time to learn, for faster debug, we also provide a one-click deployment service for free. You can get a video and audio mini program under your own account only with a few clicks, and a test server with an independent domain name is provided to allow you to quickly build your own test environment within five minutes.

## 1. Log in to Tencent Cloud via WeChat Media Platform Authorization

Open [WeChat Media Platform](https://mp.weixin.qq.com), and register and log in to the mini program by following the steps below:

1. Click "Settings" in the left menu bar.
2. Click "Developer Tools" in the right Tab bar.
3. Click "Tencent Cloud" to go to Tencent Cloud tool page, and click "Activate".
4. Scan the OR code using the WeChat account bound to the mini program to authorize the mini program to Tencent Cloud. After that, the console of Tencent Cloud's WeChat Mini Program appears, and shows that the mini program is activated in the development environment. Now, you can proceed with it.

> **Note:**
>
> It may not show Activated if you check the status of Tencent Cloud using Developer Tools of the Mini Program. The status of Activated is synchronized to the WeChat Developer Tools only after the first deployment in the development environment.

![Go to WeChat Media Platform backend](https://mc.qcloudimg.com/static/img/a3ca2891b23cfce7d3678cd05a4e14fe/13.jpg)

![Activate Tencent Cloud](https://mc.qcloudimg.com/static/img/53e34b52e098ee3a0a02ecc8fbb68a54/14.jpg)

![Console of Tencent Cloud's WeChat Mini Program](https://mc.qcloudimg.com/static/img/032d0b2b99dfcfdf4234db911e93b60f/15.png)

## 2. Activate Categories of Mini Program and Push and Pull Tags [Important]
For policy and compliance considerations, &lt;live-pusher&gt; and &lt;live-player&gt; are not supported by all WeChat mini programs:

- Mini programs of personal and enterprise accounts only support the categories in the following table:

<table>
  <tr align="center">
    <th width="200px">Primary Category</th>
    <th width="700px">Sub-category</th>
  </tr>
  <tr align="center">
    <td>"Social"</td>
		<td>LVB</td>
  </tr>
	<tr align="center">
    <td>"Education"</td>
		<td>Online education</td>
  </tr>
	<tr align="center">
    <td>"Health care"</td>
		<td>Internet hospital and public hospital</td>
  </tr>
	<tr align="center">
    <td>"Government Affairs and Livelihood"</td>
		<td>All secondary categories</td>
  </tr>
	<tr align="center">
    <td>"Finance"</td>
		<td>Funds, trusts, insurance, banking, securities/futures, micro-credit of non-financial institutions, credit investigation, and consumer finance</td>
  </tr>
</table>

- For mini programs meeting requirements of categories, you need to enable the component permissions in "Settings" -> "API Settings" of the mini program management backend, as shown below:

![](https://mc.qcloudimg.com/static/img/a34df5e3e86c9b0fcdfba86f8576e06a/weixinset.png)

Note: If a mini program cannot work properly while the above settings are correct. That may be because the cache within the WeChat is not updated. Delete the mini program, restart WeChat, and try again.

## 3. Activate Tencent Cloud Service
### Activating LVB

#### 1. Apply for Activation of LVB
Enter the [LVB Console](https://console.cloud.tencent.com/live). If the service has not been activated yet, the following page will appear:
![](https://mc.qcloudimg.com/static/img/c40ff3b85b3ad9c0cb03170948d93555/image.png)
Click "Request for Activation", and then go to Tencent Cloud's manual review stage. Upon the approval of Tencent Cloud, the service is activated.


#### 2. Configure LVB Code
After activating the LVB service, enter "LVB Console" -> "LVB Code Access" -> "Access Configuration" (https://console.cloud.tencent.com/live/livecodemanage) to complete relevant configurations, and then activate the LVB Code service:
![](https://mc.qcloudimg.com/static/img/32158e398ab9543b5ac3acf5f04aa86e/image.png)
Click "Confirm Access" button.

#### 3. Obtain LVB Configuration Information
Obtain bizid and pushSecretKey from the LVB console, which will be used by the configuration server later:
![](https://mc.qcloudimg.com/static/img/2e8c581554c8d790e2b0a212d14d0d46/image.png)

### Activating Instant Messaging (IM)
#### 1 Apply for Activation of IM
Go to [IM Console](https://console.cloud.tencent.com/avc). If you have not activated the service yet, just click the **Directly Activate IM** button. For a new verified Tencent Cloud account, the IM App list is empty, as shown below:
![](https://mc.qcloudimg.com/static/img/c033ddba671a514c7b160e1c99a08b55/image.png)

Click the **Create App Access** button to create an App access, that is, the name of the App for which you want to get the access to Tencent Cloud IM service. Our test App is called "RTMPRoom Demo", as shown below:
![](https://mc.qcloudimg.com/static/img/96131ecccb09ef06e50aa0ac591b802d/yuntongxing1.png)

Click the "OK" button, and then you can see in the App list the item you just added, as shown below:
![](https://mc.qcloudimg.com/static/img/168928a60c0b4c07a2ee2c318e0b1a62/yuntongxing2.png)

#### 2 Configure the Standalone Mode
In the list in the above figure, there is an **App Configuration** button. Click it to proceed with configuration, as shown below:
![](https://mc.qcloudimg.com/static/img/3e9cd34ca195036e21cb487014cc2c81/yuntongxing3.png)

#### 3 Obtain IM Configuration Information
Obtain SdkAppid, accountType, privateKey, and administrator from the LVB console, which will be used by the configuration server later:
![](https://mc.qcloudimg.com/static/img/f3e0576d89d044a4ee452f8ba0c231ae/yuntongxing4.png)

Download and decompress the public and private keys from the Verification Method, and open private_key with a text editor, for example:
```bash
-----BEGIN PRIVATE KEY-----
MIGHAgEAsUj5ep7r9TVxTrZiSpXQKhRANCAASuxr7AJGiXRqGpiO7pPrLAchyORc
Y5uWCqVm+QFTn0H+ZcHP93ss3OhgZKh8pq+g7X26dW5fQkiSH1PXG/FY
zbTbMHaWCqVm+QFTn0H+QKhRANCAASuxr7AJGiXRqGpiO7pPr7jTFTmg
-----END PRIVATE KEY-----
```

Convert it to strings as follows, which will be used in the configuration files of the server:

```bash
"-----BEGIN PRIVATE KEY-----\r\n"+
"MIGHAgEAsUj5ep7r9TVxTrZiSpXQKhRANCAASuxr7AJGiXRqGpiO7pPrLAchyORc\r\n"+
"Y5uWCqVm+QFTn0H+ZcHP93ss3OhgZKh8pq+g7X26dW5fQkiSH1PXG/FY\r\n"+
"zbTbMHaWCqVm+QFTn0H+QKhRANCAASuxr7AJGiXRqGpiO7pPr7jTFTmg\r\n"+
"-----END PRIVATE KEY-----\r\n"
```
## 4. Install WeChat Mini Program Development Tools

Download and install the latest version of [WeChat Developer Tools](https://mp.weixin.qq.com/debug/wxadoc/dev/devtools/download.html), and scan the QR code using the WeChat account bound to the mini program to log in to the Developer Tools.

![WeChat Developer Tools](https://mc.qcloudimg.com/static/img/4fd45bb5c74eed92b031fbebf8600bd2/1.png)

## 5. Download Demo 

Access [SDK+Demo](https://cloud.tencent.com/document/product/454/7873#XiaoChengXu), and obtain the mini program demo and backend source codes.

## 6. Upload and Deploy Codes

1. Open WeChat Developer Tools installed in the Step 4, and click the "Mini Program Project" button.
2. Enter the mini program AppID, select the code directory downloaded in the previous step for Project Directory, and then click "OK" to create a mini program project.
3. Click "OK" to enter Developer Tools.

  > **Note:** 
  >
  > For directory, select `RTMPRoom` root directory including `project.config.json` instead of `wxlite` directory only.

  ![Upload Codes](https://mc.qcloudimg.com/static/img/fd7074730e5b37af8a4d86dc8125d120/xiaochengxustart.png)

  ![Developer Tools](https://mc.qcloudimg.com/static/img/f14303d2aa1a0d4609a4d679bf1b761a/image.png)

4. In the `config.js` file under the`server` directory of Demo codes, configure `bizid`, `pushSecretKey`, `APIKey`, `sdkAppID`, `accountType`, `administrator`, `privateKey` to the values generated in the above LVB service and IM service, and then **save** them.

  ![Modify MySQL Password](https://mc.qcloudimg.com/static/img/5a11569b0d8eb50e3ff93ed7f4714bfb/image.png)

5. Click on the "Tencent Cloud" icon on the upper right corner of the interface, and select "Upload Test Code" in the drop-down menu bar.

  ![Upload Button](https://mc.qcloudimg.com/static/img/8480bbc02b097bac0d511c334b731e12/5.png)

6. Select "Module Upload" with all options selected, select "Automatically Install Dependencies after Installation", and then click "OK" to upload codes.

  ![Select Modules](https://mc.qcloudimg.com/static/img/d7ff3775c77a662e9c18807916ab8045/6.png)

  ![Uploaded](https://mc.qcloudimg.com/static/img/a78431b42d0edf0bddae0b85ef00d40f/7.png)

7. After the codes are uploaded, click the "Details" button on the upper right corner, select "Tencent Cloud Status", and then your development environment domain name automatically assigned by Tencent Cloud appears:

  ![View Development Domain Name](https://mc.qcloudimg.com/static/img/f7549e6b1f6f5f9690c910957082f49c/%7B04138BF0-C29C-4A8B-A494-89E072C84B38%7D.png)

8. Fully copy development environment request domain name (including `https://`), open `wxlite/config.js` in the editor, and then enter and save the copied domain name in `url`. After that, the editor automatically compiles the mini program, and the simulator window on the left displays the demo of the client in real time:

  ![Modify the Client Configuration](https://mc.qcloudimg.com/static/img/227e5b6de550496e6841ff0053644e15/image.png)

9. Compile and run in the simulator, and click multi-person audio/video. The log of successful login in the console on the right indicates successful configuration. 

  ![Login Test](https://mc.qcloudimg.com/static/img/536b77d25e5927690bcb93632a528470/image.png)

10. Use a mobile phone to test. Enter by directly scanning the QR code generated by Developer Tools preview. Enable debugging as the backend deployed here is the development test environment:

  ![Enable Debugging](https://mc.qcloudimg.com/static/img/1abfe50750f669ca4e625ec3cdfbd411/xiaochengxutiaoshi.png)
 
   Note: The test environment deployed by the backend server is valid for seven days. If you need more test experience, redeploy the backend.

## FAQs
##### 1. How to troubleshoot runtime errors?
 - Modify the URL in `wxlite/config.js`, use the default official demo backend (https://lvb.qcloud.com), and directly run the mini program.
 - Re-decompress the downloaded demo and directly run the mini program. The official demo backend is used by default.
 - Go back to step 2 to check whether the enabled category of the mini program is correct and whether pull and push tags are enabled in the mini program console.
 - If the official demo backend runs properly, please see this document and redeploy it again.
 - If it still does not work, submit a ticket or contact the customer service by calling 400-9100-100.
  
##### 2. Why can't I see the screen after running the mini program and entering the multi-person audio/video?
  - The mini program is only available on mobile phones. It cannot be run on the simulator of the WeChat Developer Tools.
  - Check whether the information can be found in the mini program basic library version wx.getSystemInfo. Only basic library version 1.7.0 or later supports the audio and video feature.
  - Check the category of the mini program. In compliance with regulatory requirements, not all categories of mini programs are equipped with the audio and video feature. For categories equipped with such feature, please see [DOC](https://cloud.tencent.com/document/product/454/13037).
  - For more requirements or deep cooperation, submit a ticket or contact customer service by calling 400-9100-100.
  
##### 3. What to do if I want to launch or deploy an official environment?
  - Apply for a domain name and obtain the ICP license.
  - Deploy the server code to the requested server.
  - Add the business server domain name and IM domain name to the valid "request" domain names on the mini program console. The IM domain name is https://webim.tim.qq.com.
   

