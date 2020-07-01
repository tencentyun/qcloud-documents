# DCDB����������MySQL������

## ����

DCDB��ʹ��������������ʵ��������MySQL�������棩������Ĺ��ܣ�MySQL��������Ҫ���ھ������ݷֲ��ͷ��ʡ��������ݡ�����ɾ����ˮ���ݵ�������ĿǰMySQL�������棩������֧��RANGE,LIST,HASH,KEY�������͡�DCDBĿǰ�Ѿ����ڶ��������ķ�����֧��������MySQL������RANGE����������֧��LIST���㷨���ķ�������ԭ�����£�

 - DCDB�ĵ�һ�����������ǳ�˵��ˮƽ��֣��ֱ���Ŀǰʹ��HASH�㷨������Ŀ����ʹ�������ܾ��ȵķ�ɢ����˵���������ڵ�

 - DCDB�ĵڶ�������ʹ��RANGE�㷨������ˮƽ��ֵĻ����ϣ��ټ���һ���߼��ϵķ���������ʹ����ص������ܹ�����һ���߼�������������ͼ��

## ʹ�÷���

	Ŀǰ���������ľ����﷨���£���������id��Ϊˮƽ��ֵķֱ����shardkey����hired��Ϊ����������RANGE�ֶΣ�

```
	CREATE TABLE employees (
	    id INT NOT NULL,
	    fname VARCHAR(30),
	    lname VARCHAR(30),
	    hired DATE NOT NULL DEFAULT '1970-01-01',
	    separated DATE NOT NULL DEFAULT '9999-12-31',
	    job_code INT,
	    store_id INT
	)
	shardkey=id 
	PARTITION BY RANGE ( YEAR(hired) ) (
	    PARTITION p0 VALUES LESS THAN (1991),
	    PARTITION p1 VALUES LESS THAN (1996),
	    PARTITION p2 VALUES LESS THAN (2001)
	);
```

ע�⣺DCDB�����������ƣ�

	Shardkey�����ͱ�����int,bigint,smallint/char/varchar
	���������ֶΣ����ͱ�����DATE��DATETIME��֧�ֵ�ģʽΪRANGE����������ΪYEAR��MONTH��DAY


