# -*- coding: utf-8 -*-
'''inv matter for auto pub. 101.camp
'''

__version__ = 'pub101so v.210424.1642'
__author__ = 'Zoom.Quiet'
__license__ = 'MIT@2021-04'

#import io
import os
#import re
import sys
import time
#import datetime
#import json
#import marshal as msh
#import subprocess
#import logging

#import sys
import logging
#logging.basicConfig()
logging.basicConfig(level=logging.CRITICAL)
_handler = logging.StreamHandler()
_formatter = logging.Formatter("[%(levelname)s]%(asctime)s:%(name)s(%(lineno)s): %(message)s"
                #, datefmt='%Y.%m.%d %H:%M:%S'
                , datefmt='%H:%M:%S'
                )
_handler.setFormatter(_formatter)
LOG = logging.getLogger(__name__)
#LOG = logging.getLogger()
LOG.setLevel(logging.DEBUG)  
LOG.propagate = False

LOG.addHandler(_handler)
#LOG.debug('load LOG level')







from pprint import pprint as pp
#pp = pprint.PrettyPrinter(indent=4)
from pprint import pformat

#import platform
#os_name = platform.system()
#del platform

#import subprocess





from invoke import task
#from fabric.context_managers import cd
from textwrap import dedent as dedentxt

SROOT = os.path.dirname(os.path.abspath(__file__))
#print(SROOT)
REPO_ROOT = os.path.dirname(SROOT)#'..'    #os.environ.get("REPO_ROOT")
#print(REPO_ROOT)

AIM = 'site'


@task 
def ver(c):
    '''echo crt. verions
    '''
    print('\n\t powded by {}'.format(__version__))


#   support stuff func.
def cd(c, path2):
    os.chdir(path2)
    print('\n\t crt. PATH ===')
    c.run('pwd')

#@task 
def ccname(c, site):
    '''base cfg. write CNAME into aim path
    '''
    #print(CSITES[site]['CNAME'])
    _aim = '%s/%s/CNAME'%(CAMPROOT, CSITES[site]['ghp'])
    _cmd = "echo {} > {}".format(CSITES[site]['CNAME'], _aim)
    print(_cmd)
    #c.run(_cmd, hide=False, warn=True)
    #c.run('cat %s'% _aim, hide=False, warn=True)
    return None

#@task 
def sync4media(c):
    c.run('cp -rvf img %s/'% AIM, hide=False, warn=True)
    c.run('ls %s/'% AIM, hide=False, warn=True)
    c.run('pwd')


#@task 
def sync4readme(c):
    c.run('cp -rvf README.md %s/'% AIM, hide=False, warn=True)
    c.run('ls %s/'% AIM, hide=False, warn=True)
    c.run('pwd')



@task 
def bu(c):
    '''usgae MkDocs build AIM site
    '''
    c.run('pwd')
    #c.run('mkdocs -q build', hide=False, warn=True)
    #c.run('mkdocs -v build', hide=False, warn=True)
    c.run('mkdocs build', hide=False, warn=True)

#@task 
def pu(c):
    '''push gl manuscript...
    '''
    _ts = '{}.{}'.format(time.strftime('%y%m%d %H%M %S')
                     , str(time.time()).split('.')[1][:3] )

    c.run('pwd')
    c.run('git st', hide=False, warn=True)
    #c.run('git add .', hide=False, warn=True)
    #c.run('git ci -am '
    c.run('git imp '
          '"inv(loc) MkDocs upgraded by DAMA (at %s)"'% _ts
                    , hide=False, warn=True)
    #c.run('git pu', hide=False, warn=True)

#   'rsync -avzP4 {static_path}/media/ {deploy_path}/media/ && '


#@task 
def gh(c, site):
    '''$ inv gh [101|py] <- push gh-pages for site publish
    '''
    global CAMPROOT
    global CSITES
    print(CAMPROOT)
    
    #ccname(c, site)
    sync4media(c)
    sync4readme(c)
    
    _ts = '{}.{}'.format(time.strftime('%y%m%d %H%M %S')
                     , str(time.time()).split('.')[1][:3] )
    
    _aim = '%s/%s'%(CAMPROOT, CSITES[site]['ghp'])
    cd(c, _aim)
    #os.chdir(AIM)
    #with cd('site/'):
    #c.run('pwd')
    c.run('ls')
    c.run('git st', hide=False, warn=True)
    #c.run('git add .', hide=False, warn=True)
    #c.run('git ci -am '
    c.run('git imp '
          '"pub(site) gen. by MkDocs as invoke (at %s)"'% _ts
                    , hide=False, warn=True)
    #c.run('git pu', hide=False, warn=True)


@task 
def pub(c, site):
    '''$ inv pub [101|py] <- auto deploy new site version base multi-repo.
    '''

    c.run('ls')
    
    print('auto deplo NOW:')
    #return None
    return None
    bu(c)

    pu(c)
    #ccname(c)
    #sync4media(c)
    gh(c, site)
    ver(c)

    return None






