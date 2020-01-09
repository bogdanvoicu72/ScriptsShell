#!/bin/bash
echo Recived #$ args 
pwd
if [ $1 == "Raluca" ]; then
	grep -E  -o "\b[A-Za-z0-9._%+-]+@[yahoo]+\.[A-Za-z]{2,6}\b" sample
else
	echo Naspa
fi
exit 0 
