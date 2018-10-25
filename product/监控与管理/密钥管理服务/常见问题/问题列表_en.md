## 1. CMK cannot be found

When using a cloud API, the region to which CMK belongs must be the same as the region specified in the API. For a detailed list of regions and access addresses, see [Region](/document/product/573/8922). If no ID key specified for the current region, an error code 10630 is returned.

## 2.HTTPS Restriction

To enhance security, all KMS-related cloud APIs are only accessible over HTTPS. Pay attention to the type of protocol you specified when calling the cloud API in your code.

## 3. Alias Conflict

CMK must have an alias, and the alias in each region must be unique. An error code 10480 is returned when the CMK alias you are trying to modify already exists in the current region.

## 4. Error Codes

For more information, please see [Error Codes](/document/product/573/8919).
