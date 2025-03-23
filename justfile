alias r := run
alias t := test
alias c := clean
alias b := build
alias m := minify
alias l := check-broken-links
alias i := check-broken-links-images

run:
    ./scripts/run.sh

test:
    ./scripts/test.sh

clean:
    @rm -rf _site/ .jekyll-cache/

build:
    @bundle exec jekyll build

minify:
    @minify -r -o _site/ _site/

check-broken-links:
    @python scripts/check_broken_links.py links/links.txt

check-broken-links-images:
    @python scripts/check_broken_links.py links/images.txt

format:
    ruff format .; ruff check . --fix

lint:
    ruff check .; ruff check . --diff