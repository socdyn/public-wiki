##Working with data on the command line
from [data-on-the-command-line](http://www.datamazing.co.uk/2014/01/25/working-with-data-on-the-command-line#.UuZ-Bnn0D5c)  
Date Sat 25 January 2014 `#tools`

Full-blown computing environments like R and Python are great for analyzing a dataset in detail. But for quick and simple data inspection and manipulation, Unix command-line tools are incredibly efficient. In this post, I will highlight a few of the tools I find myself using on a daily basis. Hopefully you'll find a couple of new tools to add to your repertoire.  

###Peeking at a file (head, tail, less)

Let's start by downloading some sample web log data from NASA.
`$ wget ftp://ita.ee.lbl.gov/traces/NASA_access_log_Jul95.gz`

The downloaded file is compressed with gzip, so less won't uncompress it by default, but you can usezless instead. Alternatively, you can have gunzip output to stdout instead of to a file, which is convenient if you want to pipe it to a another command, such as head or tail to inspect the beginning or end of the file, respectively.

```
$ gunzip -c NASA_access_log_Jul95.gz | head -n 5
199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245
unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
199.120.110.21 - - [01/Jul/1995:00:00:09 -0400] "GET /shuttle/missions/sts-73/mission-sts-73.html HTTP/1.0" 200 4085
burger.letters.com - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/countdown/liftoff.html HTTP/1.0" 304 0
199.120.110.21 - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/missions/sts-73/sts-73-patch-small.gif HTTP/1.0" 200 4179
```

###Filtering columns (awk, cut)

It looks like the first column contains the (sub-)domains/IPs from where requests originated. Common tools that can be used to extract them include awk and cut.

```
$ gunzip -c NASA_access_log_Jul95.gz | head -n 5 | awk '{print $1}'
199.72.81.55
unicomp6.unicomp.net
199.120.110.21
burger.letters.com
199.120.110.21
```

### Counting the number of unique records (sort, uniq, wc)

Counting the number of unique (sub-)domains/IPs can be easily accomplished by sorting the records (sort), eliminating duplicates (uniq), and counting the resulting lines (wc). Note that all lines will be loaded into memory for sorting.

```
$ gunzip -c NASA_access_log_Jul95.gz | awk '{print $1}' | sort | uniq | wc -l
   81983
```

### Filtering lines (grep)

A very common operation is to filter lines from a text file that match a regular expression, which can be accomplished with grep or its variants. Say we are only interested in requests for which we have the source IPs.

```
$ gunzip -c NASA_access_log_Jul95.gz | egrep '^\d+\.\d+\.\d+\.\d+' | head -n 5
199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245
199.120.110.21 - - [01/Jul/1995:00:00:09 -0400] "GET /shuttle/missions/sts-73/mission-sts-73.html HTTP/1.0" 200 4085
199.120.110.21 - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/missions/sts-73/sts-73-patch-small.gif HTTP/1.0" 200 4179
205.212.115.106 - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/countdown.html HTTP/1.0" 200 3985
129.94.144.152 - - [01/Jul/1995:00:00:13 -0400] "GET / HTTP/1.0" 200 7074

$ gunzip -c NASA_access_log_Jul95.gz | egrep '^\d+\.\d+\.\d+\.\d+' | wc -l
  419797
```

### To exclude a pattern, simply add the -v flag.

```
$ gunzip -c NASA_access_log_Jul95.gz | egrep -v '^\d+\.\d+\.\d+\.\d+' | head -n 5
unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
burger.letters.com - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/countdown/liftoff.html HTTP/1.0" 304 0
burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 304 0
burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/video/livevideo.gif HTTP/1.0" 200 0
d104.aa.net - - [01/Jul/1995:00:00:13 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985

$ gunzip -c NASA_access_log_Jul95.gz | egrep -v '^\d+\.\d+\.\d+\.\d+' | wc -l
 1471918
```

###Sampling data (shuf, head)

Another common task is to draw a random sample of lines from a file. If the contents fit into memory, you can use shuf to shuffle the lines and pick a subset with head. (In OS X, you can get shuf by installingcoreutils. If you use Homebrew, you can brew install coreutils. Note that by default the installed tools will be prefixed with 'g' to avoid shadowing previously installed ones. Thus, shuf will be available as gshuf.)

```
$ gunzip -c NASA_access_log_Jul95.gz | gshuf | head -n 5
rs710.gsfc.nasa.gov - - [24/Jul/1995:15:32:01 -0400] "GET /images/launch-logo.gif HTTP/1.0" 200 1713
annex-065.gower.net - - [21/Jul/1995:23:37:43 -0400] "GET /images/ HTTP/1.0" 200 17688
cevennes.jpl.nasa.gov - - [23/Jul/1995:16:03:57 -0400] "GET /images/vab-small.gif HTTP/1.0" 200 35709
eoi18.eda.mke.ab.com - - [05/Jul/1995:09:08:35 -0400] "GET /shuttle/countdown/countdown.html HTTP/1.0" 200 3985
131.156.47.24 - - [05/Jul/1995:10:13:50 -0400] "GET /shuttle/missions/sts-71/mission-sts-71.html HTTP/1.0" 200 8192
```

###Working with CSV files (csvtool)

For the simplest cases, column -s, -t file.csv is a quick way to inspect a CSV (comma-separated values) file on the command line, but it gets cumbersome to handle cases such as missing values and values containing commas. There are lots of tools out there specifically designed to work with CSV files. Below I showcase csvtool.   

On Debian-based Linux distributions, you can install csvtool with sudo apt-get install csvtool. Getting it installed on OS X is a bit fiddly, but worth the effort. The tool is written in OCaml, so that's the first thing you need to install. With Homebrew, installing the OCaml package manager OPAM will install OCaml as a dependency. You can then use OPAM to install the relevant package.

```
$ brew install opam
...
$ opam install csv
...
$ sudo ln -s ~/.opam/system/bin/csvtool /usr/local/bin/
$ csvtool --help | head -n 6
csvtool - Copyright (C) 2005-2006 Richard W.M. Jones, Merjis Ltd.

csvtool is a tool for performing manipulations on CSV files from shell scripts.

Summary:
  csvtool [-options] command [command-args] input.csv [input2.csv [...]]
```

Now that we got the installation out of the way, let's download some example CSV data. Here I'll use adataset of senior officials "high earners" salaries published by the UK Cabinet Office.

```
$ wget https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/83716/high-earners-pay-2012.csv
$ wc -l high-earners-pay-2012.csv
     259 high-earners-pay-2012.csv
$ head -n1 high-earners-pay-2012.csv
Post Unique Reference,Surname,Forename(s),Grade Equivalent,Job Title,Job/Team Function,Parent Department,Organisation,Total Pay Floor (£),Total Pay Ceiling (£),Change from 2011,Notes,Contact Email
```

We can see above that the file contains 258 rows plus a header row with column names. Say we want to select a subset of the columns (job title, organisation, total pay floor, and total pay ceiling), outputting using tab as a separator.

```
$ csvtool -u TAB col 5,8-10 high-earners-pay-2012.csv | head -n 5
Job Title   Organisation    Total Pay Floor (£) Total Pay Ceiling (£)
Director    Serious Fraud Office    165000  169999
Non-Executive Director Defence Board and Chair Audit Committee  Ministry of Defence 30000   34999
Chairman    Olympic Delivery Authority  250000  254999
HM Inspector of Constabulary Northern Region    HM Inspectorate of Constabulary 185000  189999
```

Now let's sort the data in descending order based on the total pay floor and inspect the top records. We first remove the header row, and pipe the result back to csvtool using - to read input from stdininstead of from a file. We then sort the rows in descending numeric order based on the 3rd column, and pipe the top records back to csvtool for pretty printing.

```
$ csvtool drop 1 high-earners-pay-2012.csv | csvtool -u TAB col 5,8-10 - | sort -t$'\t' -k3rn | head -n 4 | csvtool -t TAB readable -
Chief Executive         Olympic Delivery Authority        310000 314999
Chief Executive         Office of Fair Trading            275000 279999
Chief Executive Officer Nuclear Decommissioning Authority 265000 269999
NHS Chief Executive     Department of Health              265000 269999
```

###Working with data in JSON format (jq)

Last but not least, I would like to mention jq, an incredibly useful tool for working with data in JSON format. Binaries are available on their download page. On OS X, you can install it using Homebrew withbrew install jq.

Let's download current weather forecast data for London using forecast.io.

```
$ curl "https://api.forecast.io/forecast/$API_KEY/51.51121389999999,0.11982439999997041" > forecast.json
$ wc forecast.json
       0     142   25804 forecast.json
```

That's a big response in a single line. We can neatly format the data with jq:

```
$ cat forecast.json | jq . | head
{
  "flags": {
    "units": "us",
    "darksky-stations": [
      "uk_london"
    ],
    "datapoint-stations": [
      "uk-324164",
      "uk-350286",
      "uk-351142",
```

Let's find what are all the keys present in the JSON object.

```
$ cat forecast.json | jq 'keys'
[
  "currently",
  "daily",
  "flags",
  "hourly",
  "latitude",
  "longitude",
  "minutely",
  "offset",
  "timezone"
]
```

Now let's filter the current weather conditions.

```
$ cat forecast.json | jq '.currently'
{
  "ozone": 311.54,
  "temperature": 42.65,
  "precipProbability": 0,
  "precipIntensity": 0,
  "nearestStormBearing": 191,
  "nearestStormDistance": 176,
  "icon": "wind",
  "summary": "Breezy",
  "time": 1390689251,
  "apparentTemperature": 34.98,
  "dewPoint": 35.04,
  "humidity": 0.74,
  "windSpeed": 15.9,
  "windBearing": 286,
  "visibility": 10,
  "cloudCover": 0,
  "pressure": 1013.82
}
```

We just scratched the surface of what jq can do. Check the excellent jq documentation for many more great features.

