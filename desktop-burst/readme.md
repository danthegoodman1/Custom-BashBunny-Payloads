# Windows Desktop Burst
---
- Author: DanTheGoodman
- Target: Windows 10 only

### Description
---
What prank is better than something that is completely harmless, but requires the victim to spend tedious time reversimng your actions?

**Enter the Windows Desktop Burst:**
This payload is simple, it creates a configurable amount of virtual desktop spaces in Windows 10 (which are quite annoying to delete).



### Dependencies
---
None :)



### Configuration (optional)
---
In the b.ps1 file, you can change the amount of desktops made by changing the range in the while loop.
```
While ($i -le 10)
    {
    $i
    $KeyShortcut::CreateVirtualDesktopInWin10()
    $i++
    }
```


### Status:
---
|LED|Status|
|---|---|
|Yellow single blink|Running payload|
|Blue Single blink|Copying any files to Bash Bunny|
|Solid Green|Loop Completed|

---
This is my first payload for the Bash Bunny, and I have finals right now, and I am doing this instead of studying so it's not fancy but I wanted to make something.
