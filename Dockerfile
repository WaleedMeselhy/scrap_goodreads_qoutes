FROM python:3.7-alpine as base

FROM base as builder
RUN apk update && \
    apk add --virtual .build-deps git \
    gcc \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    musl-dev \
    openssl-dev \
    py3-setuptools \
    linux-headers \
    libc-dev \
    python3-dev && \
    python3 -m ensurepip && \
    pip3 install setuptools
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --install-option="--prefix=/install" --prefer-binary -r /tmp/requirements.txt && \
    rm -r /root/.cache && \
    apk del .build-deps 

FROM base
RUN apk add libxslt
COPY --from=builder /install /usr/local
COPY crawl_tutsplus_categories /app/crawl_tutsplus_categories
COPY scrapy.cfg /app/scrapy.cfg

WORKDIR /app
ENTRYPOINT [ "scrapy" ]
CMD [ "crawl" , "goodreades"]