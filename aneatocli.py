#!/usr/bin/env python
"""
aneatocli : a Neato Robot command and state querying cli.

Usage:
    aneatocli.py (--gc | --get-commands) <robotname>
    aneatocli.py [--go | --start-cleaning  ] <robotname>
    aneatocli.py [--stp | --stop-cleaning  ] <robotname>
    aneatocli.py [--pse | --pause-cleaning ] <robotname>
    aneatocli.py [--res | --resume-cleaning] <robotname>
    aneatocli.py [--base | --send-to-base  ] <robotname>
    aneatocli.py [--gi |--get-infos	   ] <robotname>
    aneatocli.py (--lgsc | --log-secrets) <mail>
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
    --lgsc , --log-secrets       Log the credentials into the json file.

"""
from sys import exit
from os.path import exists as chkf
from pprint import pprint
from getpass import getpass as getp
import json

try:
	from pybotvac import Robot
	from pybotvac import Account
except:
	print("pybotvac package is not installed.\n\nPlease run 'pip install pybotvac' from your command prompt\n")
	exit()
	
try:
    from docopt import docopt
except:
	print("docopt package is not installed.\n\nPlease run 'pip install docopt==0.6.2' from your command prompt\n")
	exit()
	

def logCreds():
    try:
    	mail=arguments["<mail>"]
        passwd=getp("Password:")
        acc=Account(mail,passwd)
    except:
        print("Cannot login. Please try again.")
        raise
    
    try:
        for robot in acc.robots:
            json_data="{\"serialID\": \""+robot.serial+"\" ,\"secretID\": \""+robot.secret+"\" ,\"traits\": \""+robot.traits[0]+"\" ,\"name\": \""+robot.name+"\"}"
            json_filename=robot.name+".json"
            with open(json_filename,"w") as json_file:
                json_file.write(json_data)
                json_file.close()

    except:
        print("Cannot write robot creds.")
        raise

def initRobot():
    json_filename=arguments["<robotname>"]+".json"
    try:
        with open(json_filename,"r") as json_file:
        	creds=json.load(json_file)
    except:
        print("File doesn't exist.")
        exit()
        
    try:
        robot = Robot(creds["serialID"],creds["secretID"],creds["traits"],creds["name"])
        return robot
    except:
        print("Cannot init the robot "+arguments["<robotname>"])
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
        exit()

    # write available cmds to file
    try:
        json_state_file=arguments["<robotname>"]+"-robotcommands.json"
        with open(json_state_file, "w") as json_file:
                json.dump(cmds, json_file)
        print("File "+json_state_file+" created")
    except:
        raise
        exit()
    
    
def getInfos():
   rob=initRobot()
   try:
        json_info_file=arguments["<robotname>"]+"-robotinfos.json"
        with open(json_info_file, "w") as info_file:
                json.dump(rob.state,info_file, indent=4)
                json.dump(rob.get_general_info().json(),info_file, indent=4)
                json.dump(rob.get_robot_info().json(),info_file, indent=4)
        print("File "+json_info_file+" created")
   except:
        print("Cannot retrieve infos.")
        raise
        exit()
    
    
    
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
	    print("Cannot "+act+" the robot.")
    	
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
    
if __name__ == '__main__':
        arguments = docopt(__doc__, version='aneatocli 0.1')
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


    
