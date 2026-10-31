$ErrorActionPreference = 'Stop'
$subject = 'CN=SubjectZone'

# Prompt for the .pfx password instead of hardcoding it (signing material is not committed).
$pwd = Read-Host -Prompt 'Password for build\msix\SubjectZone.pfx' -AsSecureString

# remove any previous cert with the same subject so publisher identity stays stable
Get-ChildItem Cert:\CurrentUser\My | Where-Object { $_.Subject -eq $subject } | Remove-Item -Force

$cert = New-SelfSignedCertificate `
    -Type Custom `
    -Subject $subject `
    -KeyUsage DigitalSignature `
    -FriendlyName 'SubjectZone MSIX signing' `
    -CertStoreLocation 'Cert:\CurrentUser\My' `
    -TextExtension @('2.5.29.37={text}1.3.6.1.5.5.7.3.3', '2.5.29.19={text}')

$thumb = $cert.Thumbprint
Write-Host "thumbprint=$thumb"
Write-Host "subject=$($cert.Subject)"

Export-PfxCertificate -Cert $cert -FilePath 'build\msix\SubjectZone.pfx' -Password $pwd | Out-Null
Export-Certificate -Cert $cert -FilePath 'build\msix\SubjectZone.cer' -Type CERT | Out-Null
Write-Host "pfx and cer exported"
