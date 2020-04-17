#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#Persistent
SetTimer, CheckTime, 60000 ;check time every minute
Return

CheckTime:
if (A_Hour . A_Min=0830) or (A_Hour . A_Min=1630) or (A_Hour . A_Min=2301)

 RunWait random_fact.py > stdout.txt
 FileRead, Clipboard, stdout.txt
 Send ^v
 Send {Enter}
Return


