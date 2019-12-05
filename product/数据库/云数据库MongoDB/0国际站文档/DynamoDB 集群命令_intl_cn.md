

### DynamoDB协议支持情况说明
<table class="table-striped">
	<tbody>
		<tr>
		 <th>接口名</th>
			<th>参数</th>
			<th>是否支持</th>
		</tr>

		<tr>
		  <td rowspan="7">CreateTable</td>
			<td>必须输入的参数:TableName</td>
			<td>是</td>
		</tr>	
		<tr>
			<td>必须输入的参数:AttributeDefinitions</td>
			<td>是</td>
		</tr>
		<tr>
			<td>必须输入的参数:KeySchema</td>
			<td>是</td>
		</tr>
		<tr>
			<td>必须输入的参数:ProvisionedThroughput</td>
			<td>是</td>
		</tr>
		<tr>
			<td>可选输入的参数：GlobalSecondaryIndexes</td>
			<td>是</td>
		</tr>
		<tr>
			<td>可选输入的参数：LocalSecondaryIndexes</td>
			<td>是</td>
		</tr>
		<tr>
			<td>可选输入的参数：StreamSpecification</td>
			<td>否</td>
		</tr>
		
		<tr>
		  <td rowspan="5">BatchWriteItem</td>
			<td>必须输入的参数：RequestItems</td>
			<td>是</td>
		</tr>		
		<tr>
			<td>必须输入的参数：PutRequest</td>
			<td>是</td>
		</tr>
		<tr>
			<td>必须输入的参数：DeleteRequest</td>
			<td>是</td>
		</tr>
		<tr>
			<td>可选的输入参数：ReturnConsumedCapacity</td>
			<td>否</td>
		</tr>
		<tr>
			<td>可选的输入参数：ReturnItemCollectionMetrics</td>
			<td>否</td>
		</tr>
		
		
			<tr>
		  <td rowspan="5">BatchGetItem</td>
			<td>RequestItems</td>
			<td>是</td>
		</tr>	
		<tr>
			<td>ProjectionExpression</td>
			<td>是</td>
		</tr>
		<tr>
			<td>ExpressionAttributeNames</td>
			<td>是</td>
		</tr>
		<tr>
			<td>可选的输入参数：ReturnConsumedCapacity</td>
			<td>否</td>
		</tr>
		<tr>
			<td>可选的输入参数：ConsistentRead</td>
			<td>否</td>
		</tr>
		

		<tr>
		  <td rowspan="7">DeleteItem</td>
			<td>ConditionExpression </td>
			<td>是</td>
		</tr>	
		<tr>
			<td>Key</td>
			<td>是</td>
		</tr>
		<tr>
			<td>TableName</td>
			<td>是</td>
		</tr>
		<tr>
			<td>可选的输入参数：Expected</td>
			<td>是</td>
		</tr>
		<tr>
			<td>可选的输入参数：ConditionOperator</td>
			<td>否</td>
		</tr>
		<tr>
			<td>可选的输入参数：ReturnItemCollectinMetricst</td>
			<td>否</td>
		</tr>
		<tr>
			<td>可选的输入参数：ReturnConsumedCapacity</td>
			<td>否</td>
		</tr>
		
			<tr>
		  <td rowspan="1">DeleteTable</td>
			<td>必须输入的参数：TableName </td>
			<td>是</td>
		</tr>	
		

		<tr>
			<td rowspan="6" >DescribeTable</td>
			<td >必须输入的参数：TableName</td>
			<td>是</td>
		</tr>
			<tr>
			<td>返回参数中：Backfilling</td>
			<td>否</td>
		</tr>
		<tr>
			<td>返回参数中：ProvisionedThroughput </td>
			<td>否</td>
		</tr>
		<tr>
			<td>返回参数中：LatestStreamArn</td>
			<td>否</td>
		</tr>
		<tr>
			<td>返回参数中：LatestStreamLabel</td>
			<td>否</td>
		</tr>
		<tr>
			<td>返回参数中：StreamSpecification </td>
			<td>否</td>
		</tr>
		
			<tr>
			<td rowspan="6" >GetItem</td>
			<td >必须输入的参数：TableName</td>
			<td>是</td>
		</tr>
			<tr>
			<td>必须输入的参数：Key</td>
			<td>是</td>
		</tr>
		<tr>
			<td>可选的输入参数：ConsistentRead </td>
			<td>否</td>
		</tr>
		<tr>
			<td>可选的输入参数：ReturnConsumedCapacity</td>
			<td>否</td>
		</tr>
		<tr>
			<td>可选的输入参数：ReturnConsumedCapacity</td>
			<td>否</td>
		</tr>
		<tr>
			<td>可选的输入参数：ProjectionExpression</td>
			<td>否</td>
		</tr>	
		
			<tr>
			<td rowspan="3" >ListTables</td>
			<td >必须输入的参数：TableName</td>
			<td>是</td>
		</tr>
			<tr>
			<td>可选的输入参数：Limit</td>
			<td>是</td>
		</tr>
		<tr>
			<td>可选的输入参数：ExclusiveStartTableName </td>
			<td>是</td>
		</tr>
		
			<tr>
			<td rowspan="9" >PutItem</td>
			<td >必须输入的参数：TableName</td>
			<td>是</td>
		</tr>
			<tr>
			<td>必须输入的参数：Item</td>
			<td>是</td>
		</tr>
		<tr>
			<td>可选的输入参数：ConditionExpression</td>
			<td>是</td>
		</tr>
		<tr>
			<td>可选的输入参数：Expected</td>
			<td>否</td>
		</tr>
		<tr>
			<td>可选的输入参数：ConditionOperator</td>
			<td>否</td>
		</tr>
		<tr>
			<td>可选的输入参数：ReturnItemCollectinMetrics</td>
			<td>否</td>
		</tr>	
			<tr>
			<td>可选的输入参数：ReturnConsumedCapacity</td>
			<td>否</td>
		</tr>
		<tr>
			<td>返回参数中：ConsumedCapacity</td>
			<td>否</td>
		</tr>
		<tr>
			<td>返回参数中：ItemCollectionMetrics</td>
			<td>否</td>
		</tr>	
		
		
			<tr>
			<td rowspan="13" >Query</td>
			<td >必须输入的参数：TableName</td>
			<td>是</td>
		</tr>
			<tr>
			<td>可选的输入参数：FilterExpression</td>
			<td>是</td>
		</tr>
		<tr>
			<td>可选的输入参数：KeyConditions</td>
			<td>是</td>
		</tr>
		<tr>
			<td>可选的输入参数：ConditionExpression</td>
			<td>是</td>
		</tr>
		<tr>
			<td>可选的输入参数：Select</td>
			<td>否</td>
		</tr>
		<tr>
			<td>可选的输入参数：ReturnItemCollectinMetrics</td>
			<td>否</td>
		</tr>	
			<tr>
			<td>可选的输入参数：ReturnConsumedCapacity</td>
			<td>否</td>
		</tr>
		<tr>
			<td>可选的输入参数：ScanIndexForward </td>
			<td>否</td>
		</tr>
		<tr>
			<td>可选的输入参数：ConditionOperator </td>
			<td>否</td>
		</tr>	
			<tr>
			<td>可选的输入参数：ConsistentRead</td>
			<td>否</td>
		</tr>	
			<tr>
			<td>可选的输入参数：Expected</td>
			<td>否</td>
		</tr>
		<tr>
			<td>可选的输入参数：IndexName</td>
			<td>否</td>
		</tr>
		<tr>
			<td>ProjectionExpression</td>
			<td>是</td>
		</tr>		
		
		
			<tr>
			<td rowspan="9" >UpdateItem</td>
			<td >必须输入的参数：Key</td>
			<td>是</td>
		</tr>
			<tr>
			<td>必须输入的参数：TableName</td>
			<td>是</td>
		</tr>
		<tr>
			<td>可选的输入参数：Expected</td>
			<td>否</td>
		</tr>
		<tr>
			<td>可选的输入参数：ConditionOperator</td>
			<td>否</td>
		</tr>
		<tr>
			<td>可选的输入参数：ReturnConsumedCapacity</td>
			<td>否</td>
		</tr>
		<tr>
			<td>可选的输入参数：ReturnItemCollectinMetrics</td>
			<td>否</td>
		</tr>	
			<tr>
			<td>UpdateExpression</td>
			<td>是</td>
		</tr>
		<tr>
			<td>返回参数中：ConsumedCapacity</td>
			<td>否</td>
		</tr>
		<tr>
			<td>返回参数中：.ItemCollectionMetrics</td>
			<td>否</td>
		</tr>		
	
			<tr>
			<td rowspan="4" >UpdateTable</td>
			<td >必须输入的参数：TableName</td>
			<td>是</td>
		</tr>
			<tr>
			<td>可选输入的参数：TGlobalSecondaryIndexUpdates</td>
			<td>是</td>
		</tr>
		<tr>
			<td>可选输入的参数：ProvisionedThroughput</td>
			<td>否</td>
		</tr>
		<tr>
			<td>可选输入的参数：StreamSpecification</td>
			<td>否</td>
		</tr>
		
		
			<tr>
			<td >Scan</td>
			<td ></td>
			<td>否</td>
		</tr>
					<tr>
			<td >TagResourcee</td>
			<td ></td>
			<td>否</td>
		</tr>
					<tr>
			<td >UntagResource</td>
			<td ></td>
			<td>否</td>
		</tr>
					<tr>
			<td >ListTagsOfResource</td>
			<td ></td>
			<td>否</td>
		</tr>
					<tr>
			<td >DescribeLimits</td>
			<td ></td>
			<td>否</td>
		</tr>

	</tbody>
</table>
