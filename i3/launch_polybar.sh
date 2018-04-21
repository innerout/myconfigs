if type "xrandr"; then
  for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
    echo $m
    MONITOR=$m polybar --reload example &
    echo $MONITOR
  done
else
	polybar --reload example &
fi
