Imports IWshRuntimeLibrary
Public Class frmMain
    Dim txtlocation As String




    Private Sub Label1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Label1.Click

    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnSelect.Click
        Dim MyFolderBrowser As New System.Windows.Forms.FolderBrowserDialog
        MyFolderBrowser.Description = "Select The Folder To Install Application"
        MyFolderBrowser.RootFolder = Environment.SpecialFolder.MyComputer
        Dim dlgResult As DialogResult = MyFolderBrowser.ShowDialog()
        If dlgResult = Windows.Forms.DialogResult.OK Then
            txtlocation = MyFolderBrowser.SelectedPath
        End If
        lblLocation.Text = txtlocation
    End Sub

    Private Sub Label2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Label2.Click

    End Sub

    Private Sub Label3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles lblLocation.Click

    End Sub

    Private Sub btnSave_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnSave.Click
        Dim box As Integer
        box = MsgBox("Create a Desktop Shortcut?", vbYesNo)
        If box = vbYes Then
            Dim WshShell As WshShellClass = New WshShellClass
            Dim MyShortcut As IWshRuntimeLibrary.IWshShortcut
            ' The shortcut will be created on the desktop
            Dim DesktopFolder As String = Environment.GetFolderPath(Environment.SpecialFolder.DesktopDirectory)
            MyShortcut = CType(WshShell.CreateShortcut(DesktopFolder & "\Clock.lnk"), IWshRuntimeLibrary.IWshShortcut)
            MyShortcut.TargetPath = Application.StartupPath & "\Test.txt" 'Specify target app full path
            MyShortcut.Save()
        End If
        FileCopy("Test.txt", txtlocation + "\Test.txt")
        MsgBox("Installation Complete")
    End Sub

    Private Sub Button1_Click_1(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        End
    End Sub
End Class
