## How to bind a WeChat Mini Program account to Tencent Cloud

Go to [Tencent Cloud Account Center](https://console.cloud.tencent.com/developer), and click the **Associate** button behind **Login via WeChat Official Accounts Platform** for association:

<img src="https://imgcache.qq.com/open_proj/proj_qcloud_v2/mc_2014/wechat/css/img/account.png" width="300px" alt="binding account" />

After the association, you can:

- Directly log in to the corresponding Tencent Cloud account by scanning QR code using WeChat and selecting the associated WeChat Official Account and Mini Program
- **Use WeChat Developer Tools to activate, upload, and deploy Mini Program backend codes with one click.** [View Details>>](https://console.cloud.tencent.com/lav2/dev)
- Directly go to Tencent Cloud console via WeChat Developer Tools without login

## How to unbind WeChat Mini Programs from Tencent Cloud

You can unbind a WeChat Mini Program that has been bound to Tencent Cloud by following the two methods below.

#### Unbinding on Tencent Cloud

Go to [Tencent Cloud Account Center](https://console.cloud.tencent.com/developer), and click the **Unbind** button behind **Login via WeChat Official Accounts Platform** for unbinding:

<img src="https://mc.qcloudimg.com/static/img/587c7da6255ed85359dd6c0027921c72/jiebang.jpg" width="300px" alt="unbinding account" />

#### Unbinding on WeChat Official Accounts Platform

Log in to [WeChat Official Accounts Platform](https://mp.weixin.qq.com/), click **Settings** on the left menu, and select **Third Party Authorization Management**. Then you can see the authorization information of Tencent Cloud official website. Click **Terminate Authorization** to unbind the account.

> **Note:** If you unbind an account using this method, Tencent Cloud will not receive a notification from WeChat, and it still retains your binding information, which may cause unavailability of some Tencent Cloud services. Unbinding on Tencent Cloud is recommended.

<img src="https://mc.qcloudimg.com/static/img/10e412a1e58bfdd7944641a84f827c36/jiebang-wx.jpg" alt="unbinding account" />

## If I have registered a Tencent Cloud account directly with a WeChat Mini Program, how can I bind another Mini Program account?

Tencent Cloud does not support binding a Tencent Cloud account registered using WeChat Official Account (Mini Program) with another WeChat Mini Program. If your Tencent Cloud **Account A** is registered with a WeChat Official Account, the following temporary solution can be used:

1. On [Tencent Cloud login page](https://www.cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2Flav2), click WeChat Official Account in the lower right corner, then scan the code using WeChat, and **select your WeChat Mini Program to create a Tencent Cloud Account B**.

   <img src="https://ask.qcloudimg.com/draft/1000695/a8yjsi45rv.jpg" width="300px" width="login" />

2. Copy Account B's **Account ID** which can be viewed in [Account Information](https://console.cloud.tencent.com/developer):

   <img src="https://ask.qcloudimg.com/draft/1000695/mel4x2dwh6.jpg" width="400px" width="copying account ID" />

3. Log in to the console of the existing Tencent Cloud Account A, move the mouse cursor over the user name in the upper right corner of the console, and click **Permission Management** on the popup menu.

   <img src="https://ask.qcloudimg.com/draft/1000695/yp64yznt7m.jpg" width="200px" width="menu" />

4. Click **Create User** on the page, and then fill in the information on the new page. Enter the ID of Account B copied in Step 2 in **Login Account** field.

   <img src="https://ask.qcloudimg.com/draft/1000695/gvrlyulk1z.png" width="400px" width="Creating sub-account" />

5. Click **Next** and select **All Policies**.

   > You can also select the permission policies that you only want to assign to Account B.

6. After the account is created, move the mouse cursor over the user name in the upper right corner of the console, click **Switch developers** on the pop-up menu, and select a collaborative developer.

   <img src="https://ask.qcloudimg.com/draft/1000695/89qlcoyn0e.jpg" width="200px" width="switch developers" />

   <img src="https://ask.qcloudimg.com/draft/1000695/p2neq9e1ia.jpg" width="400px" width="switch developers" />

## If I accidentally cancel the Tencent Cloud authorization on WeChat Official Account Platform, how can I reauthorize?

You can reauthorize by following the steps below:

1. Go to [Tencent Cloud login page](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2Flav2%2Fdev), and click the **WeChat Official Account** button to associate a WeChat Official Accounts platform account.

   <img src="https://ask.qcloudimg.com/draft/1000695/mwfbllxwt2.png" width="300px" alt="login">

2. On the pop-up page, scan the QR code using WeChat, and select the corresponding Mini Program account to reauthorize the binding.

## What can I do when an exception occurred during WeChat Mini Program authorization?

This may be caused by the following reasons:

1. Tencent Cloud account is not associated with any WeChat Mini Program
   Go to [Tencent Cloud Account Center](https://console.cloud.tencent.com/developer), and click the **Associate** button behind the **WeChat Official Accounts Platform** to associate your WeChat Mini Program.

   <img src="https://ask.qcloudimg.com/draft/1173778/og36fmzkxj.png" alt="associate WeChat Mini Program">

2. Tencent Cloud account is associated with the WeChat Official Account instead of WeChat Mini Program
   Unbind the associated WeChat Official Account before you can bind WeChat Mini Program.
   Go to [Tencent Cloud Account Center](https://console.cloud.tencent.com/developer), and click the **Unbind** button behind **WeChat Official Accounts Platform** to complete unbinding:

   <img src="https://ask.qcloudimg.com/draft/1173778/5169qyoy49.png" alt="Unbind WeChat Official Account">

   Associate your WeChat Mini Program after unbinding WeChat Official Account.

3. WeChat Mini Program terminates third-party authorization for Tencent Cloud
   If your Tencent Cloud account is already bound with the WeChat Mini Program, you can log in to [WeChat Official Account Platform](https://mp.weixin.qq.com/), click **Settings** on the left menu, and then select **Third Party Authorization Management** to view the authorization status of Tencent Cloud.

   <img src="https://ask.qcloudimg.com/draft/1173778/aja985lm6x.png" alt="WeChat Official Accounts Platform authorization">

   If Tencent Cloud is not on your third-party authorization list, you can unbind the WeChat Mini Program currently associated with Tencent Cloud account before re-associating.
   
   > If the authorization to Tencent Cloud is suspended via the WeChat Official Accounts platform, Tencent Cloud will not receive a notification from WeChat. In this case, Tencent Cloud still retains your binding information, but is actually not authorized.

4. Authorized permissions of WeChat Mini Program are incomplete
   If your Tencent Cloud account is already bound with the WeChat Mini Program, and the third-party authorization is completed on the WeChat Official Account platform, then check the permissions authorized to Tencent Cloud.
   <img src="https://ask.qcloudimg.com/draft/1173778/z7murg5cw3.png" alt="WeChat Official Accounts Platform authorization">
   
   If authorized permissions are incomplete, you need to unbind the WeChat Mini Programs currently associated with Tencent Cloud account before re-associating.
   When you re-associate the Mini Program, select **I want to modify the authorized permissions**, check all the permissions, and then click **Authorize**.

   <img src="https://ask.qcloudimg.com/draft/1173778/7hj5gxoz14.png" width="300px" alt="modify authorized permissions">
   
   <img src="https://ask.qcloudimg.com/draft/1173778/xe5bykrhmj.png" width="300px" alt="modify authorized permissions">


