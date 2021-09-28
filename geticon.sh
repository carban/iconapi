#!/bin/sh
#Author: Carban

while getopts n:s:o: flag
do
    case "${flag}" in
        n) name=${OPTARG};;
        s) size=${OPTARG};;
        o) option=${OPTARG};;
    esac
done

# echo '{"name":"'$name'","size":'$size',"option":'$option'}'

res=$(curl localhost:5001 -d '{"name":"'$name'","size":'$size',"option":'$option'}' -H 'Content-Type: application/json' 2> /dev/null)

[ ! -z $res ] && feh $res || echo "Unexpected Error"

# echo $res
