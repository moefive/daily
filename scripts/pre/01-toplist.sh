#!/bin/bash -e
set -o pipefail

CUR_DIR=$(pwd)
TMP_DIR=$(mktemp -d /tmp/toplist.XXXXXX)

SRC_URL="https://s3.amazonaws.com/alexa-static/top-1m.csv.zip"
DEST_FILE="dist/toplist/toplist.txt"

gen_list() {
  cd $TMP_DIR

  curl -sSL $SRC_URL |
    # unzip
    gunzip |
    # extract domain
    awk -F ',' '{print $2}' > toplist.txt

  cd $CUR_DIR
}

copy_dest() {
  install -D $TMP_DIR/toplist.txt $DEST_FILE
}

clean_up() {
  rm -r $TMP_DIR
  echo "[toplist]: prepared."
}

gen_list
copy_dest
clean_up
