# L7-Inpector
A python based security auditing tool that can find various injection payloads from web server and application logs

<h4>Short working demonstration</h4>
https://www.youtube.com/watch?v=ycG3h_wuMTE

<br>
<h4>Description</h4>
The tool can be used to find various Layer7 injection payloads from any webserver logs when fed into its input. The payloads used as a conditional strings can be found in it's payload directory and can be further used in building SIEM,WAF,IDPS rules.
<br>
Currently following attack payloads are supported as follows:
<br>
1) SQL Injection<br>
2) Cross-Site-Scripting<br>
3) LDAP Injection<br>
4) Directory Traversal<br>
5) Command Injection<br>
6) XPATH Injection<br>
7) CRLF Injection<br>

<h4>Installation on Linux</h4>
1) sudo apt-get install python3
<br>
2) sudo apt-get install python3-pip
<br>
3) cd ~
<br>
4) git clone https://github.com/Sumeet-R/L7-Inspector
<br>
5) cd L7-Inspector/
<br>
6) pip3 install -v -r requirements.txt
<br>
7) python3 L7-Inspector.py
