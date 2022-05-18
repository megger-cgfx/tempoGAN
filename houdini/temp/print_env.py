import os

for key, val in dict(os.environ).items():
    if ";" in val:
        print(key, end="\n\t")
        print("\n\t".join(val.split(";")))
    else:
        print(f"{key:20}: {val}")