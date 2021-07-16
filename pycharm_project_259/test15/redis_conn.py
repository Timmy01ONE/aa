#!/usr/bin/env python
import redis

pool = redis.ConnectionPool(host="1.15.34.78", port=6379)
r = redis.Redis(connection_pool=pool)
r.set('foo','Bar')

r.get('foo')
print(r.get('foo'))