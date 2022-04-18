#install puppet-lint 2.5.0 via puppet

package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem',
  source   => 'https://rubygems.org',
}
