Ansible Role Testing Demo
=========================

Use Molecule and Tox to orchestrate Ansible Role testing across Linux Containers and EC2 hosts.

The Demo uses :

1. Vagrant (or an a BYO RHEL7 instance)
1. Molecule
1. Tox
1. Testinfa
1. SCL Python36
1. RHEL and CentOS Containers
1. AWS EC2
1. Python 2.7 and Python 3.6
1. Ansible 2.2, 2.4 and 2.7
1. The Caddy Web Server

The demo uses Tox to create four python virtualenvs.  Two for python 2.7 using Ansible 2.2 and Ansible 2.7 and two for python 3.6 using Ansible 2.4 and Ansible 2.7.  You can choose any virtualenv to use for interactive role development and testing with Molecule.  A sample role is provided which installs and starts the Caddy web server.  Testinfra tests are provided which can be invoked interactively.

Vagrant Setup Instructions
--------------------------

1. Checkout the repository : git@github.com:lshake/molecule-demo.git
2. Change to the working directory : '''cd molecule-demo'''
3. Check out the ansible role requirements: '''ansible-galaxy install -r ./requirements.txt
1. You *must* set Red Hat Portal credentials, RHN_USERNAME and RHN_PASSWORD and the Pool ID RHN_POOLID.  Developer credentials are sufficient.
2. If you plan to use AWS EC2 test environments, you should set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY credentials.
4. Create the vagrant instance: '''vagrant up'''
5. Reload the vagrant instance to pick up SELinux changes required for Python3 testing: '''vagrant reload''' 

Environment Setup Instructions
------------------------------

1. Log into the vagrant box: '''vagrant ssh'''
2. Enable Python 3 installed from software collections: '''scl enable rh-python36 bash'''
3. Change to working directory: '''cd demo/lshake.caddy'''
4. Build all four python virtual envs: '''tox --notests'''

Role Development
----------------

1. Activate a virtualenv: '''. .tox/py27-ansible27/bin/activate'''
2. Create the infrastructure using Docker: '''molecule create'''
3. Run the role against the new infrastructure: '''molecule converge'''
4. Make changes to the role and run converge again.
5. Run the lint checking against the role: '''molecule lint'''
6. Run the testinfra checks:  '''molecule verify'''
7. Run the full test suite:  '''molecule test'''

Using AWS EC2
-------------

The above role development cycle uses linux containers which are defined in the default senario of the molecule directory.   You can run the above using AWS EC2 instances by specifying the EC2 senario passed to molecule : '''molecule test -s ec2'''
