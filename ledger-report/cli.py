import argparse
from ledger_report.journal_parser import JournalParser
from ledger_report.report.summary_report import Summary_Report

def main():
    parser = argparse.ArgumentParser(description="Generate reports from ledger-cli journals.")
    parser.add_argument("--config", default="config.ini", help="Path to configuration file.")
    parser.add_argument("--report", choices=["summary", "expense"], required=True, help="Report type.")
    args = parser.parse_args()

    # Load config
    config_path = args.config

    # Generate Report
    if args.report == "summary":
        report = SummaryReport()
        report.generate(config_path)
