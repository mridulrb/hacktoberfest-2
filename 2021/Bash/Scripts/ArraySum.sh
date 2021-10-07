#!/bin/bash

echo Enter the number of elements:
read N 
read -a A
for elem in "${A[@]::N}"; do
    ((ar_sum+=$elem))
done
echo "Sum: $ar_sum"