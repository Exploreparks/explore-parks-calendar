#!/usr/bin/env python3
"""Check NPS for the Angels Landing spring 2027 lottery dates and write zion/status.json."""
import json, re, sys, urllib.request, datetime, os
URL = "https://www.nps.gov/zion/planyourvisit/angels-landing-hiking-permits.htm"
TARGET_YEAR = 2027
req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 (ExploreParks lottery checker)"})
html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
t = re.sub(r"<[^>]+>", "|", html)
t = re.sub(r"\s+", " ", t)
t = re.sub(r"(\|\s*)+", "|", t)
m = re.search(r"When to apply for hikes in (\d{4})", t)
heading_year = int(m.group(1)) if m else None
row = re.search(r"\|(March 1[^|]*May 31[^|]*)\|([^|]+)\|([^|]+)\|([^|]+)\|", t)
status = {"checked": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
          "source": URL, "target": "Spring 2027 (hikes March 1 to May 31, 2027)",
          "announced": False, "state": "not_announced", "opens": None, "closes": None, "issued": None,
          "note": "NPS has not posted the spring 2027 lottery dates yet."}
if row:
    hike, opens, closes, issued = [x.strip() for x in row.groups()]
    mentions = "2027" in hike or heading_year == TARGET_YEAR
    status["table_year"] = heading_year
    if mentions:
        status.update(announced=True, opens=opens, closes=closes, issued=issued)
        def parse(s):
            try: return datetime.datetime.strptime(f"{s} {TARGET_YEAR if 'Jan' in s or 'Feb' in s or 'Mar' in s else TARGET_YEAR}", "%B %d %Y").date()
            except Exception: return None
        o, c = parse(opens), parse(closes)
        today = datetime.date.today()
        if o and c:
            status["state"] = "upcoming" if today < o else ("open" if today <= c else "closed")
        else:
            status["state"] = "announced"
        status["note"] = f"Spring 2027 lottery: opens {opens} 8 a.m. MT, closes {closes} 11:59 p.m. MT, permits issued {issued}."
out = os.path.join(os.path.dirname(__file__), "..", "zion", "status.json")
old = {}
try: old = json.load(open(out))
except Exception: pass
keys = ("announced", "state", "opens", "closes", "issued")
changed = any(old.get(k) != status.get(k) for k in keys)
if not changed and old: status["checked"] = old.get("checked", status["checked"]) if False else status["checked"]
json.dump(status, open(out, "w"), indent=2)
print(json.dumps(status))
if changed and os.environ.get("GITHUB_OUTPUT"):
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write("changed=true\nstate=%s\nnote=%s\n" % (status["state"], status["note"]))
