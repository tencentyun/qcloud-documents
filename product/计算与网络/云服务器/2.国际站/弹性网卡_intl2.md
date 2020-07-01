### What is ENI?

[Elastic Network Interface](https://cloud.tencent.com/product/eni) (ENI) is an elastic network interface bound to CVMs in a VPC, which can be migrated freely among multiple CVMs. It is very useful for configuring management networks and establishing highly reliable network solutions.

ENIs are VPC, availability zone and subnet-specific, and can only be bound to the CVMs in the same availability zone. A CVM can be bound with multiple ENIs. The maximum number of ENIs allowed to be bound to a CVM depends on the CVM's specification.

### What are the restrictions for the use of ENIs on CVMs?

Please see [ENI Limits](https://cloud.tencent.com/document/product/213/15379#.E7.BD.91.E5.8D.A1.E7.9B.B8.E5.85.B3.E9.99.90.E5.88.B6) section in the "Overview of Use Limits".

### What is the basic information of an ENI?

Please see **Concepts** section in [ENI Overview](https://cloud.tencent.com/document/product/213/6514).

### How do I create an ENI?

Please see [Creating an ENI](https://cloud.tencent.com/document/product/215/6513#.E5.88.9B.E5.BB.BA.E5.BC.B9.E6.80.A7.E7.BD.91.E5.8D.A1) section in the "ENI Operation Guide".

### How do I view the ENI information?

Please see [Viewing ENI Information](https://cloud.tencent.com/document/product/215/6513#.E6.9F.A5.E7.9C.8B.E5.BC.B9.E6.80.A7.E7.BD.91.E5.8D.A1) section in the "ENI Operation Guide".

### How do I bind an ENI to a CVM instance?

Please see [Binding and Configuring ENI](https://cloud.tencent.com/document/product/215/6513#.E7.BB.91.E5.AE.9A.E5.92.8C.E9.85.8D.E7.BD.AE.E5.BC.B9.E6.80.A7.E7.BD.91.E5.8D.A1.EF.BC.88.E9.87.8D.E8.A6.81.EF.BC.89) section in the "ENI Operation Guide".

### How do I configure an ENI in the CVM instance?

Please see [Binding and Configuring ENI](https://cloud.tencent.com/document/product/215/6513#.E7.BB.91.E5.AE.9A.E5.92.8C.E9.85.8D.E7.BD.AE.E5.BC.B9.E6.80.A7.E7.BD.91.E5.8D.A1.EF.BC.88.E9.87.8D.E8.A6.81.EF.BC.89) section in the "ENI Operation Guide".

### How do I modify or customize the private IP of an ENI?

VPC-based CVMs support modifying and customizing the private IP of an ENI. Follow the steps below:

1. Log in to the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=1).
2. Click **ENI** in the left panel to go to the ENI list page.
3. Click the **ID/Name** of an ENI to go to its details page to view its information.
4. Click **IP Management** to go to the details page.
5. Click **Assign Private IP**, select **Manually Enter** for IP assignment mode, and then enter the modified IP.
6. Click **OK** to complete the operation.

After the modification is made on the console, you also need to modify the configuration file of the ENI. For more information, please see [Binding and Configuring ENI](https://cloud.tencent.com/document/product/215/6513#.E7.BB.91.E5.AE.9A.E5.92.8C.E9.85.8D.E7.BD.AE.E5.BC.B9.E6.80.A7.E7.BD.91.E5.8D.A1.EF.BC.88.E9.87.8D.E8.A6.81.EF.BC.89) section in the "ENI Operation Guide".
