In this section, we will introduce to you about how to set up a static IP address for external access if the cluster requires to actively make external access.

## Scenarios

This solution is applicable if the clusters of your scaling group:
- Need to receive requests from CLB;
- Need to actively access Internet;
- Need to access Internet with a **static** public IP.



## Solution Overview
1. Receive and respond to external requests via CLB.
2. Place the server in the subnet of VPC, direct the routing table to the NAT gateway and all active external request are delivered via the public IP of the NAT gateway.
3. The network attribute of the scaling group is set as this subnet, so that all the expanded servers will actively make external access via the NAT gateway.

The setting procedure is shown as follows:

![](https://mc.qcloudimg.com/static/img/9cccdddfe99dbc065c97cad27448ed9f/image.png)



## How to Set

### Step One: Create a VPN and a Subnet

#### **1. Create a VPC**

1). Log in to [VPC Console](https://console.cloud.tencent.com/vpc/).

2). Select a region in the drop-down box above the list and click "New" to create a VPC. For example, select the region of **North China (Beijing)**.

3). Enter names of the VPC and subnet as well as CIDR, and select the availability zone for the subnet.

4). Click "Create".


#### **2. Create a subnet**

1). Log in to [VPC Console](https://console.cloud.tencent.com/vpc/). Click "Subnet" in the left navigation bar. Choose a region and VPC in the drop-down box.
![](https://mc.qcloudimg.com/static/img/02c52c44678a56597b4d7053f8f8c467/3.jpg)

2). Click "New", and then enter the subnet name, CIDR, availability zone and associated routing table. After that, click "Create" to confirm.

3). After the creation is completed, you can purchase servers for this subnet.


### Step 2: Create a NAT gateway
#### **1. Purchase desired products**
1). Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), select "Virtual Private Cloud" tab, and then select "NAT Gateway".

2). Click the "New" button at the upper left corner, and enter or specify the following parameters in the pop-up box:
- Gateway name
- Gateway type (which can be changed after creation)
- VPC of the NAT Gateway service (which was just created by you)
- Assign the elastic IP for the NAT gateway. This IP is the static IP via which your server makes external access.

3). After selection, click "OK" to complete the creation of NAT gateway.

4). After the creation of the NAT gateway, you need to configure the routing rules on the Routing Table page of the VPC Console to direct the subnet traffic to the NAT gateway.

#### **2. Set the routing table (highlights)**
1). Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar to enter the [Virtual Private Cloud Console](https://console.cloud.tencent.com/vpc/vpc?rid=8), and then select "Routing Table".

2). In the routing table list, click the ID of the routing table associated to the subnet that needs to access the Internet to go to the details page of the routing table, and then click "Edit" button in the "Routing Policies".

3). Click "New Line" to fill in the destination (for example, "0.0.0.0/0" can be entered in this scenario), select "NAT Gateway" as the next hop type, select the created NAT gateway ID, and then click "OK".
![](https://mc.qcloudimg.com/static/img/3cd89bc5f80c66fd88c27cfc4e08d785/1.jpg)

Now, even without public IP, your server in this subnet can actively get external access via the NAT gateway with a static IP.

For example, the CVM below has its public IP bandwidth set　to zero, it can still actively make external access:
![](https://mc.qcloudimg.com/static/img/17ed153e06272885b56764781d9ab581/49.jpg)
However, the scaling group needs to identify this subnet and ensure that all the servers are created on this subnet.

### Step 3: Set up the scaling group
This step is to bind the subnet with the scaling group, so that scaling group can launch the newly expanded servers under this subnet.
**In this way, the expanded server uses the static IP address of the NAT gateway to access external websites.**

In the [Auto Scaling Console](https://console.cloud.tencent.com/autoscaling/config), click "New":

- Fill in the name of the scaling group, launch configuration (to be set up well in advance), maximum group size, minimum group size, initial number of instances, and other information.
- Select "Network" and "Subnet", and then direct them to the selected VPC and subnet.

The setting procedure is shown as follows:
![](https://mc.qcloudimg.com/static/img/699ee5bde186a9d4686684346032eba5/16.jpg)

The setting has been completed.

