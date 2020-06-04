from pyfiglet import Figlet
class L7inspector:
    def inspect(self,keyword,attacktype,log):
        f = open(log, mode='r', encoding='utf-8')
        r = open("report.txt", "a")
        for i in f.readlines():
            if keyword in i:
                r.write("\nPossible "+attacktype+" web payloads found:\n")
                r.write(i)
    def summarize(self):
        rr=open("report.txt", mode='r', encoding='utf-8')
        data=rr.read()
        print("\n**** Summary of Inspection ****")
        print("\nNumber of SQL injection Payloads Found: "+str(data.count("SQL-Injection")))
        print("\nNumber of Cross Site Scripting Payloads Found: " + str(data.count("Cross-Site-Scripting(XSS)")))
        print("\nNumber of LDAP Injection Payloads Found: " + str(data.count("LDAP-Injection")))
        print("\nNumber of Directory Traversal Payloads Found: " + str(data.count("Directory-Traversal")))
        print("\nNumber of Command Injection Payloads Found: " + str(data.count("Command-Injection")))
        print("\nNumber of XPATH Injection Payloads Found: " + str(data.count("XPATH-Injection")))
        print("\nNumber of CRLF Injection Payloads Found: " + str(data.count("CRLF-Injection")))
        print("\n\n\nReport saved to same project directory with name report.txt")

if __name__== "__main__":
    banner = Figlet(font='drpepper')
    name = Figlet(font='small')
    print(banner.renderText("L7-Inspector"))
    print("\t\t\t\t\tBetter know if someone tried to infiltrate your exposed web server!!!")
    print("\n#########################################################")
    print("\t\t\tAuthor:\tSumeet-R")
    print("###########################################################")
    print("\nEnter your webserver access log path:")
    inputvalue = input("\n>>")
    sendkeyword=L7inspector()
    logfile=inputvalue
    print("\nInspecting Log file "+logfile+" ...")

    # SQL-Injection Payloads
    with open("payloads/sqli", 'r') as f:
        for line in f:
            sendkeyword.inspect(str(line.strip()),"SQL-Injection",logfile)

    # Cross-Site-Scripting(XSS) Payloads
    with open("payloads/xss", 'r') as f:
        for line in f:
            sendkeyword.inspect(str(line.strip()),"Cross-Site-Scripting(XSS)",logfile)

    # Directory-Traversal Payloads
    with open("payloads/dirtrav", 'r') as f:
        for line in f:
            sendkeyword.inspect(str(line.strip()),"Directory-Traversal",logfile)
    # Command-Injection Payloads
    with open("payloads/cmdi", 'r') as f:
        for line in f:
            sendkeyword.inspect(str(line.strip()),"Command-Injection",logfile)

    # LDAP-Injection Payloads
    with open("payloads/ldapi", 'r') as f:
        for line in f:
            sendkeyword.inspect(str(line.strip()),"LDAP-Injection",logfile)

    # XPATH-Injection Payloads
    with open("payloads/xpath", 'r') as f:
        for line in f:
            sendkeyword.inspect(str(line.strip()), "XPATH-Injection", logfile)

    # CRLF-Injection Payloads
    with open("payloads/crlf", 'r') as f:
        for line in f:
            sendkeyword.inspect(str(line.strip()), "CRLF-Injection", logfile)

    #Summarize
    sendkeyword.summarize()


