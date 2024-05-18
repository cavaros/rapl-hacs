time=1
T0=($(sudo cat /sys/class/powercap/*/energy_uj))
sleep $time
T1=($(sudo cat /sys/class/powercap/*/energy_uj)); sum=0
for i in "${!T0[@]}"
    do 
        power=$(echo - | awk "{printf \"%.1f\", $((${T1[i]}-${T0[i]})) / $time / 1e6 }")
        sum=$(echo $sum+$power | bc)
done
echo "Total power consumption: $sum W"
