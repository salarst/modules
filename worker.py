import paramiko
import time
import subprocess
import colors
class worker():
	def __init_(self):
		pass
	
	def wait_for_finish(self, stdout):
		'''
		wait for paramiko.SSHClient excute command finish
		'''
		while not stdout.channel.exit_status_ready():
			time.sleep(0.5)
	
	def do_work_local(self,cmdList,returncode=False,returnStdout=False,returnStderr=False):
		'''
		execute linux commands with subprocess module and if return* is Ture
		return the reqiurement values.
		'''
		res = {}
		pipe = subprocess.PIPE
		p = subprocess.Popen(cmdList,stdout = pipe,stderr = pipe)
		p.wait()
		if isReturncode:
			res['returncode'] = p.returncode
		if isReturnStdout:
			res['stdout'] = p.stdout
		if isReturnStderr:
			res['stderr'] = p.stderr.read()
		return res
	
	def do_work_remote(self,ssh,cmd,returnStdout=False,returnExitStauts=False,returnStderr=False):
		'''
		use paramiko to excute command on remote server and return the results of excution. 
		'''
		res = {}
		stdin,stdout,stderr = ssh.exec_command(cmd)
		self.wait_for_finish(stdout)
		if isReturnStdout:
			res['stdout'] = stdout
		if isReturnExitStauts:
			res['exitstatus'] = stdout.channel.recv_exit_status()
		if isReturnStderr:
			res['stderr'] = stderr.read()
		return res
	
	def check_service_status(self,ssh,cmd,serviceName):
		'''
		check service status.you can use commands like 'netstat -tlnp | grep $port' 
		or 'systemctl status $service' to check the service status
		'''
		stdin, stdout, stderr = ssh.exec_command('%s'%cmd)
		if stdout.channel.recv_exit_status() == 0:
			print(color.color['green'] + '%s start sucessfully!'%serviceName + color.end)
		else:
			print(color.color['red'] + '%s start failed!'%serviceName + color.end)
	
	
	def ssh_handers(self,ip,port=22,keyLogin=True,passowrd=None):
		'''
		ssh login to linux server with key or password.
		if keyLogin is True,use ssh key login,else use password.
		if password is none,will raise an exception
		'''
		if isKeyLogin:
			pkey = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		try:
			if not passowrd:
				ssh.connect(hostname=ip,port=port,username='root',pkey=pkey)
			else:
				ssh.connect(hostname=ip,port=port,username='root',passowrd=passowrd)
		except paramiko.SSHException as e:
            print(color.color['red'] + 'please check hostFile.txt to confirm the config is correct!'+color.end)
            print(color.color['red']+'the error IP is %s,ssh exception:%s'%(ip,e) + color.end)
            ssh.close()
            sys.exit(1)
		return ssh
	