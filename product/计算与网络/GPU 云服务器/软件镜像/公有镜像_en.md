## What is an Image?
A Tencent Cloud image contains all necessary information required to launch CVM instances. You can launch any number of instances from a specified image, or from any number of different images.
## Functions of Images
- **Deploy a specific software environment**
By quickly building a specific software environment using shared images, custom images and service marketplace images, you can be freed from complex and time-consuming tasks, such as manual environment configuration and software installation. These images can satisfy your requirements for website building, application development, visualized management and other features, to allow GCC instances to be ready to use, thus saving time and effort.
- **Deploy software environment in batch**
You can create an image out of an instance with deployed environment, then use the image as the operating system when creating instances in batches. These instances have the same software environment as the original instance after creation, achieving batch deployment of software environment.
- **Back up of server running environment**
Create an image for an instance. If the instance's software environment becomes broken, you can restore the instance using this image.

For more information on images, please see [Overview of CVM Images](/doc/product/213/4940).
## Image Type
Tencent Cloud provides the following types of images:
- Public Image
- Custom Image
- Shared Image
- Service Marketplace Image

### Public Image
Public images are provided, supported and maintained by Tencent Cloud. Each image is composed of a basic operating system and initialization components from Tencent and is available to all users. Public images have the following features:
- **Operating system at your option**: You are free to choose an operating system (such as, Linux-based or Windows-based operating system), and can update it regularly.
- **Secure environment**: Public images are integrated with software packages (such as API) provided by Tencent Cloud, and support multiple versions of common software with full permissions, such as Java, MySQL, SQL Server, Python, Ruby, Tomcat.
- **Low cost**: All public images are free of charge, except Windows images in some oversea regions which require a certain amount of license fee.

### Custom Image
Custom images are made by users with image creation feature, or imported via image import feature. They are only available to their creators and sharers. Custom images have the following features:
- **Quick copy**: Using an image out of an instance with deployed applications, you can quickly create more instances that contain the same configuration.
- **Free management**: You can create, copy, share and terminate images.
- **Limited number**: A maximum of 10 custom images are allowed to be created for each region.
- **Fee inheritance**: Some custom images that are Windows images in oversea regions come with certain fees. Refer to the prices displayed on the instance creation page for the actual prices. Currently, copying custom images across regions is free of charge.

For more information on custom images, please see [Create Custom Image](/doc/product/213/4942), [Copy Custom Image](/doc/product/213/4943), [Share Custom Image](/doc/product/213/4944), [Cancel Custom Image Sharing](/doc/product/213/7148), [Delete Custom Image](/doc/product/213/6036), and [Import Custom Image](/doc/product/213/4945).
### Shared Image
Shared images are custom images shared by other Tencent cloud users to the current users via the image sharing feature, and are displayed in the same region as the original images of the users with whom these images are shared. Shared images have the following features:
- **Quick deployment**: You can help another user quickly create a CVM using a shared image.
- **Limited number**: Each custom image can be shared to a maximum of 50 Tencent Cloud users.
- **Operation limits**:A shared image can only be used to create CVMs. You cannot modify its name, copy it, share it with other users, or perform any operations on it. The region to which the image is shared should be the same as the image's source region.
> **Note**:
> Shared images are not reviewed by Tencent Cloud, thus may contain security risk. Therefore, we strongly recommend against using images from unknown sources.

Learn more information about the operation methods and limits of shared image, please see [Share Custom Image](https://cloud.tencent.com/doc/product/213/4944) and [Cancel Custom Image Sharing](https://cloud.tencent.com/doc/product/213/7148).
### Service Marketplace Image
 [Service marketplace images](http://market.qcloud.com/) are provided by third-party service providers. They are published and made available to all users after being reviewed by Tencent Cloud. Service marketplace images have the following features:
- **Multiple operating systems are supported**: Service marketplace images support many pre-installation environments such as regular operating systems.
- **Integrated with multiple software environments**: Service marketplace images are integrated with many popular software environments, such as PHP, Java, FTP, Nginx, Docker, WordPress, and Discuz.
- **Secure contents**: All providers have gone through our strict review and signed our agreement. The images are strictly tested by the providers to make sure that the image contents are secure.
The fees for service marketplace images are determined by their providers (some of them are free, some cost money). When you purchase a fee-based image to launch an instance, the charge includes the fee for the CVM instances and the fee for the image.




