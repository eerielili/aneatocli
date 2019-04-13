#!/usr/bin/env python
"""
aneatocli : a Neato Robot command and state querying cli.

Usage:
    aneatocli.py (--gc | --get-commands) <robotname>
    aneatocli.py (--go | --start-cleaning  ) <robotname>
    aneatocli.py (--stp | --stop-cleaning  ) <robotname>
    aneatocli.py (--pse | --pause-cleaning ) <robotname>
    aneatocli.py (--res | --resume-cleaning) <robotname>
    aneatocli.py (--base | --send-to-base  ) <robotname>
    aneatocli.py (--gi |--get-infos   ) <robotname>
    aneatocli.py (--lgsc | --log-secrets) <mail>
    aneatocli.py (--ltst | --log-tests)
    aneatocli.py -h | --help
    aneatocli.py -v | --version

Options:
    -h , --help                  Show this message.
    -v , --version               Show version.
    --go , --start-cleaning      Tell the robot to start cleaning.
    --stp , --stop-cleaning      Tell the robot to stop cleaning.
    --pse , --pause-cleaning     Tell the robot to pause cleaning.
    --res , --resume-cleaning    Tell the robot to resume cleaning.
    --base ,--send-to-base       Tell the robot to go back to its dock.
    --gc , --get-commands        Get the available commands.
    --gi, --get-infos		     Get various infos about the current robot.
    --lgsc , --log-secrets       Log the credentials into the json file.

"""
#from os.path import exists as chkf
#from pprint import pprint
from getpass import getpass as getp
import json

try:
	from pybotvac import Robot
	from pybotvac import Account
except:
	print("pybotvac package is not installed.\n\nPlease run 'pip install pybotvac' from your command prompt\n")
	raise
	
	
try:
    from docopt import docopt
except:
	print("docopt package is not installed.\n\nPlease run 'pip install docopt==0.6.2' from your command prompt\n")
	raise
	

# I cannot make this function works with nosetest. Will see later, as it's not critical and login can be tested via the command line.
def logTest():
    print("Welcome here, it's the test for the Neato Controls command line interface (cli), which is at the core of it. There may be more test in the future.\n For the moment, there's a login test.\n ")
    try:
        validMail=False
        while not validMail:
            mail=raw_input("\nProvide your Neato Robotics login e-mail: ")
            
            # 7 characters because : a@b.foo
            if len(mail) >= 7 and "@" in mail and "." in mail:
                validMail=True
            else:
                validMail=False

        passwd=getp("Password:")
        acc=Account(mail,passwd)
    except:
        print("\nCannot login. Please try again.")
        raise
    
    try:
        print("\n Here are your robots :\n")
        for robot in acc.robots:
            print(robot)
    except:
        print("\nCannot write robot creds.")
        raise	

def logCreds(mailarg=""):
    try:
        if len(arguments["<mail>"]) <= 0 and len(mailarg) > 0 and "@" in mailarg:
            mail=mailarg
        elif len(arguments["<mail>"]) > 0 and "@" in arguments["<mail>"]:
            mail=arguments["<mail>"]
        else:
            print("The mail provided is invalid.")
        passwd=getp("Password:")
        acc=Account(mail,passwd)
    except:
        print("\nCannot login. Please try again.")
        raise
    
    try:
        for robot in acc.robots:
            json_data="{\"serialID\": \""+robot.serial+"\" ,\"secretID\": \""+robot.secret+"\" ,\"traits\": \""+robot.traits[0]+"\" ,\"name\": \""+robot.name+"\"}"
            json_robot_file=robot.name+".json"
            with open(json_robot_file,"w") as json_robot:
                json_robot.write(json_data)
                json_robot.close()
            print("File "+json_robot_file+" created")

    except:
        print("\nCannot write robot creds.")
        raise

def initRobot():
    json_filename=arguments["<robotname>"]+".json"
    try:
        with open(json_filename,"r") as json_robot:
        	creds=json.load(json_robot)
    except:
        print("File doesn't exist.")
        
        
    try:
        robot = Robot(creds["serialID"],creds["secretID"],creds["traits"],creds["name"])
        return robot
    except:
        print("\nCannot init the robot "+arguments["<robotname>"])
        raise
    
def getCmds():
    rob=initRobot()
    getInfos()
    # get the available commands
    try:
        cmds = rob.state["availableCommands"]
    except:
        print("HTTP Error or Network failure.")
        raise
        

    # write available cmds to file
    try:
        json_state_file=arguments["<robotname>"]+"-robotcommands.json"
        with open(json_state_file, "w") as json_robot_commands:
                json.dump(cmds, json_robot_commands)
        print("File "+json_state_file+" created")
    except:
        raise
        
    
    
def getInfos():
   rob=initRobot()
   try:
        json_info_file=arguments["<robotname>"]+"-robotinfos.json"
        with open(json_info_file, "w") as json_robot_info:
                json.dump(rob.state, json_robot_info, indent=4)
                json.dump(rob.get_general_info().json(), json_robot_info, indent=4)
                json.dump(rob.get_robot_info().json(), json_robot_info, indent=4)
        print("File "+json_info_file+" created")
   except:
        print("\nCannot retrieve infos.")
        raise
        
    
    
    
def funCallFromArgs(simpleArg, verboseArg, func, *args):
    if arguments[simpleArg] or arguments[verboseArg]:
        func( *args )


def actC(act):
    rob=initRobot()
    
    def checkActRun(robofunc):
    	
	try: 
	    if rob.state["availableCommands"][act]:
	    	robofunc()
	except:
	    print("\nCannot "+act+" the robot.")
    	
    if "start" in act:
    	checkActRun(rob.start_cleaning)
    elif "stop" in act:
    	checkActRun(rob.stop_cleaning)
    elif "pause" in act:
    	checkActRun(rob.pause_cleaning)
    elif "resume" in act:
    	checkActRun(rob.resume_cleaning) 
    elif "goToBase" in act:
    	checkActRun(rob.send_to_base)

#if __name__ == '__main__':
arguments = docopt(__doc__, version='aneatocli 0.8')
#nts:useful pour debugging
#pprint(arguments)
    
    
funCallFromArgs("--go","--start-cleaning",actC,"start")
funCallFromArgs("--stp","--stop-cleaning",actC,"stop")
funCallFromArgs("--pse","--pause-cleaning",actC,"pause")
funCallFromArgs("--res","--resume-cleaning",actC,"resume")
funCallFromArgs("--base","--send-to-base",actC,"goToBase")
funCallFromArgs("--gc","--get-commands",getCmds)
funCallFromArgs("--gi","--get-infos",getInfos)
funCallFromArgs("--lgsc","--log-secrets",logCreds)
funCallFromArgs("--ltst","--log-tests",logTest)

    
