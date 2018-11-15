We use Python code as an example to demonstrate basic access and data read/write in a DynomaDB instance. After the instance is created
```
Sample code:
#!/usr/bin/python

from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
import time
from boto3.dynamodb.conditions import Key, Attr

#dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://10.247.10.101:9000")
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://10.112.112.228:8000")

table = dynamodb.create_table(
    TableName='music',
    KeySchema=[
        {
            'AttributeName': 'Artist',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'SongTitle',
            'KeyType': 'RANGE'  #Sort key
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Artist',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'SongTitle',
            'AttributeType': 'S'
        },

    ],
    
    GlobalSecondaryIndexes=[
        {
            "IndexName": "t1Index",
            "KeySchema": [
                {
                    "AttributeName": 'Artist',
                    "KeyType": "HASH"
                },
                {
                    "AttributeName": 'SongTitle',
                    "KeyType": "HASH"
                },
            ],
            "Projection": {
                "ProjectionType": "KEYS_ONLY"
            },
            "ProvisionedThroughput": {
                'ReadCapacityUnits': 3,
                'WriteCapacityUnits': 3
            }  
        }
    ],
    
    ProvisionedThroughput={
        'ReadCapacityUnits': 3,
        'WriteCapacityUnits': 3
    }
)

print("Table status:", table)
#print "Table status: ",table

time.sleep(30)
#write data
response = dynamodb.batch_write_item(
    RequestItems={
        'music': [
            {
                'PutRequest': {
                    'Item': {
                        "Artist": "The Acme Band 2",
                        "SongTitle": "Look Out, World",
                        "AlbumTitle":"The Buck Starts Here",
                        "Price": decimal.Decimal('0.99'),
                        "Genre": "Rock",
                    }
                }
            },
            {
                'PutRequest': {
                    'Item': {
                        "Artist": "none know",
                        "SongTitle": "test World",
                        "AlbumTitle":"The Buck Starts Here",
                        "Price": decimal.Decimal('0.99'),
                        "Genre": "Rock",
                    }
                }
            },
            {
                'PutRequest': {
                    'Item': {
                        "Artist": "The Acme Band 4",
                        "SongTitle": "Look Out, World",
                        "AlbumTitle":"The Buck Starts Here",
                        "Price": decimal.Decimal('3.99'),
                        "Genre": "Rock 4",
                    }
                }
            },
            {
                'PutRequest': {
                    'Item': {
                        "Artist": "The Acme Band 5",
                        "SongTitle": "Look Out, World",
                        "AlbumTitle":"The Buck Starts Here 5",
                        "Price": decimal.Decimal('5.99'),
                        "Genre": "Rock",
                    }
                }
            },

        ]
    },
    ReturnConsumedCapacity='TOTAL',
    ReturnItemCollectionMetrics='SIZE',
)

print("BatchputItem succ!")
print(json.dumps(response, indent=4))


#update data
t_name='music'
table = dynamodb.Table(t_name)

response = table.update_item(
    Key={
        "Artist": "none know",
        "SongTitle": "test World"
    },
    
    UpdateExpression="SET test = :incr REMOVE Tags.del",
    ExpressionAttributeValues={
        ":incr": 'cat'
    },
    ReturnValues="UPDATED_NEW"
)

print("updateItem succ")
print(json.dumps(response, indent=4))


#query data
t_name='music'
table = dynamodb.Table(t_name)

response = table.query(    
    KeyConditionExpression=Key('SongTitle').eq('test World')
)

items = response['Items']
print(items)


#delete Item
test_table='music'
table = dynamodb.Table(t_name)
response = table.delete_item(
    Key={
        'Artist': 'none know',
        "SongTitle": "test World",
    }
)

print("DeleteItem succ!")
print(json.dumps(response, indent=4))

```

Execution results
![](https://mc.qcloudimg.com/static/img/65db8919a3263e464a3c3a52988c08ad/%7BBAC77695-B44F-4ECC-9FBA-38AF9FFC5575%7D.png)








