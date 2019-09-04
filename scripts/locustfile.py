'''
Locust task sets to execute
'''

import json
import random
from locust import HttpLocust
from locust import TaskSet, task, HttpLocust

NUM = 1000
LAST_BLOCK = None
LAST_CHALLENGE = None

class BlockSet(TaskSet):
    '''
    Block route specific tasks to run
    '''
    def setup(self):
        global LAST_BLOCK
        resp = self.client.get("/api/blocks?limit=1")
        if resp.status_code == 200:
            data = json.loads(resp.content.decode('utf-8'))
            LAST_BLOCK = data['data'][0]['height']

    @task(2)
    def index(self):
        self.client.get("/api/blocks")

    @task(1)
    def index_half(self):
        self.client.get("/api/blocks?limit=500")

    @task(1)
    def index_max(self):
        self.client.get("/api/blocks?limit=1000")

    @task(1)
    def txns(self):
        if LAST_BLOCK:
            for i in  random.choices(range(2, LAST_BLOCK), k=NUM):
                self.client.get(f"/api/blocks/{i}/transactions")
        else:
            pass

class ChallengeSet(TaskSet):
    '''
    Challenge route specific tasks to run
    '''
    def setup(self):
        global LAST_CHALLENGE
        resp = self.client.get("/api/challenges?limit=1")
        if resp.status_code == 200:
            data = json.loads(resp.content.decode('utf-8'))
            LAST_CHALLENGE = data['data'][0]['id']

    @task(2)
    def index_10(self):
        self.client.get("/api/challenges?limit=10")

    @task(1)
    def index_50(self):
        self.client.get("/api/challenges?limit=50")

    @task(1)
    def index_default(self):
        self.client.get("/api/challenges")

    @task(1)
    def index_max(self):
        self.client.get("/api/challenges?limit=1000")

    @task(1)
    def index_half(self):
        self.client.get("/api/challenges?limit=500")

    @task(10)
    def challenges(self):
        if LAST_CHALLENGE:
            for i in random.choices(range(1, LAST_CHALLENGE), k=NUM):
                self.client.get(f"/api/challenges/{i}")
        else:
            pass


class BlockLocust(HttpLocust):
    task_set = BlockSet
    min_wait = 5000
    max_wait = 9000

class ChallengeLocust(HttpLocust):
    task_set = ChallengeSet
    min_wait = 5000
    max_wait = 9000
