If you need to build a container image from Git code repository, you must first configure the source code authorization. Currently, Github repository and Gitlab repository authorization are supported.
 
## Steps
1. Log in to the [Tencent CCS Console](https://console.cloud.tencent.com/ccs).
2. Click "Image Registry" on the left navigation bar, and click "My Images" in the drop-down list to go to **My Image Registries** page, and then click "Source Code Authorization".
 ![](//mc.qcloudimg.com/static/img/4019d743e8a653a333b984d68f4ce3f5/image.png)
3. Enter the code source authorization page for selection.
![](https://mc.qcloudimg.com/static/img/47dc0339b4a602a07ba2f92dda6290ff/image.png)

## Github Authorization
If your code repository is located in Github, click "Authorize to sync with Github code source".
After being redirected to Github website, you are prompted that APP needs to access your code repository, personal information and other data. Click "Authorize" to complete authorization for Github code repository.
![](//mc.qcloudimg.com/static/img/80b89840adbfcb9dac1f27b1e5a83e10/image.png)

## Gitlab Authorization
If your code repository is located in a self-built Gitlab server or an official Gitlab hosting server, click "Authorize to sync with Gitlab code source".
You are redirected to the **Gitlab Code Source Authorization** page.
![](https://mc.qcloudimg.com/static/img/68d44d7dd5d621f288e56efdc8bad7f3/image.png)
- **Service address**: Gitlab server address. It must contain http or https protocol and be accessed through public network.
- **User name**: The user name that you have registered on Gitlab. Click "Profile" -> "Name" in the Gitlab page to view your user name.
- **Private Token**: This must be Access Token. If you don't have Access Token, you can create one on Gitlab:
![](//mc.qcloudimg.com/static/img/993e48f457b7e9db35bd8402da6f6291/image.png)

>**Note:**
> A user can authorize both Github and Gitlab accounts at a time, but each of them can only authorize one account. To change Github or Gitlab account, you need to register the original account.
  

