To ensure the security and reliability of the instance, Tencent Cloud provides two encrypted login methods: [Password Login](/doc/product/213/6093) and SSH key pair login. This document describes common operations of SSH key pairs.


## Creating an SSH key
 1. Log in to [Cloud Server Console](https://console.cloud.tencent.com/cvm/).
 2. Click **SSH Key** in the left navigation pane.
 3. Click **Create Key**
  - If the creation method is **Create a new key pair**, enter the key name and click **OK**;
  - If the creation method is **Use existing public key**, enter the key name and enter the original public key information, and then click **OK**.
 4. In the pop-up window, click **Download** (please download the private key within 10 minutes).

## Binding/Unbinding Keys with Servers
 1. Log in to [Cloud Server Console](https://console.cloud.tencent.com/cvm/).
 2. Click **SSH Key** in the left navigation pane.
 3. Select the SSH key and click **Bind/Unbind CVM** (or right-click on the key name to be modified and click **Bind/Unbind CVM**).
 4. Select the region, select the server to be bound/unbound (uncheck the server selected on the right side to unbind), and click **OK**.
 5. The system delivers the SSH key automatically. And you will get notice about whether the operation is successful or failed.

## Modify SSH Key Name/Description
 1. Log in to [Cloud Server Console](https://console.cloud.tencent.com/cvm/).
2. Click **SSH Key** in the left navigation pane.
 3. Select the key to be modified in the key list, and click **Modify** (or right-click on the key name to be modified and click **Modify**).
 4. Enter a new name and description click **OK**.

## Deleting SSH keys
>**Note**:
> If the SSH key is associated with a CVM or an associated custom image, it cannot be deleted.

 1. Log in to [Cloud Server Console](https://console.cloud.tencent.com/cvm/).
 2. Click **SSH Key** in the left navigation pane.
 3. Select all the SSH keys you want to delete and click the **Delete** button (or right-click on the key name you want to delete, click **Delete**, and click **OK** in the pop-up window).

## Log in to the Linux CVM using the SSH key
Before you log in to the Linux CVM using an SSH key, you need to create an SSH key and bind the SSH key to the CVM.

For details, please refer to [Logging In to Linux CVM](/doc/product/213/5436).

