
echo "Listen for changes..."
fswatch bavest |while read num; do poetry install; done
