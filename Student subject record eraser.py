records = {
    "Asha": {"Math": 85, "Science": 90},
    "Ravi": {"Math": 78, "Science": 82},
    "Ravi_duplicate": {"Math": 78, "Science": 82},
}


print("Asha's Math:", records.get("Asha", {}).get("Math"))
print("Missing student:", records.get("Zoe", "Not Found"))


records["Meena"] = {"Math": 92, "Science": 88}
records["Ravi"]["Math"] = 80


removed = records.pop("Ravi_duplicate")
print("Removed:", removed)


print("Total records:", len(records))


for name, subjects in records.items():
    print(name, "->", subjects)