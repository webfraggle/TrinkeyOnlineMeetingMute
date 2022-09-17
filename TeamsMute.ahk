#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


; MICROSOFT TEAMS - Toggle Mute
+^!M::  ; Ctrl-Alt-Shift + M
WinGet, winid, ID, A	; Save the current window ID

; Can't find a reliable way to find the Teams Window with my Teams Version
;if WinExist("Microsoft Teams")
;{
	WinActivate, ahk_exe Teams.exe
	Send, ^+M   ; Teams' native Mute shortcut
;    WinActivate ahk_id %winid% ; Restore previous window focus, if you want
	return
;}

