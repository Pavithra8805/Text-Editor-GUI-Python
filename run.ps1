# Helper PowerShell script to launch the Modern Text Editor
# Note: You may need to allow running local scripts (Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned)
$python = 'C:\Program Files\Python313\python.exe'
$script = Join-Path -Path $PSScriptRoot -ChildPath 'main.py'
& $python $script
