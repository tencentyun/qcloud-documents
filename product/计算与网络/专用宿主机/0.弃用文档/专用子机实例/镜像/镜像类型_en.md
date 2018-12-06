The CVM instance described below also refers to dedicated CVM.

Users can choose the images to be used based on following features:

- Location (please see [Region and Availability Zone](https://cloud.tencent.com/doc/product/213/6091))
- Operating system type
- Architecture (32-bit or 64-bit)

Tencent Cloud provides the following images based on different sources. Choose one that is most suitable for your applications.

## Public Images

Public images are provided, supported and maintained by Tencent Cloud. Each image is composed of basic OS and initialization components from Tencent Cloud and is available to all users. You are free to choose either Linux system or Windows system.

The public images provided by Tencent Cloud are created by our internal security and OPS teams, which are strictly tested and equipped with optional Tencent Cloud security components. Tencent Cloud public images support:

- Stable, secure and high-performance application environment.
- Use and full control of multiple versions of common software such as Java, MySQL, SQL Server, Python, Ruby and Tomcat.
- Periodic update of system.
- Integration of software packages (such as API) provided by Tencent Cloud.
- All operating systems are official, legitimate and compliant with laws and regulations.
- All images are free of charge, except some Windows images in ***oversea*** regions which require a certain amount of license fee.

## Service Marketplace Images
[Service Marketplace](http://market.qcloud.com/) images are provided by the third-party service providers. Generally, in addition to the pre-installed environments such as standard operating systems, the service marketplace images also include popular software environments such as PHP, Java, FTP, Nginx, Docker, Wordpress and Discuz. They are published to the service market and made available to all users after being reviewed by Tencent Cloud.

Images in the service market are created by the third-party service providers. All providers have gone through our strict review and signed our agreement. The images are strictly tested by the service providers and reviewed by Tencent Cloud to make sure that the image contents are secure. The fees for service marketplace images are determined by their providers. Some of them are free of charge. When you start CVM instances with a non-free image, the fee you are billed includes the fee for the CVM instances and the fee for the image.

## Custom Images
Custom images are created by users with the image creation feature or imported using the image importing feature. This type of images is only available to the account under which they are created or imported. You can easily create an image CVM instance with deployed application, to quickly create more instances with the same configuration. Custom images could be freely created, copied, shared and terminated, which are an important part of Tencent Cloud's fast deployment feature. For more information about the custom images, please see [Create Custom Images](/doc/product/213/4942), [Copy Custom Images](/doc/product/213/4943), [Share Custom Images and Cancel Image Sharing](/doc/product/213/4944) and [Import Custom Images](/doc/product/213/4945).

Using custom images may come with certain fees because they are created based on the public images (if the original public images are Windows type images in the oversea regions). For more information about the price, please see the prices shown when instances are created.

- Currently, across-region image duplication is free of charge.
- A maximum of 10 custom images are allowed to be created for each region.
- Each user can perform no more than 5 operations on custom images per region every day (including cloud API operations).
- Image duplication feature is only supported in Guangzhou, Beijing, Shanghai and Hong Kong regions. Currently, North America and Singapore regions do not support this feature.

## Shared Images
Shared images are the custom images shared by other Tencent Cloud users to the current user with image sharing feature. The images shared to the user are shown in the same region of the original images of this user. Shared images could only be used to create CVMs. You can't modify their names, copy them or share them.

- Each custom image can be shared to a maximum of 50 Tencent Cloud accounts.
- A shared image can only be used to create CVMs and its name and description cannot be changed.
- The region to which the image is shared must be the same as the image's source region.



