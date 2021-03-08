#!/usr/bin/perl

use strict;
use warnings;

if (scalar @ARGV < 2) {
    die "Usage: $0 seconds command [args...]\n";
}

$| = 1;  # Ensure output appears

my($interval, @command) = @ARGV;

# print ">>> interval=$interval command=(@command)\n";

while (1) {
    print "sleep ", $interval - time % $interval, "\n";
    sleep $interval - time % $interval;
    system @command; # TODO: Handle errors (how?)
}