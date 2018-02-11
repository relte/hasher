#define MyAppName "Hasher"
#define MyAppVersion "0.1.0"
#define MyAppPublisher "Krzysztof Lament"
#define MyAppURL "https://github.com/Tykzz/hasher"

[Setup]
AppId={{7D28203F-10A4-456B-AE30-622A075AD6DE}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
AppSupportURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
OutputBaseFilename=hasher-v{#MyAppVersion}-setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: ".\..\..\build\exe.win-amd64-3.6\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Run]
Filename: "{app}\install.exe";

[UninstallRun]
Filename: "{app}\uninstall.exe";
