The CVM instance described below also refers to dedicated CVM.

## What is an Image?

A Tencent Cloud image contains all necessary information required to launch CVM instances. You can launch any number of instances from a specified image, or from any number of different images.

The main functions of images are:

- Deploy Software Environment in Batch
  You can create an image out of a CVM instance with deployed environment, then use the image as the operating system when batch creating CVM instances. These CVM instances will have the same software environment as the original CVM instance after creation, achieving batch deployment of software environment.

- As the Backup of a Server's Operating Environment
  Create an image for a CVM instance. If the instance's software environment becomes broken, you can restore the instance using this image.

## Image Type

Tencent Cloud provides the following types of images:

- Public image: available to all users. They cover most mainstream operating systems;
- Service marketplace image: available to all users. Some applications are integrated into the operating systems;
- Custom image: only available to the creator and users whom the images are shared with. Created from running instances or imported from external sources.
- Shared image: images shared by other users. They can only be used to create instances.

## Image Lifecycle

The following diagram illustrates the lifecycle of custom images. After creating or importing a new custom image, you can use it to launch new instances (you can also launch instances using public images or service marketplace images). Custom images can be copied to other regions under the same account and become independent images in these regions. You can also share custom images with other users.

![](//mccdn.qcloud.com/static/img/d773034279721f814f9451e17e45c21c/image.png)

## Service Limits
Public Image: none.

Custom Image:
1)	Currently, copying custom images across regions is free of charge.

2)	Currently, each region can have a maximum of 10 custom images.

3)	Each user can perform no more than 5 operations per region every day (including cloud API operations).

4)	Image copying is only supported for Guangzhou, Beijing, Shanghai and Hong Kong regions. It's currently not supported for North America region.

Shared Image:
1)	Each custom image can be shared to a maximum of 50 Tencent Cloud master accounts;

2)	A shared image can only be used to create CVMs and its name and description cannot be changed;

3)	The region to which the image is shared should be the same as the image's source region;

Service Marketplace Image: none.

## Billing Method
All public images provided by Tencent Cloud are free, except Windows images in oversea regions (they require a certain amount of license fee). The fees for service marketplace images are determined by their providers. When you purchase CVM instances with an image, the fee you are billed includes the fee for the CVM instances and the fee for the image. Furthermore, using custom images may come with certain fees because they are created based on standard images. Details regarding prices and billing methods are shown on the item page.

## Security
The public images provided by Tencent Cloud are made by our professional security and OPS teams. The images are strictly tested and include optional Tencent Cloud security components, which make them highly trustworthy.

Images in the service market are created by third-party providers. All providers have gone through our strict review and signed our agreement. The images are strictly tested by the providers and reviewed by Tencent Cloud to make sure that the image contents are secure and highly trustworthy.

Images provided by other users are not reviewed by Tencent Cloud thus may contain security risk. Therefore, we strongly recommend against using images from unknown sources.

