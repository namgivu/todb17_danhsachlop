SH=`dirname $BASH_SOURCE`
cd $SH

docker build -t                           webapp_i .  2>&1 | tee /tmp/t
docker rm       -f webapp_c
docker run  --name webapp_c -p 89:5000 -d \
  --network nn \
  webapp_i
