def main():
        try:
            while True:
                    input_str = input('intek-sh$ ')
                    conver_input = input_str.split()
                    if len(conver_input) == 0:
                        pass
                    else:
                        func = conver_input[0]
                        if func == 'exit':
                            handle_exit(conver_input)
                        elif func == 'printenv':
                            printenv(conver_input)
                        elif func == 'cd':
                            cd(conver_input)
                        elif func == 'export':
                            export(conver_input)
                        elif func == 'unset':
                            unset(conver_input)
                        else:
                            run_ex_bin(conver_input)
        except EOFError:
            pass
