transform=$(niri msg outputs | grep Transform)
rotation=$(echo $transform | cut -d ' ' -f 2)
if [[ $rotation == "normal" ]]; then
  niri msg output DSI-1 transform 90
elif [[ $rotation == "90°" ]]; then
  niri msg output DSI-1 transform 180
elif [[ $rotation == "180°" ]]; then
  niri msg output DSI-1 transform 270
elif [[ $rotation == "270°" ]]; then
  niri msg output DSI-1 transform normal
else
  niri msg output DSI-1 transform normal
fi
