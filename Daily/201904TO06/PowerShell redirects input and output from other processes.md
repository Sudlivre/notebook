# PowerShell重定向其它进程的输入和输出

```powershell
# 控制台程序路径
$MyConsole = 'E:\MyConsole.exe'
 
# 设置进程启动信息
$psi= New-Object System.Diagnostics.ProcessStartInfo
$psi.FileName = $MyConsole
# 设置进程自动重定向输入和输出
$psi.RedirectStandardInput = $true
$psi.RedirectStandardOutput = $true
$psi.CreateNoWindow = $true
$psi.UseShellExecute = $false
$process = New-Object System.Diagnostics.Process
$process.StartInfo = $psi
 
# 给System.Diagnostics.Process添加OutputDataReceived事件的订阅
$sub = Register-ObjectEvent -InputObject $process -EventName OutputDataReceived -action {
    # 打印源进程的输出信息
    Write-Host $Event.SourceEventArgs.Data
    # 注意： $Event输入自动化变量：
    # 包含了 Register-ObjectEvent 命令的Action参数中的上下文，
    # 尤其是Sender和Args
 
    # .Sender默认是Object对象，需要转换成Process对象
    $p = [System.Diagnostics.Process]$Event.Sender
 
    # 接收源进程的输出，并根据输出写入相应的输入
    if ($Event.SourceEventArgs.Data -eq "请输入A:")
    {
        Write-Host "自动输入：我喜欢"
        $p.StandardInput.WriteLine("我喜欢");
    }
    elseif ($Event.SourceEventArgs.Data -eq "请输入B:")
    {
        Write-Host "自动输入：PSTips.NET"
         $p.StandardInput.WriteLine("PSTips.NET");
    }
}
$process.Start()
$process.BeginOutputReadLine()
```
