import sys
print("Версия Python:", sys.version.split()[0])
print("Интерпретатор:", sys.executable)

print("Количество путей поиска:", len(sys.path))
for q in sys.path[:4]:
    print(" ", q)
import math, random
print("math.pi =", math.pi)
print("random.random() =", random.random())
mods = sorted(sys.modules)
print("Всего загружено модулей:", len(mods))
print("Пример:", mods[:5])
public = [n for n in dir(math) if not n.startswith(" ")]
print("Первые 8:", public[:8])
print("Мой_name_=", __name__)
print("Мой_name_=", __file__)