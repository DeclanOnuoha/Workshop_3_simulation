import simpy
import random
from collections import deque


class Hospital:
    def __init__(self, env, prep_rooms, rec_rooms, seed=None):
        self.env = env
        self.prep = simpy.Resource(env, capacity=prep_rooms)
        self.surgery = simpy.Resource(env, capacity=1)
        self.recovery = simpy.Resource(env, capacity=rec_rooms)
        self.waiting_room = deque()           # Entrance queue

        # Tracking variables
        self.queue_length = 0
        self.surgery_busy = 0
        self.surgery_blocked = 0

        # For time-weighted averages
        self.log = []
        self.last_time = 0
        self.log_state()

        if seed is not None:
            random.seed(seed)

    def log_state(self):
        now = self.env.now
        if now > self.last_time:
            duration = now - self.last_time
            self.log.append({
                'time': self.last_time,
                'duration': duration,
                'queue': self.queue_length,
                'surgery_busy': self.surgery_busy,
                'surgery_blocked': self.surgery_blocked,
                'all_recovery_busy': (self.recovery.count == self.recovery.capacity)
            })
        self.last_time = now

    def patient(self):
        # Arrival
        self.waiting_room.append(True)
        self.queue_length = len(self.waiting_room)
        self.log_state()

        # Preparation
        with self.prep.request() as req:
            yield req
            self.waiting_room.popleft()
            self.queue_length = len(self.waiting_room)
            self.log_state()
            yield self.env.timeout(random.expovariate(1/40))

        # Surgery
        with self.surgery.request() as req:
            yield req
            self.surgery_busy = 1
            self.log_state()
            yield self.env.timeout(random.expovariate(1/20))

        # Recovery (blocking occurs here)
        with self.recovery.request() as req:
            self.surgery_busy = 0
            self.surgery_blocked = 1
            self.log_state()
            yield req
            self.surgery_blocked = 0
            self.log_state()
            yield self.env.timeout(random.expovariate(1/40))

        self.log_state()


def run_one_run(prep, rec, seed, warmup=1000, observe=1000):
    env = simpy.Environment()
    hospital = Hospital(env, prep, rec, seed)

    def arrivals():
        while True:
            yield env.timeout(random.expovariate(1/25))
            if env.now > warmup + observe:
                break
            env.process(hospital.patient())

    env.process(arrivals())
    env.run(until=warmup + observe)

    # Only keep observation period
    data = [entry for entry in hospital.log if entry['time'] >= warmup]
    total_time = observe

    weighted_queue = sum(e['queue'] * e['duration'] for e in data)
    weighted_blocked = sum(e['surgery_blocked'] * e['duration'] for e in data)
    weighted_rec_full = sum((1 if e['all_recovery_busy'] else 0) * e['duration'] for e in data)

    return {
        'queue_length': weighted_queue / total_time,
        'blocking_probability': weighted_blocked / total_time,
        'rec_full_probability': weighted_rec_full / total_time
    }