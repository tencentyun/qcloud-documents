**Q: What is NVIDIA Tesla?**
A: NVIDIA Tesla is a new product line introduced by NVIDIA following the launch of professional acceleration card QUADRO and the entertainment graphics card GeForce series, which is mainly used for scenarios that require high performance computing in a broad range of scientific research. With NVIDIA(r) Tesla(r) GPU accelerator, it can handle the workloads that require super strict HPC in ultra-large data centers faster.

**Q: What is computing acceleration?**
A: Computing acceleration is used to perform floating-point computing and graphic processing with a hardware accelerator or a coprocessor, which is more efficient than using a software running on CPU. Tencent Cloud offers three computing acceleration models: GCC computing (GN2, GN8) for generic computing, and GCC rendering GA2 for graphics-intensive applications.

**Q: What are the advantages of GPU over CPU?**
A: GPU has more arithmetic logic units (ALU) than CPU and supports large-scale multi-threaded parallel computing.

**Q: When should I use GCC instances?**
A: GCC instances are most suitable for highly parallel applications, such as workloads that use thousands of threads. When a great deal of computation is required for graphics processing where each task is relatively small, a group of operations to be performed form a pipeline. The throughput of this pipeline is more important than the latency of a single operation. To build an application that makes full use of this parallelism, you need to master the expertise of GPU devices, and to learn how to program for various graphical APIs (DirectX, OpenGL) or GPU computing programming models (CUDA, OpenCL).

**Q: How is GCC instance billed?**
A: Currently, two billing methods are supported for GCC instances: Prepaid and Postpaid. In prepaid mode which is suitable for mature businesses with stable and long-term device demands, you need to pay the service fee of GCC instances for one or several months in advance. In postpaid mode, fees are calculated per second and settled per hour, and the resources are released whenever you purchase the service. The postpaid mode is applicable to the scenarios where the demand for devices fluctuates dramatically, such as snap-up campaign on an e-commerce site. For more information, please see [Price Overview](https://cloud.tencent.com/doc/product/560/8025).

**Q: Can I upgrade/degrade GCC instance configuration?**
A: GCC instance upgrade and degrade are currently not supported.

**Q: What is local SSD?**
A: Local SSD is a local storage on the physical machine where the CVM resides in. It provides instances with block-level data access capability with a low latency, high random IOPS, and high I/O throughput. Since GCC computing instances are mounted with local SSD, you cannot upgrade hardware (CPU and memory), and can only upgrade bandwidth.

**Q: Can GCC instances access CVMs?**
A: Yes. GCC instances have private IPs and public IPs, so they can communicate with other cloud products such as CVMs.

