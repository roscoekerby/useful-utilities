counter=0
folder_name="folder_name"

print_folder_recurse() {
	
	
    for i in "$1"/*;do
        if [ -d "$i" ];then
            echo "dir: $i"
            folder_name=$i            
            print_folder_recurse "$i"
        elif [ -f "$i" ]; then
        	counter=$((counter+1))
        	echo "$folder_name"
        	variablename='\usr\bin\env '
			myvariable='_Awesome'
			varname="$folder_name"_"$counter"
			echo "$varname"
			SUBSTRING=$(echo $folder_name| cut -d'/' -f 2)
			echo $SUBSTRING
			SUBSTRING2=$(echo $varname| cut -d'/' -f 2)
			echo $SUBSTRING2
			SUBSTRING3=$(echo $varname| cut -d'/' -f 1)
			echo $SUBSTRING3
			final="$SUBSTRING3/"
			final+="$SUBSTRING/" 
			final+="$SUBSTRING2"
			echo "$final"
        	mv "$i" "$final"
           	echo "renamed file: "$i" to "$SUBSTRING2""
            
        fi
    done
}

# try get path from param
path="test"
if [ -d "$1" ]; then
    path=$1;
else
    path="test"
fi

#echo "base path: $path"
print_folder_recurse $path
