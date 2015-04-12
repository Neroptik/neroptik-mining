# neroptik-mining

## Setup Ultima Online with EasyUO (for Ashworld freeshard players)

* Install Ultima Online from Ashworld website:
	* http://www.ashworld-uo.com/download/AshWorld-UO.exe
* Checkout this repository. You will obtain:
	* The mining script
	* legacy_to_mul tool
	* EasyUO 1.5.1.284
* Convert UOP map files to MUL files with **legacy_to_mul** tool
* Copy generated files from "Output" directory to UO directory
	* By default: "C:\Program Files (x86)\Ultima Online\"
* Start EasyUO.exe as Administrator
	* Open the script **NeroptikMiner2.0.euo**
	* Start a new client
	* Choose "Ashworld.exe"
* Open regedit as Administrator
	* Find the key "HKCUser/Software/EasyUO/"
	* The value of "ExePath" should be the UO directory. If not then create it.
* Start the script

Enjoy !

I found another guide from MSDN on how the user can suppress system and application error messages from occurring on an embedded system. The registry location is at the following, by default the value data is 0 and we should change it to 2 to set all messages to invisible. HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Windows\ErrorMode. Weirdly even after doing all that, it’s still not enough to disable the error window when the game server crashes. So I continue digging and I found that there’s another important registry key which you need to modify in order to totally suppress the “.exe has stopped working” dialog.” Go to the following registry location and change the value data to 1. HKEY_CURRENT_USER\Software\ Microsoft\Windows\Windows Error Reporting\DontShowUI

Read More: https://www.raymond.cc/blog/disable-program-has-stopped-working-error-dialog-in-windows-server-2008/