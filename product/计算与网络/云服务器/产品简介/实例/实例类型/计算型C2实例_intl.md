

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Computational C2 instance can provide the highest-performance processor and the best cost performance among CVMs. It is an ideal choice for applications subject to compute such as high computing performance and high concurrent read and write, which is suitable for the following situations:

- Batch workloads
- High-traffic Web server, massively multiplayer online (MMO) game server
- High performance computing (HPC) 

and other compute-intensive applications. 

A computational C2 machine features **3.2** GHz Intel E5-2667 Broadwell (v4) processor and DDR4 memory, and offers the options of SSD local and cloud disks for the system and data disks. It supports network boost and up to 300,000 packets per second (PPS). Disk IO and network IO are specially optimized to deliver superior performance.

For the available configurations when you purchase a C2 computational instance, refer to [CVM Instance Configurations](https://cloud.tencent.com/doc/product/213/2177).

## Hardware Specification
The hardware specification for a computational C2 instance is as follows:

- Intel Xeon E5-2667 Broadwell (v4) processor on which C2 instances are based. The processor has a base frequency of **3.2GHz**, and a clock frequency of **3.5GHz**(max turbo frequency) can be achieved with the Intel Turbo Boost Technology.

|Function|Specification|
|---|---|
|Processor No.|E5-2667 v4|
|Intel Smart Cache|25MB|
|Instruction set|64-bit|
|Instruction set expansion|AVX 2.0|
|Processor base frequency|3.2GHz|
|Max turbo frequency|3.5GHz|
|Intel Turbo Boost Technology|2.0|


- CPU performance is **40%** higher than Series 1 Standard S1
- Network Enhanced type is used by default (up to 300k pps)

## Functions of Computational C2 instances
- Data storage of C2 instances can be based on SSD local storage and SSD cloud storage. If a C2 instance is based on SSD local storage, the system and data disks of the C2 instance only exist within the life cycle of the instance. When the instance expires or you terminate it, applications and data on the instace are cleared. It's recommended to backup your data periodically. 
- Support network boost by default. The network boost provides you with significant increase in packets per second (PPS) and decrease in network jittering and latency.


## Requirements for computational C2 instance

- A C2 instance can be used on the basis of  [postpaid](https://cloud.tencent.com/doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9), or as the production instance of computational host HC20 in dedicated hosts;
- Support C2 instance startup in basic network and [Virtual Private Cloud](https://cloud.tencent.com/doc/product/215/535#.E8.85.BE.E8.AE.AF.E4.BA.91.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E6.98.AF.E4.BB.80.E4.B9.88.EF.BC.9F);
- For the available configurations when you purchase a C2 computational instance, refer to [CVM Instance Configurations](https://cloud.tencent.com/doc/product/213/2177).



