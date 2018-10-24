## What is CVM Instance?
**Instance** can be understood as a CVM, which contains the most basic computing components such as CPU, memory, operating system, network, and disk.

CVM instances can provide elastic computing services in the cloud in a secure and reliable way to meet computing requirements. As business demands change, computing resources can be scaled in real time to lower the procurement costs of your software/hardware, and simplify IT OPS work.

Different types of instances provide different computing and storage capacities, and they are applicable to different application scenarios. You can choose the computing capacity, storage, and network access method of the instances based on the service scope as needed. For more instance types and application scenarios, please see [CVM Instance Configuration](/doc/product/213/2177) and [Model Recommendation](https://cloud.tencent.com/act/recommended). After an instance is started, you can use it in the same way as you use any other traditional computer, and you have full control over the started instance.

## Instance Image
**Image** is the template for CVM software configuration (operating system, pre-installed programs, etc.). A Tencent Cloud image provides all information required to launch a CVM instance. Tencent Cloud requires users to start the instance via image. An image can launch multiple instances and you can use the image repeatedly. In another word, an image is an "installation disk" of a CVM.

Tencent Cloud provides the following types of images:

 - Public images: Available to all users. They cover most mainstream operating systems.
 - Service market images: Available to all users. In addition to operating systems, some applications are also integrated into these images.
 - Custom images: Only available to the creator and users with whom these images are shared. They are created from running instances or imported from external sources.
 - Shared images: Shared by other users. They can only be used to create instances.

For more information about images, please see [Image Overview](/doc/product/213/4940) and [Image Type](/doc/product/213/4941).

## Instance Storage
The storage of instances is similar to normal CVMs and is divided into **system disk** and **data disk**:

- System disk: Similar to the C drive in the Windows system. The system disk contains a full copy of the image used to launch an instance, and the running environment for the instance. A larger system disk than the used image is required when starting.
- Data disk: Similar to D and E drives in the Windows system. Data disk is used to save user data, and supports free expansion, mounting and unmounting.

Both system disk and data disk support different types of storage provided by Tencent Cloud. For more information, please see [Storage Overview](/doc/product/213/4952).

## Instance Security

Tencent Cloud provides the following instance security protection methods:

- [Policy Control](/doc/product/378/4513): When multiple accounts are used to control the same set of cloud resources, users can use Policy Control to manage their access to cloud resources.
-  [Security Group](/doc/product/213/5221): Users can use a security group to control access by allowing trusted addresses to access the instance.
- Login control: Log in to your Linux instances by using [SSH Key](/doc/product/213/6092) whenever possible. For the instances that you [Log in with Password](/doc/product/213/6093), the password needs to be changed from time to time.


