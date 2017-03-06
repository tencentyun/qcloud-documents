To facilitate your effective use of Tencent Cloud CVM, please complete the following steps to set up the CVM:

## Sign up for a Tencent Cloud account

If you already have a Tencent Cloud account, you can skip the sign-up step and make the following settings.
![](//mccdn.qcloud.com/static/img/b95541efd781757035eef96d73088513/image.png)
![](//mccdn.qcloud.com/static/img/f5ad4b5f92a32060ed1122114388226b/image.png)
![](//mccdn.qcloud.com/static/img/0665bd87d4759d39dc9cb0bb048a9485/image.png)

Please set a strong password for your account and keep all the login information.

## Identity verification

After you have signed up as a Tencent Cloud user, you need to go through identity verification before the use of some products (such as the pay-per-use CVMs, COS, CDN, etc.). When you have completed the identity verification, you can use all of Tencent Cloud services by default (except those services that specially need a separate application).
![](//mccdn.qcloud.com/static/img/61e2b15b057ef2508656e1972c422c1c/image.jpg)
![](//mccdn.qcloud.com/static/img/2e668e7e607ea863f1d2b4540397334d/image.png)

## (Optional) Create SSH key
SSH key is an instance login method <font color="red">that applies to Linux CVM and</font> is more secure than the ordinary password login. For more information about SSH key, see [SSH Key](/doc/product/213/6092).

## (Optional) Create a Virtual Private Cloud (VPC)

Tencent Cloud VPC allows you to customize a network environment that is logically isolated and start the cloud resources of Tencent Cloud within it. For more information about VPC, see [VPC product documentation](https://www.qcloud.com/doc/product/215/535).

A VPC contains at least one subnet. The resources of Cloud Services can only be added in the subnet.
![](//mccdn.qcloud.com/static/img/55cdba64e785d9b073bc4169a9459e39/image.png)

## (Optional) Create a Security Group

Security Group can be considered as the firewall for CVM and is used to control the inbound and outbound data flow at the instance level. You need to add rules in the Security Group to connect to instance from your local IP address using SSH. You can also add any other rules to restrict the access to the instance.

> Please note that if you want to start instances under multiple [Regions](/doc/product/213/6091), you need to create a Security Group in each region.  Tencent Cloud has created several Security Groups in each region in advance to allow users to remotely log in to the instances. For more information, see [Security Group](/doc/product/213/5221).

## (Optional) Create a Cloud API key

Tencent Cloud's [Cloud API](https://www.qcloud.com/product/api.html) provides developers with a simple and efficient call interface so that users can use and manage Cloud Services of Tencent Cloud in a development environment. Cloud API key is the prerequisite for the use of Cloud API. Each call to the Cloud API requires an authentication using the Cloud API key.  For more information about the authentication using the Cloud API key, see [Authentication](https://www.qcloud.com/doc/api/229/1227). If you have not created any Cloud API key yet, you need to create it by yourself through the console by following the steps below.
> Note: There is a limit on the number of Cloud API keys that can be created for each account. At present, a maximum of 2 keys can be created.