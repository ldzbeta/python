import http.client
import threading
from queue import Queue

HOST = "localhost"
PORT = 5600
BASE_PATH = "/api/0/buckets/aw-watcher-window_Ldzbeta/events/"
HEADERS = {"accept": "application/json"}
NUM_THREADS = 10  # Tune based on your system/network

def delete_event(event_id):
    try:
        conn = http.client.HTTPConnection(HOST, PORT, timeout=10)
        path = BASE_PATH + str(event_id)
        conn.request("DELETE", path, headers=HEADERS)
        response = conn.getresponse()
        status = response.status
        response.read()
        conn.close()

        if status >= 400:
            print(f"❌ Failed ID {event_id}: HTTP {status}")
        else:
            print(f"✅ Deleted ID {event_id}")
    except Exception as e:
        print(f"⚠️ Error ID {event_id}: {e}")

def worker(queue):
    while True:
        event_id = queue.get()
        if event_id is None:
            break
        delete_event(event_id)
        queue.task_done()

def main():
    start_id = int(input("Start ID: "))
    end_id = int(input("End ID: "))
    if start_id > end_id:
        print("Start must be <= End")
        return

    queue = Queue()
    threads = []

    for _ in range(NUM_THREADS):
        t = threading.Thread(target=worker, args=(queue,))
        t.start()
        threads.append(t)

    for event_id in range(start_id, end_id + 1):
        queue.put(event_id)

    queue.join()

    for _ in range(NUM_THREADS):
        queue.put(None)
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
