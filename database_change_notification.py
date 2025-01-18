import os
import psycopg2
import asyncio

def run_main():
    conn = psycopg2.connect(host="192.168.1.113", dbname="qtaquarium", user="", password="")

    cursor = conn.cursor()
    cursor.execute(f"LISTEN match_updates;")
    conn.commit()

    def handle_notify():
        try:
            for notify in conn.notifies(stop_after=0):
                print(notify.payload)
        except:
            print('Error occurred')
            raise

    loop = asyncio.get_event_loop()
    loop.add_reader(conn, handle_notify)
    loop.run_forever()

if __name__ == "__main__":
    try:
        print(f'Starting')
        run_main()
    finally:
        print('Exiting')