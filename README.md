# usefulMiscScripts
Usefull 'one day build' scripts. Doesn't quite need a repo but too cool for a gist. Effectively just a back up and documentation for various scripts and projects I've worked on over time. Doubles as a referencing tool for programming techniques learned over time but not used frequently enough to recite by heart. The more that is added the more GitHub's language percentages becomes reflective of my actual programming language knowlege.

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

## generateWebpageIconButtons
Assign your favorite websites to **hardcoded.txt**. Run **generateHTML.py** and an **index.html** with be generated. For each website specified, it will try to grab the favicon/apple icon for the website (if the website has one) then use that icon as a button which links to said webpage.<br>
<br>
The overall layout/styling of the buttons and html is pretty relative (adjusts depending on screen size/browser) but could use some work. Usecase is for quick/customizeable access to favorite or repeatedly visited websites. Still needs work, but the goods are there.<br>
Example:<br>
<br>
<img src='https://camo.githubusercontent.com/d4b39be4ed30f6367d39ca0989e6ecb4b66596ce/68747470733a2f2f7331312e706f7374696d672e6f72672f7538766166387765722f3332313332312e706e67'>

## eBayFeesCalculator.py
This is a spin off of the basic **Fun Money and Net Paycheck Calculator** calculator GUI. Only for calculating sales on eCommerce Platforms. With eCommerce Poll Taxes, shipping and such in mind. ie: hardcoded PayPal fee of .029% (+.30 cent transaction fee), ebay's 10% of the total sale, manual shipping cost. All minus gross sales to get net profit. So on, so forth. TODO: Margins, Markup, etc...
<a href='https://github.com/BiTinerary/usefulMiscScripts/blob/master/eBayFeesCalculator.py'><img src='https://github.com/BiTinerary/usefulMiscScripts/blob/master/ebayCalculatorImg.png'></a>
