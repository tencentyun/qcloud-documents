## 1. Feature Description  

1. Batch updating of the relationship chain data for multiple friends of a user is supported.
2. It is recommended to update multiple friends of a user in batches to avoid write conflict caused by concurrent writes.

## 2. Description of API Calling 

### 2.1 Request URL 
```
https://console.tim.qq.com/v4/sns/friend_update?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```
### 2.2 Request Parameters 

For more information on the meaning and input method of parameters in URL, please see <a href="https://cloud.tencent.com/document/product/269/1519">REST API Overview</a>. 

### 2.3 Maximum Call Frequency 

100 times/sec. If you need to increase calling frequency, submit a ticket for application according to <a href="https://cloud.tencent.com/document/product/269/3916#2.15-rest-api.E8.B0.83.E7.94.A8.E9.A2.91.E7.8E.87.E8.B0.83.E6.95.B4">Adjustment of REST API Calling Frequency</a>.

### 2.4 HTTP Request Method 

POST 

### 2.5 HTTP Request Packet Format 

JSON 

### 2.6 Example of Request Packet

#### 2.6.1 Basic Format

```
{
    "From_Account":"id",
    "UpdateItem":
    [
        {
            "To_Account":"id1",
            "SnsItem":
            [
                {
                    "Tag":"Tag_SNS_IM_Remark",
                    "Value":"remark1"
                }
            ]
        }
    ]
}

```

#### 2.6.2 Complete Format

```
{
    "From_Account":"id",
    "UpdateItem":
    [
        {
            "To_Account":"id1",
            "SnsItem":
            [
                {
                    "Tag":"Tag_SNS_IM_Remark",
                    "Value":"remark1"
                },
                {
                    "Tag":"Tag_SNS_IM_Group",
                    "Value":"group1"
                },
                {
                    "Tag":"Tag_SNS_Custom_Test",
                    "Value":"test"
                }
            ]
        }
    ]
}
```

#### 2.6.3 Add Friends in Batches

```
{
    "From_Account":"id",
    "UpdateItem":
    [
        {
            "To_Account":"id1",
            "SnsItem":
            [
                {
                    "Tag":"Tag_SNS_IM_Remark",
                    "Value":"remark1"
                }
            ]
        },
        {
            "To_Account":"id2",
            "SnsItem":
            [
                {
                    "Tag":"Tag_SNS_IM_Remark",
                    "Value":"remark2"
                },
                {
                    "Tag":"Tag_SNS_IM_Group",
                    "Value":"group2"
                }
            ]
        },
        {
            "To_Account":"id3",
            "SnsItem":
            [
                {
                    "Tag":"Tag_SNS_IM_Remark",
                    "Value":"remark3"
                },
                {
                    "Tag":"Tag_SNS_IM_Group",
                    "Value":"group3"
                },
                {
                    "Tag":"Tag_SNS_Custom_Test",
                    "Value":"test"
                }
            ]
        }
    ]
}
```

### 2.7 Request Packet Field 

<table style="display:table;width:100%">
	<tbody>
		<tr style="background:#C2D3FC;border:1px solid blue;">
			<td style="width:15%;">Field</td>
			<td style="width:10%;">Type</td>
			<td style="width:10%;">Attribute</td>
			<td style="width:65%;">Description</td>
		</tr>
		<tr>
			<td>From_Account</td>
			<td>String</td>
			<td>Required</td>
			<td>The relationship chain data for this Identifier needs to be updated.</td>
		</tr>
		<tr>
			<td>UpdateItem</td>
			<td>Array</td>
			<td>Required</td>
			<td>The object array of friend that needs to be updated.</td>
		</tr>
		<tr>
			<td>To_Account</td>
			<td>String</td>
			<td>Required</td>
			<td>Friend's Identifier</td>
		</tr>
		<tr>
			<td>SnsItem</td>
			<td>Array</td>
			<td>Required</td>
			<td>The object array of relationship chain data that needs to be updated</a>.</td>
		</tr>
		<tr>
			<td>Tag</td>
			<td>String</td>
			<td>Required</td>
			<td>The name of the relationship chain field that needs to be updated. Users are only allowed to update remark, group and custom fields of relationship chain. For more information on relationship chain field, please see <a href="https://cloud.tencent.com/document/product/269/1501#3-.E5.A5.BD.E5.8F.8B.E8.A1.A8">Friend List</a>.</td>
		</tr>
		<tr>
			<td>Value</td>
			<td>Array/String/Integer</td>
			<td>Required</td>
			<td>For more information on the value and value type of the relationship chain field that needs to be updated, please see <a href="https://cloud.tencent.com/document/product/269/1501#3-.E5.A5.BD.E5.8F.8B.E8.A1.A8">Friend List</a>.</td>
		</tr>
	</tbody>
</table>


### 2.8 Example of Response Packet

#### 2.8.1 Basic Format and Complete Format

```
{
	"ResultItem":
	[
		{
			"To_Account":"id1",
			"ResultCode":0,
			"ResultInfo":""
		}
	],
	"Fail_Account":[],
	"Invalid_Account":[],
	"ActionStatus":"OK",
	"ErrorCode":0,
	"ErrorInfo":"",
	"ErrorDisplay":""
}
```

#### 2.8.2 Add Friends in Batches

```
{
	"ResultItem":
	[
		{
			"To_Account":"id1",
			"ResultCode":0,
			"ResultInfo":""
		},
		{
			"To_Account":"id2",
			"ResultCode":0,
			"ResultInfo":""
		},
		{
			"To_Account":"id3",
			"ResultCode":0,
			"ResultInfo":""
		}
	],
	"Fail_Account":[],
	"Invalid_Account":[],
	"ActionStatus":"OK",
	"ErrorCode":0,
	"ErrorInfo":"",
	"ErrorDisplay":""
}
```

### 2.9 Description of Response Packet Field 

<table style="display:table;width:100%">
	<tbody>
		<tr style="background:#C2D3FC;border:1px solid blue;">
			<td style="width:15%;">Field</td>
			<td style="width:10%;">Type</td>
			<td style="width:75%;">Description</td>
		</tr>
		<tr>
			<td>ResultItem</td>
			<td>Array </td>
			<td>The object array of the result for batch updating of friends</td>
		</tr>
		<tr>
			<td>To_Account</td>
			<td>String </td>
			<td>Identifier of friend requested for updating.</td>
		</tr>
		<tr>
			<td>ResultCode</td>
			<td>Integer </td>
			<td>The processing result for a single friend after friends are updated in batches. 0: Successful; other values: Failed.</td>
		</tr>
		<tr>
			<td>Fail_Account</td>
			<td>Array </td>
			<td>Returned list of friend accounts that are failed to process.</td>
		</tr>
		<tr>
			<td>Invalid_Account</td>
			<td>Array </td>
			<td>Returned list of invalid accounts in the request packet.</td>
		</tr>
		<tr>
			<td>ActionStatus</td>
			<td>String </td>
			<td>Processing result of request. "OK": Successful; "FAIL": Failed.</td>
		</tr>
		<tr>
			<td>ErrorCode</td>
			<td>Integer </td>
			<td>Error code</td>
		</tr>
		<tr>
			<td>ErrorInfo</td>
			<td>String </td>
			<td>Detailed error message</td>
		</tr>
		<tr>
			<td>ErrorDisplay</td>
			<td>String </td>
			<td>Detailed information displayed at the client end</td>
		</tr>
	</tbody>
</table>

### 2.10 Error Codes 

Unless network error occurs (such as 502 error), the HTTP error code returned for this API is 200. The actual error code and error message are represented by ErrorCode and ErrorInfo in the response packet. 
For more information about common error codes (60000 to 79999), please see <a href="https://cloud.tencent.com/document/product/269/1671#rest-api.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81">REST API Common Error Codes</a>. 
 The private error codes for this API are as follows: 

<table style="display:table;width:100%">
	<tbody>
		<tr style="background:#C2D3FC;border:1px solid blue;">
			<td style="width:5%;">Error Code</td>
			<td style="width:95%;">Detailed Error Message</td>
		</tr>
		<tr>
			<td>30001</td>
			<td>
				Failed to resolve the request packet by the relationship chain system:<br />
				If it is a REST API request, confirm whether the request packet is valid and complete by referring to the REST API document.<br />
				If it is not a REST API request, contact technical customer service.
			</td>
		</tr>
		<tr>
			<td>30002</td>
			<td>SDKAppId is invalid. Check whether SDKAppId and account are valid or contact the technical customer service.</td>
		</tr>
		<tr>
			<td>30003</td>
			<td>The account is invalid. Check whether the account is valid or contact the technical customer service.</td>
		</tr>
		<tr>
			<td>30004</td>
			<td>You have received a request sent via REST API, but do not have admin permission. Contact the technical customer service.</td>
		</tr>
		<tr>
			<td>30005</td>
			<td>Relationship chain field contains sensitive words. Check whether the value of relationship chain field is valid or contact technical customer service.</td>
		</tr>
		<tr>
			<td>30701</td>
			<td>
				The parameters for updating friend data are incorrect. Check whether the length of remark exceeds 96 bytes, the length of group name exceeds 30 bytes, multiple group names are left empty, and the Tag name is valid. The name of Tag only supports: "Tag_SNS_IM_Remark" and "Tag_SNS_IM_Group".<br />
			</td>
		</tr>
		<tr>
			<td>30702</td>
			<td>Failed to obtain friend while updating friend data. Try again or contact technical customer service.</td>
		</tr>
		<tr>
			<td>30703</td>
			<td>Failed to obtain friend metadata while updating friend data. Try again or contact technical customer service.</td>
		</tr>
		<tr>
			<td>30704</td>
			<td>Failed to obtain friend row data while updating friend data. Try again or contact technical customer service.</td>
		</tr>
		<tr>
			<td>30705</td>
			<td>Failed to perform standard configuration of information row data while updating friend data. Try again or contact technical customer service.</td>
		</tr>
		<tr>
			<td>30706</td>
			<td>Failed to perform standard configuration of information metadata while updating friend data. Try again or contact technical customer service.</td>
		</tr>
		<tr>
			<td>30707</td>
			<td>Failed to perform standard configuration of information while updating friend data. Try again or contact technical customer service.</td>
		</tr>
		<tr>
			<td>30708</td>
			<td>Failed to customize information row data while updating friend data. Try again or contact technical customer service.</td>
		</tr>
		<tr>
			<td>30709</td>
			<td>Failed to customize information metadata while updating friend data. Try again or contact technical customer service.</td>
		</tr>
		<tr>
			<td>30710</td>
			<td>Failed to customize information while updating friend data. Try again or contact technical customer service.</td>
		</tr>
		<tr>
			<td>30711</td>
			<td>Failed to execute task while updating friend data. Try again or contact technical customer service.</td>
		</tr>
		<tr>
			<td>30712</td>
			<td>Friend does not exist while updating friend data. No friend that needs to be updated is found in the friend list. The caller can capture this error to prompt users.</td>
		</tr>
		<tr>
			<td>30713</td>
			<td>
				The number of groups has reached the limit set by the system while updating friend data. For more information, please see <a href="https://cloud.tencent.com/document/product/269/1501#3.1-.E6.A0.87.E9.85.8D.E5.A5.BD.E5.8F.8B.E5.AD.97.E6.AE.B5">Standard Configuration of Friend Fields</a>. The caller can capture this error to prompt users.<br />
			</td>
		</tr>
	</tbody>
</table>

## 3. API Debugging Tool 

Debug this API using the <a href="https://avc.cloud.tencent.com/im/APITester/APITester.html#v4/sns/friend_update">REST API Debugging Tool</a>. 

## 4. API Integration 

None

## 5. Callback That Can Be Triggered 

None

## 6. References

REST API: <a href="https://cloud.tencent.com/document/product/269/1643">Add Friends</a>
REST API: <a href="https://cloud.tencent.com/document/product/269/8301">Import Friends</a>
REST API: <a href="https://cloud.tencent.com/document/product/269/1644">Delete Friends</a>
REST API: <a href="https://cloud.tencent.com/document/product/269/1645">Delete All Friends</a>
REST API: <a href="https://cloud.tencent.com/document/product/269/1646">Verify Friends</a>
REST API: <a href="https://cloud.tencent.com/document/product/269/1647">Pull Friends</a>
REST API: <a href="https://cloud.tencent.com/document/product/269/8609">Pull Specified Friends</a>


