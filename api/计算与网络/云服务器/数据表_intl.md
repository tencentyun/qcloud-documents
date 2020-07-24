### INSTANCE_STATE

> The entire life cycle of an instance.

| ID | Description |
|---------|---------|
| PENDING | Preparing |
| RUNNING | Running |
| STOPPED | Stopped |
| REBOOTING | Restarting |
| STARTING | Starting |
| STOPPING | Stopping |


### REGION

> List of regions

| ID | Description |
|---------|---------|
| ap-guangzhou | Guangzhou |
| ap-shanghai | Shanghai |
| ap-hongkong | Hong Kong (China) |
| na-toronto | North America |
| ap-shanghai-fsi | Shanghai Finance |
| ap-beijing | Beijing |
| ap-singapore | Singapore |
| ap-shenzhen-fsi | Shenzhen Finance |
| ap-guangzhou-open | Guangzhou Open |
| ap-seoul| Seoul |
| ap-singapore| Singapore |
| eu-frankfurt| Frankfurt |
| na-siliconvalley| Silicon Valley |
| na-toronto| Toronto |


### ZONE

> List of availability zones

| ID | Description |
|---------|---------|
| ap-guangzhou-1 | Guangzhou Zone 1 |
| ap-guangzhou-2 | Guangzhou Zone 2 |
| ap-guangzhou-3 | Guangzhou Zone 3 |
| ap-guangzhou-4 | Guangzhou Zone 4 |
| ap-shanghai-1 | Shanghai Zone 1 |
| ap-shanghai-2 | Shanghai Zone 2 |
| ap-hongkong-1 | Hong Kong Zone 1 |
| ap-beijing-1 | Beijing Zone 1 |
| ap-beijing-2 | Beijing Zone 2 |
| ap-shanghai-fsi-1 | Shanghai Finance Zone 1 |
| ap-shanghai-fsi-2 | Shanghai Finance Zone 2 |
| ap-chengdu-1| Chengdu Zone 1 |
| ap-chengdu-2| Chengdu Zone 2 |
| ap-shenzhen-fsi-1 | Shenzhen Finance Zone 1 |
| ap-shenzhen-fsi-2 | Shenzhen Finance Zone 2 |
| ap-guangzhou-open-1 | Guangzhou Open Zone |
| ap-seoul-1| Seoul Zone 1 |
| ap-singapore-1| Singapore Zone 1 |
| eu-frankfurt-1| Frankfurt Zone 1 |
| na-siliconvalley-1| Silicon Valley Zone 1 |
| na-toronto-1| Toronto Zone 1 |


### BLOCK_DEVICE

> Disk types

| ID | Description |
|---------|---------|
| LOCAL_BASIC | Local HDD |
| LOCAL_SSD | Local SSD |
| CLOUD_BASIC | HDD cloud disk |
| CLOUD_PREMIUM | Premium cloud disk |
| CLOUD_SSD | SSD cloud disk |


### AUTO_RENEW

> The method of auto renewal

| ID | Description |
|---------|---------|
| NOTIFY_AND_MANUAL_RENEW | Notify without auto renewal (notify expiry but not renew automatically)
| NOTIFY_AND_AUTO_RENEW | Notify with auto renewal (notify expiry and renew automatically)
| DISABLE_NOTIFY_AND_MANUAL_RENEW | No notification or auto renewal (neither notify expiry nor renew automatically)


### INSTANCE_PAID

> The billing method of an instance

| ID | Description |
|---------|---------|
| POSTPAID_BY_HOUR | Postpaid |
| CDHPAID| Charge only the CDH but not the instances on it |


### NETWORK_PAID

> Network billing method

| ID | Description |
|---------|---------|
| BANDWIDTH_POSTPAID_BY_MONTH | Postpaid on a monthly basis |
| TRAFFIC_POSTPAID_BY_HOUR | Bill by traffic |
| BANDWIDTH_POSTPAID_BY_HOUR | Bill by bandwidth usage time |
| BANDWIDTH_PACKAGE| Bill by bandwidth package |


### IMAGE_SOURCE

> Image source

| ID | Description |
|---------|---------|
| OFFICIAL | Images from Tencent Cloud.
| IMAGE_CREATE | Images generated from official images by means of creating instance images. |
| EXTERNAL_IMPORT | Images generated from images imported from external resources. |



### ZONE_STATE

> Availability zone status

| ID | Description |
|---------|---------|
| AVAILABLE | Available |
| UNAVAILABLE | Unavailable |


### IMAGE_TYPE

> Image type

| ID | Description |
|---------|---------|
| PRIVATE_IMAGE | Private images (images created by current account) 
| PUBLIC_IMAGE | Public images (images from Tencent Cloud)
| MARKET_IMAGE | Service marketplace images (images provided by service marketplace) 
| SHARED_IMAGE | Shared images (images shared by other accounts to current account)


### IMAGE_STATE

> Image status

| ID | Description |
|---------|--------|
| CREATING | Creating
| NORMAL | Normal
| USING | Using
| SYNCING | Syncing
| IMPORTING | Importing
| DELETING | Deleting


### EIP_STATE

> EIP status

| ID | Description |
|---------|--------|
| CREATING | Creating
| BINDING | Binding
| BIND | Bound
| UNBINDING | Unbinding
| UNBIND | Unbound
| OFFLINING | Deactivating
| CREATE_FAILED | Creation failed
| BIND_ENI | Bound to ENI which is not mounted to an instance

