sum=0
count=0
for num in "$@"; do
  sum=$((sum + num))
  count=$((count + 1))
done
avg=$((sum / count))