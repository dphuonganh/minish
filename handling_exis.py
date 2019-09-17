def handle_exit(in_exit):
    str = '123456789'
    if len(in_exit) == 1:
        print('exit')
    elif in_exit[1] in str:
        print('exit')
    else:
        print("intek-sh$ exit" + "\n" + "intek-sh: exit:")
    exit()


def run_ex_bin(run_in):
    filepath = run_in[0]
    if './' in filepath:
        if not os.access(filepath, os.F_OK):
            print('intek-sh: {}: No such file or directory'.format(filepath))
        elif not os.access(filepath, os.X_OK):
            print('intek-sh: {}: Permission denied'.format(filepath))
        else:
            run(filepath)
        return
    elif os.environ.get("PATH"):
        for item in os.environ['PATH'].split(':'):
            if os.path.exists(item + '/' + run_in[0]):
                run([item + '/' + run_in.pop(0)] + run_in)
                return
    print("intek-sh: " + filepath + ": command not found")
