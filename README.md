# scrap_goodreads_qoutes

* Using scrapy to scrap qoutes from goodreads
* Using MongoDbPipeline to save qoutes in mongodb
## sample output
```json
[
    {
        "text": "Don't cry because it's over, smile because it happened.",
        "author": "Dr. Seuss",
        "tags": "attributed-no-source, cry, crying, experience, happiness, joy, life, misattributed-dr-seuss, optimism, sadness, smile, smiling"
    },
    {
        "text": "I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best.",
        "author": "Marilyn Monroe",
        "tags": "attributed-no-source, best, life, love, mistakes, out-of-control, truth, worst"
    },
    {
        "text": "Be yourself; everyone else is already taken.",
        "author": "Oscar Wilde",
        "tags": "attributed-no-source, be-yourself, honesty, inspirational, misattributed-oscar-wilde"
    }
]
```

## Run

```sh
$ cd scrap_goodreads_qoutes
$ scrapy crawl goodreades -o txt.json
```

or run in docker-compose

```sh
$  docker-compose up --build
```
