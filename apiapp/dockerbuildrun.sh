SH=`dirname $BASH_SOURCE`
cd $SH

docker build \
  -t apiapp_i \
  . \
  2>&1 | tee /tmp/t

docker rm -f apiapp_c

docker run \
  -d \
  --name apiapp_c \
  -p 88:5000 \
  --network nn \
  apiapp_i
