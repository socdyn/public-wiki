#Using awk to break up large sim files for analysis

Simulation makes it easy to generate huge files that cannot be opened by regular programs. To get around this, you must break the file into smaller parts. One approach might be the separate the cases into files based on combinations of parameters (next time, have the simulation code do this automatically!)

`awk` is a unix tool that can operate on a file to find the lines that match a certain criteria and perform operations when a match is found. My simulations usually generate "flat" ie: a table with the same number of columns on each row with the tab character as a delimiter.

Something like this:

|nodeID|threshold|trial	|degree|wave_num|mean\_inf\_len|inf\_tie\_len|
|------|---------|-----|------|--------|------------|--------|
|0|1|0|232|3|2|2|
|1|1|0|165|3|2|2|
|2|1|0|223|2|3|3|
|3|1|0|154|3|2|2|
|...|...|...|...|...|...|...|


The following command takes my 1.5 GB file and divides it into several smaller, more manageable files based on the value in the second data column. This command generates one file for each value of the second column encountered in the input file.

`% awk '$0 ~ /^[0-9]{1,10}[ \t][0-9]{1,10}[ \t] {f="ba_" $2 ".txt"; print $0 > f }' ba_10k_d8_pu_trials.txt`

Parts of the command:  
`'stuff in single quotes'` This constitutes the command to awk  
`/ stuff in right slashes /` This constitutes the pattern  
`$0 ~ ` Match the query against the whole line  
`^` line starts with  
`[0-9]{1,10}` 1 to 10 digits in the range 1-9  
`[ \t]` followed by a tab,
`[0-9]{1,10}` followed by 1 to 10 digits in the range 1-9  
`[ \t]` followed by a tab  

When a matching line is found, (all of them but the header), then execute the commands inside the curly braces `{ }`:  
`f="ba_" $2 ".txt";` create a variable f with the text "ba_<value from second column>.txt", the semicolon indicates a second command follows this one.  

`print $0 > f` if f was created successfully (is not null), print `$0` (the whole line) to the file named f.  

`ba_10k_d8_pu_trials.txt` This is the inputut file.  

