I first tried putting the 'q or 1=1 value to check whether it worked it displayed a different pic. I then put a single quote ' in the login page to check whether there was a vulnerability, it gave a huge error i.e error page. I checked out the source code and checked the various sql queries used to detect the exploit. I then used the following "' or 1; --" in the login page with a random password. It then directed me to the forum page. I checked the source code and found the secret hidden in the source code.