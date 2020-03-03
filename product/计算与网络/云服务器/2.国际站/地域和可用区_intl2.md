### How to view the region list?

See [Regions and Availability Zones](https://cloud.tencent.com/document/product/213/6091)

#### Query via API:

- [Query Region List](https://cloud.tencent.com/document/product/213/15708)
- [Query Availability Zone List](https://cloud.tencent.com/document/product/213/15707)

### Can the region be changed for a purchased CVM?

The region of a purchased CVM cannot be changed. And the availability zone cannot be modified for an instance that has been launched. If you need to change the region and availability zone, refer to the following two solutions:

- If the CVM is purchased within 5 days, [submit a ticket](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=7&source=0&data_title=%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%20CVM&level3_id=158&radio_title=%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%80%80%E8%BF%98&queue=1&scene_code=12646&step=2) to apply for CVM return. Back up your data before returning the CVM, and then re-purchase another one.
- Create a custom image from the original instance. Use the custom image to launch an instance in a new availability zone and update the configuration of the new instance.
  1. Create a custom image for current instance. For more information, please see [Create Custom Image](https://cloud.tencent.com/doc/product/213/4942).
  2. If the network environment of the current instance is [VPC](https://cloud.tencent.com/doc/product/213/5227) and the private IP needs to be retained after the migration, users can first delete the subnet in the current availability zone and then create a subnet in the new availability zone with the same IP address range as that of the original subnet. Note that a subnet can be deleted only when it contains no available instance. Thus, all the instances in the current subnet should be migrated to the new subnet.
  3. Create a new instance in the new availability zone using the custom image you have just created. You can choose the same type and configuration as those of the original instance, or choose new ones. For more information, please see [Create Instance](https://cloud.tencent.com/doc/product/213/4855).
  4. If an elastic IP address is associated with the original instance, then dissociate it from the old instance and associate it with the new instance. For more information, please see [Elastic Public IP](https://cloud.tencent.com/doc/product/213/5733).
  5. (Optional) If the original instance is [postpaid](https://cloud.tencent.com/doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9), you can terminate the original instance. For more information, please see [Terminate Instance](https://cloud.tencent.com/doc/product/213/4930). If the original instance is [prepaid](https://cloud.tencent.com/doc/product/213/2180#1.-.E5.8C.85.E5.B9.B4.E5.8C.85.E6.9C.88), you can leave it alone before it expires and is reclaimed.
