To start using a CVM, please do the following:

## Signing Up for a Tencent Cloud Account

If you already have a Tencent Cloud account, just skip this step.
![](//mc.qcloudimg.com/static/img/323529f3a9239acde216b5689bd6849f/image.png)
![](//mc.qcloudimg.com/static/img/d3695860b17f7dc4d9447d5782cac5d2/image.png)
![](//mc.qcloudimg.com/static/img/5646fdd83971eefa821e21025d788939/image.png)

Please set a strong password for your account and keep all the login information safe.

## Verifying Identity

Identity verification is required for some Tencent Cloud products (such as the postpaid CVMs, COS, CDN, etc.). 
![](//mc.qcloudimg.com/static/img/dc9771468866bc768a7a9f7039799f06/image.png)

## (Optional) Creating an SSH key
SSH key is used to log into Linux CVM and is more secure than password login. For more information about SSH keys, see [here](/doc/product/213/6092).

1. Log in to [CVM Console](https://console.cloud.tencent.com/) and select **SSH Keys** from the left. 
2. Click **Create a key** and enter the key name in the pop-up window. Click **OK** to confirm. 
3. Download the private key issued by Tencent Cloud within the specified period. 

## (Optional) Creating a Virtual Private Cloud (VPC)

With VPC, you can customize a network environment that is logically isolated and start the cloud resources of Tencent Cloud within it. For more information about VPC, see [here](https://cloud.tencent.com/doc/product/215/535).

A VPC contains at least one subnet. The resources of Cloud Services can only be added in the subnet.
![ ](//mc.qcloudimg.com/static/img/9e2c47ba8ce922c20ef49055c533bbcf/image.png)

1. Log in to [VPC Console](https://console.cloud.tencent.com/vpc).

2. Select a region from the drop-down list and click **New**.

3. Enter the VPC and subnet name, [CIDR](https://cloud.tencent.com/doc/product/215/4925#cidr) and select the AZ. 

4. Click **Create** to complete. 
![ ](//mc.qcloudimg.com/static/img/9e2c47ba8ce922c20ef49055c533bbcf/image.png)

## (Optional) Creating a Security Group

Security Group can be considered as the firewall for CVM and is used to control the inbound and outbound data flow at the instance level. You need to add rules in the Security Group to connect to instance from your local IP address using SSH. You can also add any other rules to restrict the access to the instance.

1. Log in to [CVM Console](https://console.cloud.tencent.com/cvm), select **Security Groups** from the left column. 

2. Click **New** and enter the security group name (e.g. my-security-group) and description. 

3. In the **Inbound Rules** section, click **Add**. Configure the inbound rule as required. Please note that if **Source** is set to `0.0.0.0/0`, all IP addresses can access CVMs in this security group.

4. In the **Outbound Rules** section, click **Add**. Configure the outbound rule as required. Please note that if **Destination** is set to `0.0.0.0/0`, CVMs in this security group can access all IP addresses.

5. Click **New** to save the security group.

> Note: If you want to start instances under multiple [regions](/doc/product/213/6091), you need to create a Security Group in each region. Tencent Cloud has created several Security Groups in each region in advance to allow users to remotely log in to the instances. For more information, see [Security Group](/doc/product/213/5221).

## (Optional) Generating a Cloud API key

Tencent Cloud provides rich Cloud APIs for developers. To use these APIs, you need to get a Cloud API key. Each call to the Cloud API requires an authentication using the Cloud API key. For more information about the authentication using the Cloud API key, see [here](https://cloud.tencent.com/document/product/213/6984?lang=en). You can generate a Cloud API key on the console by following steps.

1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/) with your Tencent Cloud account, and choose **Cloud API Keys** from the product list at the top of the page.

2. Open **API Keys** and click **New Key**.
> Note: Each user can generate up to 2 Cloud API keys.

