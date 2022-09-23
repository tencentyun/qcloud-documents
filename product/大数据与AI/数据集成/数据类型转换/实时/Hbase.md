## 写入

| 内部类型 | HBase 类型 |
|---------|---------|
| CHAR，VARCHAR，STRING| byte[] toBytes(String s)，String toString(byte[] b)	| 
| BOOLEAN| byte[] toBytes(boolean b)，boolean toBoolean(byte[] b)	| 
| BINARY VARBINARY| Returns byte[] as is.	| 
| DECIMAL| byte[] toBytes(BigDecimal v)，BigDecimal toBigDecimal(byte[] b)	| 
| TINYINT| new byte[] { val }，bytes[0] // returns first and only byte from bytes	| 
| SMALLINT| byte[] toBytes(short val)，short toShort(byte[] bytes)	| 
| INT| byte[] toBytes(int val)，int toInt(byte[] bytes)	| 
| BIGINT| byte[] toBytes(long val)，long toLong(byte[] bytes)	| 
| FLOAT| byte[] toBytes(float val)，float toFloat(byte[] bytes)	| 
|DOUBLE|  byte[] toBytes(double val)，double toDouble(byte[] bytes)	| 
| DATE| Stores the number of days since epoch as int value.	| 
| TIME| Stores the number of milliseconds of the day as int value.	| 
| TIMESTAMP| Stores the milliseconds since epoch as long value.	| 

