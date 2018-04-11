## What is CVM Instance?
**Cloud Virtual Machine (CVM)** provides elastic computing services in a secure and reliable way. Services are provided on the cloud to meet the requirements for computing. As business demands change, computing resources can be scaled in real time to lower the procurement costs of your software/hardware, and simplify IT OPS work.


Different types of instances provide different computing and storage capacities, and they are applicable to different application scenarios. You can choose the computing capacity, storage and network access method of the instances based on the service scope as needed. For more instances and application scenarios, please see [CVM Instance configuration](https://intl.cloud.tencent.com/document/product/213/2177). After an instance is started, you can use it in the same way as you use any other traditional computer, and you have full control over the started instance.


## What is Image?
**Image** is the template for CVM software configuration (operating system, pre-installed programs, etc.). A Tencent Cloud image provides all necessary information required to launch a CVM instance and you must start the instance via image. An image can launch more than one instance so that you can use it repeatedly. Generally speaking, an image is the "disk for installation" of a CVM.

Tencent Cloud provides the following types of images:

 - Public images: Available to all users. They cover most mainstream operating systems.
 - Service market images: Available to all users. Addition to operating systems, some applications are also integrated into these images.
 - Custom images: Only available to the creator and users with whom these images are shared. They are created from running instances or imported from external sources.
 - Shared images: Shared by other users. They can only be used to create instances.


For more information about images, please see [Image Overview](https://intl.cloud.tencent.com/document/product/213/4940) and [Image Type](https://intl.cloud.tencent.com/document/product/213/4941).


## Instance Storage
The storage of instance is similar to normal computers and is divided into **system disk** and **data disk**:
- System disk: Like C disk in Windows system, the system disk contains a full copy of image used to start instances and the operating environment for instances. A lager system disk than the used image is required when starting.
- Data disk: Like D/E disk in Windows system, the data disk is used to save user data, and supports free expansion, mounting and unmounting.


Both system disk and data disk support different types of storage provided by Tencent Cloud. For more information, please see [Storage Overview](https://intl.cloud.tencent.com/document/product/213/4952).

## Instance Security

- [Policy Control](https://intl.cloud.tencent.com/document/product/378/4513): When multiple accounts are used to control the same set of cloud resources, users can use Policy Control to manage their access to cloud resources.
-  [Security Group](https://intl.cloud.tencent.com/document/product/213/5221): Users can use Security Group to control access by allowing trusted addresses to access instance.
- Login control: Log in to your Linux instances by using [SSH Key](https://intl.cloud.tencent.com/document/product/213/6092) whenever possible. For the instances that you [Log in with Password](https://intl.cloud.tencent.com/document/product/213/6093), the password needs to be changed from time to time.



