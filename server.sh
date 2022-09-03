cd ~/ardupilot/ArduCopter
if !(pidof -x gzserver && pidof -x gzclient); then
	killall -9 gzserver;
fi
if pidof -x mavproxy.py; then
	killall -9 mavproxy.py;
fi
gazebo --verbose worlds/iris_arducopter_runway.world > /dev/null & \
../Tools/autotest/sim_vehicle.py -f gazebo-iris;

if !(pidof -x gzserver && pidof -x gzclient); then
	killall -9 gzserver;
fi
