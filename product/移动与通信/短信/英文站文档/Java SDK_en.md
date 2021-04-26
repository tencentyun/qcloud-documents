## Preparations for Development
### Obtaining SDK
Download link for SMS Java SDK in Github: [SMS Java SDK](https://github.com/qcloudsms/qcloudsms_java).

### Preparations for Development
**1. Apply for SDK AppID and App Key:**
Before getting started, you need to obtain SDK AppID and App Key. If you have not done so, log in to the [SMS Console](https://console.cloud.tencent.com/sms) and add a project. After this, you can get an SDK AppID and an App Key.
>**Note:**
> SDK AppID begins with 14xxxxx.

**2. Apply for a signature:**
You must add a signature when sending an SMS message. You can apply for an SMS signature in the [SMS Console](https://console.cloud.tencent.com/sms). For more information, please see [here](https://intl.cloud.tencent.com/document/product/382/18053#create-signatureD).

**3. Apply for a template:**
The content of the SMS message you sent must be approved. You can apply for an SMS template in the [SMS Console](https://console.cloud.tencent.com/sms). For more information, please see [here](https://intl.cloud.tencent.com/document/product/382/18053#create-body-template).

You can proceed with code development after completing the above three steps.

### Configuring SDK
Tencent Cloud SMS can be configured in many ways, three of which are as follows:
- **maven**
 To use Tencent Cloud SMS feature, you need to add the following dependencies in pom.xml: 
```
<dependency>
  	<groupId>com.github.qcloudsms</groupId>
  	<artifactId>sms</artifactId>
  	<version>1.0.2</version>
</dependency>
```

- **sbt**
```
libraryDependencies += "com.github.qcloudsms" % "sms" % "1.0.2"
```

- **Other methods**
**Method 1:** Reference the [source code](https://github.com/qcloudsms/qcloudsms_java/tree/master/src) into the project directly.
**Method 2:** Reference the [JAR package](https://github.com/qcloudsms/qcloudsms_java/tree/master/releases) into the project directly.
>**Note:**
Since the following four dependencies are required in Tencent Cloud SMS:
[Org.json](http://central.maven.org/maven2/org/json/json/20170516/json-20170516.jar), [httpclient](http://central.maven.org/maven2/org/apache/httpcomponents/httpclient/4.5.3/httpclient-4.5.3.jar), [httpcore](http://central.maven.org/maven2/org/apache/httpcomponents/httpcore/4.4.7/httpcore-4.4.7.jar), and [httpmine](http://central.maven.org/maven2/org/apache/httpcomponents/httpmime/4.5.3/httpmime-4.5.3.jar), these four JAR packages need to be imported into the project in both method 1 and 2.


## Getting Started
For any questions about APIs, see [API documentation](/document/product/382/13297).

First, you need to import library:
```
import com.github.qcloudsms.*;
```
You can send SMS messages after Tencent Cloud SMS library is imported.

- **Send individual SMS messages**
```java
 try {
        SmsSingleSender sender = new   SmsSingleSender(appid, "replace with key");
	SmsSingleSenderResult result = sender.send(0, "86", "18326693192", "[Tencent Cloud] Verification code testing 1234", "", "123");
	System.out.print(result);
 } catch (Exception e) {
	e.printStackTrace();
 }
```
> **Note:**
> You can also use this API to send international SMS messages by changing the country code "86" to the code of target country.

- **Send individual SMS messages with specified template ID**
```java
//Assume that the SMS template ID is 123, and the template content is: Test SMS, {1}, {2}, {3}, go to school.
 SmsSingleSender sender = new SmsSingleSender(appid,"replace with key");
 ArrayList<String> params = new ArrayList<String>();
 params.add ("Send single SMS messages with specified template ID");
 params.add ("Shenzhen");
 params.add ("Xiao Ming");
 SmsSingleSenderResult   result = sender.sendWithParam("86", "18326693192", 123, params, "", "", "");
 System.out.println(result);
```
> **Note:**
> You must apply for a template via the console and the template must be reviewed and approved before you can send single SMS messages successfully with or without a specified template ID. Otherwise a failure message is returned.

- **Send bulk SMS message**
```java
// Initialized bulk SMS
SmsMultiSender multiSender = new SmsMultiSender(appid, "replace with key");
// Common bulk SMS
// The following are three fictitious phone numbers
ArrayList<String> phoneNumbers = new ArrayList<String>();
phoneNumbers.add("13101116651");
phoneNumbers.add("13101116652");
phoneNumbers.add("13101116653");
SmsMultiSenderResult multiSenderResult = multiSender.send(0, "86", phoneNumbers, 
	"[Tencent] Test SMS message, common bulk SMS message, Shenzhen, Xiao Ming, go to school", "", "");
System.out.println(multiSenderResult);
```

- **Send bulk messages with specified template ID**
```java
SmsMultiSender multiSender = new SmsMultiSender(appid, "replace with key");
// The following are three fictitious phone numbers
ArrayList<String> phoneNumbers = new ArrayList<String>();
phoneNumbers.add("13101116651");
phoneNumbers.add("13101116652");
phoneNumbers.add("13101116653");
// Assume that the SMS template ID is 123, and the template content is: Test SMS message, {1}, {2}, {3}, go to school.
params = new ArrayList<String>();
params.add ("Send bulk SMS messages with specified template ID");
params.add ("Shenzhen");
params.add ("Xiao Ming");
multiSenderResult = multiSender.sendWithParam("86", phoneNumbers, 123, params, "", "", "");
System.out.println(multiSenderResult);
```
> **Note:**
> A maximum of 200 phone numbers are supported for a request for sending bulk SMS messages. To send messages to more numbers, contact Tencent Cloud SMS technical support (QQ: 3012203387).

- **Send voice verification code**
```java
  // Send voice verification code
  SmsVoiceVerifyCodeSender smsVoiceVerifyCodeSender = new SmsVoiceVerifyCodeSender(appid, "replace with key");
  SmsVoiceVerifyCodeSenderResult smsVoiceVerifyCodeSenderResult = smsVoiceVerifyCodeSender.send("86",
      "1310555552", "123",2,"");
  System.out.println(smsVoiceVerifyCodeSenderResult);
```
>**Note:**
> Only numbers are required when you send verification code. For example, if the message is 123, the voice notification you receive is "Your voice verification code is 1 2 3". To customize content, use voice notification.

- **Send voice notification**
```java
   SmsVoicePromptSender smsVoicePromtSender = new SmsVoicePromptSender(appid, "replace with key");
   SmsVoicePromptSenderResult smsSingleVoiceSenderResult = smsVoicePromtSender.send("86", "13758028086", 2,2,
     "Welcome to XXX. This event xxx", "");
   System.out.println(smsSingleVoiceSenderResult);
```

- **Pull SMS receipt and reply**
```java
   SmsStatusPuller pullstatus = new SmsStatusPuller(appid, "replace with key");
   SmsStatusPullCallbackResult callbackResult = pullstatus.pullCallback(10);
   System.out.println(callbackResult);
   SmsStatusPullReplyResult replyResult = pullstatus.pullReply(10);
   System.out.println(replyResult);
```
> **Note:**
> To apply for SMS message pulling feature, contact Tencent Cloud SMS technical support (QQ: 3012203387). Customers who need to pull a large number of messages can use this feature for batch operation. For other customers, it is not recommended.

- **Send international SMS message**
See "Send Single SMS Messages"



