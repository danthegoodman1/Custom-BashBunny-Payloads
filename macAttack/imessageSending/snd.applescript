tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "Dad" of targetService
        send "hey" to targetBuddy
end tell
