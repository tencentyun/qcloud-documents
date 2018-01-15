## Migrate Data Offline Using Command Line Tools

### 1. Generating the SQL Files to be Imported

The SQL files to be imported can be generated in the following two ways:

> Note: It is not recommended to manually construct SQL files, because the manually constructed SQL files are prone to have errors on syntax, data and so on, which may result in import failures.

Method 1:  Files exported by the export function in the cloud database console (For details, see: [Cold Backup Data Extraction](/doc/product/236/冷备数据提取));

Method 2: Data files exported by the MySQL tool mysqldump:

(1) The data files exported by mysqldump must be compatible with the SQL standard of the purchased cloud database's MySQL version. You can log in to the cloud database via select version (); to obtain corresponding MySQL version information.

(2) The data export method for mysqldump is as follows:


```
shell> mysqldump [options] db_name [tbl_name ...]
```

Options are the export options, db_name is the database name, and tbl_name is the table name.

For more details on mysqldump data export, please refer to [MySQL Official Manual](http://dev.mysql.com/doc/refman/5.1/en/mysqldump.html).

### 2. Restrictions on Imported Data Files

The SQL file name can contain English letters/numbers/underscores, but cannot contain "test" characters.

### 3. Character Set Encoding Issues of Imported Data Files

3.1. If the imported data files do not specify a character set encoding, the one set by the cloud database will be executed.

3.2. If the imported data files have specified a character set encoding, the specified one will be executed.

3.3. If the character set encoding of imported data files is different from those of the cloud database, it will display unreadable codes.
For more information about character set encoding issues, please refer to "#6. Character Set" in "Service Limits".

