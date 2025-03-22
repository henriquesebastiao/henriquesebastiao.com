alias r := run
alias t := test
alias c := clean
alias compress := compress-images
alias b := build
alias m := minify

run:
    ./scripts/run.sh

test:
    ./scripts/test.sh

compress-images:
    python scripts/compress_image.py assets/img/preview-image-posts/*/*.png

clean:
    @rm -rf _site/ .jekyll-cache/

build:
    @bundle exec jekyll build

minify:
    @minify -r -o _site/ _site/