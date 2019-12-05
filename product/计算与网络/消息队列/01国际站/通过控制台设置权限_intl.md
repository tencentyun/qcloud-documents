Taking the example of specifying a user to have **Write permission of Consume Message and Consume Messages in Batch** for CMQ queue model, this document will demonstrate how to set CMQ permissions. The CAM permission management capability of CMQ is currently under a gray release. You can contact our technical support for help.

**Note**:
Before CAM is released, both the original collaborator account and sub-account can be used to log in to CMQ console, and the resource list for root account can be obtained (i.e. the list API permission. The root account key is used originally). After CAM is connected, sub-accounts do not have the permission to get the resource list for root accounts by default (the sub-account key is used for the console login), and sub-accounts can only have access to the list with the authorization by root accounts via CAM.

The operation performed in the Console is shown below:

## Ⅰ. Creating a User

1. Visit the [Users and Permissions Console](https://console.cloud.tencent.com/cam) and click "Create user".

2. If the user needs to log in to Tencent Cloud console or call Cloud APIs, you need to select "Allow login to Tencent Cloud", and fill in "QQ Number" as login credential.
**Note:**
We recommend that you use a QQ account not used for registration in Tencent Cloud for the sub-account (you don't need to top up for sub-accounts, as the CMQ charges will be deducted from the main account)
[Apply for a free QQ account >>](https://ssl.zc.qq.com/v3/index-en.html?type=0)
![](//mccdn.qcloud.com/static/img/717db35eae2332917a152eb69e8b4339/image.png)

3. Associate policies for the user (policies specify the permissions, so the user can have the permissions which the policies specify when associating with the policies).
![](//mccdn.qcloud.com/static/img/6554d84d46a16ea7f708402600bfe08b/image.png)

4. In the "User Management" list, you can view the sub-users you just added.
![](//mccdn.qcloud.com/static/img/f25458bc47e905348883376d3d645244/image.png)

## Ⅱ. Creating a Custom Policy

We can create a custom policy to enable the permissions of a specific API, for example, to specify the write permission of a specific CMQ Queue (Consume Message, Consume Messages in Batch).

1. Configure the service type and check "Queue Model".
![](//mc.qcloudimg.com/static/img/ebe81c0f3661863f9961db0c5716081d/image.png)

2. Specify a specific API.
![](//mc.qcloudimg.com/static/img/6237ef0c57ef39db790e19638f4e1bc5/image.png)

3. Specify a resource object.
In the example, we specify the policy and use all of the existing and new Queues under the root account (including those created by the sub-account) as the associated objects.
**Note:**
Sub-accounts do not have the list API permission of CMQ by default (when you log in to CMQ console, you cannot see a list of specific resources in the console. You can consider whether to add the list permission for sub-accounts according to your actual needs)
![](//mc.qcloudimg.com/static/img/ee8053f051805493d53d6f4f67f2d531/image.png)

## Ⅲ. Associating with a Sub-user

Associate the created policy to a sub-user so that the sub-user will have the permissions of Consume Message and Consume Messages in Batch for all the Queue resources under the sub-user.

![](//mc.qcloudimg.com/static/img/0bfdf9df7ad29dbae8e51c28904be972/image.png)


## Ⅳ. Sub-user Login

After login with the sub-account, if you cannot find the corresponding resource, click in the upper right corner of the console to switch the developer account of collaborator.

![](//mc.qcloudimg.com/static/img/477c491f7e6c5b1b3a8968499590e92d/image.jpg)


