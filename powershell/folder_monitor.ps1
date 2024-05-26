$folderToMonitor = "E:\Games"

# Crear un objeto para monitorear eventos de archivos
$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $folderToMonitor
$watcher.IncludeSubdirectories = $true
$watcher.EnableRaisingEvents = $true

# Definir el tipo de eventos a monitorear
$watcher.NotifyFilter = [System.IO.NotifyFilters]::FileName -bor [System.IO.NotifyFilters]::DirectoryName

# Manejar el evento cuando se detecta una acción de archivo
$action = {
    $eventType = $event.SourceEventArgs.ChangeType
    $fileName = $event.SourceEventArgs.Name
    $fullPath = $event.SourceEventArgs.FullPath

    Write-Host "Se $eventType el archivo $fileName en $fullPath"
}

# Registrar el manejador de eventos
Register-ObjectEvent -InputObject $watcher -EventName "Created" -Action $action
Register-ObjectEvent -InputObject $watcher -EventName "Changed" -Action $action
Register-ObjectEvent -InputObject $watcher -EventName "Deleted" -Action $action
Register-ObjectEvent -InputObject $watcher -EventName "Renamed" -Action $action

# Mantener el script en ejecución
while ($true) {
    Start-Sleep -Seconds 1
}
