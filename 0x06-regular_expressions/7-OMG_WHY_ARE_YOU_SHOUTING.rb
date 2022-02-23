#!/usr/bin/env ruby
puts ARGV[0].scan(/[^\d\s[a-z]\?]/).join
