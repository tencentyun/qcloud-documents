API for prediction and query of exceptional behaviors can be called to facilitate signature authentication and API integration, and can also help users provide different types of data feedback for different industries.
## Common Parameters and APIs
### Common Request Parameters for APIs
**Common parameters (required)**

| Parameter Name | Type | Description | 
| :---: | :-----: | :----: |
| appkey | String | Identity at business side | 
| timestamp | String | UNIX timestamp when a request is sent from business side | 
| random | String | Random number used to identify the current request | 
| userid | String | User ID at business side | 
| mobile | Ulong | Mobile number | 
| signature | String | Request signature, which is used to check the validity of current request | 

Steps for signature generation:
1. Tencent provides the encryption algorithm, and assigns a dynamic encryption code to the business side.
2. Business side assembles common data, generates a ciphertext using dynamic encryption code and encryption algorithm, and then use the ciphertext to generate an MD5 value as the request signature.
### API for Querying Exception Score
**API Description**
API: http://fbi.qq.com/api/ask/score
Call: POST
Description: This API is used to obtain the risk score and the cause of risk after business side submits the information of applicants.

**Input parameters**
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called.

**Basic information (required)**

| Parameter Name | Type | Description | 
| :---:          | :-----:      | :----                                       | 
| os | String | Data channel:&nbsp;0: Unknown <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1: iOS<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2: Android<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3: H5 | 
| device | String | UNIX timestamp when a request is sent from business side | 
| random | String | Random number used to identify the current request | 
| userid | String | User ID at business side | 
| mobile | Ulong | Mobile number | 
| signature | String | Request signature, which is used to check the validity of current request | 
**Extended information**

| Parameter Name | Type | Description | 
| :---: | :-----: | :----:|
| industry | String | Industry | 
| company | String | Company name | 
| job | String | Occupation | 
| address_company | String | Company address | 
| emailAddress | String | Email address | 
| QQ | String | QQ number | 
| WX | String | WeChat number |
**Output information**

| Parameter Name | Type | Description | 
| :---: | :-----: | :----:|
| code | Uint | Code returned by API. 0: Successful; others: Error code | 
| desc | String | Error code description. 0: Successful; others: Error description | 
| flowid | String | ID of the application returned by server. It is valid only when code=0. | 
| score | Uint | Predicted exception score (in ten thousand) | 
| scoreDesc | String | Description of exception factor (separate multiple factors with semicolon ";") |
**Recommended risk responses**

| Risk Level | Score Range | Suggestion | 
| :---: | :-----: | :----:|
| High risk | [8000,10000] | High exception score. It is recommended to reject. | 
| Medium risk | [4000,8000] | Control according to business metrics | 
| Low risk | [1,4000] | Control according to business metrics | 
**Example**
1. Request example
```
http://fbi.qq.com/api/ask/score?appkey=22b608f45b291a5d2decc5fdbdf80d37180620f8bef122ee880bfce93e1db9e3&
timestamp=13252352352&random=2352352&signature=4a9c5689036bdfc304613f528dc6aba9&mobile=1321852512&userid
=23532523&idcard=532131987558651425&banknos=621412414141141;621412414141142&contacts=13221877657;17133655920
```
2. Response example
```
{"scoreDesc":"201","score":2614,"flowid":"de8eefd5b88b43fc877f4b1fa201bdf1","code":0,"desc":"success"}
```
## Financial Network Lending
### Synchronization of Authorization Data
**API Description**
API: http://fbi.qq.com/api/data/synch
Call: POST
Description: This API is used to sync the data authorized by users and collected by customers to the FBI platform.
Timeliness: The accuracy can be significantly improved with the help of correlation exception analysis. It is recommended that the business side syncs data immediately after being authorized to pull data.

**Input parameters**
Sync data (if any)

| Parameter Name | Type | Description | Attribute Value |
| :----:    | :----: | :----: | :---- |
| processTime | Ulong | Timestamp of pull authorization (in sec) | |
| phoneList | String | List of phone contacts | Nickname (n); Mobile number (m) |
| callLIst | String | Call list | Nickname (n); Mobile number (m); Time (t, format: yyyyMMddHHmmSS) |
| msgReceList | String | List of received SMS messages | Nickname (n); Mobile number (m); Time (t, format: yyyyMMddHHmmSS); Content (c) |
| msgSendList | String | List of delivered SMS messages | Nickname (n), Mobile number (m), Time (t, format: yyyyMMddHHmmSS), Content (c) |
| socialSecurityList | String | List of social security records | Payment time (t, format: yyyyMMdd); Total social security contributions (j, in CNY) |
| publicFundList | String | List of housing provident fund records | Payment time (t, format: yyyyMMdd); Total housing provident fund contributions (j, in CNY) |
| creditBillList | String | List of credit card bills | Repayment date (t1, format: yyyyMMdd); Actual repayment time (t2, format: yyyyMMddHHmmSS, and leave it empty for unpaid bills); Bill amount (j, in CNY) |

**Output parameters**

| Parameter Name | Type | Description |
| :----: | :----: | :-----: |
| code | Uint | Code returned by API. 0: Successful; others: Error code |
| desc | String | Error code description. 0: Successful; others: Error description | 

**Example**
1. Request example
```
fbi.qq.com/api/data/synch?appkey=84c8292358be3614afc35525a09f4b55180620f8bef122ee880bfce93e1db9e3&timestamp=1513688850127&random=111&signature=4dd558d888aa5f2d056e5ada4e697496&mobile=13580211212&userid=1530728&phoneList=[{"n":"John","m":"15611111111"},{"n":"Mike","m":"15611111112"}]&creditBillList=[{"t1":"20171123","j":"2602.50","t2":"20171120"},{"t1":"20171223","j":"3000.21"}]
```
2. Response example
```
{"code":0,"desc":"success"}
```

### Feedback on Lending Process
**API Description**
API: http://fbi.qq.com/api/feedback/process
Call: POST
Description: After calling the 3.2 API for risk query, the business side processes loan applications based on its own risk control policies, such as approval or rejection. This API is used to provide feedback on the process result as a control source of business feedback and subsequent credit.
Timeliness: Real-time synchronization is recommended. Delay synchronization must be performed within t+1 (the data of the previous day must be synced by 5 am of the day at latest).
>Note: <br>If the lending feedback for users who request to query score is not received within t+1, the API for querying score will be disabled officially.

**Input parameters**
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called.

| Parameter Name | Type | Description |
| :----:    | :----: | :--|
| flowid | String | ID of the application submitted at business side, which is returned by the API for querying exception score. |
| resultType | Unit | Business processing status: &nbsp;1. Reject loan<br> &nbsp;&nbsp;&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Approve loan<br> &nbsp;&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&ensp;&nbsp;&nbsp;3. Reject first credit<br> &nbsp;&nbsp;&nbsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. Approve first credit<br> &nbsp;&nbsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&emsp;&nbsp;&nbsp;&nbsp;&nbsp;5. Reject increase of credit limit<br> &nbsp;&nbsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;&nbsp;&emsp;&emsp;&nbsp;6. Approve increase of credit limit<br> &nbsp;&nbsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;&nbsp;&emsp;&emsp;&emsp;&nbsp;7. System underclocking<br> &nbsp;&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8. User cancels loan<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;(Including the scenario where user cannot receive loans) |
| processTime | Ulong | Timestamp of business processing (in sec) | 
| money | Uint | Amount (in CNY), i.e. loan amount, or first credit line, increased credit limit, amount after underclocking | 
| stages | Uint | Number of installments. 1: Non-installment products. For statuses other than "Approve loan", leave it empty. | 
| repaymentTimes | String | Repayment schedule (array). 1: Non-installment products. For statuses other than "Approve loan", leave it empty. | 
| reason | String | Reason for rejection and notes. For statuses other than "Approve loan", leave it empty. | 

**Output parameters**

| Parameter Name | Type | Description | Attribute Value |
| :----:    | :----: | :----: | :---- |
| processTime | Ulong | Timestamp of pull authorization (in sec) | |
| phoneList | String | List of phone contacts | Nickname (n); Mobile number (m) |
| callLIst | String | Call list | Nickname (n); Mobile number (m); Time (t, format: yyyyMMddHHmmSS) |
| msgReceList | String | List of received SMS messages | Nickname (n); Mobile number (m); Time (t, format: yyyyMMddHHmmSS); Content (c) |

**Output parameters**

| Parameter Name | Type | Description |
| :----:    | :----: | :----: | 
| code | Uint | Code returned by API. 0: Successful; others: Error code | 
| desc | String | Error code description. 0: Successful; others: Error description |
**Example**
1. Request example:
```
http://fbi.qq.com/api/feedback/process?appkey=22b608f45b291a5d2decc5fdbdf80d37180620f8bef122ee880bfce93e1
db9e3&timestamp=13252352352&random=2352352&signature=4a9c5689036bdfc304613f528dc6aba9&flowid=096daf24ba75
44b8b738059367678cf4&userid=23532523&resultType=2&processTime=13252352362&money=700&stages=3&repaymentTim
es=[20171101;20171201;20180101]
```

2. Response example:
```
{"code":0,"desc":"success"}
```

### Feedback on Repayment Result
**API Description**
API: http://fbi.qq.com/api/feedback/effect
Call: POST
Description: This API is used to provide feedback at the time of repayment or in subsequent determination steps for lending users.
Timeliness: Real-time synchronization is recommended. Delay synchronization must be performed within t+1 (the data of the previous day must be synced by 5 am of the day at latest).

>Note: <br>If the repayment feedback for users who request to query score is not received within t+1, the API for querying score will be disabled officially.

**Input parameters**
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called.

| Parameter Name | Type | Description |
| :----:    | :----: | :--:|
| flowid | String | ID of the application submitted at business side, which is returned by the API for risk query. |
| stageId | Uint | Number of installments. 1: Non-installment products |
| resultType | Uint | Business processing status; 1. Due payment; 2. M1 overdue (outstanding for more than 30 days); 3. M3 fraud (outstanding for more than 90 days); 4. Overdue payment; 5. Due and outstanding | 
| processTime | Ulong | Business processing time (in sec) | 
> Notes:
>1. Installment indicates that the status of repayment for each installment should be synced. This API is called multiple times if bills for multiple installments remain unpaid. 
>2. Overdue indicates that if a user's bill is due and outstanding, the status "5. Due and outstanding" should be synced to the user on a daily basis until the status is changed to 2, 3 or 4.
>3. Fraud indicates that if a user is in M1 overdue status and the bill remains outstanding for more than 90 days, then feedback is provided on the "91st day after due date".

**Output parameters**

| Parameter Name | Type | Description |
| :----:    | :----: | :----: | 
| code | Uint | Code returned by API. 0: Successful; others: Error code | 
| desc | String | Error code description. 0: Successful; others: Error description |
**Example**
1. Request example:
```
http://fbi.qq.com/api/feedback/effect?appkey=22b608f45b291a5d2decc5fdbdf80d37180620f8bef122ee880bfce93e1db9e3
&timestamp=13252352352&random=2352352&signature=4a9c5689036bdfc304613f528dc6aba9&flowid=096daf24ba7544b8b7380
59367678cf4&userid=23532523&resultType=1&processTime=13252352372&stageId=1
```

2. Response example:
```
{"code":0,"desc":"success"}
```


