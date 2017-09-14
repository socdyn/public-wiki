# What is Mongo?

A no-SQL database. I.e. there aren't rows and columns. Instead, each entry is a blob of JSON-like text. This allows flexibility when you're not sure what the exact format of the input is going to be, but sacrifices speed and correctness since different "rows" of the same collection may have different elements.

## Basic terms

A *database* is the highest organizational concept. It is not one single thing like in SQL, but rather a group of *collections*. Collections hold *documents*, which you can think of as an actual "row" of data.

So if I were doing a project on Bernie Sanders, I would organize all of my Bernie data into a database called `feel_the_bern`, and within that database have collections `bernie_tweets` and `bernie_press` to hold different types of data in a orderly way. In the `bernie_tweets` collection, each document would be an individual JSON-like tweet.

## Pros

1. If you're crawling data from web APIs, Mongo accepts JSON-like objects from Python (which is probably the format and language you're using)
2. Inserts are generally much faster than an API will give you data, so Mongo will not be your bottleneck during crawling
3. Exports easily to actual JSON on disk, which you can easily convert to Pandas, matrices, or anything else

## Cons

1. Performing certain operations on large collections is really slow. Mongo is a really bad place to do complicated operations on your data
2. You're basically limited to using a Python wrapper around Mongo, unless you want to invest some serious time
3. It's a lot of work to assess the correctness of your databases. I.e. does every Tweet document have an entry called "time"? Is it always an integer? These kinds of questions can be difficult to answer with Mongo.

## In sum

Use Mongo for your crawling and exporting, but not your analysis.

# How to transfer a collection from one database to another

You must have ownership or admin privileges over each database to do this. While there are potentially solutions in
Mongo shell or pymongo it is actually quite difficult to do stuff that requires access to multiple databases.

Usually you should be creating multiple "collections" within a database and so will not encounter this issue.

If you find yourself needing to do this then you can type a single line of code into the command line on the machine where
the database is located:

```
mongoexport -d source_db -c collection_to_copy --port 27017 -u “username" -p “password"  --authenticationDatabase “auth_db"|
mongoimport -d target_db -c collection_target --port 27017 -u “ username" -p “password"  --authenticationDatabase “auth_db”
```

This command will export a collection from the source database and pipes it to a command to import it into a specific
collection in the target database. It does this by writing the collection as a JSON, which is then read back into the target
database. Mongo will print out statements showing the progress of the transfer every couple
of seconds, including information on the number and percentage of records transfered. For a 4GB collection it took
about 15 minutes.

If you have admin privileges you can use the same username, password, and auth_db both times but if you do not then you should
enter the credentials specific to each db, e.g. `source_db` and `target_db` (I did not do this so it may not work!)

Note that this may not be suitable for all types of migration. The MongoDB docs recommend that you consider using mongodump/mongorestore.
instead for certain applications. Writing the database to JSON using export may not preserve rich BSON datatypes. The dump/restore procedure will not affect these datatypes as it simple saves the database as an archive rather than converting it to JSON.

# Note well

DO NOT TRY TO DO ANY OTHER OPERATIONS ON THE DATABASES WHILE THIS PROCESS IS RUNNING.

# How to start/restart Mongodb on Vesta

```
sudo launchctl unload /Library/LaunchDaemons/homebrew.mxcl.mongodb.plist
sudo launchctl load -w -F /Library/LaunchDaemons/homebrew.mxcl.mongodb.plist
homebrew.mxcl.mongodb.plist.txt
```

# MongoDB config as of 10.11 1/2017

**`/usr/local/etc/mongod.conf`**

```python
storage:
   dbPath: "/Volumes/pci_ssd/mongo_data/data/db"
   journal:
      enabled: true
   engine: wiredTiger
systemLog:
   destination: file
   path: "/usr/local/var/log/mongodb/mongo.log"
   logAppend: true
   logRotate: reopen
net:
   bindIp: 127.0.0.1
setParameter:
   enableLocalhostAuthBypass: false
security:
    authorization: enabled
```