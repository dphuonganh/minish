# minish


# Introduction

You have been using the terminal, and implicitly the shell, for a couple of months now. But have you ever wondered how they work? What is a shell, actually? What happens when you run a `ls`?

The shell is what we call a *command-line interpreter*; basically it reads user input, identifies the appropriate command, and executes it. What you might not know yet is that in most cases it executes a stand-alone program and supervises its execution. It also has some nifty advanced functionalities that you will discover as you work on coding your own shell.

The shell project starts with this 1-week, solo project for everybody to look into the basic mechanisms of the shell. It will be followed by a 3-week, group project where you'll develop the most advanced shell you possibly can!

(After that, save for a couple of algorithms projects, we'll move on to web-related projects. I know you have been waiting for them!)


## Your mission

You will code a basic command-line interpreter (also known as a shell) in Python. Your shell will loop over the following sequence: prompt the user for input, read the input, execute it (that's what we call a REPL - a read-eval-print loop).

You also have to implement a few "built-ins", which are internal commands of your shell (they are just regular functions in your Python code).

Your program will be called `intek-sh.py` and will be present at the root of your git repository.


## Specifications

Here's what you will do:

* Have a basic loop that starts with a prompt "intek-sh$ ", then reads whatever the user types in, handles the input (<- that's the tricky part), and displays the prompt again.
* To handle the input, you need to parse it (that is, to break it down into its components). The first word is the command name, next are its arguments. When you have got the command name, you can look for the corresponding executable file.
* When given a command to execute, the shell looks for the executable program (as known as the binary file) in the directories indicated by the PATH environment variable. It will then execute the first binary corresponding to the command name that it finds. So you should start by parsing the PATH string to have the list of directories (keeping the order they appear in) you must search in.
* When you have located the binary, execute the command in a subprocess and wait for it to finish before displaying the shell prompt again.
* You need to output an error message if the binary cannot be found or you don't have the permission to execute it.
* You will also implement some built-ins. See the next section.

Bash will be your shell of reference (for behaviours, error messages, ...). If you don't know how something works, **test it on bash**.

![shell_session__1_.gif]()


## Built-ins to implement

Built-ins are not external binaries, but internal functions of the shell: that means it's not a stand-alone program launched by the shell, it's just some Python code executed directly inside the shell. If you understand the difference between calling a function and doing an `os.system("ls -la")` (which I think you do 🙃), you are good to go.

The built-ins need to be handled differently from the other commands: you need to identify those special commands before attempting to look for a binary. 

You will implement the following built-ins: 

* cd [directory]
* printenv [variable]
* export [variables...]
* unset [variable]
* exit [exit_code]


## builtin examples

Look carefully at the examples below, and do your own tests with bash to figure out the error cases.

```python
# let's start our program from the bash shell
bash-3.2$ ./intek-sh.py


# we print the HOME environment variable with the printenv builtin
intek-sh$ printenv HOME
/Users/laurie
# let's check where we are with the pwd command (this one is not a builtin!)
intek-sh$ pwd
/Users/laurie/shell/minish
# cd without argument should take us to the directory indicated in the HOME variable.
intek-sh$ cd
# it worked!
intek-sh$ pwd
/Users/laurie
# cd with a directory specified as argument can take us there
intek-sh$ cd shell/minish
intek-sh$ pwd
/Users/laurie/shell/minish


# let's do a test with the export & unset builtins. Those allow you to add and remove variables from the environment.
# first, let's try with a variable that doesn't exist. printenv cannot find it.
intek-sh$ printenv TEST
# we set that variable with export
intek-sh$ export TEST=something
# as it's now an environment variable, printenv can find it
intek-sh$ printenv TEST
something
# let's remove it from the environment
intek-sh$ unset TEST
# nothing to print, it's gone
intek-sh$ printenv TEST
intek-sh$


# talking about being gone...
intek-sh$ exit 1
exit
# our program has exited, we are back in the bash shell
bash-3.2$
```


## Last notes

- When you modify the environment of a shell, that environment should be passed on to the programs launched by the shell. In Python this will happen if you modify `os.environ` directly.

- If a command starts with `./`, the shell will attempt to execute it in the current directory.

- You'll notice that with your regular shells, you can put whitespaces between arguments, it doesn't matter.

- You may NOT use the shell=True option when using the subprocess functions. This would effectively launch a subshell that would handle what your intek-sh itself is supposed to do.


## Bonuses:

#### Prepare yourself !
There won't be any bonuses for this project, as it's just a preliminary project for next week's full-fledged shell.

However you can start your research about:

* globbing
* how to implement pipes & redirections
* how to handle signals
* quoting (quotes & escape characters)
* command-line edition with * the curses module
the command history
* command completion

You can even go the extra mile and research:

* how to implement shell script (which means handling the full POSIX grammar!)
* job control
* ...

The shell is a open-ended project that will be as easy or as interesting as you want it to be. Have fun!

