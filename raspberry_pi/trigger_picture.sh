#!/bin/bash

# Replace with the actual Raspberry Pi IP (Tailscale or local)
PI_IP="100.72.230.30"
PORT="5050"

# Trigger the Flask endpoint
curl http://$PI_IP:$PORT/take-picture
