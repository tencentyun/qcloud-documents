You can select your images type based on the following characteristics:

- Location (see [Regions and Availability Zones](https://cloud.tencent.com/doc/product/213/6091))
- Operating system type
- Architecture (32-bit or 64-bit)

Tencent Clouds provides the following types of images, and you can select images as needed.

## Public Images

Public imagesgive are provided, supported and maintained by Tencent Cloud, including the basic operating system and the initialization components by Tencent Cloud. All users can use them and choose whether they are based on the Linux system or Windows system.

Tencent Cloud public images are manufactured after rigorous testing by the professional security team of Tencent Cloud. We also provide optional built-in Tencent Cloud security components. Tencent Cloud common images support:

- Stable, secure, and high-performance application environment.
- Multiple versions of Java, MySQL, SQL Server, Python, Ruby, Tomcat and other common software, as well as full permissions.
- Regular system updates.
- Integrated with Tencent Cloud software packages (for example APIs.).
- High-compliance operating systems, all official genuine ones.
- Free of charge except that Windows images in some ***overseas*** regions require some license fees.

## Custom Images
Custom images are created or imported by yourself. They can only be used by your account. You can easily create an image for the CVM instance with its applications deployed, and then quickly create more instances that contain the same configuration. Custom images support user creation, synchronization, sharing and termination, are an essential component of the rapid deployment feature of Tencent Cloud. For more information about custom images, see [Create Custom Images](/doc/product/213/4942), [Synchronize Custom Images](/doc/product/213/4943), [Share and Unshare Custom Images](/doc/product/213/4944) and [Import Custom Images](/doc/product/213/4945).

Since your custom images are based on public images, they may also incur costs (when the original public images are the Windows types in some overseas regions) Exact prices are those published when you create instances.

- Each region supports up to 10 custom images.
- Image synchronization is available only in Guangzhou, Beijing, Shanghai and Hong Kong, but not in North American and Singapore.

## Shared Images
Shared images means that other Tencent Cloud users share their custom images with you through the image sharing feature. Shared images will be displayed in the same region as the original images. Shared images do not support modifying names, synchronization, sharing and other operations, and can only be used to create CVMs. 

- Each custom image can be shared to up to 50 Tencent Cloud accounts.
- Shared images do not support modifying names and description, and can only be used to create CVMs.
- Sharing images to the same region as the shared account is supported.


