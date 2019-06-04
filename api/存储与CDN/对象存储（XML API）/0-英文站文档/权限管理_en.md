## Overview

COS permission architecture depends on CAM (Tencent Cloud permission system), which keeps all permission records of all Cloud Services. Each permission record consists of 4 sections: `User`, `Action`, `Condition`, `Resource`. The record defines "who can perform what kind of actions towards which resources under what conditions". Permission record is designed to describe whether a specific action meets permission requirement.

The information of `Resource` is indicated by the standard QCS method of CAM

`qcs: project:serviceType:region:account:resource`

`qcs: project: service: region: user ID: resource ID`

The figure shows one permission record in the permission system. Details of each section of the record will be described below

```JSON
{    
    "version":"2.0",
    "principal":   {"qcs":["qcs::cam::uin/<RootAccout>:uin/<SubAccount>","qcs::cam::uin/<RootAccout>:uin/<SubAccount>"]},
    "statement":
    [
       {
            "effect":"allow",        
            "action":["name/cos:<ActionName>"],
            "resource":["qcs::cos:<Region>:uid/<Accout>:prefix//<uid>/<BucketName>/<ObjectName>",
                      "qcs::cos:<Region>:uid/<Accout>:prefix//<uid>/<BucketName>/[dir1]/*"],
        }
    ]
}
```

## User

### Definition

The principal field is used to indicate the authorized target of this permission information. The user can be a sub-account, a master account or a user group. Once authorized, the user (including sub-accounts) may use **his/her own AccessKey and SercetKey** to generate a signature to access own resources or others' resources.

### Syntax

Account information can be considered as a CAM resource. In practice, we leave project and region fields empty, and get the following simple expression

Master account syntax:`qcs::cam::uin/<RootAccout>:uin/<RootAccount>`

Sub-account syntax:`qcs::cam::uin/<RootAccout>:uin/<SubAccount>`

### Example

Master account 398626565

qcs::cam::uin/398626565:uin/398626565

Sub-account 1241534935 whose master account is 398626565

qcs::cam::uin/398626565:uin/1241534935

## Resource

### Definition

The resource field is used to indicate the scope of resources authorized by this permission information. Resource can be a specific file or a Bucket. Prefix matching is supported.

### Syntax

Indication of Tencent Cloud Resource

`qcs: project:serviceType:region:account:resource`

`qcs: project: service: region: user ID: resource ID`

In which, default project is id/0; service is cos; region field is filled in based on situation, e.g. ce (china-east); user ID is used to indicate the parent dimension (appid/ID) of the resource; resource is used to indicate the child dimension (Bucket/Object) of the resource.

### Example

`bucketname-125102314.cossh.myqcloud.com` of Shanghai COS 4.0

qcs:id/0:cos:ce:uid/125102314:prefix//125102314/bucketname/

`testbucket-125102315.cosgz.myqcloud.com/foldertest/file.txt` of Guangzhou COS 4.0

qcs:id/0:cos:ce:uid/125102315:prefix//125102315/testbucket/foldertest/file.txt

## Action

### Definition

The action field is used to indicate which actions are authorized by this permission information. The action can be an independent action or a group of actions.

### Syntax

`cos: API name`

APIs are named using camel-case method

### Example

Get Bucket API

`cos:GetBucket`

## Condition (coming soon)

### Definition

The condition field is used to indicate the conditions under which this permission information can be performed. condition consists of operator, condition name and condition value.

### Syntax

`"condition operator": {"condition name": ["condition value", "condition value"]}`

| Condition Operator                   | Description     | Condition Name                    | Example                                       |
| ----------------------- | ------ | ---------------------- | ---------------------------------------- |
| ip_equal                | ip is equal to   | ip, which should conform to CIDR Standard         | {" ip_equal  ":{"ip":"10.121.2.10/24"}}  |
| ip_not_equal            | ip is not equal to  | ip, which should conform to CIDR Standard         | {" ip_not_equal  ":{"ip":["10.121.2.10/24",  "10.121.2.20/24"]}} |
| date_not_equal          | date is not equal to  | qcs:current_time (current time) | {"date_not_equal":{"qcs:current_time":"2016-06-01  00:01:00"}} |
| date_greater_than       | date is greater than   | qcs:current_time (current time) | {" date_greater_than  ":{"qcs:current_time":"2016-06-01 00:01:00"}} |
| date_greater_than_equal | date is greater than or equal to | qcs:current_time (current time) | {"  date_greater_than_equal ":{"qcs:current_time":"2016-06-01  00:01:00"}} |
| date_less_than          | date is less than   | qcs:current_time (current time) | {" date_less_than  ":{"qcs:current_time":"2016-06-01 00:01:00"}} |
| date_less_than_equal    | date is less than or equal to | qcs:current_time (current time) | {"  date_less_than_equal ":{"qcs:current_time":"2016-06-01  00:01:00"}} |

### Example

Request IP must be 10.121.2.10/24

{" ip_equal  ":{"ip":"10.121.2.10/24"}}

## ACL

### Definition

ACL is a set of pre-defined permissions, that is, one or more of the four conditions (`User`, `Action`, `Condition`, `Resource`) have been determined.

### Syntax

[x-cos-acl]: Define the ACL attribute of the Bucket. Valid values: private, public-read. Default value: private

[x-cos-grant-read]: Grant read permission to the authorized user. Format: x-cos-grant-read:  uin=" ",uin=" "
When you need to authorize a sub-account, uin="RootAcountID/SubAccountID"; when you need to authorize the root account, uin="RootAcountID"

[x-cos-grant-write]: Grant write permission to the authorized user. Format: x-cos-grant-write:  uin=" ",uin=" "
When you need to authorize a sub-account, uin="RootAcountID/SubAccountID"; when you need to authorize the root account, uin="RootAcountID"

[x-cos-grant-full-control]: Grant read and write permissions to the authorized user. Format: x-cos-grant-full-control:  uin=" ",uin=" "
When you need to authorize a sub-account, uin="RootAcountID/SubAccountID"; when you need to authorize the root account, uin="RootAcountID"

### Example

x-cos-acl：public-read

| User   | Resource               | Action                   | Condition   |
| ---- | ---------------- | -------------------- | ---- |
| All accounts  | The Bucket or the Object | Read permission group (including all Get/Head APIs) | Unconditional  |

x-cos-grant-write:uin="1241534935/1241534935"

| User                 | Resource               | Action                     | Condition   |
| ----------------- | ---------------- | ---------------------- | ---- |
| Master account (1241534935) | The Bucket or the Object | Write permission group (including all Put/Delete APIs) | Unconditional  |

## Example

```JSON
{
  "version":"2.0"
  "principal":{"qcs":["qcs::cam::uin/909619481:uin/909619481"]},
  "statement":[
   {"action":["name/cos:GetBucket"],
    "effect":"allow",
    "resource":["qcs:id/0:cos:sg:uid/1251668577:prefix//1251668577/arlenhuangtestsgnoversion/*"]
   }
  ]
}
```

Unconditional, the master account `909619481` has `GetBucket` permission to all resources with the prefix of `1251668577/arlenhuangtestsgnoversion/`

