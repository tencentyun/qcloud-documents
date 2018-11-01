There are two scenarios as for expanding cloud disk on Windows:

- Create the new capacity space as a separate new partition and leave the old partition unchanged
- Expand the existing partition to the new capacity space and keep the data on the old partition.

In both of the above two scenarios, after the upgrade of your cloud disk on Windows system (you can see the change of the cloud disk capacity), you can use the partition expanding tool (partition assistant) under Windows to complete the partition expansion while ensuring that the old data will not be lost.

## Preconditions
- You need to [expand physical cloud disk](/doc/product/362/5747) first.
- If the old empty cloud disk is directly expanded without being formatted when no file system is created on it, please refer to [Partitioning, Formatting and File System Creation on Windows System](https://cloud.tencent.com/document/product/362/6734
) for related operations.

## Formatting the new disk space as a separate partition
When opening the partition assistant, you can see the unused new disk space.

Right-click the unused disk space, and select "Create Partition".

In the pop-up box, enter the required partition size, drive letter and file system, and then click "OK".

Click the "Submit" button at the upper left corner.

In the pop-up box, verify the format partition information is correct, and click "Execute".

Verify again that the partition format information is correct, and click "Yes" in the pop-up box.

After the creation, click "OK".

When opening "My Computer", you can see the new disk partition.

## Adding the new space to the existing partition
Right click the partition you want to expand, and select "Adjust/Move Partition (R)".

In the pop-up box, drag the arrow to the right to adjust the partition size to a value you needed, and click "OK".

Click the "Submit" button at the upper left corner.

In the pop-up box, verify the partition expansion information is correct, and click "OK".

Verify again that the partition expansion information is correct, and click "Yes".

Wait until the partition expansion is completed, and click "OK".

When opening "My Computer", you can see the change of partition after the expansion.
