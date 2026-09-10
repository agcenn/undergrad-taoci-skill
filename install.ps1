param(
    [string]$Destination = "$HOME\.agents\skills\undergrad-taoci"
)

$ErrorActionPreference = "Stop"
$RepoUrl = "https://github.com/agcenn/undergrad-taoci-skill.git"

$Parent = Split-Path -Parent $Destination
New-Item -ItemType Directory -Force -Path $Parent | Out-Null

if (Test-Path $Destination) {
    Write-Error "Destination already exists: $Destination"
    exit 1
}

git clone $RepoUrl $Destination
Write-Host "Installed undergrad-taoci to: $Destination"
Write-Host "Restart/reopen Codex if the skill does not appear immediately."
