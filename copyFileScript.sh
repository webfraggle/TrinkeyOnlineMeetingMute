mdutil -i off /Volumes/CIRCUITPY
rm  /Volumes/CIRCUITPY/._*
cp -X code.py /Volumes/CIRCUITPY
cp -X State.py /Volumes/CIRCUITPY
cp -X KeyOptions.py /Volumes/CIRCUITPY
cp -X StateConfiguration.py /Volumes/CIRCUITPY
cp -X StateKeyboard.py /Volumes/CIRCUITPY
cp -X States.py /Volumes/CIRCUITPY
cp -X custom-off.keys /Volumes/CIRCUITPY
cp -X boot.py /Volumes/CIRCUITPY

rm  /Volumes/CIRCUITPY/._*

ls -Al /Volumes/CIRCUITPY/