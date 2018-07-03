## Example 1 Renew Cloud Disk for One Month and Set Auto Renewal Flag

### Request parameters

```
https://cbs.tencentcloudapi.com/?Action=RenewDisk
&DiskId=disk-jwk0zvrg
&DiskChargePrepaid.Period=1
&DiskChargePrepaid.RenewFlag=NOTIFY_AND_AUTO_RENEW
&<Common request parameters>
```
### Return parameters

```
{
  "Response": {
    "RequestId": "6e2e5089-244a-4102-d347-5a1f8058b1db"
  }
}
```

## Example 2 When renewing an instance, you need to renew the mounted prepaid cloud disk to make its expiration time the same as that of the instance.

### Scenario description

The current expiration time of the instance is: 2018-03-30 20:15:03, which needs to be renewed for one month. You can call this API to renew the prepaid cloud disk mounted on the instance to make its expiration time the same as that of the instance and enable the auto renewal for the cloud disk.

                
### Request parameters

```
https://cbs.tencentcloudapi.com/?Action=RenewDisk
&DiskId=disk-jwk0zvrg
&DiskChargePrepaid.Period=1
&DiskChargePrepaid.CurInstanceDeadline=2018-03-30 20:15:03
&DiskChargePrepaid.RenewFlag=NOTIFY_AND_AUTO_RENEW
&<Common request parameters>
```
### Return parameters

```
{
  "Response": {
    "DiskPrice": {
      "DiscountPrice": 9.0,
      "OriginalPrice": 9.0
    },
    "RequestId": "55db49cf-b9d7-da27-825b-5a02ba6884ca"
  }
}
```


        
