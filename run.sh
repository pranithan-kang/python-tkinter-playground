docker run -e DISPLAY=docker.for.mac.host.internal:0 \
-v $(pwd)/app:/app \
--rm \
tkinter_in_docker