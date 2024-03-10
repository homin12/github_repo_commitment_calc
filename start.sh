#!bin/bash

if test -z $GOOGLE_TOKEN; 
then python3 main.py $MODE -t $GIT_TOKEN -l $REPO_LIST -o $OUT_FILE; \
else python3 main.py $MODE -t $GIT_TOKEN -l $REPO_LIST -o $OUT_FILE --google_token $GOOGLE_TOKEN --table_id $TABLE_ID --sheet_id $SHEET_ID; fi