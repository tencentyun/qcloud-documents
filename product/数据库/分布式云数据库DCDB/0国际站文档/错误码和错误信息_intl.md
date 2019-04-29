
> If you need to view or download the full development documents, please see [Development Guide for DCDB](https://cloud.tencent.com/document/product/557/7714).


## Error Codes and Error Messages

The following error codes are added to DCDB:
```
	    ER_PROXY_GRAM_ERROR_BEGIN=800,

	    ER_PROXY_SANITY_ERROR,         /*SQL type error*/
	    ER_PROXY_BAD_COMMAND,          /*SQL command is not supported*/
	    ER_PROXY_SQL_NOT_SUPPORT,      /*The type is not supported by DCDB*/
	    ER_PROXY_SQLUSE_NOT_SUPPORT,   /*The usage is not supported by DCDB*/
	    ER_PROXY_ERROR_SHARDKEY,       /*Error when using primary and secondary partitioning keys to select partitions during creation of a table. The two partitioning keys need to select different columns.*/

	    ER_PROXY_ERROR_SUB_SHARDKEY,   /*Invalid secondary partitioning grammar, for example, invalid functions in the grammar.*/
	    ER_PROXY_PRE_DEAL_ERROR,       /*JOIN does not conform to the rules*/
	    ER_PROXY_SHADKEY_ERROR,        /*Complex SQL. For example, "derived table" needs to contain shardkey*/
	    ER_PROXY_COMBINE_SQL_ERROR,    /*SQL reorganization error. For example, no corresponding secondary partitioned table*/
	    ER_PROXY_SQL_ERROR,            /*General SQL error*/
	    ER_PROXY_ONE_SET,              /*count (distinct) must be sent to a set*/
 
	    ER_PROXY_TRANSACTION_ERROR,    /*Transaction-related error*/


	    ER_PROXY_GRAM_ERROR_END,  /*Syntax error*/

	    ER_PROXY_SYSTEM_ERROR_BEGIN=900,/*System error. The DCDB team will receive an alarm when this error occurs*/

	    ER_PROXY_SLICING,
	    ER_PROXY_NO_DEFAULT_SET,       /*set is empty*/
	    ER_PROXY_SOCK_ADDRESS_ERROR,   /*set address is empty*/
	    ER_PROXY_SOCK_ERROR,           /*Failed to connect the backend database*/
	    ER_PROXY_STATUS_ERROR,         /*group status error*/
	    ER_PROXY_UNKNOWN_ERROR,        /*Unknown error*/

      ER_PROXY_LOG_GTID_TIMEOUT,     /*Write log timeout during two-phase commit*/
      ER_PROXY_LOG_GTID_ERROR,       /*Write log timeout during two-phase commit*/
      ER_PROXY_COMMIT_TEMP_ERROR,    /*A temporary error occurs during two-phase commit. The agent will automatically commit the transaction*/
      ER_PROXY_ABORT_TEMP_ERROR,     /*A temporary error occurs when the transaction is rolled back. The agent will automatically roll back the transaction*/
      ER_PROXY_SQL_RETRY,
      ER_PROXY_CONN_BROKEN_ERROR,    /*The gateway and backend DB are disconnected*/
```

