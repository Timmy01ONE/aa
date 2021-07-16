#!/usr/bin/svn python
import paramiko
transport = paramiko.Transport(('10.0.0.103', 22))
transport.connect(username='root', password='123456')
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('less.txt', '/tmp/test_from_win')
# 将remove_path 下载到本地 local_path
sftp.get('/root/test', 'fromlinux.txt')

transport.close()