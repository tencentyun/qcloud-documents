By creating a logical layer over the hard disk and partition, Logical Volume Manager (LVM) divides the disk or partition into physical extents (PE) with the same size. Different disks or partitions can be grouped into the same volume group (VG). A logical volume (LV) can be created on VG, and file system can be created on LV. The concept of VG can be simply linked with disk, and the concept of LV can be simply linked with partition. Compared with using the disk partition directly, LVM focus on adjusting the capacity of the file system elastically:

- The file system is no longer limited by the size of the physical disk. Instead, it can be distributed across multiple disks: For example, you can buy 3 elastic cloud disks with 4TB and use LVM to create an extra-large file system of nearly 12TB.
- You can dynamically adjust the size of LV instead of repartitioning the disk: When the LVM VG space cannot meet your needs, you can purchase an elastic cloud disk separately and mount it on the corresponding CVM, and then refer to the instructions below to add it to the LVM VG to expand the capacity.
....

The following describes how to use three Tencent Cloud elastic cloud disks to create a file system via LVM which its size can be adjusted dynamically.

![](//mccdn.qcloud.com/static/img/a22b0e07c2430684faedc44a9bf3f2c2/image.png)

## Creating Physical Volume (PV)
Execute the following command to create a physical volume (PV):

```
pvcreate disk path 1 ... disk path N
```

![](//mccdn.qcloud.com/static/img/6bda1d27a97c2bc4a2f6ecc12d5ce407/image.png)

Execute `pvscan`, `lvmdiskscan`, `pvs`, `pvdisplay physical volume path `and other commands to view the physical volumes in current system:

![](//mccdn.qcloud.com/static/img/89b9329aee52edbd46098da4d8eba8c8/image.png)

## Creating Volume Group (VG)
Execute the following commands to create a volume group (VG):

```
vgcreate [-s specifies PE size] volume group name physical volume path
```
![](//mccdn.qcloud.com/static/img/b6bef868d56920544969fb3de29278a9/image.png)

After the creation is completed, you can add new physical volumes to the volume group with the `vgextend volume group name new physical volume path`
![](//mccdn.qcloud.com/static/img/5a6e292aa42c06da83faeafb64ff4634/image.png)

Use `vgs`, `vgdisplay` and other commands to view volume groups in the current system:
![](//mccdn.qcloud.com/static/img/a5939970bb877134961aa57cac492082/image.png)

## Creating Logical Volume (LV)
After creating a large volume group, you can start building the logical volume (LV). Execute the following command to create a logical volume:

```
lvcreate [-L logical volume size][-n logical volume name] VG name
```
![](//mccdn.qcloud.com/static/img/6a333909caf1197979f433b5144725ea/image.png)
Here, we created an 8G logical volume named "lv_0".

We can find that only PE in vdc has been used by executing `pvs` command:
![](//mccdn.qcloud.com/static/img/0de6857e273bf94736e601d691aff855/image.png)

## Creating File System
Execute the following command to create a file system on an established logical volume:

```
mkfs
```

![](//mccdn.qcloud.com/static/img/910be0713d9e6a216d5a114ab6cae5d4/image.png)

Use the `mount` command to mount the file system:
![](//mccdn.qcloud.com/static/img/72f94b557077a76cbbf6dffe95bbc994/image.png)

## Dynamically Expand the Size of Logical Volume and File System
If VG is left with surplus capacity, the LV capacity can be dynamically expanded. Execute the following command to expand the size of logical volume:

```
lvextend [-L +/- increase or decrease capacity] logical volume path
```

![](//mccdn.qcloud.com/static/img/a56f7ab937831f3bef2ba68962a543fc/image.png)
Here, 4G capacity has been expanded for the logical volume named "lv_0".

We can find that vdc has been fully used and 2G has been used for vdd by executing `pvs` command:
![](//mccdn.qcloud.com/static/img/59a3c0ce8fa6c004144eb2c8ea8d12cc/image.png)

Now, we have only expanded the size of logical volume, and the file system should also be expanded according to the logical volume before using. Here, we can use `resize2fs` to expand the size of the file system:

![](//mccdn.qcloud.com/static/img/3b39782a7826c8c262f1500d083682ce/image.png)
Now, we can find that the size of lv_0 has been modified to 12G by executing `df` command.

