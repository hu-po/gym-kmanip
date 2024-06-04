export DATA_PATH="/mnt/data"
docker build \
     -t "kmanip-orin" \
     -f .docker/Dockerfile.orin .
docker run \
    -it \
    --rm \
    -p 5555:5555 \
    --gpus 0 \
    -v ${DATA_PATH}:/data \
    kmanip-orin \
    python3 gym_kmanip/client.py