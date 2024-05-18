#!/usr/bin/bash

time=1
T0=($(sudo cat /sys/class/powercap/*/energy_uj))
sleep $time
T1=($(sudo cat /sys/class/powercap/*/energy_uj))
sum=0
for i in "${!T0[@]}"
    do 
        power=$(echo - | awk "{printf \"%.0f\", $((${T1[i]}-${T0[i]})) / $time / 1e6 }")
        # echo $power
        # echo "somando $sum e $power"
        # sum=$(python3 -c "print(float($sum)+float($power))")
        sum=$(($sum+$power))
        # echo $sum
done
echo "$sum W/h"