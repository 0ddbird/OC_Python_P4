from tinydb import TinyDB, Query
import gc

# create a TinyDB instance and open the table you want to reset
db = TinyDB("my_table.json")
table = db.table("my_table_name")

# truncate the table and run garbage collection to free up memory
table.truncate()
gc.collect()

# close the table and database
table.close()
db.close()
