A common solution is using a Tencent Cloud CDB instance in Tencent Cloud VPC, which shares data with the Web server in the same VPC. Based on this solution, this document introduces the way to create a VPC and add a CDB to the VPC for use.

### Step 1: Create a VPC and initialize subnets and routing tables
A VPC contains at least one subnet, only in which the cloud service resources can be added.

1) Log in to [Tencent Cloud Console][1], click "Virtual Private Cloud" in the navigation bar, or click "Experience" in Tencent Cloud's [VPC Overview][2] page to enter the [VPC Console][3].
2) Select a region in the drop-down box above the list and click "New" to create a VPC. For example, select the "North China (Beijing)" region.
3) Enter the names of VPC and subnet as well as CIDR, and then select the availability zone for the subnet.
4) Click "Create".

![ ](https://mc.qcloudimg.com/static/img/12901f65ca2844a88814a7190168391e/1.jpg)

### Step 2: Create a subnet
You can create one or more subnets at a time.

1) Log in to [Tencent Cloud Console][4], click "Virtual Private Cloud" in the navigation bar, or click "Experience" in Tencent Cloud's [VPC Overview][5] page to enter the [VPC Console][6].
2) Click "Subnets" in the left navigation pane.
3) Select a region and a VPC in the drop-down boxes.
4) Click "New", and then enter the subnet name, CIDR, availability zone and associated routing table.
5) (Optional) Click "New Line" to create multiple subnets at a time.
6) Click "Create".

![](https://mc.qcloudimg.com/static/img/ebda9d255ef99e0107b5d52198cc9d43/2.jpg)


### Step 3: Create a routing table to associate with a subnet
You can create a custom routing table, edit the routing policy, and then associate it with specified subnet. The routing table associated with the subnet is used to specify the outbound route for the subnet.

1) Log in to [Tencent Cloud Console][7], click "Virtual Private Cloud" in the navigation bar, or click "Experience" in Tencent Cloud's [VPC Overview][8] page to enter the [VPC Console][9].
2) Click "Routing Tables" in the left navigation pane, and click "New" button on the top of the list. Then enter the name, network and new routing rule in the pop-up box.
3) Click "Create" to view the new routing table in the routing table list.
4) Click "Subnets" in the left navigation pane.
5) Move the mouse over the "subnet" to be associated with the routing table, and the "Edit" button will appear in the "associated routing table" column.
6) Click the "Edit" button, and select the associated routing table in the drop-down box.
7) Click "Save".

![](https://mc.qcloudimg.com/static/img/7078df53ec8ce935cc1763761bc67b40/3.jpg)

### Step 4: Add a CDB
A newly purchased CDB can be used in the VPC. It should be noted that once you select the VPC to which a CDB is added, it cannot be changed.
1) Log in to [Tencent Cloud Console][10], click "Relational database" in the navigation bar to enter [Cloud Database Console][11], and click "New" button.
![](https://mc.qcloudimg.com/static/img/94b355ae34f75f64874eb53346513914/4.jpg)
2) On the Cloud Database purchase page, click "VPC" on "Network" tab, and select the VPC and the corresponding subnets created in the above steps, to add the newly purchased CDB to the VPC.
![](https://mc.qcloudimg.com/static/img/ba3116f44e2ccaec036b0fa5df0a9a9b/5.jpg)

### Step 5: Add CVM
You can now use newly purchased CVM in VPC. Please note that **network cannot be changed once selected.**
Please go to the product purchase page, click "Network Type" and select "VPC".  You can select the same VPC that was used for the CDB, and add the new CVM to the VPC.
![](//mc.qcloudimg.com/static/img/c7407f3d9d4c4ab323487dd5fc308fd5/image.png)

[1]:	https://console.cloud.tencent.com/
[2]:	https://cloud.tencent.com/product/vpc.html
[3]:	https://console.cloud.tencent.com/vpc/
[4]:	https://console.cloud.tencent.com/
[5]:	https://cloud.tencent.com/product/vpc.html
[6]:	https://console.cloud.tencent.com/vpc/
[7]:	https://console.cloud.tencent.com/
[8]:	https://cloud.tencent.com/product/vpc.html
[9]:	https://console.cloud.tencent.com/vpc/
[10]:	https://console.cloud.tencent.com/
[11]:	https://console.cloud.tencent.com/cdb/ "Cloud Database Console"