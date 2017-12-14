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
- Poisons common desktop shortcuts to launch more shells using a fancy method (needs elevation, read below), giving incredibly stealthy persistence
- Options of getting elevated privs for many things including above
- Persistence options for all attacks
- Option to steal files (ftp and/or usb)

The really cool part is the desktop shortcut poisoning. Essentially, what it does is for each shortcut it finds, it creates a .cmd file that launches both the intended target of the shortcut, as well as the poison (payload). The CMD window doesn't even pop up on the screen, therefore it looks almost completely normal (there is a little CMD icon in the task bar for a split second). Using the elevated version, CMD mysteriously request for privileges. If it doesn't get it, it won't launch what ever the shortcut should normally launch, thus causing the user to keep trying and eventually figure out that it needs to give permissions to have it launch. Now you have a system level shell ;) (If you want to read more on how I accomplished this, check at the bottom of the readme)


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

### How I did the shortcut poisoning
---
After LOTS of trial and error, I finally figured out a good system for poisoning shortcuts. Essentially what this part of the payload does is create a `temp\` folder in the user's directory, and stores some payload files on there. Then the real shortcut on the desktop is replaces with a lookalike. This shortcut launches one of the new files store in the `temp\` folder: `f o.cmd`. This has a space in it because windows `.lnk` files won't keep double quotes surrounding their target unless the file name has a space in it. The Double quotes are required for when the target's home directory has a space in it _(I'm over here thinking about everything, right!?)_. `o f.cmd` launches the expected program, as well as another payload file silently using a VBS script (or you can have it just execute what ever CMD script you want!). You can also choose to drop the elevated version, which asks for system privileges before executing, thus giving the next commands system level privileges _(did somebody say infinite silent system level shells?)_. From there, you can really customize and choose what you want to happen. I have included a powershell script for downloading a reverse shell, as well as a local powershell script to spawn a shell.
