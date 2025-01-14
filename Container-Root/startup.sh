#!/bin/sh

# Container startup script
echo "Container-Root/startup.sh executed"

#while true; do date; sleep 10; done

fastapi dev main.py --host 0.0.0.0 --port 8000

