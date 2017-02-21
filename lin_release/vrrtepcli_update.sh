#!/bin/bash
#    Vrrtep CLI is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public Licence as published by
#    the Free Software Foundation, either version 3 of the Licence, or
#    (at your option) any later version.
#
#    Vrrtep CLI is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Vrrtep CLI.  If not, see <http://www.gnu.org/licenses/>
#
#    Rewritten by Tsyalatun (c/o Twitter/facebook/learnnavi.org) to be
#    more careful with error handling.

#Loads of cool awesome edits by Tsyalatun

# Add a quiet mode to avoid all the noisy output from curl/wget
curl_opts=
wget_opts=
if [ "$1" = "-q" ]; then
	curl_opts="-s -S"
	wget_opts="-q"
fi

###curl/wget bug fix by Tsyesika###
# Checks if wget or curl is here
if [ "`which wget 2>/dev/null`" != "" ]; then
	prog="wget $wget_opts"
elif [ "`which curl 2>/dev/null`" != "" ]; then
	prog="curl $curl_opts -O"
else
	echo "Failed to update - you need curl or wget" >&2
	exit 1
fi
####################################

# Select the directory to hold the dictionary
if [ "$(id -u)" != "0" ]; then
	dir=~/.vrrtepcli
else
	# This can be simplified to...
	# dir="$(dirname "$0")"
	# cd "$dir"
	dir="$( cd "$( dirname "$0" )" && pwd )"
fi

# List of files to download and update
files="localizedWords.txt metaWords.txt naviwords.txt de.txt eng.txt est.txt hu.txt nl.txt sv.txt ru.txt dictversion.txt"

tmpdir=$(mktemp --tmpdir -d vrrtepcli.XXXXXXXXXX)

trap 'e=$?; rm -rf $tmpdir; exit $e' EXIT

# Temporarily switch to the tmpdir for the download
pushd $tmpdir >/dev/null
for file in $files; do
	###curl/wget bug fix fix by Tirea Aean (you forgot dollar sign on prog here) ###
	$prog "http://tirea.learnnavi.org/dictionarydata/$file"
	#If the above line does not work for some reason, then just replace prog with either wget or curl explicitly. Had to do this on my Samsung Chromebook running Ubuntu via Crouton
done
popd >/dev/null

# Now move the existing files out of the way
# Note, that we change the error handling trap to undo this stage now
trap 'e=$?; for f in $files; do [ -f "$dir/$f~" ] && mv -f "$dir/$f~" "$dir/$f"; done; rm -rf "$tmpdir"; exit $e' EXIT

# Move existing files out the way, and update with replacements
for file in $files; do
	mv -f "$dir/$file" "$dir/$file~"
	mv -f "$tmpdir/$file" "$dir/$file"
done

# The new dictionaries are in place, get rid of our error handling
trap '' EXIT

# Okay, that was all successful, remove the old files
for file in $files; do
	rm -f "$dir/$file~"
done
