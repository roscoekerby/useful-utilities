counter=0
folder_name="folder_name"

iterate_through_folders_recursively() {	
    for item in "$1"/*;do
        if [ -d "$item" ];then
            echo "dir: $item"
            folder_name=$item            
            iterate_through_folders_recursively "$item"
            counter=0
        elif [ -f "$item" ]; then
        	counter=$((counter+1)) 
        	if [ $((counter)) -lt $(($num_copies+1)) ]; then
				echo "$item"
				cp "$item" query_$num_copies
			fi
        fi
    done
}


mkdir query_"$2"

# try get path from param
path="test"
if [ -d "$1" ]; then
    path=$1;
    num_copies=$2
else
    path="test"
    num_copies=$2
fi

echo "$num_copies"

iterate_through_folders_recursively $path $num_copies

