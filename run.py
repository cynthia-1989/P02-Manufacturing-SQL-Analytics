from src.data_extractor import DataExtractor
from config import logger, INDUSTRY, DB_AVAILABLE

def main():
    logger.info("=" * 60)
    logger.info("  MODULE 03 — SQL AND POSTGRESQL")
    logger.info(f"  Industry: {INDUSTRY}")
    logger.info(f"  DB Available: {DB_AVAILABLE}")
    logger.info("=" * 60)

    logger.info("[EXTRACT] Starting production extraction...")
    extractor = DataExtractor()
    extractor.extract().save().report()

if __name__ == "__main__":
    main()
