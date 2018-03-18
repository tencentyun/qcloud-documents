## How about the accuracy of BSP text recognition?

You need to test and evaluate the text recognition service by yourself. According to our test result, this service can recognize as much as 95% of malicious information.

## Does the text recognition service support custom policies?

No. The text recognition service does not support custom logics and sensitive words. Contact us if the accuracy and coverage of the service cannot meet your requirement. We will adjust them as needed.

## How to connect BSP to the system?

APIs are used to connect BSP to systems. The APIs used by various services for connection can be found in relevant documents at [Tencent Cloud official website](https://cloud.tencent.com/).

## How long does it take to access BSP?

BSP is deployed in Shanghai, Tianjin and Shenzhen to ensure that developers can access it efficiently. You can also access BSP via Tencent Cloud private network, which takes less than 100 ms.

## How does Tencent Cloud excel over its competitors?

1. Tencent Cloud is secured by Tencent's big data from underground industries and intelligent security engine. The big data covers all Tencent businesses and the intelligent security engine is evolved from Tencent's self-developed security system, which is well-tested. 
2. You can access Tencent products by using APIs rather than embedding JS or SDK.
3. Tencent Cloud products are widely used in various industries, including JD, 58.com, Douyu.com, Jumei.com, Qiansqian.com and other customers.

## Social engineering data is updated very fast, so how does Tencent update its blacklist library?

1. Social engineering data is updated based on the big data of Tencent and its partners. It also collects data from underground industries.
2. During ten years' battle against social engineering data, Tencent has built a policy library that can block various underground industry actions.
3. The majority of Internet users are covered because they are open users of QQ and WeChat.

## Can BSP identify a new mobile number that is used for malicious actions?

1. The mobile number can be identified through number location and other data.
2. A large number of accounts are required to make profits by making malicious actions, while a small number of accounts cannot bring any profits. Therefore, in the face of a great many of new mobile numbers, even the preliminary ones cannot be identified, the vast majority of subsequent ones can be blocked.
3. Besides, the most commonly used ID information for a new Internet user is QQ and WeChat. If such information is not recorded in the BSP platform, it is unlikely that it exists in other platforms, which can also help us to identify a mobile number.

## What to do if the server cannot be connected in the development and testing?

Check whether it is blocked by the company's network security policy. If necessary, contact us for help.

## What to do if a message of "Service Permission Not Activated" is returned from the API?

1. Check if the entered SecretId is correct.
2. Check whether the API key is correct. The key to the sub-account is not applicable in BSP. You must use the key to the owner's account.
3. If the message still appears after you use the owner's account, contact us to activate the test permission for the account.

## What to do if a message of "Authentication Failed" is returned from the API?

1. Check the availability of SecretId and SecretKey.
2. Check if the API key is correct;
3. Check if the authentication request URL and the combination parameters are correct.

