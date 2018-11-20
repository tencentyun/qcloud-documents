There are two scenarios as for expanding cloud disk on Windows:

- Create the new capacity space as a separate new partition and leave the old partition unchanged
- Expand the existing partition to the new capacity space and keep the data on the old partition.

In both of the above two scenarios, after the upgrade of your cloud disk on Windows system (you can see the change of the cloud disk capacity), you can use the partition expanding tool (partition assistant) under Windows to complete the partition expansion while ensuring that the old data will not be lost.

## Preconditions
- You need to [expand physical cloud disk](/doc/product/362/5747) first.
- If the old empty cloud disk is directly expanded without being formatted when no file system is created on it, please refer to [Partitioning, Formatting and File System Creation on Windows System](https://cloud.tencent.com/document/product/362/6734
) for related operations.

## Formatting the new disk space as a separate partition
When opening the partition assistant, you can see the unused new disk space:
![](//mccdn.qcloud.com/static/img/8bb1180fb58f1dba376084eca29502e7/image.png)

Right-click the unused disk space, and select "Create Partition":
![](//mccdn.qcloud.com/static/img/2c9c621debf86e7ae91e55fdf42216fe/image.png)

In the pop-up box, enter the required partition size, drive letter and file system, and then click "OK":
![](//mccdn.qcloud.com/static/img/2279a58dff1ecf399f53a660f46612f8/image.png)

Click the "Submit" button at the upper left corner:
![](//mccdn.qcloud.com/static/img/e406a9ab0a907fc9f33708beaad45feb/image.png)

In the pop-up box, verify the format partition information is correct, and click "Execute":
![](//mccdn.qcloud.com/static/img/0eb80f57d7ade8eec8b86b9bc82a8f92/image.png)

Verify again that the partition format information is correct, and click "Yes" in the pop-up box:
![](//mccdn.qcloud.com/static/img/b31c86dcc8e38644a8fe5835d2f676f5/image.png)

After the creation, click "OK":
![](//mccdn.qcloud.com/static/img/f424d22f58089ecf0712173484008945/image.png)

When opening "My Computer", you can see the new disk partition (in this example, it is E: drive):
![](//mccdn.qcloud.com/static/img/f53c99dd35ec9f9af00eb2d1960522ef/image.png)

## Adding the new space to the existing partition
Right click the partition you want to expand, and select "Adjust/Move Partition (R)":
![](//mccdn.qcloud.com/static/img/aacac81271ba88f35ea0dd6e25314977/image.png)

In the pop-up box, as shown in the figure, drag the arrow to the right to adjust the partition size to a value you needed, and click "OK":
![](//mccdn.qcloud.com/static/img/d548f0c5f75f9171612581c77cad072b/image.png)

Click the "Submit" button at the upper left corner:
![](//mccdn.qcloud.com/static/img/0b4e4e270c6b1e9ab43a747553119746/image.png)

In the pop-up box, verify the partition expansion information is correct, and click "OK":
![](//mccdn.qcloud.com/static/img/aab479952f267a19585c789a9511cd84/image.png)

Verify again that the partition expansion information is correct, and click "Yes":
![](//mccdn.qcloud.com/static/img/d9c99392f4542bebc1087f9d6790e722/image.png)

Wait until the partition expansion is completed, and click "OK":
![](//mccdn.qcloud.com/static/img/b06ca48c96f5c2230077b9e3430b779a/image.png)

When opening "My Computer", you can see the change of partition after the expansion (in this example, the capacity of D: drive is increased from 60 G to 109 G):
![](//mccdn.qcloud.com/static/img/cfb207b4364adc4e59cea68ad700271b/image.png)
