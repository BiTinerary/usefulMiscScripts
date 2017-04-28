# usefulMiscScripts
Usefull 'one day build' scripts. Doesn't quite need a repo but too cool for a gist.

## youtube-dl GUI Getter
<img src="https://github.com/BiTinerary/usefulMiscScripts/blob/master/youtube-dlGuiGetter.png?raw=true"><br>
Credit: <a href='https://github.com/rg3/youtube-dl'>https://github.com/rg3/youtube-dl</a><br>
youtube-dlGUIGetter.exe is a binary that runs the GUI w/o python as dependency

## WOL.py
Place in <a href='http://www.friendlyarm.com/index.php?route=product/product&path=69&product_id=151'>NanoPi Neo Air's</a> `\if-up.d` directory. When I get home, send magic packet. On startup/wakeup run script to start music/pandora.

## ESP8266 SD Card WebServer
Back up of and credz to <a href='https://github.com/esp8266/Arduino/blob/master/libraries/ESP8266WebServer/examples/SDWebServer/SDWebServer.ino'>this</a> `.ino` file.

## Fun Money and Net Paycheck Calculator
Figure out upcoming paycheck after taxes. Figure out budget after bills due.
* TODO: Output array vars to .txt/.csv
* TODO: Static numbers for income tax, wage, etc... for offline usage.
<img src='https://s11.postimg.org/qlagttk77/fun_Money_Tkinter.png'>

## csvToDictAddColumns.py
Get sums of specified columns, from a .csv with headers. Pretty print output like "Headers: columnSum". Run from CLI by passing .csv file name as argument. ie: **`python csvToDictAddColumns.py example.csv`**

## Send SMS From Command Line
Place **sendText.bat** in `C:\Windows\System32\` directory. This contains a python command to run the **sendSMS.py** script from `%USERPROFILE%\Desktop\` while passing one argument string. Usage example: <br><kbd>![Windows Key][oldwinlogo]</kbd>+<kbd>R</kbd> then run `sendText "AnyString Here"` This sends email/SMS to phone number provided on line 3 of `gmailCreds.txt` from gmail address on line 1 and 2.

[oldwinlogo]: http://i.stack.imgur.com/T0oPO.png
