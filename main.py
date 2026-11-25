import os

ENTRY = "My boss calls this office a family, so I asked for a raise. HR said families don't get raises \u2014 they get pizza Fridays and a group hug from Legal."

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
