# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "shakey/rhel7.6"
  config.vm.hostname = 'ansiblevagrant'
  config.vm.provider "virtualbox" do |v|
    v.memory = 4096
    v.cpus = 2
  end
  config.vm.provision "ansible" do |ansible|
    ansible.limit = "all"
    ansible.extra_vars = {
      rhsm_username: ENV['RHN_USERNAME'],
      rhsm_password: ENV['RHN_PASSWORD'],
      rhsm_pool_ids: ENV['RHN_POOLID'],
      rhsm_repos: [
        'rhel-7-server-rpms',
        'rhel-7-server-extras-rpms',
        'rhel-server-rhscl-7-rpms',
        'rhel-7-server-ansible-2.7-rpms'
      ]
    }
    ansible.playbook = "site.yml"
    ansible.verbose = "vv"
  end
end
