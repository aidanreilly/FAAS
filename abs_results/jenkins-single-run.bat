::hit the easy functions

echo. 
echo %date% %time% >> g-simple-local-single.txt
C:\Apache24\bin\abs.exe -k -c 1 -n 1 -s 600 https://us-central1-go-fibonacci.cloudfunctions.net/http >> g-simple-local-single.txt

echo. 
echo %date% %time% >> a-simple-local-single.txt
C:\Apache24\bin\abs.exe -k -c 1 -n 1 -s 600 https://g8h74so6w0.execute-api.us-east-1.amazonaws.com/dev/ping >> a-simple-local-single.txt

echo. 
echo %date% %time% >> az-simple-local-single.txt
C:\Apache24\bin\abs.exe -k -c 1 -n 1 -s 600 https://calfibonacci.azurewebsites.net/api/calcFibonacci >> az-simple-local-single.txt

::hit the AWS functions

echo. 
echo %date% %time% >> a-recur-local256-single.txt
C:\Apache24\bin\abs.exe -k -c 1 -n 1 -s 600 https://k9kec8cpgc.execute-api.us-east-1.amazonaws.com/dev/ping >> a-recur-local256-single.txt

echo.
echo %date% %time% >> a-recur-local512-single.txt
C:\Apache24\bin\abs.exe -k -c 1 -n 1  -s 600 https://0qwlklexf2.execute-api.us-east-1.amazonaws.com/dev/ping >> a-recur-local512-single.txt

echo.
echo %date% %time% >> a-recur-local1GB-single.txt
C:\Apache24\bin\abs.exe -k -c 1 -n 1  -s 600 https://1fd9j85pbj.execute-api.us-east-1.amazonaws.com/dev/ping >> a-recur-local1GB-single.txt

echo.
echo %date% %time% >> a-recur-local2GB-single.txt
C:\Apache24\bin\abs.exe -k -c 1 -n 1  -s 600 https://l1zp09xozj.execute-api.us-east-1.amazonaws.com/dev/ping >> a-recur-local2GB-single.txt

::hit the Google functions

echo.
echo %date% %time% >> g-recur-local256-single.txt
C:\Apache24\bin\abs.exe -k -c 1 -n 1   -s 600 https://us-central1-go-fibonacci-recur.cloudfunctions.net/http >> g-recur-local256-single.txt

echo.
echo %date% %time% >> g-recur-local512-single.txt
C:\Apache24\bin\abs.exe -k -c 1 -n 1   -s 600 https://us-central1-go-fibonacci-recur.cloudfunctions.net/http-512 >> g-recur-local512-single.txt

echo.
echo %date% %time% >> g-recur-local1GB-single.txt
C:\Apache24\bin\abs.exe -k -c 1 -n 1  -s 600 https://us-central1-go-fibonacci-recur.cloudfunctions.net/http-1GB >> g-recur-local1GB-single.txt

echo.
echo %date% %time% >> g-recur-local2GB-single.txt
C:\Apache24\bin\abs.exe -k -c 1 -n 1  -s 600 https://us-central1-go-fibonacci-recur.cloudfunctions.net/http-2GB >> g-recur-local2GB-single.txt

::hit the Azure functions

echo.
echo %date% %time% >> az-recur-local-single.txt 
C:\Apache24\bin\abs.exe -k -c 1 -n 1 -s 600 https://calfibonaccirecur.azurewebsites.net/api/calcFibonacci >> az-recur-local-single.txt
