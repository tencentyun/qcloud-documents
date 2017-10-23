## Creating a Bucket
After logging in to the console, you can create a Bucket through the COS console and you can customize the configurations of the Bucket.

Enter the COS console. Click **Create a Bucket**, then the console will pop up "Create a Bucket" dialog box:

![](//mc.qcloudimg.com/static/img/81ad8abf16cddb1c8615a7987918dbcb/image.png)

**Note**

- The limit of the Bucket is 200 (no geographical limitation). However, there is no limit to the number of directories and files under Bucket.
- Bucket is created under a project. A Bucket can only belong to one project, and users can switch the project.
- Bucket name supports the combination of lowercase letters and numbers, but it does not support special characters and underscores, and cannot exceed 40 bytes.
- In Tencent Cloud COS, the Bucket names under all projects with the same APPID must be unique.
- Bucket provides two types of access permission by default: public read permission and private write permission, and private read/write permissions.
- When creating a Bucket, you can select the region, which cannot be modified once it is set up. 



Click **Create** and you can see the created Bucket in the Bucket list page:

![](//mc.qcloudimg.com/static/img/bcac14ee35b1307afb5839798998bf66/image.png)

## Multi-region and Access Domain
COS supports multi-region storage which is currently available in three regions including North China, South China, and East China. Different regions have different default access domains. We recommend users to choose the nearest storage region according to their own business scenarios to improve the upload and download speed.

| Region   | Region Abbreviation | Default Download Domain                                  | Upload Domain                  | Status   |
| ---- | ---- | --------------------------------------- | -------------------- | ---- |
| South China   | gz   | [bucketname]-[appid].cosgz.myqcloud.com | gz.file.myqcloud.com | Launched  |
| North China   | tj   | [bucketname]-[appid].costj.myqcloud.com | tj.file.myqcloud.com | Launched  |
| East China   | sh   | [bucketname]-[appid].cossh.myqcloud.com | sh.file.myqcloud.com | Launched  |
| Singapore  | -    | -                                       | -                    | To be determined |

**Private Network Cross-Region Access: Different Tencent Cloud Services in different regions cannot be visited directly. If you need to achieve private network cross-region access (for example, CVM in Guangzhou needs the data on Singapore COS), then you need to use VPC to deploy exclusive network tunnel to implement high-speed access.  [Click to view more information about VPC](https://cloud.tencent.com/product/vpc.html)**

## Access Permission
> Public read permission and private write permission: Anyone (including anonymous visitors) has read permission to the files in the Bucket, but only the Bucket creator and accounts with the appropriate permission have write permission to the files in the Bucket.
>
> 
> Private read/write permissions: Only the creator of the Bucket and accounts with the appropriate permissions have read and write permissions to the files in the Bucket, and no one else has read and write permissions to the files in the Bucket.

If you need to modify the Bucket permission later, you can modify it by using the console space attribute.



