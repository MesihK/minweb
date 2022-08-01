HOME=/home/ubuntu
PRJ=$HOME/minweb/
ENV=$HOME/env
LOG=$HOME/logs
LOGLVL=DEBUG
APP=minapp:app
PORT=80
THREAD=1
WORKER=2

logf=$(date +%H.%M-%m.%d.%y)
mkdir -p $LOG/$logf

cd $PRJ

#mkdir $LOG
#mkdir pid
sudo $ENV/bin/gunicorn -w $WORKER -k eventlet -b 0.0.0.0:$PORT  --preload --timeout 600 \
		    --access-logfile $LOG/$logf/access.log --threads $THREAD \
		    	    --log-file $LOG/$logf/error.log --log-level $LOGLVL $APP  -D  &
echo $! > pid/app
wait
echo done
