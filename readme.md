# Emotion classification of MIDI lyrics

(Also check out <https://github.com/serkansulun/midi-emotion> for another, more accurate MIDI dataset with continuous-valued valence-arousal labels.)

To only download the datasets, with pairs of MIDI file names and predicted emotions from the lyrics, you can right-click and choose "Save Link As...", using the links below:

[7-labels](https://raw.githubusercontent.com/emotionalmusic/lyricsemotions/master/datasets/7labels.csv)

[28-labels](https://raw.githubusercontent.com/emotionalmusic/lyricsemotions/master/datasets/28labels.csv)

[Download](https://drive.google.com/drive/folders/1k9qAEUMjbUlgBLshTUn-_5-EZiPt-q7J?usp=sharing) the models and place inside the `models` folder. 

Required Python packages: transformers, pretty_midi

Usage:

`python main.py --midi_file_path "John Lennon - Imagine.mid"`

or

`python main.py --lyrics "I hope some day you'll join us. And the world will be as one"`