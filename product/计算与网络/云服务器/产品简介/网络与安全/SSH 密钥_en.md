The first step is to log into the CVM instance. To ensure the security of the instance, Tencent provides two encryption login modes: [password login](/doc/product/213/6093) and SSH key pair login .

Tencent Cloud allows public key cryptography to encrypt and decrypt logins for Linux instances. Public key cryptography uses a public key to encrypt a piece of data, such as a password, and then the recipient can decrypt the data using the private key. Public and private keys are called key pairs. Users can securely connect to a CVM via a key pair, which is a more secure way to log into a CVM than using a regular password.

To log into your Linux instance using an SSH key, you must first create a key pair, specify the name of the key pair when you start the instance, and then use the private key to connect to the instance. Tencent Cloud will only store the public key; you need to store the private key yourself. Anyone with your private key can decrypt your login information, so it's important to keep your private key in a safe location.

> Note: Windows instances do not support SSH key logins.

## Create SSH Key
1) Open [CVM console](https://console.cloud.tencent.com/cvm/).
2) Click [SSH Key] in the navigation pane.
3) Click [Create Key]:
- For the "Create New Key Pair" method, input the key name, and click [OK].
- For the "Use an Existing Public Key" method, in addition to entering the key name, you also need to enter the original public key information, and finally click the [OK] button.
4) After clicking the [OK] button, a pop-up box will appear, and the user will need to download the private key within 10 minutes.

## Bind/unbind the key to the server
1) Open [CVM console](https://console.cloud.tencent.com/cvm/).
2) Click [SSH Key] in the navigation pane.
3) Select SSH Key and click the [Bind/Unbind Cloud Host] button.
4) Select the region, then select the CVM to be associated/unbound, drag it to the right, and click OK.
5) The SSH key is issued in the background, and the result window is displayed when the configuration is complete. For example, when an association succeeds or fails.
6) Click the [Details] URL to view the results of the most recent operation.

## Modify the SSH key name / description
1) Open [CVM console](https://console.cloud.tencent.com/cvm/).
2) Click [SSH Key] in the navigation pane.
3) Select the key you want to modify in the key list and click the [Modify] button.
Or right-click the name of the key to be modified, and click the [Modify] button.
4) Enter the new name and description in the pop-up box, and click [OK].


## Delete SSH Key

**Note**: If the SSH key is associated with a CVM or a custom mirror, it cannot be deleted.

1) Open [CVM console](https://console.cloud.tencent.com/cvm/).
2) Click [SSH Key] in the navigation pane.
3) Select all SSH keys to be deleted, and click the [Delete] button. Or right-click the name of the key to be deleted, and click [Delete]; then in the pop-up window, click [OK].

## Log into a Linux CVM using the SSH key
To log into a Linux CVM using the SSH key, you first need to bind the SSH key to the CVM.

For details on how to log into a Linux CVM using the SSH key, see [Logging onto a Linux CVM](/doc/product/213/5436).
