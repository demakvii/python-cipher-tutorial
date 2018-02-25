#!/bin/bash
# SCRIPT:  happynewyear.sh
# PURPOSE: Prints Happy new year 2011 on screen.
#                         \\\\ ////
#                         \\ - - //
#                            @ @
#                    ---oOOo-( )-oOOo---
#
##############################################################################
#                              Arguments Checking                            #
##############################################################################

if [ $# -eq 1 ]
then
    fname=$1
else
    echo "Invalid Arguments"
    echo "Usage: happynewyear.sh filename"
    exit
fi

##############################################################################
#                               Main Starts                                  #
##############################################################################

clear
i=0

while read line
do

   if [ $i -lt 8 ] ; then
       COLOR1="\e[1;31;40m" ; COLOR2="\e[0m"     # Dark Red 
   elif [ $i -gt 8 -a $i -lt 17 ] ; then
       COLOR1="\e[1;37;40m" ; COLOR2="\e[0m"     # White 
   elif [ $i -gt 17 -a $i -lt 26 ] ; then
       COLOR1="\e[1;32;40;5m" ; COLOR2="\e[0m"   # Dark Green with blinking 
   fi                                            # effect
   

   newline=`echo "$line" | tr '69' ' @' `
   printf "$COLOR1$newline $COLOR2"        # you can also use echo -e "...."
   let i++
   sleep 0.1


done < $fname

read                                        # Waits for enter
