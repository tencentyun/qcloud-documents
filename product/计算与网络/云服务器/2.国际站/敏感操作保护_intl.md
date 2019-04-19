## Overview
CVM supports sensitive operation protection. Before you perform sensitive operations, you need to enter a credential that can prove your identity. After the authentication is passed, you can perform related operations.

The sensitive operation protection of CVM can effectively protect the security of account resources, including the shutdown, restart, password reset, and termination of CVM.
## Enable Operation Protection
Tencent Cloud provides two ways to protect operations:
1. Provide operation protection by enabling **MFA authentication**.
2. Provide operation protection by enabling **mobile verification code**.

You can enable the operation protection through [Access Management Console](https://console.cloud.tencent.com/cam). For more information on operation instructions, please see [Operation Protection](https://cloud.tencent.com/document/product/378/10740).
## Operation Protection Verification
When you have enabled the operation protection, the system will first perform operation protection verification when you perform sensitive operations:
- If you have enabled **MFA verification** for operation protection, you need to enter the 6-bit dynamic verification code on the MFA device.
- If you have enabled **mobile verification code** for operation protection, you need to enter the mobile verification code.

As shown in the following figure, when you try to shut down an instance, the following verification box pops up, and you need to verify the MFA device:
![](https://main.qcloudimg.com/raw/91be83cce330c750728b5a2b2312c720.png)
#### How do I view the MFA verification code?
1. Turn on the MFA device:
Open the **Tencent Cloud Assistant Mini Program** and select "Tools" to see the bound authenticator.

2. View the dynamic verification code of the corresponding account. The dynamic verification code is updated every 30 seconds.
  ![Dynamic verification code](https://main.qcloudimg.com/raw/477cc15372bef421d3c870630a58a55d.png)

