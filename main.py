#!/usr/bin/env python3
from subprocess import run
from datetime import datetime

class c:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def cluster():
    check_cluster = run("kubectl config current-context", shell=True, capture_output=True, text=True)
    check_namespace = run("kubectl config get-contexts -ojson | grep '*' | awk -F ' ' '{ print $5 }'", shell=True, capture_output=True, text=True)
    return c.FAIL + check_cluster.stdout.rstrip() + c.ENDC + '|' + c.HEADER + check_namespace.stdout.rstrip() + c.ENDC

def when():
    return c.OKGREEN + datetime.now().strftime("%H:%M:%S %Z") + c.ENDC

def git():
    check_git = run("git branch | grep '*' | awk -F ' ' '{ print $2 }'", shell=True, capture_output=True, text=True)
    if check_git.returncode == 0:
        return c.OKBLUE + check_git.stdout.rstrip() + c.ENDC + ' |'
    else:
        return '-'

def pwd():
    check_pwd = run("pwd", shell=True, capture_output=True, text=True)
    pathlist = check_pwd.stdout.split('/')
    segment = pathlist[len(pathlist)-1].rstrip()
    if segment == 'willnewby':
        return '~'
    else:
        return segment

def who():
    check_who = run("whoami", shell=True, capture_output=True, text=True)
    return c.BOLD + check_who.stdout.rstrip() + "@roci" + c.ENDC

print("{}({}) {} {}/{}".format(when(), cluster(), git(), who(), pwd()), end='')
