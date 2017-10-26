As shown in the figure below, in this exercise, you will create a VPC and a subnet, deploy a CVM within the subnet and allow the CVM to communicate with the Internet by binding an EIP. Finally, you need to filter the inbound and outbound traffic of the CVM through security group to guarantee the security of the communication of CVM. In a real application environment, you can access your CVM from local machine and use this scenario to create a Web server for public use, for example, blog hosting.
![](//mccdn.qcloud.com/static/img/7a428200fc9782b02d05d220ae6328bb/image.png)



### Step 1: Create a VPC and initialize subnets and routing tables
A VPC contains at least one subnet, only in which the cloud service resources can be added.

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar, or click "Experience" in Tencent Cloud's [VPC Overview](https://cloud.tencent.com/product/vpc.html) page to enter the [VPC Console](https://console.cloud.tencent.com/vpc/).
2)	Select a region in the drop-down box above the list and click "New" to create a VPC. For example, select the "North China (Beijing)" region.
3)	Enter the names of VPC and subnet as well as CIDR, and select the availability zone for the subnet.
4)	Click **Create**.

![](//mccdn.qcloud.com/static/img/55cdba64e785d9b073bc4169a9459e39/image.png)

### Step 2: Create a subnet
You can create one or more subnets at a time.


1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar, or click "Experience" in Tencent Cloud's [VPC Overview](https://cloud.tencent.com/product/vpc.html) page to enter the [VPC Console](https://console.cloud.tencent.com/vpc/).
2)	Click "Subnets" in the left navigation pane.
3)	Select a region and a VPC in the drop-down boxes.
4)	Click **New**, and then enter the subnet name, CIDR, availability zone and associated routing table.
5)	(Optional) Click **New Line** to create multiple subnets at a time.
6)	Click **Create**.

![](//mccdn.qcloud.com/static/img/66a4e93f7f8dfeeed421fb799fd09137/image.png)


### Step 3: Create a routing table to associate with a subnet
You can create a custom routing table, edit the routing policy, and then associate it with specified subnet. The routing table associated with the subnet is used to specify the outbound route for the subnet.

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar, or click "Experience" in Tencent Cloud's [VPC Overview](https://cloud.tencent.com/product/vpc.html) page to enter the [VPC Console](https://console.cloud.tencent.com/vpc/).
2) Click "Routing Tables" in the left navigation pane, and click "New" button on the top of the list. Then enter the name, network and new routing rule in the pop-up box.
3) Click "Create" to view the new routing table in the routing table list.
4) Click "Subnets" in the left navigation pane.
5) Move the mouse over the "subnet" to be associated with the routing table, and the "Edit" button will appear in the "Associated routing table" column.
6) Click the "Edit" button, and select the associated routing table in the drop-down box.
7) Click "Save".

![](//mccdn.qcloud.com/static/img/a41758221e11cacef5dbdbd53f06049a/image.png)

### Step 4: Add a CVM to the subnet

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar, or click "Experience" in Tencent Cloud's [VPC Overview](https://cloud.tencent.com/product/vpc.html) page to enter the [VPC Console](https://console.cloud.tencent.com/vpc/).
2) Select "Subnets" in the left navigation pane.
3) In the line for the subnet for which a CVM will be added, click "Add Cloud Virtual Machine" icon. Note: Please select a bandwidth greater than 0 or select "Bill by Traffic" for the CVM instance to be created, because the Internet needs to be accessed in other steps in this guide.

Or

1)	On the [CVM Overview](https://cloud.tencent.com/product/cvm.html) page, click "Experience" button.
2)	When you select storage and network in the third step, select the VPC you just created and its subnet. Note: Please select a bandwidth greater than 0 or select "Bill by Traffic" for the CVM instance to be created, because the Internet needs to be accessed in other steps in this guide.

### Step 5: Bind an EIP to the CVM for accessing the public network
[Elastic IP](https://cloud.tencent.com/doc/product/213/1941) is a public IP address associated with user's account, used for the communication with the Internet. Users can bind an elastic IP (EIP) to any CVM quickly to make the CVM communicate with the public network.

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), and click "Cloud Virtual Machine" in the navigation bar, and click "EIP" in the left navigation pane.
2) Click "Apply" button.
3) Apply for the EIP in the same region where the VPC resides in. After this, you can view the applied EIP in the EIP list.
4) Select the specified EIP in the EIP list, click **Bind** to bind the EIP to the CVM you just created in the VPC. After the binding, your CVM can access the public network.
![](//mccdn.qcloud.com/static/img/4853aa0215993d8ce40e965cafee6bf8/image.png)

### (Optional) Step 6: Create a security group for network traffic control
[Security Group](https://cloud.tencent.com/doc/product/213/500) is an instance-level firewall provided by Tencent Cloud, used to control the inbound and outbound traffic of any CVM.

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), and click "Cloud Virtual Machine" in the navigation bar, and click "Security Groups" in the left navigation pane.
Click "New" button, enter the name of the Security Group (e.g. my-security-group) and provide a description to complete the creation.
3) Click "Bind an instance" button at the end of the line for the security group in the list, and select the CVM you just created.
6) Click "Inbound rule" and "Outbound rule" tabs on the top to edit inbound and outbound rules for traffic control.

For example, to allow your local computer (IP: 186.23.55.90) to send HTTP requests to the CVM, you can create a rule as shown in the figure below:

![](//mccdn.qcloud.com/static/img/3dab4565be71898ca2e0e9cf79639c92/image.png)


