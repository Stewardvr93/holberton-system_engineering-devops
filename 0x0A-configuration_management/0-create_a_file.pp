# A file is created in the path of 'file'

file { '/tmp/school':
    ensure  => 'present',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
}
