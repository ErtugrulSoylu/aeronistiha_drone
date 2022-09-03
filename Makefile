all:	server
	python3 arayuz.py
server:
	if !(pidof -x gzserver && pidof -x gzclient) || !(pidof -x mavproxy.py); then \
		echo 'No mavproxy server found, running a new one.' && \
		gnome-terminal --tab -- sh server.sh; \
	fi
