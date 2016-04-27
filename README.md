# production

# commands to run on gunicorn server side (inside ~/triproulette/production)
python app.py \n
gunicorn --bind 0.0.0.0:PORT --reload app \n
watch -n[seconds] -d git pull --rebase origin master \n
iwatch -t "\.py$" -c "aplay [sound-path]" -e close_write [target] \n