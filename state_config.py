"""
State configuration for this KansasDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "KS"
STATE_NAME = "Kansas"
APP_NAME = "KansasDischargeWatch"
APP_TAGLINE = "Kansas Discharge Monitoring"
DOMAIN = "kansasdischargewatch.org"
DATA_FILE = "ks_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@kansasdischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "CST"
EPA_REGION = 7
