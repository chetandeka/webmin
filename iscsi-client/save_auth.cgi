#!/usr/local/bin/perl
# Save authentication options

use strict;
use warnings;
require './iscsi-client-lib.pl';
our (%text, %config, %in);
&lock_file($config{'config_file'});
my $conf = &get_iscsi_config();
&error_setup($text{'auth_err'});

# Authentication method
&save_directive($conf, "node.session.auth.authmethod", $in{'method'});

# Login and password to iSCSI server
if ($in{'username_def'}) {
	&save_directive($conf, "node.session.auth.username", undef);
	&save_directive($conf, "node.session.auth.password", undef);
	}
else {
	$in{'username'} =~ /\S/ || &error($text{'auth_eusername'});
	$in{'password'} =~ /\S/ || &error($text{'auth_epassword'});
	&save_directive($conf, "node.session.auth.username", $in{'username'});
	&save_directive($conf, "node.session.auth.password", $in{'password'});
	}

# Login and password by the iSCSI server to the client
if ($in{'username_in_def'}) {
	&save_directive($conf, "node.session.auth.username_in", undef);
	&save_directive($conf, "node.session.auth.password_in", undef);
	}
else {
	$in{'username_in'} =~ /\S/ || &error($text{'auth_eusername_in'});
	$in{'password_in'} =~ /\S/ || &error($text{'auth_epassword_in'});
	&save_directive($conf, "node.session.auth.username_in",
			$in{'username_in'});
	&save_directive($conf, "node.session.auth.password_in",
			$in{'password_in'});
	}

# XXX more

&flush_file_lines($config{'targets_file'});
&unlock_file($config{'config_file'});
&webmin_log("auth");
&redirect("");
