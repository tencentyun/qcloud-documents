Capacity expansion for Windows cloud disk can be divided into two scenarios:

- Format the new capacity space as a new separate partition while the old partition remains unchanged.
- Expand the old partition to the new empty space while keeping the data of the old partition unchanged.

In the two scenarios above, after your Windows cloud disk is successfully upgraded (the cloud disk capacity change can be seen), you can complete the partition expansion through the partition expansion tool Partition Assistant in Windows while keeping the original data unaffected.

## Prerequisites
- You need to download [Partition Assistant](http://www.disktool.cn/).
- Complete the [capacity expansion of cloud disk](/doc/product/362/5747).
- If the cloud disk is not formatted and no file system is created, and the capacity is directly added to the original empty cloud disk, you can refer to [Partitioning, Formatting, and File System Creation on Windows System](https://intl.cloud.tencent.com/document/product/362/6734) 
to perform subsequent operations.

## Formatting New Space as an Independent Partition
Open the Partition Assistant, and you can find the unused capacity of the new disk space:
![](//mccdn.qcloud.com/static/img/8bb1180fb58f1dba376084eca29502e7/image.png)

Right-click the unused disk space, and select **Create Partition**:
![](//mccdn.qcloud.com/static/img/2c9c621debf86e7ae91e55fdf42216fe/image.png)

In the pop-up box, enter the desired partition size, drive letter, and file system, and then click the **OK** button:
![](//mccdn.qcloud.com/static/img/2279a58dff1ecf399f53a660f46612f8/image.png)

In the upper left corner, click the **Submit** button:
![](//mccdn.qcloud.com/static/img/e406a9ab0a907fc9f33708beaad45feb/image.png)

In the pop-up box, after confirming that the partition formatting information is correct, click the **Execute** button:
![](//mccdn.qcloud.com/static/img/0eb80f57d7ade8eec8b86b9bc82a8f92/image.png)

After confirming that the partition formatting information is correct again, click the **Yes** button in the pop-up box:
![](//mccdn.qcloud.com/static/img/b31c86dcc8e38644a8fe5835d2f676f5/image.png)

After the partition is created, click the **Confirm** button:
![](//mccdn.qcloud.com/static/img/f424d22f58089ecf0712173484008945/image.png)

Open **My Computer**, and you can find the new disk partition (E drive in this example):
![](//mccdn.qcloud.com/static/img/f53c99dd35ec9f9af00eb2d1960522ef/image.png)

## Adding New Space to Existing Partition Space
Right-click the partition to be expanded, and select **Adjust/Move Partition (R)**:
![](//mccdn.qcloud.com/static/img/aacac81271ba88f35ea0dd6e25314977/image.png)

As shown in the figure, in the pop-up box, drag the small arrow to the right to adjust the partition space, and then click the **OK** button:
![](//mccdn.qcloud.com/static/img/d548f0c5f75f9171612581c77cad072b/image.png)

In the upper left corner, click the **Submit** button:
![](//mccdn.qcloud.com/static/img/0b4e4e270c6b1e9ab43a747553119746/image.png)

In the pop-up box, after confirming that the partition expansion information is correct, click the **Confirm** button:
![](//mccdn.qcloud.com/static/img/aab479952f267a19585c789a9511cd84/image.png)

After confirming the partition expansion information again, click the **Yes** button:
![](//mccdn.qcloud.com/static/img/d9c99392f4542bebc1087f9d6790e722/image.png)

After the partition capacity expansion is completed, click **OK**:
![](//mccdn.qcloud.com/static/img/b06ca48c96f5c2230077b9e3430b779a/image.png)

Open **My Computer**, you can view the partition change after capacity expansion (in this example, D drive is expanded from 60 G to 109 G):
![](//mccdn.qcloud.com/static/img/cfb207b4364adc4e59cea68ad700271b/image.png)

