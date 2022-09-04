all:	server
	@echo 'Arayuz baslatiliyor..'
	@python3 arayuz.py

server:
	@if !(pidof -x gzserver && pidof -x gzclient) || !(pidof -x mavproxy.py); then \
		echo 'Mavproxy sunucusu bulunamadi, yeni bir tane aciliyor.' && \
		gnome-terminal --tab -- sh inc/server.sh; \
	fi

fclean:	clean
	@rm -rf logs/*

clean:
	@rm -rf src/__pycache__
	@rm -rf inc/__pycache__
	@rm -rf __pycache__

.PHONY: all server clean fclean
