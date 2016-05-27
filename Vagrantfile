# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.provider :virtualbox do |vb, override|
    host = RbConfig::CONFIG["host_os"]

    if host =~ /darwin/ # OS X
      # sysctl returns bytes, convert to MB
      vb.memory = `sysctl -n hw.memsize`.to_i / 1024 / 1024 / 3
      vb.cpus = `sysctl -n hw.ncpu`.to_i
    elsif host =~ /linux/ # Linux
      # meminfo returns kilobytes, convert to MB
      vb.memory = `grep 'MemTotal' /proc/meminfo | sed -e 's/MemTotal://' -e 's/ kB//'`.to_i / 1024 / 2
      vb.cpus = `nproc`.to_i
    end
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
  end

  box = ENV['VAGRANT_BOX'] || 'ubuntu/trusty64'
  config.vm.box = box
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.provision "ansible" do |ansible|
    ansible.limit = 'all'
    ansible.inventory_path = "inventory/development"
    ansible.playbook = "#{ENV['PLAYBOOK'] || 'provision'}.yml"
  end
  config.ssh.forward_agent = true
end
