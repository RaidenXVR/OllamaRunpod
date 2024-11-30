#!/bin/bash

pgrep ollama | xargs kill

ollama serve 2>&1 | tee ollama.server.log &
# Store the process ID (PID) of the background command

check_server_is_running() {
    # Replace "Listening" with the actual expected output
    
    if curl -I 127.0.0.1:11434 | grep -q "200 OK"; then
        return 0 # Success
    else
        return 1 # Failure
    fi
}

# Wait for the process to print "Listening"
while ! check_server_is_running; do
    echo "not started... loading..."
    sleep 1
done

ollama create assistant -f ./LaserDolphinMistral/Modelfile


