#!/usr/bin/env python3
"""
AI Cost Analysis — Data to Charts Converter
Reads JSON data files from data/ and generates gnuplot PNG charts in docs/charts/.

Chart categories:
  - $10/$20 rankings: Computational value (USD) per provider
  - Free rankings: Rank position with usage limit type
  - API pricing: Cache/batch discount % and model variety
"""

import json
import os
import re
import subprocess
import sys
import tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
CHARTS_DIR = os.path.join(PROJECT_ROOT, "docs", "charts")

# Color palette
RANKING_COLORS = {
    "exceptional_value": "#22c55e",
    "great_value": "#84cc16",
    "good_value": "#eab308",
    "moderate_value": "#f97316",
    "limited_value": "#ef4444",
    "poor_value": "#991b1b",
}

DARK_BG = "#1a1a2e"
WHITE = "#e0e0e0"
BRIGHT_WHITE = "#ffffff"
GRID_COLOR = "#333355"


def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path) as f:
        return json.load(f)


def run_gnuplot(script):
    """Run a gnuplot script and return success/failure."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".gp", delete=False) as f:
        f.write(script)
        f.flush()
        result = subprocess.run(["gnuplot", f.name], capture_output=True, text=True)
        os.unlink(f.name)
        if result.returncode != 0:
            print(f"  gnuplot error: {result.stderr.strip()}")
            return False
        return True


def esc(s):
    """Escape a string for gnuplot double-quoted contexts."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def bar_chart_vertical(out_path, title, subtitle, entries):
    """
    Generate a vertical bar chart using set object rectangles.
    entries: list of (label, sublabel, value, color)
    """
    n = len(entries)
    if n == 0:
        return False

    max_val = max(e[2] for e in entries)
    if max_val == 0:
        max_val = 1

    # Dynamic sizing: wider with more entries
    width = max(800, n * 120)
    height = 500
    bar_half = 0.35
    y_top = max_val * 1.2

    xtics_parts = []
    for i, (label, sublabel, value, color) in enumerate(entries):
        safe = esc(label)
        xtics_parts.append(f'"{safe}" {i}')
    xtics = ", ".join(xtics_parts)

    script = f"""\
set terminal pngcairo size {width},{height} enhanced font "Sans,11"
set output "{out_path}"
set title "{esc(title)}\\n{esc(subtitle)}" textcolor "{BRIGHT_WHITE}" font "Sans,13" offset 0,1
set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor "{DARK_BG}" behind
set border lc rgb "{WHITE}" lw 1
set grid y lc rgb "{GRID_COLOR}"
set key off
set xrange [-0.5:{n - 0.5}]
set yrange [0:{y_top:.1f}]
set ylabel "USD" textcolor "{WHITE}" font "Sans,11"
set xtics ({xtics}) rotate by -35 textcolor "{WHITE}" font "Sans,9"
set ytics textcolor "{WHITE}" scale 0 font "Sans,9"
set lmargin 8
set bmargin 10
"""

    # Draw bars and labels
    for i, (label, sublabel, value, color) in enumerate(entries):
        obj_id = i + 2
        script += (
            f'set object {obj_id} rectangle '
            f'from {i - bar_half},0 to {i + bar_half},{value} '
            f'fillcolor "{color}" fillstyle solid 0.85\n'
        )
        # Value label on top
        script += (
            f'set label {i + 100} "{value:.1f}" '
            f'at {i},{value + y_top * 0.025} center '
            f'textcolor "{BRIGHT_WHITE}" font "Sans,9"\n'
        )

    script += "plot NaN notitle\n"
    return run_gnuplot(script)


def generate_budget_chart(data_file, title, subtitle, out_name):
    """Generate a $10 or $20 rankings chart showing computational value."""
    print(f"  Generating {out_name} ...")
    data = load_json(data_file)
    entries = sorted(data["entries"], key=lambda e: e["rank"])

    chart_entries = []
    for e in entries:
        value = e.get("computational_value_usd", e.get("monthly_price_usd", 0))
        color = RANKING_COLORS.get(e.get("ranking_class", ""), "#666666")
        label = e["provider"]
        sublabel = e.get("limit_vulnerability", "")
        if len(sublabel) > 30:
            sublabel = sublabel[:27] + "..."
        chart_entries.append((label, sublabel, value, color))

    out_path = os.path.join(CHARTS_DIR, out_name)
    return bar_chart_vertical(out_path, title, subtitle, chart_entries)


def generate_free_rankings_chart():
    """Generate free tier rankings chart — rank position with limit type."""
    print("  Generating free-rankings.png ...")
    data = load_json("free-rankings.json")
    entries = sorted(data["entries"], key=lambda e: e["rank"])

    chart_entries = []
    for e in entries:
        rank = e["rank"]
        color = RANKING_COLORS.get(e.get("ranking_class", ""), "#666666")
        label = e["provider"]
        sublabel = e.get("primary_limit", e.get("main_limitation", ""))
        if len(sublabel) > 25:
            sublabel = sublabel[:22] + "..."
        chart_entries.append((label, sublabel, float(rank), color))

    out_path = os.path.join(CHARTS_DIR, "free-rankings.png")
    return bar_chart_vertical(
        out_path,
        "Free Tier Rankings",
        "Lower rank = better (1st place is best)",
        chart_entries,
    )


def generate_cache_discount_chart():
    """Generate API cache discount % chart."""
    print("  Generating api-cache-discount.png ...")
    data = load_json("api-pricing.json")

    entries_with_discount = []
    for e in data["entries"]:
        p = e.get("pricing", {})
        disc = p.get("cached_input_discount", "")
        if not disc:
            continue
        match = re.search(r"(\d+)", str(disc))
        if match:
            pct = int(match.group(1))
            entries_with_discount.append((e, pct))

    entries_with_discount.sort(key=lambda x: x[0]["rank"])

    chart_entries = []
    for e, pct in entries_with_discount:
        if pct >= 90:
            color = "#22c55e"
        elif pct >= 75:
            color = "#84cc16"
        elif pct >= 50:
            color = "#eab308"
        else:
            color = "#ef4444"
        chart_entries.append((e["provider"], f"{pct}% off", float(pct), color))

    out_path = os.path.join(CHARTS_DIR, "api-cache-discount.png")
    return bar_chart_vertical(
        out_path,
        "API Cache Discount",
        "% off input tokens when cached",
        chart_entries,
    )


def generate_model_variety_chart():
    """Generate API model variety chart — number of models per provider."""
    print("  Generating api-model-variety.png ...")
    data = load_json("api-pricing.json")
    entries = sorted(data["entries"], key=lambda e: e["rank"])

    chart_entries = []
    for e in entries:
        models = e.get("models", [])
        count = len(models)
        if count == 0:
            continue
        color = RANKING_COLORS.get(e.get("ranking_class", ""), "#666666")
        names = ", ".join(m["name"] for m in models[:3])
        if len(models) > 3:
            names += f" +{len(models) - 3}"
        if len(names) > 35:
            names = names[:32] + "..."
        chart_entries.append((e["provider"], names, float(count), color))

    out_path = os.path.join(CHARTS_DIR, "api-model-variety.png")
    return bar_chart_vertical(
        out_path,
        "API Model Variety",
        "Number of models available per provider",
        chart_entries,
    )


def main():
    os.makedirs(CHARTS_DIR, exist_ok=True)

    charts = [
        ("20-rankings-value.png", lambda: generate_budget_chart(
            "20-rankings.json",
            "$20 Budget — Computational Value",
            "Total USD value of usage you get for $20/month",
            "20-rankings-value.png",
        )),
        ("10-rankings-value.png", lambda: generate_budget_chart(
            "10-rankings.json",
            "$10 Budget — Computational Value",
            "Total USD value of usage you get for $10/month",
            "10-rankings-value.png",
        )),
        ("free-rankings.png", generate_free_rankings_chart),
        ("api-cache-discount.png", generate_cache_discount_chart),
        ("api-model-variety.png", generate_model_variety_chart),
    ]

    success = 0
    for name, gen_fn in charts:
        try:
            ok = gen_fn()
            if ok:
                print(f"  ✓ {name}")
                success += 1
            else:
                print(f"  ✗ {name} (gnuplot error)")
        except Exception as ex:
            print(f"  ✗ {name}: {ex}")

    print(f"\nDone: {success}/{len(charts)} charts generated.")
    return 0 if success == len(charts) else 1


if __name__ == "__main__":
    sys.exit(main())
