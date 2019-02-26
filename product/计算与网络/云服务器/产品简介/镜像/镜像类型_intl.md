You can select an image based on the following attributes:

- Location (please see [Region and Availability zone](/doc/product/213/6091)).
- Operating System
- Architecture ( 32-bit or 64-bit )

Based on different sources, images provided by Tencent Cloud are divided into public images, custom images, shared images, and service market images.

## Public Images

**Public images** are provided, supported and maintained by Tencent Cloud. Each image is composed of a basic operating system and initialization components from Tencent, and is available to all users.

Features:
 - **Operating system:** You are free to choose a Linux-based or Windows-based operating system, and update it regularly.
 - **Software support:** Public images are integrated with software packages (such as APIs) provided by Tencent Cloud, and support multiple versions of common software with full permissions, such as Java, MySQL, SQL Server, Python, Ruby, Tomcat.
 - **Security:** The operating system provided officially is completely legitimate and compliant. The images are made by our professional security and OPS teams. They are strictly tested with optional built-in Tencent Cloud security components.
 - **Limit:** None.
 - **Fees:** All public images are free of charge, except for Windows images in some oversea regions which require a certain amount of license fee.

## Service Marketplace Images
[**Service marketplace images**](http://market.cloud.tencent.com/) are provided by third-party service providers. They are published and made available to all users after having gone through an audit of Tencent Cloud.

Features:
 - **Operating system:** Pre-installed environments including multiple conventional operating systems.
 - **Software support:** Integrated with common software environments, such as PHP, Java, FTP, Nginx, Docker, WordPress, and Discuz.
 - **Security:** All providers have gone through our strict audit and entered into an agreement with us. The images are strictly tested by the providers to ensure the security of image content.
 - **Limit:** None.
 - **Fees:** The prices of images are determined by their providers. Some images are free, and some are fee-based. When you use a fee-based image to launch an instance, both instance and image will incur costs.

## Custom Images
**Custom images** are made by users with image creation feature, or imported via image import feature. They are only available to their creators and sharers.

Features:
 - **Application scenario:** An image created out of an CVM instance with deployed applications can be used to quickly create more instances that contain the same configuration.
 - **Supported features:** You can create, copy, share and terminate images.
 - **Limit:** Each region supports a maximum of 10 custom images.
 - **Fees:** Creation of images may incur a fee. Refer to the prices displayed on the instance creation page for the actual prices. Copying custom images across regions is free of charge.

For more operations and limits, please see [Create Custom Images](/doc/product/213/4942), [Copy Custom Images](/doc/product/213/4943), [Share Custom Images](/doc/product/213/4944), [Cancel Custom Image Sharing](/doc/product/213/7148), and [Import Custom Images](/doc/product/213/4945).

## Shared Images
**Shared images** are custom images shared by other Tencent Cloud users to the current user via the image sharing feature.
These images are displayed in the same region as the original images of the users with whom they are shared.

Features:
 - **Application scenario:** A shared image can be used to quickly create a CVM.
 - **Supported features:** A shared image can only be used to create CVMs. You cannot modify its name, copy it, share it with other users, or perform any operations on it.
 - **Security:** Shared images are not reviewed by Tencent Cloud, and thus may pose security risks. Therefore, we strongly recommend against using images from unknown sources.
 - **Limit:** Each custom image can be shared to a maximum of 50 Tencent Cloud users. An image can only be shared to the accounts in the same region as the source account.

For more operations and limits, please see [Share Custom Images](/doc/product/213/4944) and [Cancel Custom Image Sharing](/doc/product/213/7148).


