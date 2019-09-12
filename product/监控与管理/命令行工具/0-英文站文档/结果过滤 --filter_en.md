Some command lines return a large amount of information (such as all instance lists) with a complex structure that contains not only the key information you want to get. In this case, you can use the basic command filter to help you only retain the key information.

The following takes DescribeAvailabilityZones as an example to show how to use filter. Region is set to South China (Guangzhou). This API is used to view all availability zones under the region.

## 1. Output not filtered

```
qcloudcli cvm DescribeAvailabilityZones

{
    "codeDesc": "Success",
    "totalCount": 4,
    "message": "",
    "code": 0,
    "zoneSet": [
        {
            "zoneId": 100001,
            "idcList": [
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                }
            ],
            "zoneName": "Guangzhou Zone 1"
        },
        {
            "zoneId": 100002,
            "idcList": [
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                }
            ],
            "zoneName": "Guangzhou Zone 2"
        },
        {
            "zoneId": 100003,
            "idcList": [
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                }
            ],
            "zoneName": "Guangzhou Zone 3"
        },
        {
            "zoneId": 100004,
            "idcList": [
                {
                    "idcId": "",
                    "idcName": ""
                }
            ],
            "zoneName": "Guangzhou Zone 4"
        }
    ]
}
```
## 2. Viewing only one field

Take viewing the field totalCount (the number of availability zones in the current region) as an example:

```
qcloudcli cvm DescribeAvailabilityZones --filter totalCount

4

```

You can see the field value by adding the name of the field to be retained after `--filter`.

## 3. Specifying the information of a sub-object under a certain object in array type

Take viewing the first sub-object in the availability zone information list as an example:

```
qcloudcli cvm DescribeAvailabilityZones --filter zoneSet[0]

{
    "zoneId": 100001,
    "idcList": [
        {
            "idcId": "",
            "idcName": ""
        },
        {
            "idcId": "",
            "idcName": ""
        },
        {
            "idcId": "",
            "idcName": ""
        },
        {
            "idcId": "",
            "idcName": ""
        },
        {
            "idcId": "",
            "idcName": ""
        },
        {
            "idcId": "",
            "idcName": ""
        },
        {
            "idcId": "",
            "idcName": ""
        }
    ],
    "zoneName": "Guangzhou Zone 1"
}

```
Only Guangzhou Zone 1 information is displayed after filtering.

## 4. Specifying a field of all sub-objects with a certain name under an object in array type

Take viewing the value of zoneName in all availability zone information lists as an example:

```
qcloudcli cvm DescribeAvailabilityZones --filter zoneSet[*].zoneName

[
    "Guangzhou Zone 1",
    "Guangzhou Zone 2",
    "Guangzhou Zone 3",
    "Guangzhou Zone 4"
]

```
Only zoneName information is displayed after filtering.

## 5. Filtering the sub-objects in an array and displaying them with a new name

This operation is more complex than other supported ones. It allows you to rename the results and use them for coding and other format-demanding scenarios. You are advised to save the edited command line to local for later use.

``Note: You need to enclose the filtering criteria in single quotes.``

```
qcloudcli cvm DescribeAvailabilityZones --filter 'zoneSet[*].{name:zoneName, id:zoneId}'

[
    {
        "name": "Guangzhou Zone 1",
        "id": 100001
    },
    {
        "name": "Guangzhou Zone 2",
        "id": 100002
    },
    {
        "name": "Guangzhou Zone 3",
        "id": 100003
    },
    {
        "name": "Guangzhou Zone 4",
        "id": 100004
    }
]

```

Filter out all the sub-objects with zoneName and zoneId from the original availability zone list and display them with a new name and ID.


