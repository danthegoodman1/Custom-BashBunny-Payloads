# Super Shell
---
- Author: DanTheGoodman
- Creds: thehappydinoa, sebkinne, Nutt, Rob Milner (http://www.squiggle.org/2010/02/powershell-script-to-mass-change-shortcut-path/)

### Description
---
An incredibly customizable and powerful Bash Bunny payload which absolutely annihilates windows.
It Can:
- Delete the runline history
- Gets reverse shell
- Poisons common desktop shortcuts to launch more shells using an invisible vbs launcher that is copied to the host
- Options of getting elevated privs for many things including above
- Persistence options for all attacks
- Option to steal files (ftp and/or usb)
- Switch out exe files for poisoned ones.

The really cool part is the desktop shortcut poisoning. Essentially, what it does is for each shortcut it finds, it creates a .cmd file that launches both the intended target of the shortcut, as well as the poison (payload). Since windows gets really grumpy about setting the icon for the shortcut, so I have it set to the little monitor so it just looks like windows glitched out or something ;)

Now ever time the shortcut is executed, it will pop up a little window, so that might make people catch on to something. So, as a more targeted approach, you can use the .exe poisoning to get around this.

### .exe Poisoning instructions:
---
To be honest, this part of the payload is not for total newcomers, which is why it is disabled by default. What it does is replace the existing .exe file with one that has been wrapped with a payload (using something like the shell project). Every time it is executed it then runs the real program and reverse shell.

### Dependencies
---
None :)



### Configuration (optional)
---
By default the payload is set to pull all .pdf and .docx files from the Desktop, Downloads, and Documents folders. You can add new items/locations by making new xcopy lines in the x.cmd file.


### Status:
---
Can I make files to check progress?

|LED|Status|
|---|---|
|Yellow single blink|Running payload|
|Solid Green|Files copied|

---
This is my first payload for the Bash Bunny, and I have finals right now, and I am doing this instead of studying so it's not fancy but I wanted to make something.
