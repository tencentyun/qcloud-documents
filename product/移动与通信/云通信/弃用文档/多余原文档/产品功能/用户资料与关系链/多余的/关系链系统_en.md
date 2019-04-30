## Introduction to Relationship Chain System

Instant Messaging (IM) provides the relationship chain system, which offers a complete set of services related to the relationship chain. If you want each user to have its own friends and to easily perform various operations such as adding and deleting friends, you can choose the IM's relationship chain hosting service:

1. We provide the capacity of storing relationship chains, ensuring that your data has the capabilities of remote disaster recovery, multi-region deployment and auto-scaling, so that you can be completely free from complex processing flows, such as server downtime, multi-copy master-slave replication, capacity expansion and reduction.
2. We provide the business processing flows commonly used in the industry, which frees you from the logics of IM relationship chain.
3. We provide professional operation processes and teams with up to 99.99% guaranteed service quality stability per year, helping you offer services with a steady reputation to your users.
4. We provide easy-to-use service APIs and easy-to-access guidelines with star-level services in the whole process.

Relationship chain is a set of data used to describe the relationship between a user and other users. The relationship chains supported by IM include Friend List and Blacklist.

## Relationship Chain Field
The IM relationship chain system supports standard and custom relationship chain fields. The relationship chain field has the following features:

1. The relationship chain field is displayed in a format of key-value.
2. Key is a string, and its name only supports uppercase and lowercase letters, numbers and underscores.
3. Value has the following types:
 (1) An integer of uint64_t type (not supported for custom relationship chain fields).
 (2) A string of string type (the length of string cannot exceed 500 bytes).
 (3) A buffer of bytes type (the length of buffer cannot exceed 500 bytes);
 (4) A string array of string type (the length of each string cannot exceed 500 bytes, which is used only for the Tag_SNS_IM_Group field of friend list).

## Friend List
You are allowed to add 1,000 friends to IM friend list by default. If you have special requirements for the size of friend list, please contact Tencent Cloud customer service.
The friend list supports standard friend field and custom friend field.

### Standard Friend Field
IM supports the following standard friend fields:

<table style="display:table;width:100%">
	<tbody>
		<tr style="background:#C2D3FC;border:1px solid blue;">
			<td style="width:20%;">Field Name</td>
			<td style="width:10%;">Type</td>
			<td style="width:70%;">Description</td>
		</tr>
		<tr>
			<td>Tag_SNS_IM_Group</td>
			<td>Array </td>
			<td>
				Group:<br />
				1. A maximum of 32 groups are supported<br />
				2. The group name cannot be empty<br />
				3. The length of a group name cannot exceed 30 bytes<br />
				4. The available value range for group ID is [1, 32]<br />
				5. The same friend can have multiple different groups<br />
			</td>
		</tr>
		<tr>
			<td>Tag_SNS_IM_Remark</td>
			<td>string </td>
			<td>
				Remark:<br />
				1. The maximum length of a remark cannot exceed 96 bytes.<br />
			</td>
		</tr>
		<tr>
			<td>Tag_SNS_IM_AddSource</td>
			<td>string </td>
			<td>
				Source from which a friend is added:<br />
				1. The source field contains prefix and keyword<br />
				2. The prefix of source field is: AddSource_Type_<br />
				3. Keyword: It must be English letters with a length not more than 8 bytes. It is recommended to use an English word or its abbreviation<br />
				4. Example: If the keyword of source is Android, the source field is: AddSource_Type_Android<br />
			</td>
		</tr>
		<tr>
			<td>Tag_SNS_IM_AddWording</td>
			<td>string </td>
			<td>
				Request content:<br />
				1. The maximum length of a request cannot exceed 256 bytes<br />
			</td>
		</tr>
	</tbody>
</table>

### Custom Friend Field

The custom friend field is the friend data set by each App according to its own business needs. By customizing the fried field, an App can add additional data to friends, and perform read and write operations through the existing API.
When an App needs to apply for a custom friend field, it can submit a ticket to the Tencent Cloud customer service. After the ticket is submitted, the configuration will be completed by Tencent Cloud and take effect within three working days.

The naming rules of a custom friend field are as follows:
1. The name of a custom friend field is divided into two parts: prefix and keyword.
2. The prefix of a custom friend field is: Tag_SNS_Custom.
3. Keyword: It must be a letter with a length not more than 8 bytes. It is recommended to use a word or its abbreviation.
4. Example: If the keyword of a custom friend field to be applied for by an App is Test, then the name of the custom relationship field is: Tag_SNS_Custom_Test.

When applying for a custom friend field, you need to submit the following information for each custom friend field:
1. The name of custom friend field (Key).
2. The type of custom friend field (Value): For more information, please see <a href="https://cloud.tencent.com/document/product/269/1501#2-.E5.85.B3.E7.B3.BB.E9.93.BE.E5.AD.97.E6.AE.B5">Relationship Chain Field</a>.

### Adding Friend

IM supports the following modes for adding friend: adding friends in batches, adding friend in one round, and adding friend in two rounds. For more information, please see <a href="https://cloud.tencent.com/document/product/269/1643">Add Friend</a>.

Two-way friend: User A's friend list contains user B, and user B's friend list also contains user A.
One-way friend: User A's friend list contains user B, but user B's friend list doesn't contain user A.
Verification method for adding friend: Each user can choose the way with which he/she is added as a friend by another user. For more information, please see the field of verification method for adding friend in <a href="https://cloud.tencent.com/document/product/269/1500#3-.E6.A0.87.E9.85.8D.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5">Standard Information Field</a>.
Adding friend in one round: If the verification method for adding friend set by account A is AllowType_Type_AllowAny, then anyone who wants to add A as a friend can directly add him/her. So, the scenario where a user can be successfully added as friend with one request is called adding friend in one round.
Adding friend in two rounds: If the verification method for adding friend set by account A is AllowType_Type_NeedConfirm, then for anyone who wants to add A, A will receive a message to verify the request for adding friend, and this is the first round. Then, A accepts the request, and this is the second round. So, the scenario where a verification is required for adding friend is called adding friend in two rounds.

### Deleting Friend
IM supports two modes for deleting friend: deleting friend unilaterally, and deleting friend bilaterally.

<table style="width:100%;" >
		<tbody>
			<tr>
				<td style="width:25%;background-color:#CCCCCC;">Deletion Mode</td>
				<td style="width:5%;background-color:#CCCCCC;">DeleteType</td>
				<td style="background-color:#CCCCCC;">Description</td>
			</tr>
			<tr>
				<td>Delete friend unilaterally</td>
				<td>Delete_Type_Single</td>
				<td>Only To_Account is deleted from the friend list of From_Account, but From_Account is not deleted from the friend list of To_Account.</td>
			</tr>
			<tr>
				<td>Delete friend bilaterally</td>
				<td>Delete_Type_Both</td>
				<td>To_Account is deleted from the friend list of From_Account, and From_Account is also deleted from the friend list of To_Account at the same time.</td>
			</tr>
		</tbody>
	</table>

IM also supports deleting friends in batches. For more information, please see <a href="https://cloud.tencent.com/document/product/269/1644">Delete Friend</a>.

### Pulling Friend
IM supports the following three modes for pulling friend: incrementally pulling without friends, completely pulling by page, and pulling with friends. For more information, please see <a href="https://cloud.tencent.com/document/product/269/1647">Pull Friend</a>.

### Verifying Friend

IM supports the two friendship verification modes: unidirectional friendship verification and bidirectional friendship verification.

<table style="width:100%;" >
		<tbody>
			<tr>
				<td style="width:25%;background-color:#CCCCCC;">Verification Mode</td>
				<td style="width:5%;background-color:#CCCCCC;">Check Type</td>
				<td style="background-color:#CCCCCC;">Description</td>
			</tr>
			<tr>
				<td>Unidirectional friendship verification</td>
				<td>CheckResult_Type_Singal</td>
				<td>It is only used to check whether To_Account is in the friend list of From_Account, but cannot check whether From_Account is in the friend list of To_Account.</td>
			</tr>
			<tr>
				<td>Bidirectional friendship verification</td>
				<td>CheckResult_Type_Both</td>
				<td>It is used to check both whether To_Account is in the friend list of From_Account and whether From_Account is in the friend list of To_Account.</td>
			</tr>
		</tbody>
	</table>

The result for unidirectional friendship verification:

<table style="width:100%;" >
		<tbody>
			<tr>
				<td style="width:25%;background-color:#CCCCCC;">Relation</td>
				<td style="background-color:#CCCCCC;">Description</td>
			</tr>
			<tr>
				<td>CheckResult_Type_NoRelation</td>
				<td>To_Account is not in the friend list of From_Account, but it cannot confirm whether From_Account is in the friend list of To_Account.</td>
			</tr>
			<tr>
				<td>CheckResult_Type_AWithB</td>
				<td>To_Account is in the friend list of From_Account, but it cannot confirm whether From_Account is in the friend list of To_Account.</td>
			</tr>
		</tbody>
	</table>

The result for bidirectional friendship verification:

<table style="width:100%;" >
		<tbody>
			<tr>
				<td style="width:25%;background-color:#CCCCCC;">Relation</td>
				<td style="background-color:#CCCCCC;">Description</td>
			</tr>
			<tr>
				<td>CheckResult_Type_BothWay</td>
				<td>To_Account is in the friend list of From_Account, and From_Account is also in the friend list of To_Account.</td>
			</tr>
			<tr>
				<td>CheckResult_Type_AWithB</td>
				<td>To_Account is in the friend list of From_Account, but From_Account is not in the friend list of To_Accout.</td>
			</tr>
			<tr>
				<td>CheckResult_Type_BWithA</td>
				<td>To_Account is not in the friend list of From_Account, but From_Account is in the friend list of To_Accout.</td>
			</tr>
			<tr>
				<td>CheckResult_Type_NoRelation</td>
				<td>To_Account is not in the friend list of From_Account, and From_Account is also not in the friend list of To_Account.</td>
			</tr>
		</tbody>
	</table>

For more information on friend verification, please see <a href="https://cloud.tencent.com/document/product/269/1646">Verify Friend</a>.

## Blacklist
Each user has a blacklist, which is used to store the accounts blocked by this user.
After user A adds user B to the blacklist, A will unfriend B (if they are friends), and neither A nor B can send a request for adding friend again.
You are allowed to add 1,000 accounts to the IM blacklist by default. If you have special requirements for the size of blacklist, please contact the Tencent Cloud customer service.

### Adding Blacklist
IM supports adding blacklists in batches. For more information, please see <a href="https://cloud.tencent.com/document/product/269/3718">Add Blacklist</a>.

### Deleting Blacklist
IM supports deleting blacklists in batches. For more information, please see <a href="https://cloud.tencent.com/document/product/269/3719">Delete Blacklist</a>.

### Pulling Blacklist
IM supports completely pulling blacklists by page. For more information, please see <a href="https://cloud.tencent.com/document/product/269/3722">Pull Blacklist</a>.

## Verifying Blacklist
IM supports two blacklist verification modes: unidirectional verification and bidirectional verification.

<table style="width:100%;" >
		<tbody>
			<tr>
				<td style="width:25%;background-color:#CCCCCC;">Verification Mode</td>
				<td style="width:5%;background-color:#CCCCCC;">Check Type</td>
				<td style="background-color:#CCCCCC;">Description</td>
			</tr>
			<tr>
				<td>Unidirectional blacklist relationship verification</td>
				<td>BlackCheckResult_Type_Singal</td>
				<td>It is only used to check whether To_Account is in the blacklist of From_Account, but cannot check whether From_Account is in the blacklist of To_Account.</td>
			</tr>
			<tr>
				<td>Bidirectional blacklist relationship verification</td>
				<td>BlackCheckResult_Type_Both</td>
				<td>It is used not only to check whether To_Account is in the blacklist of From_Account, but also to check whether From_Account is in the blacklist of To_Account.</td>
			</tr>
		</tbody>
	</table>

The result for unidirectional blacklist relationship verification:

<table style="width:100%;" >
		<tbody>
			<tr>
				<td style="width:25%;background-color:#CCCCCC;">Relation</td>
				<td style="background-color:#CCCCCC;">Description</td>
			</tr>
			<tr>
				<td>CheckResult_Type_AWithB</td>
				<td>To_Account is in the blacklist of From_Account, but it cannot confirm whether From_Account is in the blacklist of To_Account.</td>
			</tr>
			<tr>
				<td>CheckResult_Type_NoRelation</td>
				<td>To_Account is not in the blacklist of From_Account, but it cannot confirm whether From_Account is in the blacklist of To_Account.</td>
			</tr>
		</tbody>
	</table>

The result for bidirectional blacklist relationship verification:

<table style="width:100%;" >
		<tbody>
			<tr>
				<td style="width:25%;background-color:#CCCCCC;">Relation</td>
				<td style="background-color:#CCCCCC;">Description</td>
			</tr>
			<tr>
				<td>CheckResult_Type_BothWay</td>
				<td>To_Account is in the blacklist of From_Account, and From_Account is also in the blacklist of To_Account.</td>
			</tr>
			<tr>
				<td>CheckResult_Type_AWithB</td>
				<td>To_Account is in the blacklist of From_Account, but From_Account is not in the blacklist of To_Account.</td>
			</tr>
			<tr>
				<td>CheckResult_Type_BWithA</td>
				<td>To_Account is not in the blacklist of From_Account, but From_Account is in the blacklist of To_Account.</td>
			</tr>
			<tr>
				<td>CheckResult_Type_NoRelation</td>
				<td>To_Account is not in the blacklist of From_Account, and From_Account is also not in the blacklist of To_Account.</td>
			</tr>
		</tbody>
	</table>

For more information on blacklist verification, please see <a href="https://cloud.tencent.com/document/product/269/3725">Verify Blacklist</a>.


