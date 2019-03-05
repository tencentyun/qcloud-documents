
If you forget your password, you can reset the login password of the instance on the console. This document introduces how to change the login password of the instance on the CVM console.


>**Note:**
>
>1. Password resetting is only allowed for instances that have been shut down.
>
>2. For a running instance whose password has been modified on the console, the CVM is shut down in the process of password reset. Schedule the time in advance to avoid data loss. You are recommended to perform the operation at the lows of business to minimize the impact.


## Resetting Password of Single Instance

- Log in to the [CVM console](https://console.cloud.tencent.com/cvm/index), and select a CVM whose password needs to be reset.
- Click **More** -> **Password/Key** ->**Reset Password** on the page.
![](https://main.qcloudimg.com/raw/6ab6b5ca227f49c6fe2b52e6b6d493f1.png)
- Go to the Reset Password page. If the instance has been shut down, directly select the account whose password needs to be reset, then enter and confirm the new password, and click **Reset**.
![](https://main.qcloudimg.com/raw/9a6c43a633e91ed58acde8f82abf7b4c.png)
- Go to the Reset Password page. If the instance is running, select the account whose password needs to be reset, then enter and confirm the new password, and click **Next**. Select **Agree to force shutdown**, and click **Change Now**.
![](https://main.qcloudimg.com/raw/076eeb851e7b6f3e9d1f2eb217fcd9af.png)
![](https://main.qcloudimg.com/raw/b35b664cbf44adaaf79fc140db0a18cf.png)
## Resetting Password of Multiple Instances
- Log in to the [CVM console](https://console.cloud.tencent.com/cvm/index), and select multiple CVMs whose password needs to be reset.
- Click **Reset password** on the page.
- Go to the Reset password page. If all of the instances have been shut down, directly select the account whose password needs to be reset, then enter and confirm the new password, and click **Reset**.
- Go to the Reset password page. If some instances are still running, select the account whose password needs to be reset, then enter and confirm the new password, and click **Next**. Select **Agree to forced shutdown**, and click **Change Now**.

