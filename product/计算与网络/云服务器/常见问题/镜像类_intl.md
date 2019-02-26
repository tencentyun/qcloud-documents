### What is image?

Image is the template for CVM software configuration (operating system, pre-installed programs, etc.). Tencent Cloud requires users to launch the instance via image. An image can launch more than one instance so that users can repeatedly use it. For more information on image, please see [Image Overview](https://cloud.tencent.com/document/product/213/4940).

### What preparations do I need to make before importing an image?

Before importing an image, two major steps need to be completed: applying for permissions and preparing image files. For more information, please see [Import Image](https://cloud.tencent.com/document/product/213/4945).

### What if a Windows system custom image fails to be created?

If a Windows system image fails to be created, perform a check following the steps below.
(1) Check and make sure the following services and all the services coming from the official source of Tencent Cloud and starting with Win_Agent are working properly:

| **Program Name**        | **Installation Location**  | **Service Name**          |
| ----------------- | ------------- | --------------------- |
| QcloudService.exe | C:\Windows\   | Qcloud service            |
| WinAgent.exe      | C:\WinAgent\  | WinAgent Display Name |
| win-agent.exe     | C:\win-agent\ | win-agent             |

(2) The creation of a custom image relies on the Windows Modules Installer provided by Microsoft. Make sure this service is working properly.

(3) Some anti-virus tools or Safedog may block custom image creation scripts. To avoid creation failure, it is recommended that you close these tools before creating a custom image.

(4) If the image creation tool is interrupted by system pop-ups, remotely log in to the CVM, and then check and adjust the CVM settings to avoid pop-ups.

### To how many users can each image be shared at most?

50.

### Can the name and description of a shared image be changed?

No.

### Does a shared image take up my image quota?

No.

### Is there any region limitation on a shared image when creating and reinstalling a CVM?

Yes, there is. The shared image should be in the same region as the source image, and the CVM can only be created and reinstalled in the same region.

### Can a shared image be copied to other regions?

No.

### Can a custom image that has been shared to other users be deleted?

Yes, but you should cancel all the sharing for this custom image first.

### Can an image shared by other users be deleted?

No.

### What are the risks of using custom images shared by other users?

Tencent Cloud does not guarantee the integrity and security of images shared by other users. Please select the images shared by a trusted account.

### Can I share the image another user shared to me to other users?

No.

