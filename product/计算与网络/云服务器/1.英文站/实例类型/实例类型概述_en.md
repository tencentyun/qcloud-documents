
When a Tencent Cloud CVM is created, the ***instance type*** specified by the user determines the host hardware configuration of the instance. Each instance type provides different computing, memory and storage functions. Uses can choose a proper instance type according to the scale of application to be deployed.

Related resources including CPU, memory, storage and network are specifically for this CVM. But resource sharing also happens between instances, such as [network sharing](https://cloud.tencent.com/doc/product/213/509#2.-.E5.85.B1.E4.BA.AB.E7.BD.91.E7.BB.9C).

## Hardware Specification
For more information about hardware specifications of each instance type, please see [CVM Instance Configurations](https://cloud.tencent.com/doc/product/213/2177).

To figure out the instance type that fits you the most, it is recommended that you start a charge-by-quantity instance, and use your own benchmark test application. Since the fee is charged by the actually used quantity, you can try different types of instances conveniently and economically before making the decision.

After purchasing and using a type of instance, you still can adjust the size of the instance when your need changes. For more information, please see [Adjust CVM Hardware Configurations] (/doc/product/213/5730). 

The following is introduction of various instance series and types: Please note that a CVM instance that has been created ***cannot*** be changed into other types. Please create a new instance type when needed.

## Available Instance Types
Based on different underlying hardware, Tencent Cloud offers two series of instances - *Series 1* and *Series 2* (also referred to as *last-generation instance* and *current-generation instance*). They respectively provide the following instance types:

**Current-generation instance types**: [Standard S2](https://cloud.tencent.com/doc/product/213/7154), [High IO I2](https://cloud.tencent.com/doc/product/213/7155), [Memory M2](https://cloud.tencent.com/doc/product/213/7156), [Computational C2](https://cloud.tencent.com/doc/product/213/7157)
**Last-generation instance type**: standard S1, High-I/O I1, memory type M1

To get optimum performance, you are recommended to create an instance using a current-generation instance type.

### Current-generation instances


### Last generation instances
Series 1 features Intel Xeon CPU and DDR3 memory.

## Restrictions on Instances

Currently, Series 2 is only available in South China (Guangzhou) - Guangzhou Zone 1, and East China (Shanghai) - Shanghai Zone 1. Please click [here](http://cloud.tencent.com/event/cvm2.html) to purchase.

The total number of instances started in one zone is limited. For more information about the restrictions, please see [Restrictions on CVM Instance Purchase](https://cloud.tencent.com/doc/product/213/2664)






