**Reporting methods**
For more information on how to report logs to the server (only data of "custom event" type are supported), please see [Create Messages](#.E6.9E.84.E5.BB.BA.E6.8A.A5.E6.96.87) below.
>Note:
>Only reporting API of HTTP protocol is supported. For more information, please see [Report to MTA](#.E4.B8.8A.E6.8A.A5.E5.88.B0mta) below.

## Creating Messages
Create a log in JSON format, which can contain the fields in the following table. All the fields marked with Required must be reported, otherwise the log will be invalid.

Multiple logs can be reported in the form of JSON array, and a single log must be marked with "[...]". It is recommended to report multiple logs simultaneously so as to improve the transmission efficiency.

| Field ID	 | Description | 	Required | 	Example |
| :---: |----| :--: |
| ky	 | (System field) APPKEY assigned by MTA	 | Yes | "if8888mta" |
| ts	 | (System field) Current UNIX timestamp	 | Yes	 | 1512057600 |
| et	 | (System field) Log type	 | Yes (fill in 1000)	 | 1000 |
| cui	 | Account ID	 | Yes	 | "13823965426" |
| ei	 | Event ID	 | Yes | 	"\__LOAN\__bind_card" |
| kv	 | Event parameters (JSON format)	 | No	 | {"status": 1, "product_id": "1000234"} |

### Message Example
```
[
  {
    "ky": "if8888mta",
    "ts": 1512057600,
    "et": 1000,
    "cui": "13823965426",
    "ei": "__LOAN__bind_card",
    "kv": {"status": 1, "product_id": "1000234"}
  }, {
    "ky": "if8888mta",
    "ts": 1512057600,
    "et": 1000,
    "cui": "13823965426",
    "ei": "__LOAN__card_confirm",
    "kv": {"product_id": "1000234"}
  }
]
```

## Reporting to MTA
**API type:** HTTP POST

**Supported encoding:** UTF-8

**Reporting example**
```
curl -d '[{"ky": "if8888mta","ts": 1512057600,"et": 1000,"cui":
 "13823965426","ei": "__LOAN__bind_card","kv": {"status": 1, "product_id": 
"1000234"}}]' http://pingma.qq.com/mstat/submit
```

## Description of Events and Parameters
>Note:
>Please report a log based on the event ID and parameter ID provided below according to [Reporting Code Examples](#.E4.BA.8B.E4.BB.B6id.2F.E5.8F.82.E6.95.B0id.E7.A4.BA.E4.BE.8B), otherwise the log is invalid.

### Event ID/Parameter ID Examples
*Only part of examples are shown below. To view all examples, please [download](http://mta.qq.com/mta/resource/download/MTA_loan_introduction.xlsx).*    

| Funnel	 | Event Name	 | Event ID | 	Required | 	Reporting Time	 | Event Parameter ID	 | Parameter Description	 | Required	 | Data Metric |
|---|---|---|---|---|------|----|----|
| Funnel | 	Product | 	\__LOAN\__product	 | Yes	 | Report the ID of loan product every day | 	product_id | 	Product ID	 | Yes | 	Product dimension |
| Credit funnel	 | User registration	 | \__LOAN\__register	 | Yes	 | Report once after the user registration is completed. | 	status | 	Registration status | 	Yes | 	Successful registration |
| Credit funnel	 | Click the Application Limit	 | \__LOAN\__apply_edu | 	Yes | 	Report once when the user clicks the Application Limit button.	 | product_id	 | Product ID	 | No	 | Application limit |
| Credit funnel | 	Fill in verification materials | 	\__LOAN\__fill_info	 | Yes	 | Report once when the user starts to fill in the verification materials for the limit application. |	 product_id	 | Product ID | 	No | 	Credit verification |
| Credit funnel | 	Submit the limit | \__LOAN\__submit | 	Yes | 	Report once when the user clicks "Submit application for review" button.	 | product_id | 	Product ID | 	No	 | Limit review |

### Sample Codes
*Only part of examples are shown below. To view all examples, please [download](http://mta.qq.com/mta/resource/download/MTA-loan-code-sample.pdf).*

**Example 1**
Event Name & ID: User Registration\__LOAN\__register (Required)

- Reporting Time: Report once after the user registration is completed.

| Field	 | Description | 	Required | 	Code Example | 	Function |
|--|----|--|---|
| status | 	Registration status | 	Yes | 	"status":1 | 	Filter (1: "Successful"; 0: "Failed")
- Report: Credit analysis/Funnel analysis
- Name: Successful registration
- Output Dimension: None
- - Output Metric
- -  - Number of users: Remove user account duplicates.

**Example 2**
Event Name & ID: Click Application Limit\__LOAN\__apply_edu (Required)

- Reporting time: Report once when starting to apply for the limit.

| Field	 | Description | 	Required | 	Code Example | 	Function |
|--|----|--|---|
| product_id | 	Product ID | 	No | 	"product_id":"10000100" | 	Dimension |
- Report: Credit analysis/Funnel analysis
- Name: Application limit
- Output Dimension: None
- - Output Metric:
- - - Number of users: Remove user account duplicates.

## Message Returned by API
The message is returned in JSON format with two fields, ret and msg.
- ret field: 0 indicates that the reporting is received successfully, and other values indicate failed reception.
- msg field: In case of failed reception, the reason (such as invalid appkey) is stored in this field.
Error code description

| Error Code	 | Description |
|---|---|
| invalid appkey	 | Incorrect appkey |
| Json parse error	 | Json parse error |
| Gzip error | 	Gzip decompression fails. |
Successful reception does not mean that the log has been processed successfully. If any required field in [Event Parameter Description]() is missing, the log may still be invalid.

After the reporting is received successfully, you can view the loan analysis the next day.

