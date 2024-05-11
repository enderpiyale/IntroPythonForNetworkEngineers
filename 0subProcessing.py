import subprocess

hosts = ['192.168.1.1', '192.168.1.2', '192.168.1.3','192.168.1.4','192.168.1.5','192.168.1.6','192.168.1.7','192.168.1.8']

def pingTest(hosts):
    reached = []
    not_reached = []

    for ip in hosts:
        try:
            subprocess.check_output(["ping", "-c", "1", ip])
            reached.append(ip)
        except subprocess.CalledProcessError:
            not_reached.append(ip)
    return reached, not_reached

def printResult(reached, not_reached):
    for r in reached:
        print(r, 'is REACHABLE')
    print('\n')

    if not not_reached:
        print('everything is fine!')
    else:
        for r in not_reached:
            print(r, 'is UNREACHABLE')
    print('\n')  

reachedresult, unreachedResult = pingTest(hosts)

printResult(reachedresult,unreachedResult)