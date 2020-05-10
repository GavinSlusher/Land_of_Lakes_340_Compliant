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

## Running the app on Flip

1. If not running the virtual environment - `source ./LoL/bin/activate`
2. `export FLASK_APP=run.py`
3. `python -m flask run -h 0.0.0.0 -p [port number] --reload`

Now, your website should be accessible at http://flipN.engr.oregonstate.edu:YOUR_PORT_NUMBER

## Running the app persistently on Flip!

1. Follow steps 1 and 2 above if not already done
2. `gunicorn run:app -b 0.0.0.0:YOUR_PORT_NUMBER -D` 
