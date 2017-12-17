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
- Change all icon logos to a "hacked" image to scare the crap out of people

The really cool part is the desktop shortcut poisoning. Essentially, what it does is for each shortcut it finds, it creates a .cmd file that launches both the intended target of the shortcut, as well as the poison (payload). The CMD window doesn't even pop up on the screen, therefore it looks almost completely normal (there is a little CMD icon in the task bar for a split second). Using the elevated version, CMD mysteriously request for privileges. If it doesn't get it, it won't launch what ever the shortcut should normally launch, thus causing the user to keep trying and eventually figure out that it needs to give permissions to have it launch. Now you have a system level shell ;) (If you want to read more on how I accomplished this, check at the bottom of the readme)


### Dependencies
---
None :)



### Configuration (optional)
---
With this payload, some configuration is required for SO MUCH POWER.

Basic configuration is done in the `p.ps1` file, in which you will determine whether you want to use the various attacks of SuperShell.

More complicated, and not as essential configuration is for the shortcut poisoning (which just happens to be the centerpiece of SuperShell). To do so, we need to populate `z.cmd` with some actual commands. I would recommend making that file some sort of .bat/.cmd payload generated for dropping an Empire or Metasploit shell. However one important thing to do is modify the payload file so that it does not delete itself! Also, you can just rename a .bat file to a .cmd file as they are almost the same thing. Elevation is something that should be done after a little lateral movement, because many times elevation is not even necessary, and it could potentially set off some red flags.

SuperShell comes with shortcuts for Google Chrome, Firefox (57/Quantum), MS Office, Excel, Powerpoint, and Outlook. They all simply execute `temp/_ f o.cmd` minimized (the blank being different for each shortcut), which executes the real program and z.cmd invisibly using i.vbs. The following are the different names for executing the different programs:

|Program|File Name|
|---|---|
|Google Chrome|`gc f o.cmd`|
|Mozilla Firefox|`mf f o.cmd`|
|MS Word|`msw f o.cmd`|
|MS Excel|`mse f o.cmd`|
|MS

If you want to really scare people into becoming more secure (if you are doing security testing at your company or something along those lines), enable the `$hacked_shortcut_logo` variable, which will take all existing shortcuts and give them the logo of `hl.ico` in the switch directory.


### Status:
---
Can I make files to check progress?

|LED|Status|
|---|---|
|Yellow single blink|Running payload|
|Solid Green|Payload executed, give it a few seconds to do its thang|

### How I did the shortcut poisoning
---
After LOTS of trial and error, I finally figured out a good system for poisoning shortcuts. Essentially what this part of the payload does is create a `temp\` folder in the user's directory, and stores some payload files on there. Then the real shortcut on the desktop is replaces with a lookalike. This shortcut launches one of the new files store in the `temp\` folder: `_ f o.cmd` (the blank being different for each shortcut). This has a space in it because windows `.lnk` files won't keep double quotes surrounding their target unless the file name has a space in it. The Double quotes are required for when the target's home directory has a space in it _(I'm over here thinking about everything, right!?)_. `_ f o.cmd` launches the expected program, as well as another payload file silently using a `i.vbs` (or you can have it just execute what ever CMD script you want!). You can also choose to drop an elevated version, which asks for system privileges before executing, thus giving the next commands system level privileges _(did somebody say infinite silent system level shells?)_. So interestingly enough most installations place their shortcuts in the `C:\Users\Public\Desktop` folder. This isn't a problem, because we can just delete them! The shortcut is then replaced on the user's desktop. This will most likely cause the icons to rearrange a little, which shouldn't be a tip-off to users because my icons on windows shift around all the time! An important thing to note is that this will delete the shortcuts for other user accounts on the computer, but you probably aren't pentesting a family who doesn't have their own devices. From there, you can really customize and choose what you want to happen. I have included a powershell script for downloading a reverse shell, as well as a local powershell script to spawn a shell.
