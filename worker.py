import paramiko
import time
import subprocess
import colors
class worker():
	def __init_(self):
		pass
	
	def wait_for_finish(self, stdout):
		while not stdout.channel.exit_status_ready():
			time.sleep(0.5)
	
	def do_work_local(self,cmd,isReturncode=False,isReturnStdout=False,isReturnStderr=False):
		res = {}
		pipe = subprocess.PIPE
		p = subprocess.Popen(cmd,stdout = pipe,stderr = pipe,shell=True)
		p.wait()
		if isReturncode:
			res['returncode'] = p.returncode
		if isReturnStdout:
			res['stdout'] = p.stdout.read()
		if isReturnStderr:
			res['stderr'] = p.stderr.read()
		return res
	
	def do_work_remote(self,ssh,cmd,isReturnStdout=False,isReturnExitStauts=False,isReturnStderr=False):
		res = {}
		stdin,stdout,stderr = ssh.exec_command(cmd)
		self.wait_for_finish(stdout)
		if isReturnStdout:
			res['stdout'] = stdout.read()
		if isReturnExitStauts:
			res['exitstatus'] = stdout.channel.recv_exit_status()
		if isReturnStderr:
			res['stderr'] = stderr.read()
		return res
	
	def check_service_status(self,ssh,cmd,serviceName):
		stdin, stdout, stderr = ssh.exec_command('%s'%cmd)
		if stdout.channel.recv_exit_status() == 0:
			print(color.color['green'] + '%s start sucessfully!'%serviceName + color.end)
		else:
			print(color.color['red'] + '%s start failed!'%serviceName + color.end)
	
	
	def ssh_handers(self,ip,port=22,isKeyLogin=True,passowrd=None):
		if isKeyLogin:
			pkey = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
		ssh = paramiko.SSHClient()
		try:
			if passowrd:
				ssh.connect(hostname=ip,port=port,username='root',pkey=pkey)
			else:
				ssh.connect(hostname=ip,port=port,username='root',passowrd=passowrd)
		except paramiko.SSHException as e:
            print(color.color['red'] + 'please check hostFile.txt to confirm the config is correct!'+color.end)
            print(color.color['red']+'the error IP is %s,ssh exception:%s'%(ip,e) + color.end)
            ssh.close()
            sys.exit(1)
		return ssh
	