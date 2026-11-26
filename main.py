import os

LINE = "My doorbell rang, nobody was there, so I thanked the wind for finally learning manners."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
