import tkinter as tk
from tkinter import messagebox
import threading
import subprocess

from ui.ui_test_cases import run_ui_tests
from api.api_test_cases import run_api_tests
from database.db_test_cases import run_db_tests
from performance.performance_test_cases import run_performance_tests
from security.security_test_cases import run_security_tests
from accessibility.accessibility_test_cases import run_accessibility_tests
from core.test_runner import execute_all


def run_locust(site):
    """
    Runs Locust load test in headless mode (optional, async)
    """
    try:
        subprocess.Popen([
            "locust",
            "-f", "performance/locustfile.py",
            "--headless",
            "-u", "50",
            "-r", "5",
            "--run-time", "1m",
            "--host", site
        ])
    except FileNotFoundError:
        print("[WARN] Locust not installed. Skipping performance load test.")


def execute_from_gui():
    site = site_entry.get().strip()
    tester = tester_entry.get().strip()

    if not site or not tester:
        messagebox.showerror("Error", "Website URL and Tester Name are required")
        return

    if not site.startswith("http"):
        messagebox.showerror(
            "Error",
            "Please enter a valid URL starting with http:// or https://"
        )
        return

    modules = []

    try:
        if ui_var.get():
            modules.append(run_ui_tests(site))

        if api_var.get():
            modules.append(run_api_tests(site))

        if db_var.get():
            modules.append(run_db_tests(site))

        if perf_var.get():
            modules.append(run_performance_tests(site))
            run_locust(site)   # async only

        if sec_var.get():
            modules.append(run_security_tests(site))

        if acc_var.get():
            modules.append(run_accessibility_tests(site))

        if not modules:
            messagebox.showerror(
                "Error",
                "Please select at least one test module"
            )
            return

        execute_all(site, tester, modules)

        messagebox.showinfo(
            "Execution Completed",
            "All selected tests executed.\nReports generated successfully."
        )

    except Exception as e:
        messagebox.showerror("Execution Error", str(e))


def run_tests():
    # Run in background thread so GUI does not freeze
    threading.Thread(target=execute_from_gui, daemon=True).start()


# ---------------- GUI LAYOUT ----------------

root = tk.Tk()
root.title("Enterprise QA Automation Tool")
root.geometry("520x600")

tk.Label(root, text="Website URL", font=("Arial", 10, "bold")).pack(pady=5)
site_entry = tk.Entry(root, width=55)
site_entry.pack()

tk.Label(root, text="Tester Name", font=("Arial", 10, "bold")).pack(pady=5)
tester_entry = tk.Entry(root, width=55)
tester_entry.pack()

tk.Label(root, text="Select Test Modules", font=("Arial", 11, "bold")).pack(pady=15)

ui_var = tk.BooleanVar()
api_var = tk.BooleanVar()
db_var = tk.BooleanVar()
perf_var = tk.BooleanVar()
sec_var = tk.BooleanVar()
acc_var = tk.BooleanVar()

tk.Checkbutton(root, text="UI Testing (Playwright)", variable=ui_var).pack(anchor="w", padx=60)
tk.Checkbutton(root, text="API Testing", variable=api_var).pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Database Testing", variable=db_var).pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Performance Testing (Locust)", variable=perf_var).pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Security Testing (OWASP ZAP)", variable=sec_var).pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Accessibility Testing", variable=acc_var).pack(anchor="w", padx=60)

tk.Button(
    root,
    text="Run Tests",
    width=25,
    height=2,
    bg="green",
    fg="white",
    command=run_tests
).pack(pady=30)

root.mainloop()
