To start using a CVM, please do the following:

## Signing Up for a Tencent Cloud Account

If you already have a Tencent Cloud account, just skip this step.
![](//mccdn.qcloud.com/static/img/b95541efd781757035eef96d73088513/image.png)
![](//mccdn.qcloud.com/static/img/f5ad4b5f92a32060ed1122114388226b/image.png)
![](//mccdn.qcloud.com/static/img/0665bd87d4759d39dc9cb0bb048a9485/image.png)

Please set a strong password for your account and keep all the login information safe.

## Verifying Identity

Identity verification is required for some Tencent Cloud products (such as the postpaid CVMs, COS, CDN, etc.). 
![](//mccdn.qcloud.com/static/img/61e2b15b057ef2508656e1972c422c1c/image.jpg)
![](//mccdn.qcloud.com/static/img/2e668e7e607ea863f1d2b4540397334d/image.png)

## (Optional) Creating an SSH key
SSH key is used to log into Linux CVM and is more secure than password login. For more information about SSH keys, see [here](/doc/product/213/6092).

1. Log in to [CVM Console](https://console.qcloud.com/) and select **SSH Keys** from the left. 
2. Click **Create a key** and enter the key name in the pop-up window. Click **OK** to confirm. 
3. Download the private key issued by Tencent Cloud within the specified period. 

## (Optional) Creating a Virtual Private Cloud (VPC)

With VPC, you can customize a network environment that is logically isolated and start the cloud resources of Tencent Cloud within it. For more information about VPC, see [here](https://www.qcloud.com/doc/product/215/535).

A VPC contains at least one subnet. The resources of Cloud Services can only be added in the subnet.
![](//mccdn.qcloud.com/static/img/55cdba64e785d9b073bc4169a9459e39/image.png)

1. Log in to [VPC Console](https://console.qcloud.com/vpc).

2. Select a region from the drop-down list and click **New**.

3. Enter the VPC and subnet name, [CIDR](https://www.qcloud.com/doc/product/215/4925#cidr) and select the AZ. 

4. Click **Create** to complete. 
![](//mccdn.qcloud.com/static/img/55cdba64e785d9b073bc4169a9459e39/image.png)

## (Optional) Creating a Security Group

Security Group can be considered as the firewall for CVM and is used to control the inbound and outbound data flow at the instance level. You need to add rules in the Security Group to connect to instance from your local IP address using SSH. You can also add any other rules to restrict the access to the instance.

1. Log in to [CVM Console](https://console.qcloud.com/cvm), select **Security Groups** from the left column. 

2. Click **New** and enter the security group name (e.g. my-security-group) and description. 

3. In the **Inbound Rules** section, click **Add**. Configure the inbound rule as required. Please note that if **Source** is set to `0.0.0.0/0`, all IP addresses can access CVMs in this security group.

4. In the **Outbound Rules** section, click **Add**. Configure the outbound rule as required. Please note that if **Destination** is set to `0.0.0.0/0`, CVMs in this security group can access all IP addresses.

5. Click **New** to save the security group.

> Note: If you want to start instances under multiple [regions](/doc/product/213/6091), you need to create a Security Group in each region. Tencent Cloud has created several Security Groups in each region in advance to allow users to remotely log in to the instances. For more information, see [Security Group](/doc/product/213/5221).

## (Optional) Generating a Cloud API key

Tencent Cloud provides rich [Cloud APIs](https://www.qcloud.com/product/api.html) for developers. To use these APIs, you need to get a Cloud API key. Each call to the Cloud API requires an authentication using the Cloud API key. For more information about the authentication using the Cloud API key, see [here](https://www.qcloud.com/document/product/213/6984?lang=en). You can generate a Cloud API key on the console by following steps.

1. Log in to [Tencent Cloud Console](https://console.qcloud.com/) with your Tencent Cloud account, and choose **Cloud API Keys** from the product list at the top of the page.

2. Open **API Keys** and click **New Key**.
> Note: Each user can generate up to 2 Cloud API keys.

