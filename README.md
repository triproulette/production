# production

# commands to run on gunicorn server side (inside ~/triproulette/production)
watch -n[seconds] -d git pull --rebase origin master
iwatch -t "\.py$" -c "aplay [sound-path]" -e close_write [target]