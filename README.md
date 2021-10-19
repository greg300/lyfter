# Team11_Minor
Software Engineering 567, Team 11, Minor Project.

## Running on Ubuntu 20.04

Here are the steps for running the code in a virtual environment on
Ubuntu 20.04.

```
    # install git and virtualenv
    sudo apt install git python3-virtualenv

    # create a virual environment called "Team11" and activate it
    virtualenv Team11
    cd Team11/
    . bin/activate

    # clone our repository and install python package dependencies
    # Note: cloning using this URL is for Read Only access. Need
    # to set-up access token or ssh to be able to commit back
    git clone https://github.com/greg300/ECE567_Team11_Minor
    cd ECE567_Team11_Minor/src
    pip install -r requirements.txt

    # run the simulator over 100 iterations
    python3 main.py 100

    # run analyzer.py and view the output graph
    python3 analyzer.py ../results.csv
    firefox ../drivers_vs_time.png

    # deactive the virtual envrinment (go back to normal)
    deactivate
```


## Running on Windows

Running in Windows using VSCode requires installing Python, VSCode and
Git. Here are directions for running `tests_simulation.py`:

1. Navigate to Microsoft store and install Python. Python 3.9 is
   currently available.
2. Install VSCode from the [download page](code.visualstudio.com/Download).
3. Install Git. I was able to do this within VSCode by selecting the
   Source code icon on the left and "Clone Repository". The download
   likely came from [git-scm.com](https://git-scm.com/download/win). Once it is
   installed, you can clone a GitHub repository by entering the
   repository URL in the text box at the middle top and selecting a
   directory on your local machine to place it.
4. Select the file explorer view in the left hand pane, select
   `tests_simulation.py` in the file list and press F5 to run. The
   console output at in the bottom pane of VSCode show the output.
