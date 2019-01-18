## 1. Go to CVM assignment page

1. Log in to [CDH Console](https://console.cloud.tencent.com/cvm/cdh).
2. Select the CDH in the list, and click **Assign CVM** on the top.

## 2. Select a CDH

Select the region and availability zone where the purchased CDH resides, and select the CDH in the zone.

- If you select only one CDH, your dedicated CVMs will be assigned to the specified one.
- If you select multiple CDHs of the same kind, your dedicated CVMs will be assigned to a resource pool formed by all selected CDHs.

![suzhuji](http://mc.qcloudimg.com/static/img/d10eaf8b5b887cfe585c3270b63dc887/image.jpg)



## 3. Select CVM configurations (e.g. CPU and memory)

You can customize CVM configurations, such as CPU and memory, based on the remaining resources in the selected CDH or CDH resource pool.

The configurations determine the number of CVMs that can be created.

![peizhi](http://mc.qcloudimg.com/static/img/a78c4ca173e569f01fe04a38da3c0f99/image.jpg)



## 4. Select other configurations and launch CVM

You can select image, disk and network configurations for a dedicated CVM and launch the dedicated CVM in exactly the same way as for an ordinary CVM instance.

For more information, please see [Purchase and Launch CVMs >](https://cloud.tencent.com/doc/product/213/4855)

- **Billing mode and purchase period**. The billing mode for dedicated CVMs is default to Prepaid and CANNOT be changed. The available usage period of the dedicated CVM is same as that of the CDH where the CVM resides.
- **Network billing mode**. The dedicated CVM network billing mode is default to bill-by-traffic and CANNOT be changed. You only need to select the bandwidth cap of CVM network when configuring the CVM network.
