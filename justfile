alias r := run
alias t := test
alias c := compress-images

run:
    ./scripts/run.sh

test:
    ./scripts/test.sh

compress-images:
    python scripts/compress_image.py assets/img/preview-image-posts/*.png
