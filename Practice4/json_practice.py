import json

# 1. Открываем JSON файл
with open("sample-data.json") as f:
    data = json.load(f)

# 2. Заголовки таблицы
print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':20} {'Speed':6} {'MTU':6}")
print("-" * 50 + " " + "-" * 20 + " " + "-" * 6 + " " + "-" * 6)

# 3. Проходим по данным и выводим строки
for item in data["imdata"]:
    iface = item["l1PhysIf"]["attributes"]  # <-- исправлено под твою структуру
    dn = iface["dn"]
    descr = iface.get("descr", "")
    speed = iface.get("speed", "")
    mtu = iface.get("mtu", "")
    print(f"{dn:50} {descr:20} {speed:6} {mtu:6}")

