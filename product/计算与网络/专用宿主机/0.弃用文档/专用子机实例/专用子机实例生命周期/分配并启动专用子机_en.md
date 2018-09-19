The dedicated CVM has the same lifetime as its host, and it is assigned on a prepaid basis. The price is set to 0 CNY when for each dedicated CVM is created.

## 1. Go to CVM assignment page

1. Log in to [CDH Console](https://console.cloud.tencent.com/cvm/cdh).
2. Select the CDH in the list, and click "Assign CVM" on the top.



## 2. Select a CDH

Select the region and availability zone where the purchased CDH resides, and select the CDH in the zone.

- If you select only one CDH, your dedicated CVMs will be assigned to the specified one.
- If you select multiple CDHs of the same kind, your dedicated CVMs will be assigned to a resource pool formed by all selected CDHs.

![suzhuji](http://mc.qcloudimg.com/static/img/d10eaf8b5b887cfe585c3270b63dc887/image.jpg)



## 3. Select CVM configurations (e.g. CPU and memory)

You can customize CVM configurations, such as CPU and memory, based on the remaining resources in the selected CDH or CDH resource pool.

The configurations determine the number of CVMs that can be created.

![peizhi](http://mc.qcloudimg.com/static/img/a78c4ca173e569f01fe04a38da3c0f99/image.jpg)



## 4. Select other configurations and Start CVM

You can select image, disk and network configurations for a dedicated CVM and start the dedicated CVM in exactly the same way as for an ordinary CVM instance.

For more information, please see [Purchase and Start Instances>](https://cloud.tencent.com/doc/product/213/4855)

- **By default, a dedicated CVM is billed on a prepaid basis**. The available usage period of the dedicated CVM is same as that of the CDH where the CVM resides. You don't need to select the billing mode and purchased usage period when assigning CVM instances.
- **By default, network of dedicated CVM is billed on a pay-per-use basis**. You only need to select the capped bandwidth of the network when configuring the it.


