#!/bin/bash
#
set -- $(getopt -q u:g:c:d:s:k:m "$@")
#
echo
while [ -n "$1" ]
do
	case "$1" in
	-u) param="$2"
	    echo "-u (uid) option, parameter value : $param"
	    shift ;;
	-g) param="$2"
	    echo "-g (gid) option, parameter value : $param"
	    shift ;;
	-c) param="$2"
	    echo "-c (comment) option, parameter value : $param"
	    shift ;;
	-d) param="$2"
	    echo "-d (home directory) option, parameter value: $param"
	    shift ;;
	-s) param="$2"
	    echo "-s (shell) option, parameter value : $param"
	    shift ;;
	-k) param="$2"
	    echo "-k (initial scripts directory) option, parameter value : $param"
	    shift ;;
	-m) echo "-m (make home directory) option" ;;
	--) shift
	    break ;;
	*) echo "$1 is not an option" ;;
	esac
	shift
done
#
count=1
for param in "$@"
do
	echo "Parameter #$count: $param"
	count=$[ $count + 1 ]
done
#
