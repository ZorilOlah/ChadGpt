import redis
from rq import Queue

r = redis.StrictRedis()
q = Queue('task_queue', connection=r)
q.empty()
print(q.count())
