Since the solution for data importing from one distributed database to another is special, we take mysqldump as an example to summarize the importing steps as follows:

## Step 1: Install mysqldump (MariaDB version)
Purchase linux CVM and use `yum install mariadb-server` to install mysqldump.


## Step 2: Export the table structure of the source database
```
    mysqldump --no-tablespaces --default-character-set=utf8 --hex-blob --skip-add-drop-table -c 
	--skip-lock-tables --skip-opt --skip-triggers --skip-comments --skip-tz-utc --skip-extended-insert 
	--skip-disable-keys --skip-quote-names --no-data -uusername -ppassword -hxxx.xxx.xxx.xxx -Pxxxxx 
	dbname | grep -v '^\/\*\!40' > schema.sql;
```

> Note: --default-character-set=utf8 will be set based on your source table.
> -uusername is an account with permissions (-u: keyword).
> -ppassword is a password (-p: keyword).
> -hxxx.xxx.xxx.xxx -Pxxxxx is the IP and port of the database instance.
> dbname is the database name.
> Filter /*!40...*/ statements out with grep, because they are not supported in DCDB.

## Step 2: Export the table data of the source database
```
    mysqldump --no-tablespaces --default-character-set=utf8 --hex-blob --skip-add-drop-table -c 
	--skip-lock-tables --skip-opt --skip-triggers --skip-comments --skip-tz-utc --skip-extended-insert 
	--skip-disable-keys --skip-quote-names --no-create-info -uandelwu -pandelwu -hxxx.xxx.xxx.xxx -Pxxxxx 
	dbname | grep -v '^\/\*\!40' > data.sql;
```

> Note: --default-character-set=utf8 will be set based on your source table.
> -uusername is an account with permissions (-u: keyword).
> -ppassword is a password (-p: keyword).
> -hxxx.xxx.xxx.xxx -Pxxxxx is the IP and port of the database instance.
> dbname is the database name.
> Filter /*!40...*/ statements out with grep, because they are not supported in DCDB.

## Step 3: Create a database in the destination database
```
    mysql --default-character-set=utf8 -uusername -ppassword -hxxx.xxx.xxx.xxx -Pxxxxx -e "create database dbname;";
```

> Note: --default-character-set=utf8 will be set based on your destination table.
> -uusername is an account with permissions (-u: keyword).
> -ppassword is a password (-p: keyword).
> -hxxx.xxx.xxx.xxx -Pxxxxx is the IP and port of the database instance.
> dbname is the database name.



## Step 4: Import table structure in the destination database+
```
    mysql --default-character-set=utf8 -uusername -ppassword -hxxx.xxx.xxx.xxx -Pxxxxx dbname < schema.sql
```

> Note: --default-character-set=utf8 will be set based on your destination table.
> -uusername is an account with permissions (-u: keyword).
> -ppassword is a password (-p: keyword).
> -hxxx.xxx.xxx.xxx -Pxxxxx is the IP and port of the database instance.
> dbname is the database name.

## Step 5: Import table data in the destination database
```
    mysql --default-character-set=utf8 -uusername -ppassword -hxxx.xxx.xxx.xxx -Pxxxxx dbname < data.sql
```

>Note: If auto-increment field is used in the source table and error "Column 'xx' specified twice" occurred while importing data, you need to delete the backquotes in the auto-increment field (cat schema.sql | tr "\`" " " > schema_tr.sql) of schema.sql, drop database, and then repeat steps 3 to 5 using the modified schema_tr.sql.
