The first step to use a CVM instance is to log into the CVM instance. To ensure the security of the instance, Tencent provides two encryption login methods: [password login](/doc/product/213/6093) and SSH key pair login.

Tencent Cloud allows public key cryptography to encrypt and decrypt login information for CVM instances on Linux. Public key cryptography uses a public key to encrypt a piece of data, such as a password, and then the recipient can decrypt the data using the private key. Public and private keys are key pairs. Users can securely connect to CVM via a key pair, which is a more secure way than using a regular password.

To log into your CVM instance on Linux using an SSH key, you must first create a key pair, specify the name of the key pair when you start the instance, and then use the private key to connect to the instance. Tencent Cloud will only store the public key, and you need to store the private key yourself. Anyone with your private key can decrypt your login information, so it's important to safely store your private key.

> Note: Login with SSH key is not supported for the CVM instances on Windows.

## Create SSH key
1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm).
2) Click "SSH Key" in the navigation pane.
3) Click "Create Key":
- For "Create New Key Pair" method, input the key name, and click "OK" button.
- For "Use an Existing Public Key" method, in addition to entering the key name, you also need to enter the original public key information, and then click "OK" button.
4) After clicking the "OK" button, a pop-up box will appear, and the user will need to download the private key within 10 minutes.

## Bind/Unbind the Key to/from the Server
1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm).
2) Click "SSH Key" in the navigation pane.
3) Select SSH key and click the "Bind/Unbind CVM" button.
4) Select the region, then select the CVM to be bound or unbound, drag it to the right, and click "OK".
5) The SSH key is issued from the backend, and the result window is displayed upon completion. For example, when the association succeeded or failed.
6) Click the "Details" URL to view the result of the most recent operation.

## Modify SSH Key Name/Description
1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm).
2) Click "SSH Key" in the navigation pane.
3) Select the key you want to modify in the key list and click the "Modify" button above.
Or right-click the name of the key to be modified, and click the "Modify" button.
4) Enter the new name and description in the pop-up box, and click "OK".


## Delete SSH Key

**Note**: If the SSH key is associated with a CVM or a custom image, it cannot be deleted.

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm).
2) Click "SSH Key" in the navigation pane.
3) Select all SSH keys to be deleted, and click "Delete" button. Or right-click the name of the key to be deleted, click "Delete"; and click "OK" in the pop-up window.

## Log into a Linux CVM Using the SSH Key
To log into a Linux CVM using the SSH key, first, you need to bind the SSH key to the CVM.

For details on how to log into a Linux CVM using the SSH key, please see [Log into a Linux CVM](/doc/product/213/5436).

