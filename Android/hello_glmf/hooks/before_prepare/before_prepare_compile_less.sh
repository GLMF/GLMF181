#!/bin/bash

echo "Compilation de index.less en index.css"

lessc www/css/index.less > www/css/index.css
