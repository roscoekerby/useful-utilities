counter=0
folder_name="folder_name"

iterate_through_folders_recursively() {	
    for item in "$1"/*;do
        if [ -d "$item" ];then
            echo "dir: $item"
            folder_name=$item            
            iterate_through_folders_recursively "$item"
        elif [ -f "$item" ]; then
        	counter=$((counter+1))        	
		echo "$item"
        	cp "$item" query_against
        fi
    done
}

# try get path from param
path="val"
if [ -d "$1" ]; then
    path=$1;
else
    path="val"
    mkdir query_against
fi

#echo "base path: $path"
iterate_through_folders_recursively $path
