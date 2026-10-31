@echo off
set "JAVA_HOME=D:\SubjectZone\SubjectZone\_tools\jdk\jdk-17.0.20.1+1"
set "PATH=%JAVA_HOME%\bin;%PATH%"
set "ANDROID_HOME=C:\Users\Dell\AppData\Local\Android\Sdk"
set "ANDROID_SDK_ROOT=%ANDROID_HOME%"
cd /d "D:\SubjectZone\SubjectZone\android"
java -version
call gradlew.bat %*
exit /b %ERRORLEVEL%
