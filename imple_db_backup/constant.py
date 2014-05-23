#coding:utf-8

PGDUMP_CMD_PATH = '/usr/lib/postgresql/9.1/bin'

LOCALHOST = 'localhost'

PORT = '5432'

DB_USER = 'postgres'

DB_NAME = 'huitong'

# 数据库备份目录
BACKUP_PATH = '/home/why/db_backup'
# 在备份目录下建立一个待传输的目录，当备份数据库时会同时将备份的文件copy一份到该目录。当传输完成后，清空该目录。
WAIT_TRANS_PATH = '/home/why/db_backup/waiting_transfer'
# 传输而来的dmp放在该目录，同时copy一份到上级目录。当要更新数据库时，只需要查看该目录是否有文件就可，更新完成，清空该目录。
WAIT_UPDATE_PATH = '/home/why/db_backup/waiting_update'

HAS_TRANSFER = False

CENTER_IDENT = '535'

CENTER_ADDRESS = '27.136.230.5'

CENTER_USER = 'root'

CENTER_PWD = '123456'

HT_IDENT = '96315'

HT_ADDRESS = '27.136.100.3'

HT_USER = 'root'

HT_PWD = '123456'