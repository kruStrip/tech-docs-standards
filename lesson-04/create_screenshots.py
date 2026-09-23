"""Запускает примеры и создаёт PNG-скриншоты к отчёту."""

from html import escape
from pathlib import Path
import subprocess


ROOT = Path(__file__).parent
SHOTS = ROOT / "screenshots"
CHROME_PROFILE = Path("/tmp/chromium-lesson04-profile")
SCRIPTS = [
    "02_first_measurement.py", "03_growth_experiment.py", "04_constant_access.py",
    "05_linear_search.py", "06_quadratic.py", "07_list_vs_set.py",
    "10_final_experiment.py", "11_sum_comparison.py", "12_memory_comparison.py",
    "13_list_generator.py", "14_repeated_runs.py",
]

TEMPLATE = """<!doctype html><meta charset='utf-8'><style>
body {{ margin: 0; background: #171b22; color: #e6edf3; font: 17px/1.45 ui-monospace, SFMono-Regular, Consolas, monospace; }}
main {{ padding: 32px 42px; }} h1 {{ color:#7ee787; font-size: 22px; margin: 0 0 20px; }}
h2 {{ color:#79c0ff; font-size: 16px; margin: 20px 0 8px; }}
pre {{ margin:0; padding:18px; border:1px solid #30363d; border-radius:9px; background:#0d1117; white-space:pre-wrap; }}
.prompt {{ color:#7ee787; }} .output {{ color:#f0f6fc; }}
</style><main><h1>Python 3.14.7 · замер выполнен локально</h1>
<h2>Исходный код · {name}</h2><pre>{source}</pre>
<h2>Запуск и результат</h2><pre><span class='prompt'>$ python3 {name}</span>\n<span class='output'>{output}</span></pre></main>"""

SHOTS.mkdir(exist_ok=True)
CHROME_PROFILE.mkdir(exist_ok=True)
for number, name in enumerate(SCRIPTS, start=1):
    source = (ROOT / name).read_text(encoding="utf-8")
    run = subprocess.run(["python3", name], cwd=ROOT, text=True, capture_output=True, check=True)
    html = TEMPLATE.format(name=name, source=escape(source), output=escape(run.stdout.rstrip()))
    page = SHOTS / f"{number:02d}_{name[:-3]}.html"
    png = SHOTS / f"{number:02d}_{name[:-3]}.png"
    page.write_text(html, encoding="utf-8")
    subprocess.run([
        "chromium", "--headless", "--no-sandbox", "--disable-gpu",
        "--user-data-dir=" + str(CHROME_PROFILE),
        "--hide-scrollbars", "--window-size=1440,1400", "--screenshot=" + str(png),
        page.as_uri(),
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    page.unlink()
    print(png.name)
