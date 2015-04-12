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
	* Set the value of "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Windows\ErrorMode" to 2
	* Set the value of "HKEY_CURRENT_USER\Software\ Microsoft\Windows\Windows Error Reporting\DontShowUI" to 1
* Install RestartOnCrash and configure it in order to restart the UO client on crash
* Install Java JRE
* Run the sikuli script StartScript.sikuli as Administrator. This script launch the EasyUO script when the client crashed.
* Enjoy !
