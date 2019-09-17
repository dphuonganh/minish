#!/usr/bin/env python3
import os
from sys import exit
from subprocess import run


def built_cd(dicr):
    '''
    os.chdir is the method chdir changes the current working directory to
    the given path.It returns None in all the cases
    '''
    if len(dicr) == 1:
        try:
            os.chdir(os.environ["HOME"])
        except KeyError:
            print("intek-sh: cd: HOME not set")
    elif len(dicr) > 2:
        print("cd: too many arguments")


def find_file(dicr):
    if len(dicr) == 2:
        dicrpath = dicr[1]
        if not os.path.exists(dicrpath):
            print("cd: '{}': No such file or directory".format(dicrpath))
        else:
            os.chdir(dicrpath)


def built_printenv(command):
    '''
    set that variable whandleith export
    '''
    len_in = len(command)
    dictenv = os.environ
    if len_in == 1:
        for key, value in dictenv.items():
            print(key + "=" + value)
    else:
        for i in range(1, len_in):
            if command[i] in dictenv:
                variable = command[i]
                print(dictenv[variable])


def built_export(command):
    # Print the string in the list of variable, TEST = string
    len_in = len(command)
    if len_in == 1:
        for key, value in os.environ.items():
            print("declare "+" -x" + key + "=" + value)
    else:
        for i in range(1, len_in):
            variables = command[i].split("=")
            if len(variables) == 1:
                os.environ[variables[0]] = ""
            else:
                os.environ[variables[0]] = variables[1]


def built_unset(command):
    # nothing to print, it's gone
    len_in = len(command)
    if len_in == 1:
        pass
    else:
        for i in range(1, len_in):
            if command[i] in os.environ:
                os.environ.pop(command[i])
            else:
                pass


def check_exit(in_exit):
    # exit with number
    anh = "exit" + "\n" + "intek-sh: exit:"
    try:
        if len(in_exit) == 1 or int(in_exit[1]):
            print("exit")
    except ValueError:
            print(anh)
    exit()


def run_exist(run_in_exs):
    """
    os.F_OK is check value to pass as the mode parameter of access()
    to test the existence of path.
    os.X_OK Value to include in the mode parameter of access()
    to determine if path can be executed.
    For example printenv PATH and find usr by command (which) ls -a /usr/bin,
    we check for by which.
    """
    filepath = run_in_exs[0]
    # run_in_exs is remove wc in the path
    if "./" in filepath:
        if not os.access(filepath, os.F_OK):
            print("intek-sh: %s: No such file or directory" % filepath)
        elif not os.access(filepath, os.X_OK):
            print("intek-sh: %s: Permission denied" % filepath)
        else:
            run(filepath)
        return
    elif os.environ.get("PATH"):
        # find in path by command
        for item in os.environ["PATH"].split(':'):
            if os.path.exists(item + "/" + run_in_exs[0]):
                # this is the list (run)
                run([item + "/" + run_in_exs.pop(0)] + run_in_exs)
                return
    print("intek-sh: " + filepath + ": command not found")


def main():
    try:
        while True:
            input_str = input("intek-sh$ ")
            conver_input = input_str.split()
            if len(conver_input) == 0:
                pass
            else:
                function = conver_input[0]
                if function == "cd":
                    built_cd(conver_input)
                    find_file(conver_input)
                elif function == "printenv":
                    built_printenv(conver_input)
                elif function == "export":
                    built_export(conver_input)
                elif function == "unset":
                    built_unset(conver_input)
                elif function == "exit":
                    check_exit(conver_input)
                else:
                    run_exist(conver_input)
    except EOFError:
        pass


if __name__ == "__main__":
    main()
