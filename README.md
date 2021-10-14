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
    cd ECE567_Team11_Minor
    pip install -r requirements.txt

    # run analyze.py and view the output graph
    python3 analyze.py test_data.csv 
    firefox drivers_vs_time.png

    # deactive the virtual envrinment (go back to normal)
    deactivate
```
