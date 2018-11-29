

### DynamoDB Protocol Support
<table class="table-striped">
	<tbody>
		<tr>
		 <th>API Name</th>
			<th>Parameter</th>
			<th>Supported</th>
		</tr>

		<tr>
		  <td rowspan="7">CreateTable</td>
			<td>Required input parameter: TableName</td>
			<td>Yes</td>
		</tr>	
		<tr>
			<td>Required input parameter: AttributeDefinitions</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>Required input parameter: KeySchema</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>Required input parameter: ProvisionedThroughput</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>Optional input parameter: GlobalSecondaryIndexes</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>Optional input parameter: LocalSecondaryIndexes</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>Optional input parameter: StreamSpecification</td>
			<td>No</td>
		</tr>
		
		<tr>
		  <td rowspan="5">BatchWriteItem</td>
			<td>Required input parameter: RequestItems</td>
			<td>Yes</td>
		</tr>		
		<tr>
			<td>Required input parameter: PutRequest</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>Required input parameter: DeleteRequest</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>Optional input parameter: ReturnConsumedCapacity</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Optional input parameter: ReturnItemCollectionMetrics</td>
			<td>No</td>
		</tr>
		
		
			<tr>
		  <td rowspan="5">BatchGetItem</td>
			<td>RequestItems</td>
			<td>Yes</td>
		</tr>	
		<tr>
			<td>ProjectionExpression</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>ExpressionAttributeNames</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>Optional input parameter: ReturnConsumedCapacity</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Optional input parameter: ConsistentRead</td>
			<td>No</td>
		</tr>
		

		<tr>
		  <td rowspan="7">DeleteItem</td>
			<td>ConditionExpression</td>
			<td>Yes</td>
		</tr>	
		<tr>
			<td>Key</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>TableName</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>Optional input parameter: Expected</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>Optional input parameter: ConditionOperator</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Optional input parameter: ReturnItemCollectinMetricst</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Optional input parameter: ReturnConsumedCapacity</td>
			<td>No</td>
		</tr>
		
			<tr>
		  <td rowspan="1">DeleteTable</td>
			<td>Required input parameter: TableName</td>
			<td>Yes</td>
		</tr>	
		

		<tr>
			<td rowspan="6" >DescribeTable</td>
			<td >Required input parameter: TableName</td>
			<td>Yes</td>
		</tr>
			<tr>
			<td>Response parameter: Backfilling</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Response parameter: ProvisionedThroughput </td>
			<td>No</td>
		</tr>
		<tr>
			<td>Response parameter: LatestStreamArn</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Response parameter: LatestStreamLabel</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Response parameter: StreamSpecification</td>
			<td>No</td>
		</tr>
		
			<tr>
			<td rowspan="6" >GetItem</td>
			<td >Required input parameter: TableName</td>
			<td>Yes</td>
		</tr>
			<tr>
			<td>Required input parameter: Key</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>Optional input parameter: ConsistentRead</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Optional input parameter: ReturnConsumedCapacity</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Optional input parameter: ReturnConsumedCapacity</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Optional input parameter: ProjectionExpression</td>
			<td>No</td>
		</tr>	
		
			<tr>
			<td rowspan="3" >ListTables</td>
			<td >Required input parameter: TableName</td>
			<td>Yes</td>
		</tr>
			<tr>
			<td>Optional input parameter: Limit</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>Optional input parameter: ExclusiveStartTableName</td>
			<td>Yes</td>
		</tr>
		
			<tr>
			<td rowspan="9" >PutItem</td>
			<td >Required input parameter: TableName</td>
			<td>Yes</td>
		</tr>
			<tr>
			<td>Required input parameter: Item</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>Optional input parameter: ConditionExpression</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>Optional input parameter: Expected</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Optional input parameter: ConditionOperator</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Optional input parameter: ReturnItemCollectinMetrics</td>
			<td>No</td>
		</tr>	
			<tr>
			<td>Optional input parameter: ReturnConsumedCapacity</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Response parameter: ConsumedCapacity</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Response parameter: ItemCollectionMetrics</td>
			<td>No</td>
		</tr>	
		
		
			<tr>
			<td rowspan="13" >Query</td>
			<td >Required input parameter: TableName</td>
			<td>Yes</td>
		</tr>
			<tr>
			<td>Optional input parameter: FilterExpression</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>Optional input parameter: KeyConditions</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>Optional input parameter: ConditionExpression</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>Optional input parameter: Select</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Optional input parameter: ReturnItemCollectinMetrics</td>
			<td>No</td>
		</tr>	
			<tr>
			<td>Optional input parameter: ReturnConsumedCapacity</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Optional input parameter: ScanIndexForward</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Optional input parameter: ConditionOperator</td>
			<td>No</td>
		</tr>	
			<tr>
			<td>Optional input parameter: ConsistentRead</td>
			<td>No</td>
		</tr>	
			<tr>
			<td>Optional input parameter: Expected</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Optional input parameter: IndexName</td>
			<td>No</td>
		</tr>
		<tr>
			<td>ProjectionExpression</td>
			<td>Yes</td>
		</tr>		
		
		
			<tr>
			<td rowspan="9" >UpdateItem</td>
			<td >Required input parameter: Key</td>
			<td>Yes</td>
		</tr>
			<tr>
			<td>Required input parameter: TableName</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>Optional input parameter: Expected</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Optional input parameter: ConditionOperator</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Optional input parameter: ReturnConsumedCapacity</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Optional input parameter: ReturnItemCollectinMetrics</td>
			<td>No</td>
		</tr>	
			<tr>
			<td>UpdateExpression</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>Response parameter: ConsumedCapacity</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Response parameter: .ItemCollectionMetrics</td>
			<td>No</td>
		</tr>		
	
			<tr>
			<td rowspan="4" >UpdateTable</td>
			<td >Required input parameter: TableName</td>
			<td>Yes</td>
		</tr>
			<tr>
			<td>Optional input parameter: TGlobalSecondaryIndexUpdates</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>Optional input parameter: ProvisionedThroughput</td>
			<td>No</td>
		</tr>
		<tr>
			<td>Optional input parameter: StreamSpecification</td>
			<td>No</td>
		</tr>
		
		
			<tr>
			<td >Scan</td>
			<td ></td>
			<td>No</td>
		</tr>
					<tr>
			<td >TagResourcee</td>
			<td ></td>
			<td>No</td>
		</tr>
					<tr>
			<td >UntagResource</td>
			<td ></td>
			<td>No</td>
		</tr>
					<tr>
			<td >ListTagsOfResource</td>
			<td ></td>
			<td>No</td>
		</tr>
					<tr>
			<td >DescribeLimits</td>
			<td ></td>
			<td>No</td>
		</tr>

	</tbody>
</table>

