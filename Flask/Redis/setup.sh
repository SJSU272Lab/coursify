which brew > /dev/null;
if [ $? -eq  0 ]; then
	which redis-server > /dev/null
	if [ "$?" -ne  "0" ]; then
		echo "Installing redis"
		brew install redis
	fi
fi
echo "Starting redis"
redis-server redis.conf