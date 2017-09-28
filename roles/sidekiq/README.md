## WARNING: This role will be deprecated very soon

All of the functionality provided by this role and more is available in the [DebOps project](http://debops.org). If you are using some of my roles in conjunction with each other, you will find the move to DebOps most pleasurable.

This role will be **removed** from the **galaxy** and from **github** anywhere from 42 microseconds to 2-3 weeks after you read this message.

---


## What is ansible-sidekiq? [![Build Status](https://secure.travis-ci.org/nickjj/ansible-sidekiq.png)](http://travis-ci.org/nickjj/ansible-sidekiq)

It is an [ansible](http://www.ansible.com/home) role to manage a sidekiq worker for a rails application.

### What problem does it solve and why is it useful?

It is usually a good idea to create a service out of your ruby applications when it comes time to deploy them. This allows you to easily manage it in the future without having to worry about things like sourcing environments because the service script would handle all of the dirty work for you.

It gives you access to these commands after it's setup:

- `sudo service sidekiq start`
- `sudo service sidekiq stop`
- `sudo service sidekiq restart`
- `sudo service sidekiq reload`
- `sudo service sidekiq status`

## Role variables

Below is a list of default values along with a description of what they do.

```
# The path to the config file.
sidekiq_config_path: "{{ rails_deploy_path }}/config/sidekiq.yml"

# The log command or path.
# If you want to use syslog set it to:  2>&1 | logger -t sidekiq
sidekiq_log_path: -L {{ rails_deploy_path }}/log/sidekiq.log

# Should a restart be forced?
sidekiq_force_restart: false
```

## Example playbook

For the sake of this example let's assume you have a group called **app** and you have a typical `site.yml` file.

To use this role edit your `site.yml` file to look something like this:

```
---
- name: ensure app servers are configured
- hosts: app

  roles:
    # Insert other roles here to provision the server before managing sidekiq.
    - { role: nickjj.sidekiq, tags: [app, rails] }
```

Let's say you want to edit a few defaults, you can do this by opening or creating `group_vars/all.yml` which is located relative to your `inventory` directory and then making it look something like this:

```
---
sidekiq_force_restart: true
```

#### Does it automatically restart a crashed process?

Nope, init.d scripts don't do that. What you get is a service that starts on bootup and restarts when a code change was detected. If you want the process to be monitored you will want to hook up something like [monit](http://mmonit.com/monit), [runit](http://smarden.org/runit) or [god](http://godrb.com/).

I personally prefer monit because the API for adding new things to monitor is very nice and it optionally exposes a web front end. If you're interested here's a link to my [nickjj.monit role](https://github.com/nickjj/ansible-monit).

## Installation

`$ ansible-galaxy install nickjj.sidekiq`

## Dependencies

It depends on the [nickjj.rails](https://github.com/nickjj/ansible-rails) role. This role must be ran before sidekiq.

## Requirements

Tested on ubuntu 12.04 LTS but it should work on other versions that are similar.

## Ansible galaxy

You can find it on the official [ansible galaxy](https://galaxy.ansible.com/list#/roles/947) if you want to rate it.

## Example sidekiq config

Make sure sidekiq is set to write out a pidfile and logfile.

`config/sidekiq.yml`:

```
---
:pidfile: /full/path/to/your/project/tmp/sidekiq.pid
:concurrency: 25
:queues:
  - default
```

## License

MIT