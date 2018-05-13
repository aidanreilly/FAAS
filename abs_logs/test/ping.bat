::hit the AWS functions

echo. 
echo %date% %time% >> a-recur-local256.txt
C:\Apache24\bin\abs.exe -k -c 50 -n 250 https://k9kec8cpgc.execute-api.us-east-1.amazonaws.com/dev/ping >> a-recur-local256.txt

echo.
echo %date% %time% >> a-recur-local512.txt
C:\Apache24\bin\abs.exe -k -c 50 -n 250 https://0qwlklexf2.execute-api.us-east-1.amazonaws.com/dev/ping >> a-recur-local512.txt

echo.
echo %date% %time% >> a-recur-local1GB.txt
C:\Apache24\bin\abs.exe -k -c 50 -n 250 https://1fd9j85pbj.execute-api.us-east-1.amazonaws.com/dev/ping >> a-recur-local1GB.txt

echo.
echo %date% %time% >> a-recur-local2GB.txt
C:\Apache24\bin\abs.exe -k -c 50 -n 250 https://l1zp09xozj.execute-api.us-east-1.amazonaws.com/dev/ping >> a-recur-local2GB.txt

::hit the Google functions

echo.
echo %date% %time% >> g-recur-local256.txt
C:\Apache24\bin\abs.exe -k -c 50 -n 250  https://us-central1-go-fibonacci-recur.cloudfunctions.net/http >> g-recur-local256.txt

echo.
echo %date% %time% >> g-recur-local512.txt
C:\Apache24\bin\abs.exe -k -c 50 -n 250  https://us-central1-go-fibonacci-recur.cloudfunctions.net/http-512 >> g-recur-local512.txt

echo.
echo %date% %time% >> g-recur-local1GB.txt
C:\Apache24\bin\abs.exe -k -c 50 -n 250 https://us-central1-go-fibonacci-recur.cloudfunctions.net/http-1GB >> g-recur-local1GB.txt

echo.
echo %date% %time% >> g-recur-local2GB.txt
C:\Apache24\bin\abs.exe -k -c 50 -n 250 https://us-central1-go-fibonacci-recur.cloudfunctions.net/http-2GB >> g-recur-local2GB.txt

::hit the Azure functions

echo.
echo %date% %time% >> az-recur-local.txt 
C:\Apache24\bin\abs.exe -k -c 50 -n 250  https://calfibonaccirecur.azurewebsites.net/api/calcFibonacci >> az-recur-local.txt
