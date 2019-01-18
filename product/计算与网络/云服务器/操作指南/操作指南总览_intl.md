When using the CVM, you may perform various operations, such as logging in, reinstalling operating system, adjusting configuration and resetting password, etc. This document provides an overview of CVM instance and describes how to work with CVM-related products for your reference.
## Instance
[CVM Instance](https://cloud.tencent.com/document/product/213/495) is also known as Cloud Virtual Machine instance. Tencent Cloud CVM instance supports customizing all resources, including CPU, memory, disk, network, security, etc. It also allows easy adjustment of the resources in case of any change in visits, load and other demands. Common features supported by CVM instance are provided as follows:

### Common operations
- [Create Instance](https://cloud.tencent.com/document/product/213/4855)

- Log in to an instance
 - [Log in to Linux Instance](https://cloud.tencent.com/document/product/213/5436)
 - [Logging in to a Windows Instance](https://cloud.tencent.com/document/product/213/5435)

- [Search for Instance](https://cloud.tencent.com/document/product/213/15519)

- [Restart Instance](https://cloud.tencent.com/document/product/213/4928)

- [Shut Down Instance](https://cloud.tencent.com/document/product/213/4929)

- [Terminate Instance](https://cloud.tencent.com/document/product/213/4930)

- [Reclaim Instance](https://cloud.tencent.com/document/product/213/4931)

### Modifying instance attributes
- [Reset Password](https://cloud.tencent.com/document/product/213/16566)

- Adjust configurations
 - [Adjust Instance Configuration](https://cloud.tencent.com/document/product/213/2178)

 - [Adjust Network Configuration](https://cloud.tencent.com/document/product/213/15517)

 - [Adjust Project Configuration](https://cloud.tencent.com/document/product/213/16514)

- [Modify Instance Name](https://cloud.tencent.com/document/product/213/16562)

- Modify IP
 - [Modify Private IP](https://cloud.tencent.com/document/product/213/16561)

 - [Modify Public IP](https://cloud.tencent.com/document/product/213/16642)

- [Change Subnet of Instance](https://cloud.tencent.com/document/product/213/16565)

- [Change Security Group](https://cloud.tencent.com/document/product/213/16564)

- [Reinstall Operating System](https://cloud.tencent.com/document/product/213/4933)

### Billing
- [Renew Instance](https://cloud.tencent.com/document/product/213/6143)

- [Switch from Postpaid to Prepaid](https://cloud.tencent.com/document/product/213/2762)

## Image
An [Image](https://cloud.tencent.com/document/product/213/4940) provides all information required to launch a CVM instance. In another word, an image is the installation disk of a CVM. Tencent Cloud provides four types of images: public image, service marketplace image, custom image and shared image. Common operations supported by image are described as follows.
### Common operations
- [Create Custom Image](https://cloud.tencent.com/document/product/213/4942)

- [Delete Custom Image](https://cloud.tencent.com/document/product/213/6036)

- [Import Image](https://cloud.tencent.com/document/product/213/4945)

- [Copy Image](https://cloud.tencent.com/document/product/213/4943)

### Sharing image
- [Share Image](https://cloud.tencent.com/document/product/213/4944)

- [Cancel Image Sharing](https://cloud.tencent.com/document/product/213/7148)

## Security Group
[Security Group](https://cloud.tencent.com/document/product/213/12452) is an important means of network security isolation provided by Tencent Cloud. It is a stateful virtual firewall for filtering packets and is used to set the network access controls for a single or multiple CVMs. The following describes common operations supported by security group and how to set the security group in typical scenarios to meet your business needs. Overview of common ports is provided at the end of this section for your reference.

### Common operations
- [Creating a security group](https://cloud.tencent.com/document/product/213/12450#.E5.88.9B.E5.BB.BA.E5.AE.89.E5.85.A8.E7.BB.84)

- [Deleting a security group](https://cloud.tencent.com/document/product/213/12450#.E5.88.A0.E9.99.A4.E5.AE.89.E5.85.A8.E7.BB.84)

- [Cloning a security group](https://cloud.tencent.com/document/product/213/12450#.E5.85.8B.E9.9A.86.E5.AE.89.E5.85.A8.E7.BB.84)

- [Adding rules to security group](https://cloud.tencent.com/document/product/213/12450#.E5.90.91.E5.AE.89.E5.85.A8.E7.BB.84.E4.B8.AD.E6.B7.BB.E5.8A.A0.E8.A7.84.E5.88.99)

- [Configuring a security group to associate with CVM instances](https://cloud.tencent.com/document/product/213/12450#.E9.85.8D.E7.BD.AE-cvm-.E5.AE.9E.E4.BE.8B.E5.85.B3.E8.81.94.E5.AE.89.E5.85.A8.E7.BB.84)

- [Importing/exporting security group rules](https://cloud.tencent.com/document/product/213/12450#.E5.AF.BC.E5.85.A5.E5.AF.BC.E5.87.BA.E5.AE.89.E5.85.A8.E7.BB.84.E8.A7.84.E5.88.99)

### Configuration in typical scenarios
- [Remotely Log in to Linux Instance via SSH](https://cloud.tencent.com/document/product/213/12448)

- [Logging in to a Windows Instance via MSTSC](https://cloud.tencent.com/document/product/213/12448)

- [Ping Public IP of Instance](https://cloud.tencent.com/document/product/213/12448)

- [Use Instance as Web Server](https://cloud.tencent.com/document/product/213/12448)

- [Use Instance as FTP Server](https://cloud.tencent.com/document/product/213/12448)

- [Overview of Common Ports](https://cloud.tencent.com/document/product/213/12451)

## EIP
[Elastic IP Address (EIP)](https://cloud.tencent.com/document/product/213/5733) is also known as elastic IP. It is a static IP designed for dynamic cloud computing, and a fixed public IP in a certain region. With EIPs, you can quickly remap an address to another instance in your account (or NAT gateway instance) to block instance failures. Common operations supported by EIP are provided as follows.
### Common operations
- [Applying for EIPs](https://cloud.tencent.com/document/product/213/16586#.E7.94.B3.E8.AF.B7.E5.BC.B9.E6.80.A7.E5.85.AC.E7.BD.91-ip)

- [Releasing EIPs](https://cloud.tencent.com/document/product/213/16586#.E9.87.8A.E6.94.BE.E5.BC.B9.E6.80.A7.E5.85.AC.E7.BD.91-ip)

- [Binding instances](https://cloud.tencent.com/document/product/213/16586#.E5.BC.B9.E6.80.A7.E5.85.AC.E7.BD.91-ip-.E7.BB.91.E5.AE.9A.E4.BA.91.E4.BA.A7.E5.93.81)

- [Unbinding instances](https://cloud.tencent.com/document/product/213/16586#.E5.BC.B9.E6.80.A7.E5.85.AC.E7.BD.91-ip-.E8.A7.A3.E7.BB.91.E4.BA.91.E4.BA.A7.E5.93.81)

- [Adjusting bandwidth](https://cloud.tencent.com/document/product/213/16586#.E8.B0.83.E6.95.B4.E5.B8.A6.E5.AE.BD)

- [Converting public IPs to EIPs](https://cloud.tencent.com/document/product/213/16586#.E5.85.AC.E7.BD.91ip.E8.BD.AC.E5.BC.B9.E6.80.A7ip)

## SSH Key
### Common operations
- [Creating SSH keys](https://cloud.tencent.com/document/product/213/16691#.E5.88.9B.E5.BB.BA-ssh-.E5.AF.86.E9.92.A5)

- [Deleting SSH keys](https://cloud.tencent.com/document/product/213/16691#.E5.88.A0.E9.99.A4-ssh-.E5.AF.86.E9.92.A5)

- [Binding/unbinding instances](https://cloud.tencent.com/document/product/213/16691#.E5.AF.86.E9.92.A5.E7.BB.91.E5.AE.9A.2F.E8.A7.A3.E7.BB.91.E6.9C.8D.E5.8A.A1.E5.99.A8)

- [Modifying name/description](https://cloud.tencent.com/document/product/213/16691#.E4.BF.AE.E6.94.B9-ssh-.E5.AF.86.E9.92.A5.E5.90.8D.E7.A7.B0.2F.E6.8F.8F.E8.BF.B0)

- [Logging in to a Linux instance using a key](https://cloud.tencent.com/document/product/213/16691#.E4.BD.BF.E7.94.A8-ssh-.E5.AF.86.E9.92.A5.E7.99.BB.E5.BD.95-linux-.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8)

