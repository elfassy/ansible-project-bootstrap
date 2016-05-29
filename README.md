Bootstrap for your Ansible deploy.


```
ansible-playbook -i inventory/production provision.yml
```

You can watch a demo [here](https://vimeo.com/133059608).

The content of this project was created following the Ansible best practices:

https://docs.ansible.com/playbooks_best_practices.html#content-organization

# Recommended usage

1. Clone this project to a private repository and use it to version your organization infrastructure.

2. For each application, create an inventory and group_vars.
 
3. keep things simple.

# Included roles

* user (creates a deploy specific user and copies ssh keys)
* dev (installs common packages like autoconf and build essentials)
* git
* imagemagick
* nginx
* nodejs
* phantomjs
* postgresql-client
* postgresql-server
* puma
* rails
* rails-deploy
* redis
* ruby
* sidekiq
