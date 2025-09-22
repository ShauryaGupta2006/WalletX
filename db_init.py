
import subprocess

def start_mysql_if_stopped():
    """Check if MySQL server is running, if not, start it."""
    try:
        # Check if MySQL is running using pgrep (works on macOS/Linux)
        result = subprocess.run(["pgrep", "mysqld"], stdout=subprocess.PIPE)
        if result.returncode != 0:
            print("🔴 MySQL is not running. Starting MySQL server...")
            subprocess.run(["mysql.server", "start"])
            print("✅ MySQL started successfully.")
        else:
            print("✅ MySQL is already running.")
    except FileNotFoundError:
        print("⚠️ mysql.server command not found. Is MySQL installed and added to PATH?")

# Call it before your database operations
start_mysql_if_stopped()
