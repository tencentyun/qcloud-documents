## Computing Capacity

**GCC instance uses hardware accelerator to implement some features, such as floating-point computing and graphic processing, which can run software more effective than CCC instances.**

GCC instance uses high-performance NVIDIA Tesla M40 and is applicable to generic GPU computing applications with CUDA and OpenCL programming models. GCC instance offers powerful single/double-precision floating point feature. Each GPU has up to 3,072 parallel processing kernels and 24 GB GDDR5 memory, which is especially suitable for scenarios where server GPU computing workload is required, such as deep learning, graphic database, high-performance database, computational fluid dynamics, computational finance, earthquake analysis, molecular modeling, genomics, rendering and so on.

Peak computing capacity for a single GCC instance is 14T Flops for single-precision floating point arithmetic and 0.4T Flops for double-precision floating point arithmetic. In scenario of scientific computing, its performance grew 50-fold compared to traditional architecture.

In addition, GCC instance comes with the latest generation Intel Xeon E5 v4 CPU, ensuring extra high-performance computing capability, and features local SSD storage whose IO performance is more than tens of times higher than that of local HDD.
[Learn more about local SSD disk>>](https://cloud.tencent.com/doc/product/213/5798)

## Model Configurations
The following configurations are provided:

| GPU (Tesla M40) | vCPU (Xeon E5 v4) | Memory (DDR4) | GPU Memory (GDDR5) | Performance |
|---------|---------|---------|---------|---------|
| 1 | 28 cores | 60 GB | 24 GB | Peak computing capacity for single machine: 7T Flops for single-precision floating point arithmetic and 0.2T Flops for double-precision floating point arithmetic. |
| 2 | 56 cores | 120GB | 48GB | Peak computing capacity for single machine: 14T Flops for single-precision floating point arithmetic and 0.4T Flops for double-precision floating point arithmetic. |

Multiple operating systems, such as CentOS, Ubuntu, Windows, are supported for GCC instances to satisfy the requirements of different industries for professional software and modeling.

## Storage

GCC instance features local SSD storage whose IO performance is more than tens of times higher than that of local HDD. [Learn more about local SSD disk>>](https://cloud.tencent.com/doc/product/213/5798#ssd-.E6.9C.AC.E5.9C.B0.E7.9B.98)

You can mount/unmount your SSD cloud storage freely. SSD cloud storage provides professional 3-copy storage policy to eliminate single point of failure and ensure reliability of data, so as to meet the need for sharing, migration and long-term storage of data in different virtual machines.
[Learn more about local SSD disk>>](https://cloud.tencent.com/doc/product/213/5798#ssd-.E6.9C.AC.E5.9C.B0.E7.9B.98)

## Network and Security

GCC instance resides in an environment all with **10 gigabit** networks, and provides a private network environment with low latency, offering outstanding computing capacity for your business.

Designed for ease of use, it is purchased and managed in the same way as with CVM, including private and public IP assignment, security group, subnet management, etc.

It can be interfaced with [CVM](https://cloud.tencent.com/product/cvm.html), [VPC](https://cloud.tencent.com/product/vpc.html?idx=1), [CLB](https://cloud.tencent.com/product/clb.html?idx=1) and other businesses, without additional management and OPS costs. Private network traffic is free of charge.

Well-established [Security Group](https://cloud.tencent.com/doc/product/213/5221) and [Network ACL](https://cloud.tencent.com/doc/product/215/5132) settings allow you to control and securely filter the inbound and outbound network traffic to or from instances and subnets.

It can seamlessly connect to Cloud Security, and has basic protection and high defense services of Cloud Security equivalent to that of CVM. 
[Learn more about network and security>>](https://cloud.tencent.com/doc/product/213/5220)



