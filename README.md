# Neato Controls
Hi everyone !

Aneatocli is a command line interface for [pybotvac](https://github.com/stianaske/pybotvac).
Neato Control was the GUI based interface I made for pybotvac but I discontinued it due to licensing issue with PyQt4.

## USAGE

For the `aneatocli.py` script :

```bash
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
    --gc , --get-commands        Get the available commands and write them to file '<robotname>-robotcommands.json'
    --gi, --get-infos            Get various infos about the current robot and write them to file '<robotname>-robotinfos.json'
    --lgsc , --log-secrets       Log the credentials into the file '<robotname>.json'.
```
