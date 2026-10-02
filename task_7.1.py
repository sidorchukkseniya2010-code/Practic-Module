import sched
import time
s = sched.scheduler(time.time, time.sleep)
start = time.time()
def say(text):
    now = time.time() - start
    print(f"[{now:4.1f} c] {text}")
s.enter(0.5, 1, say, ("Прошло 0.5 секунды",))
s.enter(1, 1, say, ("Прошла 1 секунда",))
s.enter(2, 1, say, ("Прошло 2 секунды (приоритет 1)",))
s.enter(2, 0, say, ("Прошло 2 секунды (приоритет 0)",))
s.enter(4, 1, say, ("Прошло 4 секунды",))
s.enterabs(start + 3, 1, say, ("Абсолютное время t0+3 c",))
print("Очередь до run():", len(s.queue))
s.run()
print("Готово. Пустая очередь?", s.empty())
