# Automate_mails
this code will automate the sending of mail to user

first go to config.py and replace the dummy mail values with original values

import smtplib for [sending and recieving] mail related functionality 



sender gmail settings
----------------------
initially add 2 step verification in security tab

then select others dropdown  and add app name to sign in  

it will generate temporary password use that as a password



how to activate virtual environment
-------------------------------------
pip install virtualenv

python -m venv MailVenv


MailVenv/Scripts/activate.bat        //In CMD

MailVenv/Scripts/Activate.ps1        //In Powershel


pip list

pip freeze > requirements.txt       //to list modules installed in txt file

deactivate                       // to deactivate venv