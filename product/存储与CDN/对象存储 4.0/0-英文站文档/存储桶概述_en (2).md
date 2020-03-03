Tencent Cloud COS is a storage service on the Web, where a Bucket must be created before any file (object) is stored. Users can use Tencent Cloud console, COS API, SDK and other ways to create a Bucket and upload an object. This section introduces the basic concepts of the bucket and provides instructions on how to use it. 

## Configuring Bucket Attributes

Tencent Cloud COS supports the configuration of various bucket attributes. For example, users can configure the bucket for static website hosting, define the bucket access path, and set bucket access permissions.

For more information on attribute configurations, refer to the following documents:

[Hosting a Static Website in a Bucket](https://cloud.tencent.com/document/product/436/6249)
[Configuring Bucket Access Permissions](https://cloud.tencent.com/document/product/436/6247)
[Enabling Cross-Origin Resource Sharing](https://cloud.tencent.com/document/product/436/6251)
[Management of Domains Accessing a Bucket](https://cloud.tencent.com/document/product/436/6252)


## Multi-region Storage and Access Domains
COS supports multi-region storage. Currently, South China, North China, and East China regions are available. The default access domain is different in these regions. We recommend users choose the nearest region for storage according to their own business scenarios, in order to improve upload and download speed.

| Region   | Region Code | Default Download Domain                              | Upload Domain                 | Status   |
| ---- | ---- | ----------------------------------- | -------------------- | ---- |
| South China   | gz   | bucketname-APPID.cosgz.myqcloud.com | gz.file.myqcloud.com | Available  |
| North China   | tj   | bucketname-APPID.costj.myqcloud.com | tj.file.myqcloud.com | Available  |
| East China   | sh   | bucketname-APPID.cossh.myqcloud.com | sh.file.myqcloud.com | Available  |
| Singapore  | -    | -                                   | -                    | Coming soon |

**Private network cross-region access: Different Tencent Cloud products in different regions cannot be accessed directly. To achieve private network cross-region access, for example, a CVM in Guangzhou needs to use data on the Singapore COS, you need to use a VPC to deploy exclusive network tunnels to achieve high-speed access.  [Click to view VPC related information](https://cloud.tencent.com/product/vpc.html)**


## Access Permissions
> Public read permission and private write permission: Anyone (including anonymous visitors) has read permission to the files in the Bucket, but only the Bucket creator and accounts with the appropriate permission have write permission to the files in the Bucket.
>
> 
> Private read/write permissions: Only the creator of the Bucket and accounts with the appropriate permissions have read and write permissions to the files in the Bucket, and no one else has read and write permissions to the files in the Bucket.

You can modify the Bucket permission through Bucket Attribute on the console if there's a need to do so later.


## Bucket Restrictions
- The maximum number of Buckets is 200 (The number is the same in all regions), but there is no limit to the number of directories and files under a Bucket.
- Buckets are created under projects, and one Bucket can only belong to one project. Switch between projects is supported.
- In Tencent Cloud COS, the Bucket names under all the projects with the same APPID must be unique.
- Once created, the Bucket cannot be renamed. It is recommended that you define your Bucket name before uploading a file.
- When creating a Bucket, you can select a region. The region cannot be changed once set. 

## Bucket Naming Rules

- The Bucket name cannot be longer than 40 bytes.
- The Bucket name can only be a combination of lowercase letters and numbers.
- The Bucket name cannot contain symbols and underscores.

The following examples are valid Bucket names:

`mynewbucket`
`newproject1`

## Folders and Objects in a Bucket
Unlike the file system of computers, COS does not provide a tree index structure, which is one of the reasons why COS can support high concurrent requests. But users can still use COS to create folders. COS will request a logical index relation by using an address representing a folder structure, but in fact it does not have any physical hierarchical structure. For example, there are three files or folders in a Bucket root directory: a file `test.jpg`, a folder `photos/2015`, and a folder `photos/2016`, and there is a picture named `Me.jpg` in the `photos/2016` folder.

Tencent Cloud COS will build relative paths like `/test.jpg` and `/photos/2016/me.jpg` to make object requests.

To cater to users' viewing habits, in the COS console, the index structure will be displayed in a folder-like hierarchy.



