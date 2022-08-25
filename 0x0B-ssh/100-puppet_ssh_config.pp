# Let’s practice using Puppet to make changes to our configuration file.
file { '/etc/ssh/ssh_config':
  ensure => present,
}
-> exec { 'Append IdentityFile':
  command => '/usr/bin/echo "    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config'
}
-> exec { 'Append PasswordAuthentication':
  command => '/usr/bin/echo "    PasswordAuthentication no" >> /etc/ssh/ssh_config'
}
