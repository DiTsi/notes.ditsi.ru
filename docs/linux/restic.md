# restic

# restic

*Git-like Backup Tool*

## Google Cloud Storage

First of all you need [to create service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts) for your project

Add "Storage Admin" role to your service account [here](https://console.cloud.google.com/iam-admin)

Download JSON for service account by [selecting](https://console.cloud.google.com/iam-admin/serviceaccounts) "Menu" \[dots\] -&gt; "Create Key"

## Commands

```bash
# create new Google Cloud Storage "fook" repo
# see here: https://console.cloud.google.com/storage/browser
restic -r gs:fook:/ init

# show snapshots (older is lower)
restic -r gs:thisismybucket:/ snapshots

# show snapshot files
restic -r gs:thisismybucket:/ ls [snapshot id]

# create backup of local folder 1/
restic -r gs:thisismybucket:/ backup --verbose --verbose 1/

# restore backup
.\restic.exe -r gs:bucket:/f restore --target C:\Users\localuser\Desktop\ --include "path/in/the/bucket" <snapshot id OR "latest">
```

## Script

```bash
#!/bin/bash

ACTION=$1
SERVICE=$2


if [ ! $SERVICE ] || [ ! $ACTION ]; then
    echo No SERVICE or ACTION!
    echo Format: ./restic.sh [SERVICE] [ACTION]
    exit 0
fi

case $SERVICE in
    "bitwarden")
        DIRECTORY=/data/bwdata
        REPO=ditsi-bitwarden
        REPO_PASSWORD="G32LeEomDm3Pil6kenlq7PIuAQEcZAVnK1A"
        ;;
    "madsonic")
        DIRECTORY=/data/madsonic
        REPO=ditsi-media
        REPO_PASSWORD="csxu7My8pW05Y18UL8UNADfkIH3usNMV7JA"
        ;;
    *)
        echo Incorrect SERVICE
        exit 0
        ;;
esac


unset HISTFILE
export RESTIC_REPOSITORY="s3:https://s3.amazonaws.com/$REPO"
export AWS_ACCESS_KEY_ID="AKIAXYS832huieah5INWX67"
export AWS_SECRET_ACCESS_KEY="Qbq1MWWbJH5ZcqwedqwdetCB5HU"
export RESTIC_PASSWORD=${REPO_PASSWORD}

case $ACTION in
"init")
    restic -r $RESTIC_REPOSITORY init
    ;;
"restore")
    restic -r $RESTIC_REPOSITORY restore --target ./ latest
    ;;
"backup")
    restic -r $RESTIC_REPOSITORY backup $DIRECTORY
    ;;
*)
    echo Incorrect action
    exit 0
    ;;
esac

```