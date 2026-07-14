import time

from updater import KnowledgeUpdater


class Scheduler:

    def __init__(self):

        self.updater = KnowledgeUpdater()

    def start(self):

        print("=" * 50)
        print("Knowledge Base Scheduler Started")
        print("Checking for new documents every 10 seconds...")
        print("=" * 50)

        while True:

            self.updater.update()

            time.sleep(10)


if __name__ == "__main__":

    scheduler = Scheduler()

    scheduler.start()