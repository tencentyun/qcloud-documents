### Sharding Strategy
1. hash key sharding mechanism is supported.
2. You can combine the shard keys of fields
3. Sharding is required for all data sets under a sharding instance. It is recommended to place non-sharded data in a separate replica set instance.

### Authentication Mechanism
Fully compatible with two mechanisms: SCRAM-SHA-1 and MONGODB-CR.

### Supported Sharding Cluster Commands
<table class="table-striped">
	<tbody>
		<tr>
		 <th>&nbsp;</th>
			<th>Commands</th>
			<th>Subcommands</th>
			<th>Supported?</th>
		</tr>

		<tr>
		  <td rowspan="39">CRUD basic commands</td>
			<td rowspan="22">find</td>
			<td>filter</td>
			<td>Yes</td>
		</tr>
		
		<tr>
			<td>Sort</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>projection</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>hint</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>skip</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>limit</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>batchSize</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>singleBatch</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>comment</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>maxScan</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>maxTimeMS</td>
			<td>No</td>
		</tr>
		<tr>
			<td>readConcern</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>max</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>min</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>returnKey</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>showRecordId</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>snapshot</td>
			<td>No</td>
		</tr>
		<tr>
			<td>tailable</td>
			<td>No</td>
		</tr>
		<tr>
			<td>oplogReplay</td>
			<td>No</td>
		</tr>
		<tr>
			<td>noCursorTimeout</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td>awaitData</td>
			<td>No</td>
		</tr>
		<tr>
			<td>allowPartialResults</td>
			<td>No</td>
		</tr>
		
		
		<tr>
			<td rowspan="1" >insert</td>
			<td >Must include shardkey field, the shard keys must be consistent during batch insert operations</td>
			<td>Yes</td>
		</tr>
		
		
		
		<tr>
			<td rowspan="1">update</td>
			<td >The update field cannot be shardkey</td>
			<td>Yes</td>
		</tr>
		
		<tr>
			<td rowspan="1">delete</td>
			<td></td>
			<td>Yes</td>
		</tr>
		
				
		<tr>
			<td rowspan="1">findandmodify</td>
			<td></td>
			<td>Yes</td>
		</tr>
		
		<tr>
			<td rowspan="1">count</td>
			<td></td>
			<td>Yes</td>
		</tr>
			
			<tr>
			<td rowspan="1">distinct</td>
			<td>Must include shard key</td>
			<td>Yes</td>
		</tr>
		
    <tr>
			<td rowspan="1">aggregate</td>
			<td></td>
			<td>No</td>
		</tr>
		
		 <tr>
			<td rowspan="1">group</td>
			<td></td>
			<td>No</td>
		</tr>
		
		 <tr>
			<td rowspan="1">mapReduce</td>
			<td></td>
			<td>No</td>
		</tr>	
		
		<tr>
			<td rowspan="1">getmore</td>
			<td></td>
			<td>Yes</td>
		</tr>
		
		<tr>
			<td rowspan="1">getLastError</td>
			<td></td>
			<td>No</td>
		</tr>

		<tr>
			<td rowspan="1">getPrevError</td>
			<td></td>
			<td>No</td>
		</tr>
	
			<tr>
			<td rowspan="1">resetError</td>
			<td></td>
			<td>No</td>
		</tr>
		
			<tr>
			<td rowspan="1">eval</td>
			<td></td>
			<td>No</td>
		</tr>
		
			<tr>
			<td rowspan="1">geoNear</td>
			<td></td>
			<td>No</td>
		</tr>
		
			<tr>
			<td rowspan="1">geoSearch</td>
			<td></td>
			<td>No</td>
		</tr>
		
			<tr>
			<td rowspan="1">parallelCollectionScan</td>
			<td></td>
			<td>No</td>
		</tr>
		
			<tr>
		  <td rowspan="6">Diagnostic commands</td>
			<td rowspan="1">collStats</td>
			<td></td>
			<td>Yes</td>
		</tr>
		
			<tr>
			<td rowspan="1">dbstats</td>
			<td></td>
			<td>Yes</td>
		</tr>
		
			<tr>
			<td rowspan="1">explain</td>
			<td></td>
			<td>Yes</td>
		</tr>
		
			<tr>
			<td rowspan="1">listDatabases</td>
			<td></td>
			<td>Yes</td>
		</tr>		

			<tr>
			<td rowspan="1">serverStatus</td>
			<td></td>
			<td>No</td>
		</tr>
		
			<tr>
			<td rowspan="1">top</td>
			<td></td>
			<td>No</td>
		</tr>

			<tr>
		  <td rowspan="2">Sharding commands</td>
			<td rowspan="1">enableSharding</td>
			<td></td>
			<td>Yes</td>
		</tr>
		
			<tr>
			<td rowspan="1">shardCollection</td>
			<td></td>
			<td>Yes</td>
		</tr>
		
		
		 <tr>
		  <td rowspan="30">Managment commands</td>
			<td rowspan="1">listCollections</td>
			<td></td>
			<td>Yes</td>
		</tr>
		
			<tr>
			<td rowspan="1">dropDatabase</td>
			<td></td>
			<td>Yes</td>
		</tr>
		
			<tr>
			<td rowspan="1">drop</td>
			<td></td>
			<td>Yes</td>
		</tr>
		
			<tr>
			<td rowspan="1">creareIndexes</td>
			<td></td>
			<td>Yes</td>
		</tr>		
		
			<tr>
			<td rowspan="1">listIndexes</td>
			<td></td>
			<td>Yes</td>
		</tr>		
	
		<tr>
			<td rowspan="1">dropIndexes</td>
			<td></td>
			<td>Yes</td>
		</tr>
		
			<tr>
			<td rowspan="1">logout</td>
			<td></td>
			<td>Yes</td>
		</tr>		
		
			<tr>
			<td rowspan="1">renameCollection</td>
			<td></td>
			<td>No</td>
		</tr>	
		
			<tr>
			<td rowspan="1">copydb</td>
			<td></td>
			<td>No</td>
		</tr>		
		
			<tr>
			<td rowspan="1">create</td>
			<td></td>
			<td>No</td>
		</tr>		
		
		<tr>
			<td rowspan="1">clone</td>
			<td></td>
			<td>No</td>
		</tr>		
		
		<tr>
			<td rowspan="1">cloneCollection</td>
			<td></td>
			<td>No</td>
		</tr>				

		<tr>
			<td rowspan="1">cloneCollectionAsCapped</td>
			<td></td>
			<td>No</td>
		</tr>		
		

		<tr>
			<td rowspan="1">convetToCapped</td>
			<td></td>
			<td>No</td>
		</tr>		
		
		<tr>
			<td rowspan="1">filemd5</td>
			<td></td>
			<td>No</td>
		</tr>		

		<tr>
			<td rowspan="1">fsync</td>
			<td></td>
			<td>No</td>
		</tr>		
		
		<tr>
			<td rowspan="1">clean</td>
			<td></td>
			<td>No</td>
		</tr>		
		
		<tr>
			<td rowspan="1">connPoolSync</td>
			<td></td>
			<td>No</td>
		</tr>		
		
		
			<tr>
			<td rowspan="1">connectionStatus</td>
			<td></td>
			<td>No</td>
		</tr>		
		
		<tr>
			<td rowspan="1">compact</td>
			<td></td>
			<td>No</td>
		</tr>		
		
		
			<tr>
			<td rowspan="1">collMod</td>
			<td></td>
			<td>No</td>
		</tr>		
		
			<tr>
			<td rowspan="1">reIndex</td>
			<td></td>
			<td>No</td>
		</tr>		
		
			<tr>
			<td rowspan="1">setParameter</td>
			<td></td>
			<td>No</td>
		</tr>		
		
			<tr>
			<td rowspan="1">getParameter</td>
			<td></td>
			<td>No</td>
		</tr>		
		
			<tr>
			<td rowspan="1">repairDatabase</td>
			<td></td>
			<td>No</td>
		</tr>		
		
			<tr>
			<td rowspan="1">repairCursor</td>
			<td></td>
			<td>No</td>
		</tr>		
		
			<tr>
			<td rowspan="1">touch</td>
			<td></td>
			<td>No</td>
		</tr>		
		
		<tr>
			<td rowspan="1">shutdown</td>
			<td></td>
			<td>No</td>
		</tr>		

		<tr>
			<td rowspan="1">logrotate</td>
			<td></td>
			<td>No</td>
		</tr>		
		
		<tr>
			<td rowspan="1">killop</td>
			<td></td>
			<td>No</td>
		</tr>		
		
		
		<tr>
		  <td rowspan="1">User management commands</td>
			<td rowspan="1"></td>
			<td></td>
			<td>No</td>
		</tr>
		
			<tr>
		  <td rowspan="1">Role management commands</td>
			<td rowspan="1"></td>
			<td></td>
			<td>No</td>
		</tr>
		
				 <tr>
		  <td rowspan="30">Replica set commands</td>
			<td rowspan="1"></td>
			<td></td>
			<td>No</td>
		</tr>
		
		
	</tbody>
</table>
