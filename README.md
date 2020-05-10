# Land of Lakes README

## Initial Setup

1. `git clone https://github.com/GavinSlusher/Land_of_Lakes_340_Compliant.git`
2. Make sure you're in the right directory. If in flip, run `bash`. 
3. `virtualenv LoL -p $(which python3)`
4. `source ./LoL/bin/activate` to run the virtual environment
5. `pip3 install --upgrade pip`
6. `pip install -r requirements.txt`

## Running the app locally

1. If not running the virtual environment - `source ./LoL/bin/activate`
2. `export FLASK_APP=run.py`
3. `flask run`
