import subprocess
command = ['/bin/uname', '-a']
result = subprocess.run(command, stdout=subprocess.PIPE, timeout=10**-1)

print(result)
