# ================================================================
# src/query_runner.py
# ================================================================
# CONTEXT:
#   We wrote SQL in .sql files. Now we need to EXECUTE those queries
#   from Python and get back pandas DataFrames we can work with.
#
# THE ANALOGY:
#   Think of SQLQueryRunner as a translator.
#   You hand it a SQL query (a string).
#   It sends that query to PostgreSQL.
#   PostgreSQL sends back rows of data.
#   SQLQueryRunner catches those rows and packages them as a DataFrame.
#
# KEY pandas FUNCTION: pd.read_sql()
#   pd.read_sql(sql_string, engine) executes SQL and returns a DataFrame.
#   This is what powers every Python + database workflow.
#
# WHY A CLASS AND NOT JUST pd.read_sql() DIRECTLY?
#   The class adds:
#     - Error handling
#     - Logging
#     - Timing
#     - Query loading from .sql files
#   These extras make it production-grade rather than just a script.
# ================================================================

import sys, pathlib, time

_root = pathlib.Path(__file__).resolve().parent
while not (_root / "config.py").exists() and _root != _root.parent:
    _root = _root.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

import pandas as pd
from config import engine, DB_AVAILABLE, SQL_DIR, INDUSTRY, logger


class SQLQueryRunner:
    """
    Executes SQL queries against the Supabase PostgreSQL database.
    Returns results as pandas DataFrames.
    """

    def __init__(self):
        self.industry = INDUSTRY
        self.history = []
        logger.info(f"SQLQueryRunner ready — db_available: {DB_AVAILABLE}")

    def run(self, sql: str, params: dict = None) -> pd.DataFrame:
        """
        Execute a SQL query and return results as a DataFrame.
        """
        if not DB_AVAILABLE or engine is None:
            logger.warning("[SQL] Database not available. Returning empty DataFrame.")
            return pd.DataFrame()

        sql = sql.replace("{industry}", self.industry)

        start_time = time.time()

        try:
            df = pd.read_sql(sql, engine, params=params)

            duration_ms = round((time.time() - start_time) * 1000, 1)

            self.history.append({
                "sql_preview": sql[:80].strip(),
                "rows": len(df),
                "cols": len(df.columns),
                "duration_ms": duration_ms,
                "status": "success",
            })

            logger.info(
                f"[SQL] Query complete — "
                f"{len(df):,} rows × {len(df.columns)} cols | "
                f"{duration_ms}ms"
            )

            return df

        except Exception as e:
            self.history.append({
                "sql_preview": sql[:80].strip(),
                "rows": 0,
                "cols": 0,
                "duration_ms": round((time.time() - start_time) * 1000, 1),
                "status": f"error: {str(e)[:100]}",
            })
            logger.error(f"[SQL] Query failed: {e}")
            return pd.DataFrame()

    def run_file(self, filename: str) -> pd.DataFrame:
        """
        Load a .sql file and execute it.
        """
        sql_path = SQL_DIR / filename

        if not sql_path.exists():
            logger.error(f"[SQL] File not found: {sql_path}")
            return pd.DataFrame()

        logger.info(f"[SQL] Loading: {filename}")

        sql_text = sql_path.read_text(encoding="utf-8")
        return self.run(sql_text)

    def demo_basics(self) -> None:
        """
        Run selected healthcare patient queries for demonstration.
        """
        demos = [
            (
                "Distinct patient cities",
                f"SELECT DISTINCT city FROM {self.industry}.patients ORDER BY city"
            ),
            (
                "Active patients",
                f"SELECT patient_id, first_name, last_name, city "
                f"FROM {self.industry}.patients "
                f"WHERE is_active = TRUE "
                f"ORDER BY patient_id "
                f"LIMIT 10"
            ),
            (
                "Patients with missing email",
                f"SELECT patient_id, first_name, last_name, email "
                f"FROM {self.industry}.patients "
                f"WHERE email IS NULL "
                f"ORDER BY patient_id "
                f"LIMIT 10"
            ),
        ]

        for title, sql in demos:
            print(f"\n── {title}:")
            df = self.run(sql)
            if not df.empty:
                print(df.to_string(index=False))

    def demo_aggregation(self) -> None:
        """
        Demo healthcare aggregation queries.
        """
        sql = f"""
            SELECT
                city,
                COUNT(*) AS patient_count
            FROM {self.industry}.patients
            GROUP BY city
            ORDER BY patient_count DESC
        """
        print("\n── Patient Count by City:")
        df = self.run(sql)
        if not df.empty:
            print(df.to_string(index=False))

    def demo_joins(self) -> None:
        """
        Demo join query placeholder for healthcare.
        If you only have patients table, this can be replaced later.
        """
        sql = f"""
            SELECT
                patient_id,
                first_name,
                last_name,
                city,
                is_active
            FROM {self.industry}.patients
            ORDER BY patient_id
            LIMIT 10
        """
        print("\n── Sample Patient Records:")
        df = self.run(sql)
        if not df.empty:
            print(df.to_string(index=False))

    def __str__(self) -> str:
        return (
            f"SQLQueryRunner(industry={self.industry!r}, "
            f"queries_run={len(self.history)})"
        )

    def __repr__(self) -> str:
        return f"SQLQueryRunner(industry={self.industry!r})"