## Introduction to Container Image Service Permissions

The description format of Tencent Cloud container image is as follows: `ccr.ccs.tencentyun.com/${namespace}/${name}:${tag}`.
The permissions for image registry are configured based on the following two fields:
* `$ {namespace}`: The namespace to which the image belongs;
* `$ {name}`: Name of image.

>**Note:**
>No slash (/) is allowed in the namespace `${namespace}` and image name `${name}`;  
>Only authentication for deletion operation is supported now for `${tag}`. For more information, please see [Permissions for Image Tag](#镜像Tag权限).

With the fields `${namespace}` and `${name}`, developers can develop a detailed permission scheme for collaborators for a flexible permission management.  
For example:
* Permit Collaborator A to pull images;
* Forbid Collaborator A from deleting images;
* Forbid Collaborator B from pulling the images in the namespace ns1.
* ...


If you do not need to manage the permissions for image registry in detail, please use [Authorization by Preset Policies](#预设策略授权).

To manage the permissions of collaborators in detail, please use [Authorization by Custom Policies](#自定义策略授权).

The permissions for container image service are managed based on Tencent Cloud CAM. For more information on how to use CAM, please see:
[User Management](https://cloud.tencent.com/document/product/598/10598),
[Policy Management](https://cloud.tencent.com/document/product/598/10601),
[Authorization Management](https://cloud.tencent.com/document/product/598/10602).

## Authorization by Preset Policies

Container image service has two preset policies to simplify the management of permissions:

* [Full read-write access permissions for image registry (CCR) ](https://console.cloud.tencent.com/cam/policy/detail/419082&QcloudCCRFullAccess&2)

    All permissions for the container image service are configured under this preset policy. A collaborator associated with this preset policy has the same image registry permissions as developers. For more information, please see [Permission List](#权限列表).

* [Read-only access permission for image registry (CCR)](https://console.cloud.tencent.com/cam/policy/detail/419084&QcloudCCRReadOnlyAccess&2)

    This preset policy contains the read-only permission for the container image service. Any collaborator who is **ONLY** associated with this preset policy in the container image service is forbidden from performing the following operations:
    * Push images with `docker push`
    * Create namespace for image registry
    * Delete namespace of image registry
    * Create image registry
    * Delete image registry
    * Delete image tag

For more information on how to associate a collaborator with preset policies, please see the CAM documentation: [Overview of Preset Policies](https://cloud.tencent.com/document/product/598/10601#.E9.A2.84.E8.AE.BE.E7.AD.96.E7.95.A5) and [Associate Users with Preset Policies](https://cloud.tencent.com/document/product/598/10602#.E9.A2.84.E8.AE.BE.E7.AD.96.E7.95.A5.E5.85.B3.E8.81.94.E7.94.A8.E6.88.B7).

## Authorization by Custom Policies

With the custom policies, developers can associate different collaborators with different permissions.

When you assign permissions, the following should be taken into consideration:

* **Resource**: Which images are associated with this permission policy. For example, all image registries are described as `qcs::ccr:::repo/*`. For more information, please see [CAM Resource Description Method](https://cloud.tencent.com/document/product/598/10606).
* **Action**: What actions can be done on the **resource** under this permission policy, for example, deletion, creation, etc. Generally, they are described by APIs.
* **Effect**: The effect the permission policy has on the collaborator (Allow/Deny).

When you have planned the permission settings, you can assign the permissions. The following example shows how to "permit collaborators to create an image registry":

1. Create a custom policy ([CAM Documentation](https://cloud.tencent.com/document/product/598/10601#.E8.87.AA.E5.AE.9A.E4.B9.89.E7.AD.96.E7.95.A5)).

    * Log in to Tencent Cloud Console with a developer account.
    * Go to [CAM custom policy management page](https://console.cloud.tencent.com/cam/policy/custom), and then click the "New Custom Policy" button to open the "Select Policy Creation Method" dialog box.

        ![Select Policy Creation Method][6]

    * Select "Create by Policy Syntax" option -> "Blank Template".

        ![Select Template][7]

    * Click "Next" button at the bottom of the page to go to "Create by Policy Syntax" -> "Edit Policy".
    * Enter the following contents in the "Edit Policy Content" edit box, and then enter a meaningful name in the "Policy Name", such as `ccr-policy-demo`.

        ```
        {
            "version": "2.0",
            "statement": [{
                "action": "ccr:CreateRepository",
                "resource": "qcs::ccr:::repo/*",
                "effect": "allow"
            }]
        }
        ```

        ![Edit Policy][8]

        _Note: The \* appended to the **end** of resource indicates that an image registry can be created under any namespace_

    * Click the "New Policy" button at the bottom of the page to complete the policy creation.

        ![Edit Policy][9]

2. Associate the custom policy with collaborators. After the policy (`ccr-policy-demo`) in Step 1 is created, you can associate it with any collaborator. For more information, please see [CAM Documentation](https://cloud.tencent.com/document/product/598/10602#.E7.94.A8.E6.88.B7.E5.85.B3.E8.81.94.E8.87.AA.E5.AE.9A.E4.B9.89.E7.AD.96.E7.95.A5). After the association, the associated collaborators have the **permission to create an image registry under any namespace**.


_Format description of resource `qcs::ccr:::repo/*`_:

* `qcs::ccr:::` is a fixed format indicating the developer's Tencent Cloud container image registry service.
* `repo` is a fixed prefix indicating the resource type. In this example, it indicates image registry.
* The `*` following the slash (`/`) indicates matching all the image registries.

For more information on resource, please see [CAM Resource Description Method](https://cloud.tencent.com/document/product/598/10606).

#### Authorization by resource

You can grant authorization for multiple resources at a time. For example, to "permit the deletion of the image registries in namespaces foo and bar", you can create the following custom policies:

```
{
    "version": "2.0",
    "statement": [{
        "action": [
            "ccr:BatchDeleteRepository",
            "ccr:DeleteRepository"
        ],
        "resource": [
            "qcs::ccr:::repo/foo/*",
            "qcs::ccr:::repo/bar/*"
        ]
        "effect": "allow"
    }]
}
```

_ Note: _

* `foo/*` in `qcs::ccr:::repo/foo/*` indicates all the images under the image registry namespace `foo`;

* `bar/*` in `qcs::ccr:::repo/bar/*` indicates all the images under the image registry namespace `bar`.

####  Authorization by action (API)

You can configure multiple `actions` for a resource for a centralized management of resource permissions. For example, to "permit the creation, deletion and push of image registry in the namespace foo", you can create the following custom policies:

```
{
    "version": "2.0",
    "statement": [{
        "action": [
            "ccr:CreateRepository",
            "ccr:BatchDeleteRepository",
            "ccr:DeleteRepository",
            "ccr:push"
        ],
        "resource": "qcs::ccr:::repo/foo/*",
        "effect": "allow"
    }]
}
```

## Permission List

#### docker client permissions

resource: `qcs::ccr:::repo/${namespace}/${name}`  
action:
* `ccr:pull`     pull images with docker command line
* `ccr: push`     push images with docker command line.

#### Namespace permissions

resource: `qcs::ccr:::repo/${namespace}`  
action:
* `ccr: CreateCCRNamespace`     Create an image registry namespace;
* `ccr:DeleteUserNamespace`    Delete an image registry namespace.

Feature path: **CCS** -> **Image Registry** in the left navigation bar -> **My Images** -> **Namespace**
![New | Delete Permissions for image registry namespace][1]


#### Permissions for image registry

resurce: `qcs::ccr:::repo/${namespace}/${name}`[PI1]  
action:
* `ccr:CreateRepository`          Create an image registry
* `ccr:DeleteRepository`         Delete an image registry
* `ccr:BatchDeleteRepository`        Delete image registries in batch
* `ccr:GetUserRepositoryList`   View the list of image registries

Feature path: **CCS** -> **Image Registry** in the left navigation bar -> **My Images** -> **My Creation**
![Permissions for image registry][4]

>**Note:**
>To prevent collaborators from deleting some images, please configure multiple actions.
For example, to forbid the deletion of any image registry:
```
{
    "version": "2.0",
    "statement": [{
        "action": [
            "ccr:BatchDeleteRepository",
            "ccr:DeleteRepository"
        ],
        "resource": "qcs::ccr:::repo/*",
        "effect": "deny"
    }]
}
```

#### Permissions for image tag

resource: `qcs::ccr:::repo/${namespace}/${name}:${tag}`  
action:
* `ccr:DeleteTag`           Delete an image tag

Feature path: **CCS**-> **Image Registry** in the left navigation bar-> **My Images** -> **My Creation** -> Click an image name -> **Image Tag** page
![Permissions for image registry][5]



[1]:https://mc.qcloudimg.com/static/img/1be5647f80dcc50db26cf13ef0e29ce5/1.png
[2]:https://mc.qcloudimg.com/static/img/aec6771c2595210d3e4319e6188aafa9/2.png
[3]:https://mc.qcloudimg.com/static/img/1d7f13366192079ea3c64d70e46f5215/3.png
[4]:https://mc.qcloudimg.com/static/img/99a097e254a9e0e13839d8eaff7b26a8/4.png
[5]:https://mc.qcloudimg.com/static/img/3efec02b8ade10fa5c7778820ebdfec3/6.png
[6]:https://mc.qcloudimg.com/static/img/224dd2cc5dc809c3220d50ba6497a36e/5.png
[7]:https://mc.qcloudimg.com/static/img/daf81fe58cac20aa2c27c65a776288fa/7.png
[8]:https://mc.qcloudimg.com/static/img/fb69dccc77754060b713361034acac18/8.png
[9]:https://mc.qcloudimg.com/static/img/1492b89bdb394490ab5613a1e06b8987/9.png


