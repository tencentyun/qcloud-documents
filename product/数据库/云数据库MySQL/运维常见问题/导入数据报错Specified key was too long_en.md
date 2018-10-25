## Causes
	 ERROR 1071 (42000): Specified key was too long; max key length is 767 bytes
CDB reports the error that Specified key was too long, when the customer imports the xxxx.sql file to the CDB with the CVM command line.

The error message of "ERROR 1071 (42000): The error information that Specified key was too long and max key length is 767 bytes" indicates that "The index field exceeds 767 bytes, which is too long".

① For innodb storage engine, the maximum length of the multiple index is as follows:

  **The maximum length for each index is 767 bytes and the length summary of all the indexes is no more than 3,072 bytes**

② For myisam storage engine, the maximum length of the multiple index is as follows:

  **The maximum length for each index is 1,000 bytes and the length summary of all the indexes is 1,000 bytes**

TIPS: In the fields such as 768/2=384 double-byte or 767/3=255 three-byte, GBK is double-byte, UTF8 is three-byte, and UTF8MB4 is four-byte.

Why it is OK on the self-built database, but after importing the data into CDB, the error that Specified key was too long was reported?

CDB 5.6 and later version automatically convert all myisam tables to innodb, so the self-built database contains combined index, the length of which exceeds 767 bytes. However, since the self-built database adopts myisam storage engine, the same creation statement works well here but not applicable to CDB 5.6.

## Solutions:
### 1. Modify the combined index length of the error line in the backup file
Common example:

**create table test(test varcahr(255) primary key)charset=utf8;**

- Successful

**create table test(test varcahr(256) primary key)charset=utf8;**

- Failed

- ERROR 1071(42000):Specified key was too long; max key length is 767 bytes

### 2. Use CDB 5.5, so that the myisam engine is not automatically converted to innodb.

