The CVM instance described below also refers to dedicated CVM.

The first step in using a CVM instance is CVM instance login. To ensure the security and reliability of the instance, Tencent Cloud provides two encryption login methods: password login and [SSH key pair login](/doc/product/213/6092). A password is the login credentials exclusive to each CVM instance, and the SSH key can be used for multiple CVM instances at the same time.

Anyone with an instance login password can log into the CVM instance remotely through a public network address that is allowed by the security group. Therefore, it is recommended to use a secure password, keep it safe, and modify the instance login password periodically.

Users can specify a password or SSH key as they [Purchase and Start Instance](/doc/product/213/4855). Users can set their own passwords or use the automatically generated ones. The generated initial password will be delivered to the user via [Internal Message](https://console.cloud.tencent.com/message). Users can learn from the following content on how to setup an initial password and how to reset settings in case they forget their passwords, etc.

## Set the Initial Password
1) When you [Purchase and Start Instance](/doc/product/213/4855), you can select the login method in the section where you set CVM name and login method. The default is "Set Password".

2) Enter the CVM password according to password character limitations and confirm the password, then click "Buy Now"; the initial password will be set successfully, and wait for the CVM instance to be successfully assigned.

3) You can also select "Auto Generate Password", and click "Buy Now" to get the CVM instance initial password via [Internal Message](https://console.cloud.tencent.com/message) after the CVM instance is successfully assigned.

While setting a password, note the following character limitations:

- Linux device passwords must be between 8-16 chars, and include at least 2 of the following items (`a-z`, `A-Z`, `0-9` and `[`, `(`, `)`, `\`, `~`, `!`, `@`, `#`, `$`, `%`, `^`, `&`, `\`, `*`, `-`, `+`, `=`, `|`, `{`, `}`, `[`, `]`, `:`, `;`, `'`, `,`, `.`, `?`, `/`, `]`, ` and other special symbols)
- Windows device passwords must be between 12-16 chars, and include at least 3 of the following items (`a-z`, `A-Z`, `0-9` and `[`, `(`, `)`, `\`, `~`, `!`, `@`, `#`, `$`, `%`, `^`, `&`, `\`, `*`, `-`, `+`, `=`, `|`, `{`, `}`, `[`, `]`, `:`, `;`, `'`, `,`, `.`, `?`, `/`, `]`, ` and other special symbols)


## Reset Password
Note: You can only reset the password for the CVM when it is shut down. If the machine is running, please shut down the CVM first.

1) Open [CVM Console](https://console.cloud.tencent.com/cvm/).

2) For a single CVM instance that is shut down, click "More" - "Reset Password" on the operation column to the right side.

3) For a batch of CVM instances, select all the CVMs that need to reset the passwords; then at the top of the list, click "Reset Password" to modify the CVMs' login passwords in batches. For the CVM instance that cannot have its password reset, the reason will be displayed.

4) In the pop-up box of password reset, enter the new password, confirm the password and the verification code, then click "Confirm Reset".

5) Wait for the reset to succeed, and after you receive an internal message about the successful reset, you can use the new password to start and use your CVM right away.
