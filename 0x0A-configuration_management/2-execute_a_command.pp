#kills process named killmenow

exec { '/killmenow':
  command  => 'pkill killmenow',
  path     => '/usr/bin',
  provider => shell,
}
