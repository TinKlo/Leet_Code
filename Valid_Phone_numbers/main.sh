#cat file.txt | tr -d ' ' 
#echo "Other line"
#echo "o)O0OOOO))))____OO_______"*10

cat file.txt | grep "^\(\([0-9]\{3\}-\)\|([0-9]\{3\}) \)[0-9]\{3\}-[0-9]\{4\}$"
# condition requires string to have only 10 characthers
