counter=0
folder_name="folder_name"

iterate_folders_recursively() {	
    for item in "$1"/*;do
        if [ -d "$item" ];then
            echo "dir: $item"
            folder_name=$item            
            iterate_folders_recursively "$item"
        elif [ -f "$item" ]; then
			counter=$((counter+1))
			varname="$folder_name"_"$counter"
			class_name=$(echo $folder_name| cut -d'/' -f 2)
			new_file_name=$(echo $varname| cut -d'/' -f 2)
			root_dir=$(echo $varname| cut -d'/' -f 1)
			final="$root_dir/"
			final+="$class_name/" 
			final+="$new_file_name"
			final+=".jpg"
			mv "$item" "$final"
		   	echo "renamed file: "$item" to "$new_file_name".jpg"
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

# echo "base path: $path"
iterate_folders_recursively $path
