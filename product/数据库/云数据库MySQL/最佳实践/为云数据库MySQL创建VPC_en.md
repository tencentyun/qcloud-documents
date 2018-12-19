Tencent Cloud VPC is provided by Tencent Cloud as a platform to host Tencent Cloud CDB. It allows you to enable Tencent Cloud resources in VPC, such as Tencent Cloud CDB database instance. For more information on VPC product, please see [VPC](https://cloud.tencent.com/document/product/215/535).  
A common solution is data sharing between Tencent Cloud CDB database instance and Web server in the same VPC. Based on this solution, the tutorial describes how to create a VPC and add a cloud database to the VPC for use.

### Step 1: Create VPC and Initialize Subnet and Routing Table
A VPC contains at least one subnet. Cloud service resources can only be added to subnet.

1. Log in to the [Tencent Cloud Console][1], and click the navigation bar "Cloud Products" -> "Basic Products" -> "Cloud Computing and Network" -> "VPC", or click "Use Now" button in Tencent Cloud [VPC Overview][2] to go to the [VPC Console][3].
![](https://mc.qcloudimg.com/static/img/060a49d154e15395a8ddf7c1ba17e340/step1.png)
2. Select a region in the drop-down box above the list and click "New" to create a VPC. For example, select South China (Guangzhou) as the region.
![](https://mc.qcloudimg.com/static/img/951ddd2a8dc45b4dce6fef6d03074f3d/step3.png)
3. Enter the names of VPC and subnet as well as CIDR, select the availability zone for the subnet, and click "Create".
![](https://mc.qcloudimg.com/static/img/87bf6c4ce56ccba29c0604bb01cd1183/step4.png)

### Step 2: Create Subnet
You can create one or more subnets at a time.

1. In the [VPC Console][3], click "Subnet" in the left navigation bar.
![](https://mc.qcloudimg.com/static/img/9df489a570a7430210d97656645ec617/step5.png)
2. Select a region and a VPC in the drop-down box and click "New".
![](https://mc.qcloudimg.com/static/img/67b3e64e9f8fda011f61d6a2cf3b707d/step6.png)
3. Enter the subnet name, CIDR, availability zone and associated routing table, and then click "Create". You can create multiple subnets at a time by clicking "New Line".
![](https://mc.qcloudimg.com/static/img/627ea49132a40d2cb5fd0a5589c17c00/step7.png)

### Step 3: Create Routing Table to Associate with Subnet
You can create a custom routing table, edit the routing policy, and associate it with a specified subnet. The routing table associated with the subnet is used to specify the outbound route for the subnet.

1. In the [VPC Console][3], click "Routing Table" in the left navigation bar, then select a region and a VPC in the drop-down box, and click "New".
![](https://mc.qcloudimg.com/static/img/30a66a722bbc82f63de51c2fbf1b8185/step8.png)
2. Enter the name, network and new routing policy in the pop-up box. Click "Create" to view the new routing table in the routing table list.
![](https://mc.qcloudimg.com/static/img/835062e84a035a0a30d460719b74d7f0/step9.png)
3. Click "Subnet" in the left navigation bar. Move the mouse cursor to the "Subnet" to be associated with the routing table, and the "Edit" button appears in the "Associated Routing Table" column. Click the "Edit" button, and select the associated routing table in the drop-down box. Click "Save".
![](https://mccdn.qcloud.com/static/img/a41758221e11cacef5dbdbd53f06049a/image.png)

### Step 4: Add Cloud Database
A new cloud database can be used in the VPC. Note: The VPC cannot be changed once selected.

1. Log in to the Tencent Cloud [Console][1], move the mouse cursor to the navigation bar, and select "Cloud Products" -> "Basic Products" -> "Database". Click "Relational Database", then enter [Cloud Database Console][11], and click "New" button to go to the purchase interface of CDB for MySQL.
![](https://mc.qcloudimg.com/static/img/c5a7e2e50a04631d861d899c1e71598b/step1.png)
![](https://mc.qcloudimg.com/static/img/c8d25b4002230535f28dbc59ae58318b/step2.png)
2. On the cloud database purchase page, click "VPC" on "Network" tab, select the VPC and the subnet created in the previous steps, and then add the new cloud database to the VPC.
![](https://mc.qcloudimg.com/static/img/4f09712e3a00ca9386409c1ba359d2f8/step10.png)

### Step 5: Add a CVM
A new CVM can be used in the VPC. Note: **The VPC cannot be changed once selected.**
Enter the CVM [Product Overview Page](https://cloud.tencent.com/product/cvm), click "Buy Now", and select "VPC" in "Network Type" on the product purchase page. You need to select the same VPC of the previous database, and add the new CVM to the same VPC of the cloud database.
![](https://mc.qcloudimg.com/static/img/ede1b30456b4fe9f46e6f0ea954f8c22/step11.png)


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
[11]:	https://console.cloud.tencent.com/cdb/ 

