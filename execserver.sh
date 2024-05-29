#!/bin/bash
cd /home/lucas/repos/rapl-hacs
/home/lucas/repos/rapl-hacs/.venv/bin/gunicorn api:app -b 0.0.0.0:5467 --reload