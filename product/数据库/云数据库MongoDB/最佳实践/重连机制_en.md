## Description

Instead of simply allowing you to access mongod, Tencent Cloud MongoDB database service provides a cloud load balancer IP for access. You can use this IP to connect to a range of a route access layers similar to mongos.
The client driver will establish a persistent connection with the access machine using cloud load balancer IP. If the connection is active for a long period of time, we will not impose an intervention on this status. However, if the persistent connection is inactive for more than one day (this period will be adjusted with optimized version), the routing connection layer will terminate the connection.
Generally, the client driver will implement an automatic reconnection. However, this process cannot be implemented by some language drivers. For the language drivers that cannot implement automatic reconnection, if a user attempts to communicate with Tencent Cloud MongoDB service using a terminated connection, an error message such as "Remote server has closed the connection" will be returned. So manual reconnection is required. Here is a demo for PHP reconnection.

## Reconnection Based on PHP Mongo Driver
```
<?php

function getConnection() {
    $connection = false;
    $uri = 'mongodb://rwuser:1234567a@10.66.148.142:27017/admin?authMechanism=MONGODB-CR';
    $maxRetries = 5;
    for( $counts = 1; $counts <= $maxRetries; $counts++ ) {
        try {
            $connection = new MongoClient($uri);
        } catch( Exception $e ) {
     // Or use the catch code line below as required. Please note that, "\" is needed when some frameworks use namespace.
     // } catch( \Exception $e ) {
            continue;
        }
        break;
    }
    return $connection;
}

$connection = getConnection();

if($connection) {
		$db = $connection->testdb;
		$collection = $db->testcollection;

		$one = $collection->findOne();

		var_dump($one);
}
```


