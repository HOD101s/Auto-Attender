:: USAGE: joinmeet MEETCODE
:: Replace 'd' below with drive where script is stored. Not required if stored in c drive.
:: d:
call cd path\\to\\auto-attender
:: If using python environment uncomment and change next line
:: call activate python_environment
call python joinmeet.py -c %1
:End
PAUSE