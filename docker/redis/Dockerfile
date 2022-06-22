FROM redis
MAINTAINER Hide <padocon@naver.com>

EXPOSE 6377

COPY ./docker/redis/redis.conf /usr/local/etc/redis/redis.conf
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]