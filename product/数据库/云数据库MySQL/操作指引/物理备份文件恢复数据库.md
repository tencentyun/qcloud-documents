## �����ݻָ����ݿ�
#### 1 ���ر����ļ�
���岽����ο���[���������˵��](https://cloud.tencent.com/doc/product/236/7123)
�����ļ��ɹ�������ͼ��
![](https://mc.qcloudimg.com/static/img/d02b20501dd1c42a95f2b7a74c266b98/1.png)

#### 2 ��ѹ�����ļ�
��ѹ�����ļ���
```
tar   xfv  backup.tgz
```
��ѯ��ѹ�����ɵ��ļ���������ɫ�����Ŀ¼�ļ�Ϊ��������ʱ CDB ���ڵ����ݿ�
![](https://mc.qcloudimg.com/static/img/62a64dc648edb040b9bbd9f2bbd65491/2.png)


#### 3 �����ļ��޸�
���ڴ��ڵİ汾���⣬�뽫��ѹ�ļ� backup-my.cnf �е�
innodb_checksum_algorithm��
innodb_log_checksum_algorithm��
innodb_fast_checksum��
innodb_page_size ��
innodb_log_block_size��
redo_log_version ע�͵�������ͼ��
![](https://mc.qcloudimg.com/static/img/10113311b33e398ce0df96ca419f7f45/3.png)

#### 4 �޸��ļ�����
�޸��ļ�������������ļ�����Ϊmysql�û�
```
chown -R mysql:mysql /home/mysql/backup/data
```
![](https://mc.qcloudimg.com/static/img/efbdeb20e1b699295c6a4321943908b2/4.png)

#### 5 ����mysqld���̲��ҵ�¼��֤
����mysqld���̣�����֤�����ɹ�
```
mysqld_safe --defaults-file=/home/mysql/backup/data/backup-my.cnf --user=mysql --datadir=/home/mysql/backup/data &
```
�ͻ��˵�¼mysql��֤
mysql  -uroot
![](https://mc.qcloudimg.com/static/img/346346626997b85385408ac728bf82ff/5.png)

ע�⣺
?	 �ָ���ɺ󣬱� mysql.user ���ǲ����� CDB �д������û�����Ҫ�½���
?	 �½��û�ǰ��ִ������ SQL��
```
delete from mysql.db where user<>'root' and char_length(user)>0;
delete from mysql.tables_priv where user<>'root' and char_length(user)>0;
flush privileges;
```





