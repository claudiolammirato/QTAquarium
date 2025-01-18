import select
import psycopg2
import psycopg2.extensions
from setting_class import ConfigClass

settings = ConfigClass()
settings_loaded = settings.load_item("settings")
conn = psycopg2.connect(database=settings_loaded['database']['name'],
                        host=settings_loaded["database"]["url"],
                        user=settings_loaded["database"]["username"],
                        password=settings_loaded["database"]["password"],
                        port=settings_loaded["database"]["port"])
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

curs = conn.cursor()
curs.execute("LISTEN device_snapshot_change;")

print("Waiting for notifications on channel 'test'")
while True:
    if select.select([conn],[],[],5) == ([],[],[]):
        print("Timeout")
    else:
        conn.poll()
        while conn.notifies:
            notify = conn.notifies.pop(0)
            print("Got NOTIFY:", notify.pid, notify.channel, notify.payload)