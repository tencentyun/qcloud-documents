## What are images?
Tencent Cloud images provide all the information needed to start CVM instances. After you specify an image, you can start any number of instances from it. You can also start instances from any number of images.

The major roles of images are:

- Batch deployment of software environment 
By creating an image for the CVM instance with its software environment deployed and then using the image in batch-creating CVM instances, you can make these CVMs instances created later have the same software environment as the original one, therefore to achieve batch deployment of software environment. 

- As a backup of CVM operating environment
After an image is created for a CVM instance, you can use the image to recover the CVM instance if its software environment is corrupted and cannot run normal during subsequent use.

## Image types

Tencent Cloud provides the following types of images:

- Common images: All users can use them, covering most of the mainstream operating systems.
- Service market images: All users can use them, which integrate some special applications in addition to the operating system.
- Custom images: Only the creators and shared objects can use them, which are created from existing running instances, or imported externally.
- Shared images: Shared by other users and used only to create instances.

## Image lifecycle

The following figure summarizes the lifecycle of custom images. After you create or import a new custom image, you can use it to start a new instance (you can also start an instance from an existing common image or a service market image). A custom image can be synchronized to the same accounts in another region, and becomes an independent image in that region. You can also share custom images to other users.

![](//mccdn.qcloud.com/static/img/d773034279721f814f9451e17e45c21c/image.png)

## Usage restrictions
Common images: No usage restrictions.

Custom images:
1) Cross-regional synchronization of custom images is free.

2) Each region supports 10 custom images.

3) Each user can only carry out five operations every day (including cloud API operations, counted by region).

4) Image synchronization is available only in Guangzhou, Beijing, Shanghai, Hong Kong, but not in the North American region.

Shared images:
1) Each custom image can be shared up to 50 Tencent Cloud master accounts.

2) Shared images do not support modifying names and description, and can only be used to create CVMs.

3) Sharing images to the same region as the shared account is supported.

Service market images: No usage restrictions.

## Charging standards
Currently, all Tencent Cloud common images are free of charge except that Windows images in overseas regions require some license fees. Service market images are priced by the providers. When you start a CVM instance using an image, the costs consist of two parts: CVM instance costs and image costs. In addition, since your custom images are based on some standard images, they may also incur costs. Specific prices and charge modes will be published on the product page.

## Security 
Tencent Cloud common images are manufactured after rigorous testing by the professional security O&M team of Tencent Cloud. We also provide optional built-in Tencent Cloud security components, so you can use them confidently.

Service market images are manufactured by third-party providers, who have been selected carefully by Tencent Cloud and have signed settlement agreements. Those images have been tested rigorously by the providers and reviewed by Tencent Cloud, to guarantee the security of their contents, so you can also use them. 

Images shared by other users may be subject to security risks because they are not reviewed by Tencent Cloud. Therefore, it is strongly recommended that you do not accept images from unknown sources.
