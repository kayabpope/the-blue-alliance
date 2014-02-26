import json
import time

from google.appengine.api import taskqueue


class FirebasePusher(object):
    @classmethod
    def updated_event(self, event_key_name):
        taskqueue.add(url='/tasks/posts/firebase_push',
                      method='POST',
                      queue_name='firebase',
                      payload=json.dumps({'key': 'events/{}'.format(event_key_name),
                                          'data': int(time.time())}))
