The first step in using a CVM instance is to login. To ensure the security and reliability of the instance, Tencent provides two encryption login methods: password login and [SSH key pair login](/doc/product/213/6092). A password is the login credentials specific to each CVM instance, and the SSH key can be used for multiple CVM instances at the same time.

Anyone with an instance login password can log into the CVM instance remotely through a public network address that is allowed by the security group. Therefore, it is recommended that you use a more secure password, keep it safe, and modify the login password for your instance periodically.

A user can specify to use a password or SSH key when purchasing [Purchase and Start Instance](/doc/product/213/4855). When using a password, it can be set by itself or automatically generated. When the password is generated automatically, the initial password will be delivered to the user via [Internal Message](https://console.cloud.tencent.com/message). Users can learn from the below content on how to set an initial password and how to reset settings in case you forgot your password, etc.

## Set the initial password
1) [Purchase and Start Instance](/doc/product/213/4855), you can select the login method in the Set Host Name and Login Mode section. The default is [Set Password].

2) In accordance with password character limitations, enter the host password and confirmation, then click Buy Now; the initial password will be set successfully when the CVM instance is successfully assigned.

3) You can also select [Auto Generate Password], and click [Buy Now] to get the CVM instance initial password via [Internal Message](https://console.cloud.tencent.com/message) after the CVM instance is successfully assigned.

It is important to note that the character limitations for setting a password is as follows:

- Linux device passwords must be between 8-16 chars, and include 2 of the following items (`a-z`、`A-Z`、`0-9`and`[`、`(`、`)`、`\`、`~`、`!`、`@`、`#`、`$`、`%`、`^`、`&`、`\`、`*`、`-`、`+`、`=`、`|`、`{`、`}`、`[`、`]`、`:`、`;`、`'`、`,`、`.`、`?`、`/`、`]`and ` or other special symbols)
- Windows device passwords must be between 12-16 chars, and include 3 of the following items (`a-z`、`A-Z`、`0-9`and`[`、`(`、`)`、`\`、`~`、`!`、`@`、`#`、`$`、`%`、`^`、`&`、`\`、`*`、`-`、`+`、`=`、`|`、`{`、`}`、`[`、`]`、`:`、`;`、`'`、`,`、`.`、`?`、`/`、`]`and ` or other special symbols)


## Reset password
> Note: You can reset the password for the cloud host only when it is powered off. If the machine is running, please shut down the host first.

1) Open [CVM console](https://console.cloud.tencent.com/cvm/).

2) For a single CVM instance that is shut down, in the right-hand action bar, click [More] - [Reset Password].

3) For batch CVM instances, select all the hosts that need a password reset; then at the top of the list, click [Reset Password] to modify the host login password in batches. A CVM instance that cannot have its password reset will display the reason why.

4) In the Reset password pop-up box, enter the new password, confirm the password and the verification code, then click [Confirm Reset].

5) Wait for the reset to succeed, and you will receive a successful reset message in your station inbox; now you can use the new password to start and use your CVM.