#!/usr/bin/env python3
"""
AI Cost Analysis — Data to Charts Converter
Reads JSON data files from data/ and generates gnuplot PNG charts in docs/charts/.
"""

import json
import os
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
WHITE = "#ffffff"
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


def generate_20_rankings_chart():
    """Generate $20 budget computational value chart."""
    print("  Generating 20-rankings-value.png ...")
    data = load_json("20-rankings.json")
    entries = sorted(data["entries"], key=lambda e: e["rank"])

    # Write CSV
    csv_path = os.path.join(CHARTS_DIR, "_tmp_20.csv")
    with open(csv_path, "w") as f:
        f.write("provider,value,color\n")
        for e in entries:
            value = e.get("computational_value_usd", e.get("monthly_price_usd", 0))
            color = RANKING_COLORS.get(e.get("ranking_class", ""), "#666666")
            safe_name = e["provider"].replace('"', "'")
            f.write(f'"{safe_name}",{value},{color}\n')

    n = len(entries)
    out_path = os.path.join(CHARTS_DIR, "20-rankings-value.png")
    script = f"""\
set terminal pngcairo size 800,500 enhanced font "Sans,10"
set output "{out_path}"
set title "$20 Budget — Computational Value (USD)" textcolor "{WHITE}" font "Sans,13"
set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor "{DARK_BG}" behind
set border lc rgb "{WHITE}" lw 1
set style data histograms
set style histogram rowstacked
set style fill solid 1.0 border -1
set boxwidth 0.7
set xtics textcolor "{WHITE}"
set ytics textcolor "{WHITE}" scale 0
set xlabel "USD" textcolor "{WHITE}"
set grid x lc rgb "{GRID_COLOR}"
set key off
set yrange [0:{n + 0.5}]
set xrange [0:]
# Plot horizontal bars — use labels via set label
"""
    # Since gnuplot histograms are tricky for colored bars per row, use boxxyerrorbars
    script = f"""\
set terminal pngcairo size 800,500 enhanced font "Sans,10"
set output "{out_path}"
set title "$20 Budget — Computational Value (USD)" textcolor "{WHITE}" font "Sans,13"
set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor "{DARK_BG}" behind
set border lc rgb "{WHITE}" lw 1
set xtics textcolor "{WHITE}"
set ytics textcolor "{WHITE}" scale 0
set grid x lc rgb "{GRID_COLOR}"
set key off
set xrange [0:]
set yrange [{n - 0.5}:-0.5]
set xlabel "Computational Value (USD)" textcolor "{WHITE}"
set style fill solid 0.9 border -1
"""
    for i, e in enumerate(entries):
        value = e.get("computational_value_usd", e.get("monthly_price_usd", 0))
        color = RANKING_COLORS.get(e.get("ranking_class", ""), "#666666")
        safe_name = e["provider"].replace('"', '\\"')
        script += f'set label {i+1} "{safe_name}" at {value + 1.5},{i} left textcolor "{WHITE}" font "Sans,9"\n'
        script += f'set object {i+2} rectangle from 0,{i-0.35} to {value},{i+0.35} fillcolor "{color}" fillstyle solid 0.9\n'

    script += "plot NaN notitle\n"

    ok = run_gnuplot(script)
    if os.path.exists(csv_path):
        os.unlink(csv_path)
    return ok


def generate_10_rankings_chart():
    """Generate $10 budget computational value chart."""
    print("  Generating 10-rankings-value.png ...")
    data = load_json("10-rankings.json")
    entries = sorted(data["entries"], key=lambda e: e["rank"])

    n = len(entries)
    out_path = os.path.join(CHARTS_DIR, "10-rankings-value.png")
    script = f"""\
set terminal pngcairo size 800,500 enhanced font "Sans,10"
set output "{out_path}"
set title "$10 Budget — Computational Value (USD)" textcolor "{WHITE}" font "Sans,13"
set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor "{DARK_BG}" behind
set border lc rgb "{WHITE}" lw 1
set xtics textcolor "{WHITE}"
set ytics textcolor "{WHITE}" scale 0
set grid x lc rgb "{GRID_COLOR}"
set key off
set xrange [0:]
set yrange [{n - 0.5}:-0.5]
set xlabel "Computational Value (USD)" textcolor "{WHITE}"
set style fill solid 0.9 border -1
"""
    for i, e in enumerate(entries):
        value = e.get("computational_value_usd", e.get("monthly_price_usd", 0))
        color = RANKING_COLORS.get(e.get("ranking_class", ""), "#666666")
        safe_name = e["provider"].replace('"', '\\"')
        script += f'set label {i+1} "{safe_name}" at {value + 1.5},{i} left textcolor "{WHITE}" font "Sans,9"\n'
        script += f'set object {i+2} rectangle from 0,{i-0.35} to {value},{i+0.35} fillcolor "{color}" fillstyle solid 0.9\n'

    script += "plot NaN notitle\n"
    return run_gnuplot(script)


def generate_free_rankings_chart():
    """Generate free tier rankings chart."""
    print("  Generating free-rankings.png ...")
    data = load_json("free-rankings.json")
    entries = sorted(data["entries"], key=lambda e: e["rank"])

    n = len(entries)
    max_rank = n + 1
    out_path = os.path.join(CHARTS_DIR, "free-rankings.png")
    script = f"""\
set terminal pngcairo size 800,600 enhanced font "Sans,10"
set output "{out_path}"
set title "Free Tier Rankings" textcolor "{WHITE}" font "Sans,13"
set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor "{DARK_BG}" behind
set border lc rgb "{WHITE}" lw 1
set xtics textcolor "{WHITE}"
set ytics textcolor "{WHITE}" scale 0
set grid x lc rgb "{GRID_COLOR}"
set key off
set xrange [0:{max_rank}]
set yrange [{n - 0.5}:-0.5]
set xlabel "Rank (lower is better)" textcolor "{WHITE}"
set style fill solid 0.9 border -1
"""
    for i, e in enumerate(entries):
        rank = e["rank"]
        color = RANKING_COLORS.get(e.get("ranking_class", ""), "#666666")
        safe_name = e["provider"].replace('"', '\\"')
        main_lim = e.get("main_limitation", "").replace('"', '\\"')
        label_text = f"{safe_name} — {main_lim}" if main_lim else safe_name
        script += f'set label {i+1} "{label_text}" at {rank + 0.3},{i} left textcolor "{WHITE}" font "Sans,8"\n'
        script += f'set object {i+2} rectangle from 0,{i-0.35} to {rank},{i+0.35} fillcolor "{color}" fillstyle solid 0.9\n'

    script += "plot NaN notitle\n"
    return run_gnuplot(script)


def generate_api_pricing_chart():
    """Generate API pricing comparison chart."""
    print("  Generating api-pricing-comparison.png ...")
    data = load_json("api-pricing.json")
    # Only include entries with actual numeric pricing
    entries = []
    for e in data["entries"]:
        p = e.get("pricing", {})
        inp = p.get("flagship_input_per_m")
        out = p.get("flagship_output_per_m")
        if inp is not None and out is not None:
            entries.append(e)

    entries.sort(key=lambda e: e["rank"])
    n = len(entries)
    out_path = os.path.join(CHARTS_DIR, "api-pricing-comparison.png")

    script = f"""\
set terminal pngcairo size 900,600 enhanced font "Sans,10"
set output "{out_path}"
set title "API Pricing — Flagship Model Cost per 1M Tokens" textcolor "{WHITE}" font "Sans,13"
set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor "{DARK_BG}" behind
set border lc rgb "{WHITE}" lw 1
set xtics textcolor "{WHITE}"
set ytics textcolor "{WHITE}" scale 0
set grid x lc rgb "{GRID_COLOR}"
set key top right textcolor "{WHITE}"
set xrange [0:]
set yrange [{n - 0.5}:-0.5]
set xlabel "Cost per 1M Tokens (USD)" textcolor "{WHITE}"
set style fill solid 0.8 border -1
set boxwidth 0.35 absolute
"""
    # Two bars per provider (offset by ±0.2)
    for i, e in enumerate(entries):
        p = e.get("pricing", {})
        inp = p.get("flagship_input_per_m", 0)
        out = p.get("flagship_output_per_m", 0)
        safe_name = e["provider"].replace('"', '\\"')
        y_off = i - 0.2
        y_in = i + 0.2
        script += f'set object {i*3+2} rectangle from 0,{y_off - 0.17} to {out},{y_off + 0.17} fillcolor "#ef4444" fillstyle solid 0.8\n'
        script += f'set object {i*3+3} rectangle from 0,{y_in - 0.17} to {inp},{y_in + 0.17} fillcolor "#3b82f6" fillstyle solid 0.8\n'
        script += f'set label {i*3+2} "{safe_name}" at 1,{i} left textcolor "{WHITE}" font "Sans,8" offset 0.3,0\n'

    # Manual legend
    script += f'set label 999 "■ Input" at graph 0.85, graph 0.05 left textcolor "#3b82f6" font "Sans,9"\n'
    script += f'set label 998 "■ Output" at graph 0.85, graph 0.10 left textcolor "#ef4444" font "Sans,9"\n'

    script += "plot NaN notitle\n"
    return run_gnuplot(script)


def generate_cache_discount_chart():
    """Generate API cache discount chart."""
    print("  Generating api-cache-discount.png ...")
    data = load_json("api-pricing.json")

    # Parse cache discounts — extract numeric percentages
    entries_with_discount = []
    for e in data["entries"]:
        p = e.get("pricing", {})
        disc = p.get("cached_input_discount", "")
        if not disc:
            continue
        # Try to extract a primary numeric value
        disc_str = str(disc).strip()
        # Parse things like "99%", "85%", "75-80%", "90%", "passes through", "varies", etc.
        import re
        match = re.search(r"(\d+)", disc_str)
        if match:
            pct = int(match.group(1))
            entries_with_discount.append((e, pct))

    entries_with_discount.sort(key=lambda x: x[0]["rank"])
    n = len(entries_with_discount)
    if n == 0:
        print("  No cache discount data found, skipping.")
        return True

    max_pct = max(p[1] for p in entries_with_discount) + 10
    out_path = os.path.join(CHARTS_DIR, "api-cache-discount.png")

    script = f"""\
set terminal pngcairo size 800,500 enhanced font "Sans,10"
set output "{out_path}"
set title "API Cache Discount (% off)" textcolor "{WHITE}" font "Sans,13"
set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor "{DARK_BG}" behind
set border lc rgb "{WHITE}" lw 1
set xtics textcolor "{WHITE}"
set ytics textcolor "{WHITE}" scale 0
set grid x lc rgb "{GRID_COLOR}"
set key off
set xrange [0:{max_pct}]
set yrange [{n - 0.5}:-0.5]
set xlabel "Cache Discount (%)" textcolor "{WHITE}"
set style fill solid 0.9 border -1
"""
    for i, (e, pct) in enumerate(entries_with_discount):
        safe_name = e["provider"].replace('"', '\\"')
        # Color gradient: higher = more green
        if pct >= 90:
            color = "#22c55e"
        elif pct >= 80:
            color = "#84cc16"
        elif pct >= 60:
            color = "#eab308"
        elif pct >= 40:
            color = "#f97316"
        else:
            color = "#ef4444"
        script += f'set label {i+1} "{safe_name} ({pct}%)" at {pct + 2},{i} left textcolor "{WHITE}" font "Sans,9"\n'
        script += f'set object {i+2} rectangle from 0,{i-0.35} to {pct},{i+0.35} fillcolor "{color}" fillstyle solid 0.9\n'

    script += "plot NaN notitle\n"
    return run_gnuplot(script)


def main():
    os.makedirs(CHARTS_DIR, exist_ok=True)

    charts = [
        ("20-rankings-value.png", generate_20_rankings_chart),
        ("10-rankings-value.png", generate_10_rankings_chart),
        ("free-rankings.png", generate_free_rankings_chart),
        ("api-pricing-comparison.png", generate_api_pricing_chart),
        ("api-cache-discount.png", generate_cache_discount_chart),
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
